#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = ["python-docx>=1.1"]
# ///
"""build_report.py: turn the thematic analysis report (Markdown) into a Word file.

The report is written once, as Markdown, in the shape of the skill's output
template. This script lays it out as an APA-style manuscript: 12-point Times
New Roman, one-inch margins, double spacing, centered bold first-level
headings, indented block quotes for data extracts, a hanging indent under
"References", and the thematic map as a numbered figure.

Usage:
  python build_report.py report.md --out report.docx
  python build_report.py report.md --out report.docx --spacing 1.5
  python build_report.py --self-test

With uv, `uv run build_report.py ...` installs python-docx on its own. Without
python-docx the script tries pandoc; with neither it exits 2 and the Markdown
report stands as the deliverable.

Markdown it understands:
  # Title                    the report title (first one only)
  ## / ### / ####            heading levels 1, 2, 3
  plain paragraphs           **bold**, *italic*, `code`, [text](url)
  > quoted lines             a data extract, set as a block quote
  - item / 1. item           lists
  | a | b | tables           the first row is the header
  ![Figure 1. Title](map.png)   a figure; the path is relative to the report
  ```mermaid ... ```         skipped when the report also has a figure image
Anything under a heading named "References" gets a hanging indent.
"""
from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
import sys
import tempfile

INLINE_RE = re.compile(r"(\*\*.+?\*\*|(?<![\*\w])\*(?!\s).+?(?<!\s)\*(?![\*\w])|`[^`]+`|\[[^\]]+\]\([^)]+\))")
IMAGE_RE = re.compile(r"^!\[(.*?)\]\((.+?)\)\s*$")
TABLE_SEP_RE = re.compile(r"^\s*\|?\s*:?-{2,}:?\s*(\|\s*:?-{2,}:?\s*)*\|?\s*$")
LIST_RE = re.compile(r"^(\s*)([-*+]|\d+[.)])\s+(.*)$")


def parse(md: str) -> list:
    """Markdown text to a flat list of blocks: (kind, payload)."""
    blocks, para = [], []
    lines = md.replace("\r\n", "\n").split("\n")

    def flush():
        if para:
            blocks.append(("p", " ".join(s.strip() for s in para)))
            para.clear()

    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        if stripped.startswith("```"):
            flush()
            lang = stripped[3:].strip().lower()
            body = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith("```"):
                body.append(lines[i])
                i += 1
            blocks.append(("code", (lang, "\n".join(body))))
        elif not stripped or re.fullmatch(r"-{3,}|\*{3,}|_{3,}", stripped):
            flush()
        elif stripped.startswith("#"):
            flush()
            level = len(stripped) - len(stripped.lstrip("#"))
            blocks.append(("h", (min(level, 5), stripped.lstrip("#").strip())))
        elif IMAGE_RE.match(stripped):
            flush()
            alt, path = IMAGE_RE.match(stripped).groups()
            blocks.append(("img", (alt, path)))
        elif stripped.startswith(">"):
            flush()
            quote = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                quote.append(lines[i].strip()[1:].strip())
                i += 1
            # blank ">" lines split a quote into paragraphs
            chunk = []
            for q in quote + [""]:
                if q:
                    chunk.append(q)
                elif chunk:
                    blocks.append(("quote", " ".join(chunk)))
                    chunk = []
            continue
        elif "|" in stripped and i + 1 < len(lines) and TABLE_SEP_RE.match(lines[i + 1]) and "-" in lines[i + 1]:
            flush()
            rows = [split_row(stripped)]
            i += 2
            while i < len(lines) and "|" in lines[i] and lines[i].strip():
                rows.append(split_row(lines[i].strip()))
                i += 1
            blocks.append(("table", rows))
            continue
        elif LIST_RE.match(line):
            flush()
            marker = LIST_RE.match(line).group(2)
            ordered = marker[0].isdigit()
            items = []
            while i < len(lines):
                m = LIST_RE.match(lines[i])
                if m:
                    items.append(m.group(3).strip())
                elif lines[i].strip() and lines[i].startswith((" ", "\t")) and items:
                    items[-1] += " " + lines[i].strip()
                else:
                    break
                i += 1
            blocks.append(("ol" if ordered else "ul", items))
            continue
        else:
            if re.match(r"\*\*[^*]+:\*\*", stripped):
                flush()  # a "**Label:** value" line is its own paragraph
            para.append(line)
        i += 1
    flush()
    return blocks


