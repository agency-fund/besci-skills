#!/usr/bin/env python3
"""
check_sync.py — keep bundled copies identical to their sources.

Several files are authored once at the repo root and shipped inside meta-skills
so they work in Claude Desktop / claude.ai, where the repo is not available:

  scripts/besci_validate.py         -> skills/besci-skill-creator/scripts/besci_validate.py
                                    -> skills/besci-eval/scripts/besci_validate.py
  docs/skill-spec.md                -> skills/besci-skill-creator/references/skill-spec.md
  template/skill-template/ (dir)    -> skills/besci-skill-creator/assets/skill-template/
  workflows/WORKFLOW-TEMPLATE.md    -> skills/besci-navigator/references/workflow-template.md
  skills/besci-skill-creator/references/checklist.md -> skills/besci-eval/references/checklist.md
  template/shared/citing-sources.md -> references/citing-sources.md in each skill that searches
                                       for studies or reads the studies it is given

Some text is shared as a block inside files rather than as a whole file:

  template/shared/voice.md          -> the block between VOICE_START and VOICE_END in
                                       template/skill-template/SKILL.md and in every
                                       skills/*/SKILL.md that carries the markers

CI fails if a copy drifts. `--fix` overwrites the copies from the sources.
A pair is skipped (exit 0) if the target's skill folder does not exist yet.
Blocks are synced before files, so the template folder copy carries the current block.
The validator, not this script, checks that a skill carries the markers at all.
"""
from __future__ import annotations

import argparse
import filecmp
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

PAIRS = [
    ("scripts/besci_validate.py", "skills/besci-skill-creator/scripts/besci_validate.py"),
    ("scripts/besci_validate.py", "skills/besci-eval/scripts/besci_validate.py"),
    ("docs/skill-spec.md", "skills/besci-skill-creator/references/skill-spec.md"),
    ("template/skill-template", "skills/besci-skill-creator/assets/skill-template"),
    ("workflows/WORKFLOW-TEMPLATE.md", "skills/besci-navigator/references/workflow-template.md"),
    ("skills/besci-skill-creator/references/checklist.md", "skills/besci-eval/references/checklist.md"),
    ("template/shared/citing-sources.md", "skills/assess-evidence-base/references/citing-sources.md"),
    ("template/shared/citing-sources.md", "skills/assess-evidence-transferability/references/citing-sources.md"),
    ("template/shared/citing-sources.md", "skills/estimate-expected-effect/references/citing-sources.md"),
]

# Shared blocks: (source file, start marker, end marker). The markers must match the
# validator's VOICE_START and VOICE_END.
VOICE_START = "<!-- shared: template/shared/voice.md. Edit it there, then run scripts/check_sync.py --fix. -->"
VOICE_END = "<!-- /shared -->"
BLOCKS = [("template/shared/voice.md", VOICE_START, VOICE_END)]


def block_targets() -> list:
    """The skill template and every skill's SKILL.md, repo-relative."""
    out = ["template/skill-template/SKILL.md"]
    skills = os.path.join(ROOT, "skills")
    if os.path.isdir(skills):
        for name in sorted(os.listdir(skills)):
            if os.path.exists(os.path.join(skills, name, "SKILL.md")):
                out.append(f"skills/{name}/SKILL.md")
    return out


def sync_blocks(fix: bool) -> int:
    problems = 0
    for src_rel, start, end in BLOCKS:
        src = os.path.join(ROOT, src_rel)
        if not os.path.exists(src):
            print(f"FAIL  source missing: {src_rel}")
            problems += 1
            continue
        with open(src, encoding="utf-8") as fh:
            want = fh.read().strip()
        for rel in block_targets():
            path = os.path.join(ROOT, rel)
            with open(path, encoding="utf-8") as fh:
                text = fh.read()
            if start not in text:
                continue
            head, rest = text.split(start, 1)
            if end not in rest:
                print(f"FAIL  {rel} opens the {src_rel} block but has no closing {end}")
                problems += 1
                continue
            have, tail = rest.split(end, 1)
            if have.strip() == want:
                print(f"ok    {rel} (block from {src_rel})")
            elif fix:
                with open(path, "w", encoding="utf-8") as fh:
                    fh.write(f"{head}{start}\n{want}\n{end}{tail}")
                print(f"fixed {rel} (block from {src_rel})")
            else:
                print(f"FAIL  {rel}: the block differs from {src_rel}. Edit {src_rel}, then run: uv run scripts/check_sync.py --fix")
                problems += 1
    return problems


def dirs_equal(a: str, b: str) -> bool:
    cmp = filecmp.dircmp(a, b, ignore=[".DS_Store", "__pycache__"])
    if cmp.left_only or cmp.right_only or cmp.diff_files or cmp.funny_files:
        return False
    return all(dirs_equal(os.path.join(a, d), os.path.join(b, d)) for d in cmp.common_dirs)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Check bundled copies match their sources.")
    ap.add_argument("--fix", action="store_true", help="Copy each source over its bundled copy.")
    args = ap.parse_args(argv)

    problems = sync_blocks(args.fix)
    for src_rel, dst_rel in PAIRS:
        src = os.path.join(ROOT, src_rel)
        dst = os.path.join(ROOT, dst_rel)
        skill_dir = os.path.join(ROOT, *dst_rel.split("/")[:2])
        if not os.path.exists(src):
            print(f"FAIL  source missing: {src_rel}")
            problems += 1
            continue
        if not os.path.isdir(skill_dir):
            print(f"skip  {dst_rel} (skill folder does not exist yet)")
            continue
        if args.fix:
            if os.path.isdir(src):
                if os.path.exists(dst):
                    shutil.rmtree(dst)
                shutil.copytree(src, dst, ignore=shutil.ignore_patterns(".DS_Store", "__pycache__"))
            else:
                os.makedirs(os.path.dirname(dst), exist_ok=True)
                shutil.copyfile(src, dst)
            print(f"fixed {dst_rel}")
            continue
        if not os.path.exists(dst):
            print(f"FAIL  {dst_rel} is missing. Run: uv run scripts/check_sync.py --fix")
            problems += 1
        elif os.path.isdir(src):
            if dirs_equal(src, dst):
                print(f"ok    {dst_rel}")
            else:
                print(f"FAIL  {dst_rel} differs from {src_rel}. Run: uv run scripts/check_sync.py --fix")
                problems += 1
        elif filecmp.cmp(src, dst, shallow=False):
            print(f"ok    {dst_rel}")
        else:
            print(f"FAIL  {dst_rel} differs from {src_rel}. Run: uv run scripts/check_sync.py --fix")
            problems += 1
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
