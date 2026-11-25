#!/usr/bin/env python3
"""check_extracts.py: confirm that every coded extract and every quote in the
report is in the data, word for word, and that no data item was skimmed.

A language model can tidy a quote, merge two speakers, or write a line nobody
said. This script compares each extract with the file it is said to come from
and lists the ones that do not match. It also counts extracts per data item,
because every item should get equal attention in coding (Braun & Clarke,
2006, table 2, criterion 2). Standard library only; Python 3.8+.

Usage:
  python check_extracts.py codes.json --data data/
      checks the coded extracts and prints the count per data item
  python check_extracts.py codes.json --data data/ --report report.md
      also checks every block quote ("> ...") in the report
  python check_extracts.py --self-test

codes.json is a list of coded extracts:
  [{"item": "CHW-03", "file": "chw-03.txt", "where": "lines 41-44",
    "extract": "the exact words from the data", "codes": ["Being watched"]}]
"file" is relative to --data. Data files are plain text or Markdown; convert
Word or PDF files to text first. Inside an extract, "[...]" marks words left
out; the parts on each side must appear in the file in that order.

Exit code 0: everything matched. 1: at least one extract or quote is not in
the data, or a data item has no extracts. 2: a file could not be read.
"""
from __future__ import annotations

import argparse
import difflib
import json
import os
import re
import statistics
import sys
import tempfile

SWAPS = {"‘": "'", "’": "'", "“": '"', "”": '"', "–": "-", "—": "-", " ": " "}
ELISION_RE = re.compile(r"\s*(?:\[\s*(?:\.\.\.|…)\s*\]|\(\s*\.\.\.\s*\)|…)\s*")
TEXT_EXT = (".txt", ".md", ".markdown", ".text", ".csv", ".tsv", ".vtt", ".srt")


def norm(text: str) -> str:
    for a, b in SWAPS.items():
        text = text.replace(a, b)
    return re.sub(r"\s+", " ", text).strip()


def found_in(extract: str, source: str) -> bool:
    """True if the extract, split at its elision marks, appears in order in the source."""
    parts = [p for p in ELISION_RE.split(norm(extract)) if p]
    if not parts:
        return False
    pos = 0
    for part in parts:
        hit = source.find(part, pos)
        if hit < 0:
            return False
        pos = hit + len(part)
    return True


def nearest(extract: str, source: str) -> str:
    """The stretch of the source that shares the most with the extract, for the error message."""
    ext = norm(extract)
    match = difflib.SequenceMatcher(None, source, ext, autojunk=False).find_longest_match(0, len(source), 0, len(ext))
    if match.size < 12:
        return "nothing close to it in the file"
    start = max(0, match.a - match.b)
    return "closest text in the file: \"" + source[start:start + len(ext) + 20].strip() + "\""


def read_sources(data_dir: str) -> dict:
    sources = {}
    for root, _, files in os.walk(data_dir):
        for name in sorted(files):
            if name.lower().endswith(TEXT_EXT):
                path = os.path.join(root, name)
                with open(path, encoding="utf-8", errors="replace") as fh:
                    sources[os.path.relpath(path, data_dir)] = norm(fh.read())
    return sources


def report_quotes(md: str) -> list:
    """Block quotes in the report, with a trailing '(P03)' style label removed."""
    quotes, chunk = [], []
    for line in md.split("\n") + [""]:
        s = line.strip()
        if s.startswith(">"):
            body = s[1:].strip()
            if body:
                chunk.append(body)
                continue
        if chunk:
            text = re.sub(r"\s*[\(\[][^()\[\]]{1,60}[\)\]]\s*$", "", " ".join(chunk))
            quotes.append(text.strip().strip('"').strip("“”").strip())
            chunk = []
    return [q for q in quotes if q]


def check(codes: list, sources: dict, report_md: str | None = None) -> dict:
    result = {"bad": [], "per_item": {}, "unread": [], "bad_quotes": [], "n": 0, "n_quotes": 0}
    used = set()
    for n, row in enumerate(codes, start=1):
        result["n"] += 1
        item = str(row.get("item") or row.get("file") or f"row {n}")
        rel = str(row.get("file") or "")
        extract = str(row.get("extract") or "")
        source = sources.get(rel)
        if source is None:  # tolerate a bare file name
            hits = [k for k in sources if os.path.basename(k) == os.path.basename(rel)]
            source = sources[hits[0]] if len(hits) == 1 else None
            rel = hits[0] if len(hits) == 1 else rel
        if source is None:
            result["bad"].append((n, item, extract, f"data file not found: {row.get('file')}"))
            continue
        used.add(rel)
        stats = result["per_item"].setdefault(rel, {"item": item, "extracts": 0, "codes": set(), "words": len(source.split())})
        stats["extracts"] += 1
        stats["codes"].update(str(c) for c in (row.get("codes") or []))
        if not row.get("codes"):
            result["bad"].append((n, item, extract, "no code attached"))
        if not found_in(extract, source):
            result["bad"].append((n, item, extract, nearest(extract, source)))
    result["unread"] = sorted(set(sources) - used)
    if report_md is not None:
        everything = " ".join(sources.values())
        for q in report_quotes(report_md):
            result["n_quotes"] += 1
            if not any(found_in(q, s) for s in sources.values()):
                result["bad_quotes"].append((q, nearest(q, everything)))
    return result