def split_row(line: str) -> list:
    line = line.strip()
    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|"):
        line = line[:-1]
    return [c.strip() for c in re.split(r"(?<!\\)\|", line)]


def inline_runs(text: str) -> list:
    """Split a line into (text, bold, italic, mono) runs."""
    runs = []
    for part in INLINE_RE.split(text):
        if not part:
            continue
        if part.startswith("**") and part.endswith("**") and len(part) > 4:
            for sub, _, it, mono in inline_runs(part[2:-2]):
                runs.append((sub, True, it, mono))
        elif part.startswith("*") and part.endswith("*") and len(part) > 2:
            runs.append((part[1:-1], False, True, False))
        elif part.startswith("`") and part.endswith("`"):
            runs.append((part[1:-1], False, False, True))
        elif part.startswith("["):
            label, url = re.match(r"\[([^\]]+)\]\(([^)]+)\)", part).groups()
            runs.append((label if label == url or url.startswith("#") else f"{label} ({url})", False, False, False))
        else:
            runs.append((part, False, False, False))
    return runs


def build_docx(md_path: str, out_path: str, spacing: float = 2.0) -> dict:
    from docx import Document
    from docx.enum.table import WD_TABLE_ALIGNMENT
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    from docx.oxml import OxmlElement
    from docx.oxml.ns import qn
    from docx.shared import Inches, Pt, RGBColor

    with open(md_path, encoding="utf-8") as fh:
        blocks = parse(fh.read())
    base = os.path.dirname(os.path.abspath(md_path))
    has_image = any(k == "img" for k, _ in blocks)

    doc = Document()
    for section in doc.sections:
        section.top_margin = section.bottom_margin = Inches(1)
        section.left_margin = section.right_margin = Inches(1)
    normal = doc.styles["Normal"]
    normal.font.name = "Times New Roman"
    normal.font.size = Pt(12)
    normal.element.rPr.rFonts.set(qn("w:eastAsia"), "Times New Roman")
    normal.paragraph_format.line_spacing = spacing
    normal.paragraph_format.space_before = Pt(0)
    normal.paragraph_format.space_after = Pt(0)

    # page number, top right
    header = doc.sections[0].header.paragraphs[0]
    header.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    run = header.add_run()
    for tag, text in (("begin", None), (None, "PAGE"), ("end", None)):
        if tag:
            el = OxmlElement("w:fldChar")
            el.set(qn("w:fldCharType"), tag)
        else:
            el = OxmlElement("w:instrText")
            el.set(qn("xml:space"), "preserve")
            el.text = text
        run._r.append(el)

    def add_runs(par, text, bold=False, italic=False, size=None):
        for chunk, b, it, mono in inline_runs(text):
            r = par.add_run(chunk)
            r.bold = bold or b or None
            r.italic = italic or it or None
            if mono:
                r.font.name = "Courier New"
            if size:
                r.font.size = Pt(size)
        return par

    def paragraph(text="", align=None, first=None, left=None, hanging=False, keep=False, **fmt):
        par = doc.add_paragraph()
        pf = par.paragraph_format
        if align is not None:
            par.alignment = align
        if left is not None:
            pf.left_indent = Inches(left)
        if hanging:
            pf.left_indent = Inches(0.5)
            pf.first_line_indent = Inches(-0.5)
        elif first is not None:
            pf.first_line_indent = Inches(first)
        if keep:
            pf.keep_with_next = True
        if text:
            add_runs(par, text, **fmt)
        return par

    def rule(cell, edges):
        tc_pr = cell._tc.get_or_add_tcPr()
        borders = tc_pr.find(qn("w:tcBorders"))
        if borders is None:
            borders = OxmlElement("w:tcBorders")
            tc_pr.append(borders)
        for edge in edges:
            el = OxmlElement(f"w:{edge}")
            el.set(qn("w:val"), "single")
            el.set(qn("w:sz"), "8")
            el.set(qn("w:space"), "0")
            el.set(qn("w:color"), "000000")
            borders.append(el)

    counts = {"headings": 0, "paragraphs": 0, "quotes": 0, "tables": 0, "figures": 0, "references": 0, "missing_images": []}
    in_refs, seen_title = False, False
    for kind, data in blocks:
        if kind == "h":
            level, text = data
            in_refs = text.strip().lower() in ("references", "reference list")
            counts["headings"] += 1
            if level == 1 and not seen_title:
                seen_title = True
                paragraph(text, align=WD_ALIGN_PARAGRAPH.CENTER, bold=True, keep=True)
                continue
            if level <= 2:
                paragraph(text, align=WD_ALIGN_PARAGRAPH.CENTER, bold=True, keep=True)
            elif level == 3:
                paragraph(text, bold=True, keep=True)
            else:
                paragraph(text, bold=True, italic=True, keep=True)
        elif kind == "p":
            if in_refs:
                paragraph(data, hanging=True)
                counts["references"] += 1
            else:
                label = data.startswith("**") or data.lower().startswith(("*note.", "note."))
                paragraph(data, first=None if label else 0.5)
                counts["paragraphs"] += 1
        elif kind == "quote":
            paragraph(data, left=0.5)
            counts["quotes"] += 1
        elif kind in ("ul", "ol"):
            style = "List Bullet" if kind == "ul" else "List Number"
            for item in data:
                if in_refs:
                    paragraph(item, hanging=True)
                    counts["references"] += 1
                else:
                    par = doc.add_paragraph(style=style)
                    par.paragraph_format.line_spacing = spacing
                    add_runs(par, item)
        elif kind == "table":
            rows = data
            ncols = max(len(r) for r in rows)
            table = doc.add_table(rows=len(rows), cols=ncols)
            table.alignment = WD_TABLE_ALIGNMENT.CENTER
            for r_i, row in enumerate(rows):
                for c_i in range(ncols):
                    cell = table.cell(r_i, c_i)
                    par = cell.paragraphs[0]
                    par.paragraph_format.line_spacing = 1.0
                    par.paragraph_format.space_before = par.paragraph_format.space_after = Pt(3)
                    add_runs(par, row[c_i] if c_i < len(row) else "", bold=(r_i == 0), size=11)
                    edges = []
                    if r_i == 0:
                        edges += ["top", "bottom"]
                    if r_i == len(rows) - 1:
                        edges.append("bottom")
                    if edges:
                        rule(cell, edges)
            paragraph()
            counts["tables"] += 1
        elif kind == "img":
            alt, path = data
            full = path if os.path.isabs(path) else os.path.join(base, path)
            m = re.match(r"^((?:Figure|Fig\.)\s*\d+)[.:]?\s*(.*)$", alt.strip(), flags=re.IGNORECASE)
            number, title = (m.group(1), m.group(2)) if m else ("", alt.strip())
            if number:
                paragraph(number, bold=True, keep=True)
            if title:
                paragraph(title, italic=True, keep=True)
            if os.path.exists(full) and full.lower().endswith((".png", ".jpg", ".jpeg", ".gif")):
                par = paragraph(align=WD_ALIGN_PARAGRAPH.CENTER)
                par.paragraph_format.line_spacing = 1.0
                par.add_run().add_picture(full, width=Inches(6.5))
                counts["figures"] += 1
            else:
                par = paragraph(f"[Figure file not found or not a PNG/JPG: {path}]")
                par.runs[0].font.color.rgb = RGBColor(0xB0, 0x00, 0x20)
                counts["missing_images"].append(path)
        elif kind == "code":
            lang, body = data
            if lang == "mermaid" and has_image:
                continue  # the picture stands in for the diagram source
            for line in body.split("\n"):
                par = paragraph(left=0.5)
                par.paragraph_format.line_spacing = 1.0
                r = par.add_run(line)
                r.font.name = "Courier New"
                r.font.size = Pt(9.5)
    doc.save(out_path)
    return counts


