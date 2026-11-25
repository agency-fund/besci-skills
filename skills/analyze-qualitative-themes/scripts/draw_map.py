#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = ["matplotlib>=3.5"]
# ///
"""draw_map.py: draw a thematic map from a small JSON file.

A thematic map shows the themes of a thematic analysis, the sub-themes inside
each, and the relationships between them (Braun & Clarke, 2006, phases 3 to 5).
This script draws one as a picture: the research question in the middle, one
color per theme, sub-themes fanned around their theme, a dashed line for each
relationship between themes, and a strip for codes that were set aside.

Usage:
  python draw_map.py map.json --out thematic-map
      writes thematic-map.png, thematic-map.svg, and thematic-map.mmd
  python draw_map.py map.json --out thematic-map --mermaid-only
      writes thematic-map.mmd only (needs nothing installed)
  python draw_map.py --self-test

With uv, `uv run draw_map.py ...` installs matplotlib on its own. Without
matplotlib the script still writes the Mermaid file, says so, and exits 2.

map.json:
  {
    "title": "Final thematic map: <study in a few words>",
    "research_question": "<the question the analysis answers>",
    "themes": [
      {"name": "<theme>", "subthemes": ["<sub-theme>", "<sub-theme>"]}
    ],
    "relationships": [
      {"from": "<theme or sub-theme name>", "to": "<...>", "label": "in tension with"}
    ],
    "set_aside": ["<code kept out of every theme>"]
  }
"relationships" and "set_aside" may be left out. Names must be unique.
"""
from __future__ import annotations

import argparse
import itertools
import json
import math
import os
import sys
import tempfile
import textwrap

HUES = [
    {"fill": "#CFE6EC", "soft": "#F0F8FA", "stroke": "#3B7C8C", "text": "#17414B"},  # teal
    {"fill": "#F5DCC8", "soft": "#FCF3EB", "stroke": "#B5683A", "text": "#5C2F14"},  # clay
    {"fill": "#DDD6F0", "soft": "#F4F1FB", "stroke": "#6A58A8", "text": "#2F2559"},  # violet
    {"fill": "#D5E8D0", "soft": "#F1F8EF", "stroke": "#4E8A4A", "text": "#1F4420"},  # green
    {"fill": "#F3D6DE", "soft": "#FCF0F3", "stroke": "#A84E68", "text": "#521F30"},  # rose
    {"fill": "#F2E6B8", "soft": "#FBF7E4", "stroke": "#96801E", "text": "#473C08"},  # ochre
]
INK = "#2B2F36"
LINE = "#8A8F98"
ASIDE = {"fill": "#F3F3F0", "stroke": "#9A9A94", "text": "#55554F"}
REL = "#C2410C"
FONTS = ["Helvetica Neue", "Helvetica", "Arial", "DejaVu Sans"]
PX_TO_PT = 0.72  # the figure is laid out at 100 dpi, so 1 px = 0.72 pt


class MapError(ValueError):
    """The map file is missing something the drawing needs."""


def load_map(path: str) -> dict:
    with open(path, encoding="utf-8") as fh:
        raw = json.load(fh)
    return normalize(raw)