def thin_items(per_item: dict) -> list:
    """Items coded at less than half the typical density: a sign they were skimmed."""
    rates = {k: v["extracts"] / max(v["words"], 1) * 1000 for k, v in per_item.items()}
    if len(rates) < 3:
        return []
    typical = statistics.median(rates.values())
    return sorted(k for k, r in rates.items() if r < typical / 2)


def print_result(result: dict) -> int:
    print(f"Coded extracts checked: {result['n']}. Not matching the data: {len(result['bad'])}.")
    for n, item, extract, why in result["bad"]:
        print(f"  - row {n} ({item}): \"{extract[:110]}{'...' if len(extract) > 110 else ''}\"\n      {why}")
    print("\nExtracts per data item:")
    print(f"  {'file':<34} {'words':>7} {'extracts':>9} {'codes':>6} {'per 1,000 words':>16}")
    for rel, v in sorted(result["per_item"].items()):
        print(f"  {rel[:34]:<34} {v['words']:>7} {v['extracts']:>9} {len(v['codes']):>6} {v['extracts'] / max(v['words'], 1) * 1000:>16.1f}")
    thin = thin_items(result["per_item"])
    if thin:
        print("  Coded much more lightly than the rest; read these again: " + ", ".join(thin))
    if result["unread"]:
        print("  No extracts at all from: " + ", ".join(result["unread"]))
    if result["n_quotes"] or result["bad_quotes"]:
        print(f"\nQuotes in the report checked: {result['n_quotes']}. Not in the data: {len(result['bad_quotes'])}.")
        for q, why in result["bad_quotes"]:
            print(f"  - \"{q[:110]}{'...' if len(q) > 110 else ''}\"\n      {why}")
    failed = result["bad"] or result["bad_quotes"] or result["unread"]
    print("\nResult: " + ("problems found; fix them from the data, never by rewording the quote to fit." if failed
                         else "every extract and quote is in the data."))
    return 1 if failed else 0


def self_test() -> int:
    with tempfile.TemporaryDirectory() as tmp:
        with open(os.path.join(tmp, "a.txt"), "w", encoding="utf-8") as fh:
            fh.write("I: How is the app?\nR: I enter the visit even when nobody was home,\nbecause the dashboard is what she looks at. It’s tiring.\n")
        with open(os.path.join(tmp, "b.txt"), "w", encoding="utf-8") as fh:
            fh.write("R: The families trust the phone more than me.\n")
        sources = read_sources(tmp)
        codes = [
            {"item": "A", "file": "a.txt", "extract": "I enter the visit even when nobody was home, because the dashboard is what she looks at.", "codes": ["x"]},
            {"item": "A", "file": "a.txt", "extract": "I enter the visit [...] It's tiring.", "codes": ["y"]},
            {"item": "A", "file": "a.txt", "extract": "I always enter the visit because she checks the dashboard.", "codes": ["x"]},
        ]
        report = "> The families trust the phone more than me. (B)\n\n> They trust the screen, not me. (B)\n"
        result = check(codes, sources, report)
        assert [b[0] for b in result["bad"]] == [3], result["bad"]
        assert result["unread"] == ["b.txt"], result["unread"]
        assert result["n_quotes"] == 2 and len(result["bad_quotes"]) == 1, result["bad_quotes"]
        assert result["per_item"]["a.txt"]["extracts"] == 3
    print("self-test: passed (exact match across line breaks and curly quotes, elision marks, an altered quote caught, "
          "an uncoded item caught, report quotes checked).")
    return 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Check coded extracts and report quotes against the data.")
    ap.add_argument("codes", nargs="?", help="path to codes.json")
    ap.add_argument("--data", help="folder holding the data files (text or Markdown)")
    ap.add_argument("--report", help="the report in Markdown; its block quotes are checked too")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args(argv)
    if args.self_test:
        return self_test()
    if not args.codes or not args.data:
        ap.error("give codes.json and --data, or --self-test")
    try:
        with open(args.codes, encoding="utf-8") as fh:
            codes = json.load(fh)
        sources = read_sources(args.data)
        report_md = None
        if args.report:
            with open(args.report, encoding="utf-8") as fh:
                report_md = fh.read()
    except (OSError, json.JSONDecodeError) as err:
        print(f"Could not read the input: {err}", file=sys.stderr)
        return 2
    if not sources:
        print(f"No text files found under {args.data}. Convert Word or PDF files to .txt or .md first.", file=sys.stderr)
        return 2
    return print_result(check(codes, sources, report_md))


if __name__ == "__main__":
    sys.exit(main())