def build_with_pandoc(md_path: str, out_path: str) -> bool:
    exe = shutil.which("pandoc")
    if not exe:
        return False
    done = subprocess.run([exe, md_path, "-o", out_path, "--resource-path", os.path.dirname(os.path.abspath(md_path))],
                          capture_output=True, text=True)
    return done.returncode == 0 and os.path.exists(out_path)


SAMPLE = """# A sample thematic analysis

**Data set:** 3 interviews

## Method

I coded the *whole* data set. See [the paper](https://doi.org/10.1191/1478088706qp063oa).

## Findings

### The app as a second supervisor

Workers described being watched.

> I enter the visit even when nobody was home, because the dashboard is what she looks at. (CHW-03)

| Theme | Sub-themes |
|---|---|
| The app as a second supervisor | Being watched; Praise that never arrives |

![Figure 1. Final thematic map](MAP)

*Note.* Drawn from the final theme definitions.

```mermaid
flowchart LR
  A --> B
```

- one
- two

## References

Braun, V., & Clarke, V. (2006). Using thematic analysis in psychology. *Qualitative Research in Psychology*, *3*(2), 77-101. https://doi.org/10.1191/1478088706qp063oa

Clarke, V., & Braun, V. (2017). Thematic analysis. *The Journal of Positive Psychology*, *12*(3), 297-298. https://doi.org/10.1080/17439760.2016.1262613
"""