def normalize(raw: dict) -> dict:
    """Check the map and give every theme and sub-theme an id."""
    themes = raw.get("themes") or []
    if not themes:
        raise MapError("The map needs at least one theme under 'themes'.")
    if len(themes) > 8:
        raise MapError(f"The map has {len(themes)} themes. More than eight will not read as a picture; merge themes or draw one map per overarching theme.")
    out = {
        "title": str(raw.get("title") or "Thematic map"),
        "research_question": str(raw.get("research_question") or "").strip(),
        "themes": [],
        "relationships": [],
        "set_aside": [],
    }
    if not out["research_question"]:
        raise MapError("The map needs 'research_question': the question the analysis answers sits at the center.")
    by_name = {}
    for i, t in enumerate(themes, start=1):
        name = str(t.get("name") or "").strip()
        if not name:
            raise MapError(f"Theme {i} has no name.")
        subs = []
        for k, s in enumerate(t.get("subthemes") or []):
            s_name = str(s.get("name") if isinstance(s, dict) else s).strip()
            subs.append({"id": f"T{i}{chr(97 + k)}", "name": s_name})
        theme = {"id": f"T{i}", "name": name, "subthemes": subs}
        out["themes"].append(theme)
        for node in [theme] + subs:
            key = node["name"].lower()
            if key in by_name:
                raise MapError(f"Two entries are both named '{node['name']}'. Names must be unique so relationships can point to them.")
            by_name[key] = node["id"]
    for r in raw.get("relationships") or []:
        ends = []
        for side in ("from", "to"):
            key = str(r.get(side) or "").strip().lower()
            if key not in by_name:
                raise MapError(f"A relationship points to '{r.get(side)}', which is not a theme or sub-theme on the map. Names on the map: {', '.join(sorted(by_name))}.")
            ends.append(by_name[key])
        out["relationships"].append({"from": ends[0], "to": ends[1], "label": str(r.get("label") or "").strip()})
    aside = raw.get("set_aside") or []
    if isinstance(aside, dict):  # tolerate {"codes": [...]}
        aside = aside.get("codes") or []
    out["set_aside"] = [str(c).strip() for c in aside if str(c).strip()]
    return out


# ---------------------------------------------------------------- Mermaid

def mermaid(m: dict) -> str:
    """The same map as a Mermaid flowchart, for places that render Mermaid."""
    def br(s: str, w: int) -> str:
        return "<br/>".join(textwrap.wrap(s.replace('"', "'"), w))

    font = "Helvetica Neue, Helvetica, Arial"  # Mermaid drops values with a hyphen
    init = {
        "theme": "base", "fontFamily": font,
        "themeVariables": {"fontFamily": font, "fontSize": "15px", "lineColor": LINE,
                           "edgeLabelBackground": "#FFFFFF", "tertiaryColor": "#FFFFFF"},
        "flowchart": {"curve": "basis", "nodeSpacing": 16, "rankSpacing": 64, "padding": 12},
    }
    out = ["%%" + json.dumps({"init": init}).replace('{"init":', "{init:", 1) + "%%", "flowchart LR"]
    links = []
    out.append(f'  RQ(["{br(m["research_question"], 30)}"]):::rq')
    for i, t in enumerate(m["themes"]):
        h = HUES[i % len(HUES)]
        out.append(f'  {t["id"]}["{br(t["name"], 22)}"]:::t{i}')
        links.append((f'  RQ ==> {t["id"]}', f"stroke:{LINE},stroke-width:2.5px"))
        for s in t["subthemes"]:
            out.append(f'  {s["id"]}(["{br(s["name"], 26)}"]):::s{i}')
            links.append((f'  {t["id"]} --- {s["id"]}', f'stroke:{h["stroke"]},stroke-width:1.5px'))
    # A direct edge between two nodes would move one of them to a new column,
    # so each relationship is a small tag that both ends point to.
    for k, r in enumerate(m["relationships"]):
        out.append(f'  R{k}(["{br(r["label"] or "related to", 24)}"]):::rel')
        for end in (r["from"], r["to"]):
            links.append((f"  {end} -.- R{k}", f"stroke:{REL},stroke-width:2px,stroke-dasharray:6 5"))
    if m["set_aside"]:
        body = "<br/>".join(c.replace('"', "'") for c in m["set_aside"])
        out.append(f'  SA["<b>Set aside</b><br/>{body}"]:::aside')
    out.extend(line for line, _ in links)
    for i in range(len(m["themes"])):
        h = HUES[i % len(HUES)]
        out.append(f'  classDef t{i} fill:{h["fill"]},stroke:{h["stroke"]},color:{h["text"]},stroke-width:2px,font-weight:600')
        out.append(f'  classDef s{i} fill:{h["soft"]},stroke:{h["stroke"]},color:{h["text"]},stroke-width:1px')
    out.append(f"  classDef rq fill:{INK},stroke:{INK},color:#FFFFFF,font-weight:600")
    out.append(f"  classDef rel fill:#FFF7ED,stroke:{REL},color:{REL},stroke-dasharray:6 5,font-style:italic,font-size:13px")
    out.append(f'  classDef aside fill:{ASIDE["fill"]},stroke:{ASIDE["stroke"]},color:{ASIDE["text"]},stroke-dasharray:5 4,font-size:13px')
    for n, (_, style) in enumerate(links):
        out.append(f"  linkStyle {n} {style}")
    return "\n".join(out) + "\n"