# a 1x1 white PNG, so the self-test needs no other file
PIXEL = (b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x02\x00\x00\x00\x90wS\xde"
         b"\x00\x00\x00\x0cIDATx\x9cc\xf8\xff\xff?\x00\x05\xfe\x02\xfe\xdc\xccY\xe7\x00\x00\x00\x00IEND\xaeB`\x82")


def self_test() -> int:
    blocks = parse(SAMPLE.replace("MAP", "map.png"))
    kinds = [k for k, _ in blocks]
    assert kinds.count("h") == 5 and kinds.count("quote") == 1 and kinds.count("table") == 1, kinds
    assert kinds.count("img") == 1 and kinds.count("code") == 1 and kinds.count("ul") == 1, kinds
    labels = parse("**Question:** q\n**Data set:** d\nmore\n")
    assert [d for _, d in labels] == ["**Question:** q", "**Data set:** d more"], labels
    runs = inline_runs("I coded the *whole* set, **all of it**, see [the paper](https://x.org).")
    assert ("whole", False, True, False) in runs and ("all of it", True, False, False) in runs, runs
    assert runs[-2][0] == "the paper (https://x.org)", runs
    try:
        import docx  # noqa: F401
    except ImportError:
        print("self-test: parser checks passed; python-docx is not installed, so no Word file was built.")
        return 0
    with tempfile.TemporaryDirectory() as tmp:
        with open(os.path.join(tmp, "map.png"), "wb") as fh:
            fh.write(PIXEL)
        md = os.path.join(tmp, "report.md")
        with open(md, "w", encoding="utf-8") as fh:
            fh.write(SAMPLE.replace("MAP", "map.png"))
        out = os.path.join(tmp, "report.docx")
        counts = build_docx(md, out)
        assert counts["figures"] == 1 and counts["references"] == 2 and counts["quotes"] == 1, counts
        assert not counts["missing_images"] and os.path.getsize(out) > 5000
    print("self-test: passed (parser, inline styles, and a Word file with a figure, a table, a block quote, and references).")
    return 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Build an APA-style Word file from the thematic analysis report.")
    ap.add_argument("report", nargs="?", help="path to the report in Markdown")
    ap.add_argument("--out", help="path of the Word file (default: the report's name with .docx)")
    ap.add_argument("--spacing", type=float, default=2.0, help="line spacing: 2 (APA, default), 1.5, or 1")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args(argv)
    if args.self_test:
        return self_test()
    if not args.report:
        ap.error("give the path to the report, or --self-test")
    if not os.path.exists(args.report):
        print(f"No such file: {args.report}", file=sys.stderr)
        return 1
    out = args.out or os.path.splitext(args.report)[0] + ".docx"
    try:
        counts = build_docx(args.report, out, spacing=args.spacing)
    except ImportError:
        if build_with_pandoc(args.report, out):
            print(f"Wrote {out} with pandoc (python-docx is not installed, so the APA layout was not applied).")
            return 0
        print("python-docx is not installed and pandoc was not found, so no Word file was built. "
              "Install python-docx (pip install python-docx, or run this script with uv); "
              "until then the Markdown report is the deliverable.", file=sys.stderr)
        return 2
    note = f" Missing figure files: {', '.join(counts['missing_images'])}." if counts["missing_images"] else ""
    print(f"Wrote {out}: {counts['headings']} headings, {counts['paragraphs']} paragraphs, {counts['quotes']} extracts, "
          f"{counts['tables']} tables, {counts['figures']} figures, {counts['references']} references.{note}")
    return 1 if counts["missing_images"] else 0


if __name__ == "__main__":
    sys.exit(main())