# ---------------------------------------------------------------- picture

class Box:
    """A label with a measured size. x, y is the center, in pixels."""

    def __init__(self, measure, label, size, wrap, bold=False, padx=16, pady=10):
        self.lines = textwrap.wrap(label, wrap) or [""]
        self.size, self.bold = size, bold
        self.line_h = size * 1.3
        self.w = max(measure(line, size, bold) for line in self.lines) + 2 * padx
        self.h = len(self.lines) * self.line_h + 2 * pady
        self.x = self.y = 0.0

    def rect(self, margin=0.0):
        return (self.x - self.w / 2 - margin, self.y - self.h / 2 - margin,
                self.x + self.w / 2 + margin, self.y + self.h / 2 + margin)


def _overlap(a, b) -> bool:
    return not (a[2] <= b[0] or b[2] <= a[0] or a[3] <= b[1] or b[3] <= a[1])


def layout(m: dict, measure, scale: float = 1.0) -> dict:
    """Place every box. Themes sit on an inner ellipse, sub-themes on an outer one."""
    themes = m["themes"]
    extra = max(0, len(themes) - 3)
    rx1, ry1 = 322 * scale, 192 * scale
    rx2 = (520 + 30 * extra) * scale
    ry2 = (318 + 20 * extra) * scale
    padx, head, foot = 130, 70, 124
    width = 2 * (rx2 + padx)
    cx, cy = width / 2, head + ry2 + 44
    height = cy + ry2 + 44 + foot

    weights = [max(len(t["subthemes"]), 1) + 0.6 for t in themes]
    total = sum(weights)
    sectors, a = [], -90 - 360 * weights[0] / total / 2  # first theme at the top
    for wgt in weights:
        span = 360 * wgt / total
        sectors.append((a, span))
        a += span

    def pt(deg, rx, ry):
        r = math.radians(deg)
        return cx + rx * math.cos(r), cy + ry * math.sin(r)

    def leaf_angles(i, n):
        a0, span = sectors[i]
        inner = span * 0.80
        return [a0 + span / 2 - inner / 2 + inner * (k + 0.5) / n for k in range(n)]

    # Order sub-themes inside each theme so related ones sit close together.
    rels = m["relationships"]
    orders = [list(range(len(t["subthemes"]))) for t in themes]
    if rels:
        choices = [list(itertools.permutations(range(len(t["subthemes"])))) for t in themes]
        if math.prod(len(c) for c in choices) <= 20000:
            def cost(combo):
                pos = {}
                for i, (t, perm) in enumerate(zip(themes, combo)):
                    for ang, k in zip(leaf_angles(i, len(perm)), perm):
                        pos[t["subthemes"][k]["id"]] = pt(ang, rx2, ry2)
                    pos[t["id"]] = pt(sectors[i][0] + sectors[i][1] / 2, rx1, ry1)
                return sum(math.dist(pos[r["from"]], pos[r["to"]]) for r in rels)
            orders = [list(p) for p in min(itertools.product(*choices), key=cost)]

    rq = Box(measure, m["research_question"], 16, 30, bold=True, padx=24, pady=16)
    rq.x, rq.y = cx, cy
    pos, tboxes, sboxes = {}, [], []
    for i, t in enumerate(themes):
        b = Box(measure, t["name"], 15.5, 20, bold=True, padx=18, pady=12)
        b.x, b.y = pt(sectors[i][0] + sectors[i][1] / 2, rx1, ry1)
        tboxes.append(b)
        pos[t["id"]] = b
        row = []
        for ang, k in zip(leaf_angles(i, len(orders[i])), orders[i]):
            s = t["subthemes"][k]
            sb = Box(measure, s["name"], 13.5, 20)
            sb.x, sb.y = pt(ang, rx2, ry2)
            row.append(sb)
            pos[s["id"]] = sb
        sboxes.append(row)

    boxes = [rq] + tboxes + [b for row in sboxes for b in row]
    clash = any(_overlap(a_.rect(6), b_.rect(6)) for a_, b_ in itertools.combinations(boxes, 2))
    off = any(b.rect()[0] < 12 or b.rect()[2] > width - 12 for b in boxes)
    return {"w": width, "h": height, "cx": cx, "cy": cy, "foot": foot, "rq": rq, "themes": tboxes,
            "subs": sboxes, "pos": pos, "clash": clash or off}


def draw(m: dict, out_base: str) -> list:
    """Draw the map with matplotlib. Returns the files written."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.patches import FancyBboxPatch, PathPatch
    from matplotlib.path import Path

    plt.rcParams["font.family"] = FONTS
    plt.rcParams["svg.fonttype"] = "path"  # the SVG looks the same on any machine
    probe = plt.figure(figsize=(4, 4), dpi=100)
    renderer = probe.canvas.get_renderer()

    def measure(text, size, bold=False, italic=False):
        t = probe.text(0, 0, text, fontsize=size * PX_TO_PT, fontweight="bold" if bold else "normal",
                       fontstyle="italic" if italic else "normal")
        w = t.get_window_extent(renderer).width
        t.remove()
        return w

    scale, lay = 1.0, None
    for _ in range(12):  # grow the ellipses until no two boxes touch
        lay = layout(m, measure, scale)
        if not lay["clash"]:
            break
        scale *= 1.08
    plt.close(probe)

    width, height, cx, cy = lay["w"], lay["h"], lay["cx"], lay["cy"]
    fig = plt.figure(figsize=(width / 100, height / 100), dpi=100)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, width)
    ax.set_ylim(height, 0)
    ax.axis("off")
    fig.patch.set_facecolor("#FFFFFF")

    def put_text(x, y, s, size, color, bold=False, italic=False, ha="center", z=6):
        ax.text(x, y, s, fontsize=size * PX_TO_PT, color=color, ha=ha, va="center",
                fontweight="bold" if bold else "normal", fontstyle="italic" if italic else "normal", zorder=z)

    def put_box(b, fill, stroke, color, lw, radius=None, dash=None, z=4):
        r = min(b.h / 2, b.w / 2) if radius is None else radius
        ax.add_patch(FancyBboxPatch((b.x - b.w / 2, b.y - b.h / 2), b.w, b.h,
                                    boxstyle=f"round,pad=0,rounding_size={r}", facecolor=fill, edgecolor=stroke,
                                    linewidth=lw, linestyle=(0, dash) if dash else "-", zorder=z))
        y0 = b.y - (len(b.lines) - 1) * b.line_h / 2
        for i, line in enumerate(b.lines):
            put_text(b.x, y0 + i * b.line_h, line, b.size, color, bold=b.bold, z=z + 1)

    def curve(p, q, bow, color, lw, alpha=1.0, dash=None, z=2):
        mx, my = (p[0] + q[0]) / 2, (p[1] + q[1]) / 2
        dx, dy = mx - cx, my - cy
        d = math.hypot(dx, dy) or 1.0
        c = (mx + dx / d * bow, my + dy / d * bow)
        ax.add_patch(PathPatch(Path([p, c, q], [Path.MOVETO, Path.CURVE3, Path.CURVE3]), facecolor="none",
                               edgecolor=color, linewidth=lw, alpha=alpha, capstyle="round",
                               linestyle=(0, dash) if dash else "-", zorder=z))
        return (0.25 * p[0] + 0.5 * c[0] + 0.25 * q[0], 0.25 * p[1] + 0.5 * c[1] + 0.25 * q[1])

    put_text(40, 40, m["title"], 19, INK, bold=True, ha="left")

    rq = lay["rq"]
    for i, tb in enumerate(lay["themes"]):
        h = HUES[i % len(HUES)]
        curve((rq.x, rq.y), (tb.x, tb.y), 0, h["stroke"], 4.4, alpha=0.45)
        for sb in lay["subs"][i]:
            curve((tb.x, tb.y), (sb.x, sb.y), 22, h["stroke"], 1.4)

    for r in m["relationships"]:
        a_, b_ = lay["pos"][r["from"]], lay["pos"][r["to"]]
        mid = curve((a_.x, a_.y), (b_.x, b_.y), 46, REL, 1.7, dash=(4, 3.5), z=3)
        if r["label"]:
            lw_ = measure(r["label"], 12.5, italic=True) + 22
            tag = Box(lambda *_: lw_ - 22, r["label"], 12.5, 200, padx=11, pady=4)
            tag.x, tag.y = mid
            ax.add_patch(FancyBboxPatch((tag.x - tag.w / 2, tag.y - 12), tag.w, 24, boxstyle="round,pad=0,rounding_size=12",
                                        facecolor="#FFF7ED", edgecolor=REL, linewidth=0.8, zorder=7))
            put_text(tag.x, tag.y, r["label"], 12.5, REL, italic=True, z=8)

    for i, tb in enumerate(lay["themes"]):
        h = HUES[i % len(HUES)]
        for sb in lay["subs"][i]:
            put_box(sb, "#FFFFFF", h["stroke"], h["text"], 1.1)
        put_box(tb, h["fill"], h["stroke"], h["text"], 1.7, radius=14)
    put_box(rq, INK, INK, "#FFFFFF", 0, radius=22, z=5)

    fy = height - lay["foot"] + 34
    if m["set_aside"]:
        head = "Set aside (coded, in no theme)"
        x = 40.0
        chip_x = x + 18 + measure(head, 13, bold=True) + 12
        rows, row, limit = [], [], width - 380
        cur = chip_x
        for code in m["set_aside"]:
            cw = measure(code, 12.5) + 22
            if row and cur + cw > limit:
                rows.append(row)
                row, cur = [], chip_x
            row.append((code, cur, cw))
            cur += cw + 8
        rows.append(row)
        right = max(c[1] + c[2] for r_ in rows for c in r_) + 12
        strip_h = 26 + 30 * len(rows)
        top = fy - (strip_h - 52) / 2
        ax.add_patch(FancyBboxPatch((x, top), right - x, strip_h, boxstyle="round,pad=0,rounding_size=12",
                                    facecolor=ASIDE["fill"], edgecolor=ASIDE["stroke"], linewidth=0.9,
                                    linestyle=(0, (4, 3)), zorder=1))
        put_text(x + 18, top + strip_h / 2, head, 13, ASIDE["text"], bold=True, ha="left")
        for n, r_ in enumerate(rows):
            ry = top + 13 + 30 * n
            for code, c_x, cw in r_:
                ax.add_patch(FancyBboxPatch((c_x, ry), cw, 26, boxstyle="round,pad=0,rounding_size=13",
                                            facecolor="#FFFFFF", edgecolor=ASIDE["stroke"], linewidth=0.8, zorder=2))
                put_text(c_x + cw / 2, ry + 13, code, 12.5, ASIDE["text"])
    kx = width - 340
    ax.plot([kx, kx + 44], [fy + 16, fy + 16], color=LINE, linewidth=1.4)
    put_text(kx + 54, fy + 16, "theme and its sub-themes", 12.5, ASIDE["text"], ha="left")
    if m["relationships"]:
        ax.plot([kx, kx + 44], [fy + 38, fy + 38], color=REL, linewidth=1.7, linestyle=(0, (4, 3.5)))
        put_text(kx + 54, fy + 38, "relationship between themes", 12.5, ASIDE["text"], ha="left")

    written = []
    for ext, dpi in (("png", 200), ("svg", 100)):
        path = f"{out_base}.{ext}"
        fig.savefig(path, dpi=dpi, facecolor="#FFFFFF")
        written.append(path)
    plt.close(fig)
    if lay["clash"]:
        print("Note: some labels still touch after widening the map. Shorten the longest names or split the map.", file=sys.stderr)
    return written


EXAMPLE = {
    "title": "Final thematic map: community health workers and a digital job aid",
    "research_question": "How do community health workers make sense of a digital job aid in their daily visits?",
    "themes": [
        {"name": "The app as a second supervisor",
         "subthemes": ["Being watched through the data", "Entering visits to look busy", "Praise that never arrives"]},
        {"name": "Borrowed authority at the doorstep",
         "subthemes": ["The phone says so", "Families trust the screen", "Losing my own voice"]},
        {"name": "Work that spills past the visit", "subthemes": ["Syncing at night", "Paying for my own data"]},
    ],
    "relationships": [{"from": "Being watched through the data", "to": "Losing my own voice", "label": "in tension with"}],
    "set_aside": ["Phone battery", "Training day food", "Old paper registers"],
}


def self_test() -> int:
    m = normalize(EXAMPLE)
    text = mermaid(m)
    assert text.startswith("%%{init:") and "flowchart LR" in text, "Mermaid header"
    assert text.count(":::s") == 8 and text.count(":::t") == 3, "Mermaid nodes"
    try:
        normalize({"research_question": "q", "themes": [{"name": "A"}], "relationships": [{"from": "A", "to": "B"}]})
    except MapError:
        pass
    else:
        raise AssertionError("an unknown relationship end should be an error")
    big = {"research_question": "q " * 12, "themes": [
        {"name": f"A fairly long theme name number {i}", "subthemes": [f"Sub-theme {i}.{k} with a long label" for k in range(4)]}
        for i in range(6)]}
    with tempfile.TemporaryDirectory() as tmp:
        try:
            files = draw(m, os.path.join(tmp, "example")) + draw(normalize(big), os.path.join(tmp, "big"))
        except ImportError:
            print("self-test: Mermaid checks passed; matplotlib is not installed, so the picture was not tested.")
            return 0
        for f in files:
            assert os.path.getsize(f) > 2000, f
    print("self-test: passed (Mermaid text, error handling, and pictures for a small and a large map).")
    return 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Draw a thematic map from a JSON file.")
    ap.add_argument("map", nargs="?", help="path to the map JSON")
    ap.add_argument("--out", default="thematic-map", help="output path without extension (default: thematic-map)")
    ap.add_argument("--mermaid-only", action="store_true", help="write only the Mermaid file")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args(argv)
    if args.self_test:
        return self_test()
    if not args.map:
        ap.error("give the path to the map JSON, or --self-test")
    try:
        m = load_map(args.map)
    except (MapError, json.JSONDecodeError, OSError) as err:
        print(f"Could not read the map: {err}", file=sys.stderr)
        return 1
    out_dir = os.path.dirname(os.path.abspath(args.out))
    os.makedirs(out_dir, exist_ok=True)
    mmd = f"{args.out}.mmd"
    with open(mmd, "w", encoding="utf-8") as fh:
        fh.write(mermaid(m))
    written = [mmd]
    if not args.mermaid_only:
        try:
            written += draw(m, args.out)
        except ImportError:
            print(f"Wrote {mmd}. matplotlib is not installed, so no picture was drawn: "
                  "install it (pip install matplotlib, or run this script with uv), or use the Mermaid block in the report.",
                  file=sys.stderr)
            return 2
    print("Wrote " + ", ".join(written))
    return 0


if __name__ == "__main__":
    sys.exit(main())
