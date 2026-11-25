#!/usr/bin/env python3
"""
run_evals.py — diagnose a library skill through the Claude API.

Usage:
  python run_evals.py path/to/skill [--models claude-opus-5-5 claude-sonnet-5-5]
                                    [--runs 3] [--judge claude-opus-5-5]
                                    [--all-cases] [--cold "a request"] [--no-cold]
                                    [--skip-bare] [--baseline path/to/old-skill]
                                    [--catalog path/to/catalog.md]
                                    [--skip-trigger] [--skip-output] [--effort medium]
                                    [--out DIR] [--dry-run]

What it does:
  1. Structure: runs besci_validate.py (bundled next to this script).
  2. Triggering: for each request the skill should and should not fire on,
     asks a judge model whether it would load this skill, given its
     description and the descriptions of the other skills in the catalog
     snapshot.
  3. On the job: runs each case twice on each model, once with SKILL.md
     loaded and once with no skill, and asks the judge to compare the two
     answers without being told which is which: what the skill changed,
     whether the change is what the skill promises, which answer a
     practitioner would prefer, and which of the case's assertions each
     answer passes. --baseline adds the same comparison against an older
     version of the skill.

Cases: "Full run" and "Missing context" (or the first two cases when the
skill does not name them), plus one cold case the script writes from the
skill's description alone. --all-cases runs every case. A case named
"Wrong skill", or one with "should_trigger": false, is a triggering test and
is not run for output.

Writes <skill>-workspace/eval-<timestamp>/report.md and results.json.

Requires: pip install anthropic pyyaml. Credentials: ANTHROPIC_API_KEY, or an
`ant auth login` profile (the SDK picks it up with no env var).

Cost: this spends money. --dry-run prints the plan and the number of calls,
makes none, and writes nothing unless --out is given. Roughly: cases x models x runs x 3 for the comparison with
no skill (two answers and one judgement), plus one call per trigger request.

Limits: the with-skill run loads SKILL.md only, not the skill's reference
files, and every case is a single turn.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import re
import statistics
import sys
from typing import Dict, List, Optional

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import besci_validate as bv  # noqa: E402

DEFAULT_MODEL = "claude-opus-5-5"
JUDGING_PATH = os.path.join(os.path.dirname(HERE), "references", "judging.md")
DEFAULT_CASES = ["Full run", "Missing context"]
TRIGGER_ONLY_CASE = "Wrong skill"
# What the model is told when a case runs with no skill loaded.
NO_SKILL_SYSTEM = "Answer the user's request."


# ---------------------------------------------------------------------------
# API helpers
# ---------------------------------------------------------------------------

def get_client():
    try:
        import anthropic
    except ImportError:
        sys.stderr.write("pip install anthropic\n")
        sys.exit(2)
    return anthropic.Anthropic()


def call(client, model: str, system: str, user: str, effort: str, max_tokens: int = 16000) -> Dict:
    """One non-streaming Messages call. Returns {text, stop_reason, usage}."""
    resp = client.messages.create(
        model=model,
        max_tokens=max_tokens,
        system=system,
        output_config={"effort": effort},
        messages=[{"role": "user", "content": user}],
    )
    text = "".join(b.text for b in resp.content if getattr(b, "type", "") == "text")
    return {
        "text": text,
        "stop_reason": resp.stop_reason,
        "input_tokens": resp.usage.input_tokens,
        "output_tokens": resp.usage.output_tokens,
    }


def parse_json(text: str) -> Optional[dict]:
    """Find the first JSON object in a response; tolerate fences and prose."""
    m = re.search(r"\{.*\}", text, flags=re.DOTALL)
    if not m:
        return None
    try:
        return json.loads(m.group(0))
    except json.JSONDecodeError:
        return None


# ---------------------------------------------------------------------------
# The skill: its promise, its cases, its neighbors
# ---------------------------------------------------------------------------

def load_skill(path: str) -> bv.Skill:
    return bv.validate_skill(bv.parse_skill(path), bv.load_taxonomy())


def promise(skill: bv.Skill) -> str:
    """What the skill says it makes the AI do: its 'What this adds' line, or how it describes itself."""
    e = bv.catalog_entry(skill)
    return e["what_this_adds"] or e["what_it_does"] or e["description"]


def all_cases(skill: bv.Skill) -> List[dict]:
    cases = (skill.evals or {}).get("evals", []) if isinstance(skill.evals, dict) else []
    return [c for c in cases if isinstance(c, dict) and str(c.get("prompt", "")).strip()]


def should_fire(case: dict) -> bool:
    """Whether a test case is a request the skill should take."""
    if "should_trigger" in case:
        return bool(case["should_trigger"])
    if str(case.get("name", "")).strip() == TRIGGER_ONLY_CASE:
        return False
    expected = str(case.get("expected_output", "")).lower()
    return not any(k in expected for k in ("does not fire", "should not fire", "not a library skill", "does not take over"))


def output_cases(skill: bv.Skill, every: bool) -> List[dict]:
    """The cases run for output: requests the skill should take. By default the two that show most."""
    cases = [c for c in all_cases(skill) if should_fire(c)]
    if every:
        return cases
    named = [c for c in cases if str(c.get("name", "")).strip() in DEFAULT_CASES]
    return named if named else cases[:len(DEFAULT_CASES)]


def case_assertions(case: dict) -> List[str]:
    out = []
    for a in case.get("assertions") or []:
        text = (a.get("text") or a.get("description") or "") if isinstance(a, dict) else str(a)
        if text.strip():
            out.append(text.strip())
    return out


def neighbor_descriptions(catalog_path: Optional[str], this_name: str) -> List[Dict[str, str]]:
    """Name and description pairs from the navigator's catalog.md snapshot."""
    if not catalog_path or not os.path.exists(catalog_path):
        return []
    text = open(catalog_path, encoding="utf-8").read()
    details = text.split("## Skill details", 1)[-1].split("\n## ", 1)[0]
    out = []
    for block in re.split(r"^### ", details, flags=re.MULTILINE)[1:]:
        name = block.split("\n", 1)[0].strip().strip("`")
        if name == this_name:
            continue
        m = re.search(r"\*\*Description[^*]*:\*\*\s*(.+?)(?:\n\n|\n\*\*|\Z)", block, flags=re.DOTALL)
        if m:
            out.append({"name": name, "description": " ".join(m.group(1).split())})
    return out


COLD_SYSTEM = (
    "You write one test request for an AI skill. You see only the skill's name and description. "
    "Write what a busy program officer at an NGO would type when they need this: plain words, a real-sounding "
    "program with a place and numbers, something left out that they would not think to say, and none of the "
    "method's vocabulary. Three to six sentences. Reply with the request only."
)


def write_cold_case(client, judge: str, skill: bv.Skill, effort: str, dry: bool) -> str:
    if dry:
        return "(a cold case is written at run time from the description alone)"
    user = f"Skill: {skill.name}\nDescription: {skill.frontmatter.get('description', '')}"
    return call(client, judge, COLD_SYSTEM, user, effort, max_tokens=1000)["text"].strip()


# ---------------------------------------------------------------------------
# Check 1: structure
# ---------------------------------------------------------------------------

def check_structure(skill_dir: str) -> Dict:
    skills = bv.validate_path(skill_dir, bv.load_taxonomy())
    return {
        "report": bv.report_text(skills),
        "ok": all(not s.errors for s in skills),
        "errors": [f"[{f.code}] {f.file}: {f.message}" for s in skills for f in s.errors],
        "warnings": [f"[{f.code}] {f.file}: {f.message}" for s in skills for f in s.warnings],
    }


# ---------------------------------------------------------------------------
# Check 2: triggering
# ---------------------------------------------------------------------------

def trigger_cases(skill: bv.Skill, cold: List[str]) -> List[Dict]:
    should, should_not = bv.trigger_phrases(skill)
    cases = [{"phrase": p, "should_fire": True, "source": "use it when"} for p in should]
    cases += [{"phrase": p, "should_fire": False, "source": "do not use it when"} for p in should_not]
    for c in all_cases(skill):
        cases.append({"phrase": c["prompt"], "should_fire": should_fire(c), "source": f"test case {c.get('name') or c.get('id')}"})
    cases += [{"phrase": p, "should_fire": True, "source": "cold case"} for p in cold]
    return cases


TRIGGER_SYSTEM = (
    "You are the skill-selection step of an AI assistant. You see a user's request and the "
    "descriptions of the skills installed. Decide whether you would load the skill named "
    "TARGET for this request. Answer with JSON only: {\"fire\": true|false, \"reason\": \"one line\"}."
)


def check_trigger(client, judge: str, skill: bv.Skill, neighbors: List[Dict], cold: List[str], effort: str, dry: bool) -> Dict:
    desc = str(skill.frontmatter.get("description", ""))
    neigh = "\n".join(f"- {n['name']}: {n['description']}" for n in neighbors) or "- (no other skills installed)"
    results = []
    for c in trigger_cases(skill, cold):
        if dry:
            results.append({**c, "fired": None, "reason": "dry run"})
            continue
        user = (f"TARGET skill: {skill.name}\nTARGET description: {desc}\n\nOther installed skills:\n{neigh}\n\n"
                f"User request: {c['phrase']}\n\nWould you load TARGET? JSON only.")
        j = parse_json(call(client, judge, TRIGGER_SYSTEM, user, effort, max_tokens=512)["text"]) or {}
        results.append({**c, "fired": bool(j.get("fire")), "reason": str(j.get("reason", ""))[:240]})
    should = [r for r in results if r["should_fire"]]
    should_not = [r for r in results if not r["should_fire"]]
    return {
        "cases": results,
        "neighbors": len(neighbors),
        "hits": sum(1 for r in should if r["fired"]), "should": len(should),
        "false_alarms": sum(1 for r in should_not if r["fired"]), "should_not": len(should_not),
    }


# ---------------------------------------------------------------------------
# Check 3: on the job
# ---------------------------------------------------------------------------

def load_judging() -> str:
    if os.path.exists(JUDGING_PATH):
        return open(JUDGING_PATH, encoding="utf-8").read()
    return ("Compare the two answers for the job the request describes. Blocking findings: an invented citation, "
            "a full answer when the request lacked something the skill needs, a missed handoff to a specialist.")


JUDGE_SYSTEM = (
    "You compare two answers, A and B, to the same request. They were written under different conditions, such as "
    "with a skill loaded and without it, and you are not told which is which. Judge them for the job the request "
    "describes, following the guidance you are given. Be strict and quote the answers. Return JSON only, in this shape: "
    "{\"difference\": \"one or two sentences on what A does that B does not, and the reverse\", "
    "\"prefer\": \"A\"|\"B\"|\"tie\", \"why\": \"one sentence, in terms of the job\", "
    "\"A\": {\"keeps_promise\": true|false, \"assertions\": [true|false for each numbered assertion, in order], "
    "\"blocking\": [\"...\"], \"excerpt\": \"the most telling quote, under 40 words\"}, \"B\": {the same keys}}"
)


def a_first(*parts) -> bool:
    """Which answer is shown as A. Fixed by the case, model, and run, so a rerun shows the same order."""
    return int(hashlib.sha256("|".join(str(p) for p in parts).encode()).hexdigest(), 16) % 2 == 0


def judge_pair(client, judge: str, guidance: str, skill: bv.Skill, skill_md: str, case: dict, asserts: List[str],
               with_text: str, other_text: str, with_is_a: bool, effort: str) -> Dict:
    a, b = (with_text, other_text) if with_is_a else (other_text, with_text)
    user = (
        f"GUIDANCE:\n{guidance}\n\nTHE SKILL'S PROMISE (what it says it makes the AI do):\n{promise(skill)}\n\n"
        f"THE SKILL'S TEXT (a source is the skill's own only if it appears here):\n{skill_md}\n\n"
        f"REQUEST:\n{case['prompt']}\n\nWHAT A GOOD ANSWER IS:\n{case.get('expected_output') or '(not stated; judge from the request and the promise)'}\n\n"
        "ASSERTIONS (answer true or false for each, for A and for B):\n"
        + ("\n".join(f"{n}. {t}" for n, t in enumerate(asserts, 1)) or "(none)")
        + f"\n\nANSWER A:\n{a}\n\nANSWER B:\n{b}\n\nCompare them. JSON only."
    )
    j = parse_json(call(client, judge, JUDGE_SYSTEM, user, effort, max_tokens=4000)["text"]) or {}

    def side(key: str) -> Dict:
        d = j.get(key) if isinstance(j.get(key), dict) else {}
        verdicts = d.get("assertions") if isinstance(d.get("assertions"), list) else []
        verdicts = [bool(v) for v in verdicts[:len(asserts)]] + [False] * max(0, len(asserts) - len(verdicts))
        return {"keeps_promise": d.get("keeps_promise"), "assertions": verdicts,
                "blocking": [str(x) for x in d.get("blocking") or []], "excerpt": str(d.get("excerpt", ""))[:400]}

    prefer = str(j.get("prefer", "tie")).strip().upper()
    winner = "tie" if prefer not in ("A", "B") else ("with" if (prefer == "A") == with_is_a else "other")
    return {"difference": str(j.get("difference", "")), "why": str(j.get("why", "")), "prefer": winner,
            "with": side("A" if with_is_a else "B"), "other": side("B" if with_is_a else "A")}


def check_output(client, models: List[str], runs: int, judge: str, skill: bv.Skill, skill_md: str, cases: List[dict],
                 others: Dict[str, str], effort: str, dry: bool) -> Dict:
    """Run every case with the skill and under each other condition (no skill, an older version), and compare.

    `others` maps a condition's label to the system prompt it runs with."""
    guidance = load_judging()
    out = {"conditions": list(others), "models": {}}
    for model in models:
        per_case = []
        for c in cases:
            asserts = case_assertions(c)
            run_results = []
            for i in range(runs):
                if dry:
                    continue
                w = call(client, model, skill_md, c["prompt"], effort)
                r = {"run": i + 1, "with_output": w["text"], "refused": w["stop_reason"] == "refusal", "comparisons": {}}
                for label, system in others.items():
                    o = call(client, model, system, c["prompt"], effort)
                    cmp_ = judge_pair(client, judge, guidance, skill, skill_md, c, asserts, w["text"], o["text"],
                                      a_first(c.get("id"), model, i, label), effort)
                    cmp_["other_output"] = o["text"]
                    r["comparisons"][label] = cmp_
                if not others:  # nothing to compare with: grade the with-skill answer against itself for assertions only
                    r["comparisons"]["(alone)"] = judge_pair(client, judge, guidance, skill, skill_md, c, asserts, w["text"],
                                                             "(no second answer was run; grade A only and answer 'tie')", True, effort)
                run_results.append(r)
            per_case.append(summarize_case(c, asserts, run_results, list(others) or ["(alone)"]))
        out["models"][model] = {"cases": per_case}
    return out


def summarize_case(case: dict, asserts: List[str], runs: List[Dict], labels: List[str]) -> Dict:
    def med(values):
        return statistics.median(values) if values else None

    comparisons = {}
    for label in labels:
        cmps = [r["comparisons"][label] for r in runs if label in r["comparisons"]]
        failing = [a for n, a in enumerate(asserts)
                   if cmps and sum(1 for x in cmps if not x["with"]["assertions"][n]) * 2 > len(cmps)]
        comparisons[label] = {
            "runs": len(cmps),
            "prefer_with": sum(1 for x in cmps if x["prefer"] == "with"),
            "prefer_other": sum(1 for x in cmps if x["prefer"] == "other"),
            "ties": sum(1 for x in cmps if x["prefer"] == "tie"),
            "keeps_promise": sum(1 for x in cmps if x["with"]["keeps_promise"]),
            "assertions_with": med([sum(x["with"]["assertions"]) for x in cmps]),
            "assertions_other": med([sum(x["other"]["assertions"]) for x in cmps]),
            "failing_assertions": failing,
            "blocking": sorted({b for x in cmps for b in x["with"]["blocking"]}),
            "difference": next((x["difference"] for x in cmps if x["difference"]), ""),
            "why": next((x["why"] for x in cmps if x["why"]), ""),
            "excerpt_with": next((x["with"]["excerpt"] for x in cmps if x["with"]["excerpt"]), ""),
            "excerpt_other": next((x["other"]["excerpt"] for x in cmps if x["other"]["excerpt"]), ""),
        }
    return {"id": case.get("id"), "name": str(case.get("name") or f"case {case.get('id')}"), "prompt": case["prompt"],
            "assertions": asserts, "runs": runs, "comparisons": comparisons,
            "refused": any(r.get("refused") for r in runs)}


# ---------------------------------------------------------------------------
# Report
# ---------------------------------------------------------------------------

def of(n, total) -> str:
    return f"{n:g} of {total}" if n is not None else f"n/a of {total}"


def clip(text: str, n: int) -> str:
    text = " ".join(str(text).split())
    return text if len(text) <= n else text[: n - 1].rstrip() + "…"


def findings(structure: Dict, trigger: Optional[Dict], output: Optional[Dict]) -> Dict:
    """What decides the verdict, and the list of things to fix, most important first."""
    fixes: List[str] = []
    blocking: List[str] = []
    not_preferred: List[str] = []
    compared = 0
    if output:
        for m, d in output["models"].items():
            for p in d["cases"]:
                if p.get("refused"):
                    blocking.append(f"{p['name']} on {m}: the model refused the request with the skill loaded.")
                for label, c in p["comparisons"].items():
                    blocking += [f"{p['name']} on {m}: {b}" for b in c["blocking"]]
                    if label == "no skill" and c["runs"]:
                        compared += 1
                        if c["prefer_with"] * 2 <= c["runs"]:
                            not_preferred.append(f"{p['name']} on {m}: the answer with the skill was preferred in {of(c['prefer_with'], c['runs'])} runs. {clip(c['why'], 200)}")
    fixes += [f"Blocking: {b}" for b in blocking]
    fixes += [f"Validator: {e}" for e in structure["errors"]]
    misses, alarms = [], []
    if trigger:
        misses = [c for c in trigger["cases"] if c["should_fire"] and c["fired"] is False]
        alarms = [c for c in trigger["cases"] if not c["should_fire"] and c["fired"]]
        fixes += [f"The description misses a request it should take: \"{clip(c['phrase'], 110)}\". {clip(c['reason'], 160)}" for c in misses]
        fixes += [f"The description takes a request it should leave: \"{clip(c['phrase'], 110)}\". {clip(c['reason'], 160)}" for c in alarms]
    fixes += [f"Adds little: {n}" for n in not_preferred]
    if output:
        for m, d in output["models"].items():
            for p in d["cases"]:
                for c in p["comparisons"].values():
                    fixes += [f"{p['name']} on {m} fails its check: \"{clip(a, 140)}\"" for a in c["failing_assertions"]]
    return {"fixes": fixes, "blocking": blocking, "misses": misses, "alarms": alarms,
            "not_preferred": not_preferred, "compared": compared}


def verdict_of(args, structure: Dict, trigger: Optional[Dict], output: Optional[Dict], f: Dict) -> tuple:
    if args.dry_run:
        return "dry run", "no calls were made"
    if not trigger and not output:
        return ("fix first", "the validator reports errors") if not structure["ok"] else ("could not test", "only the structure was checked")
    if f["blocking"]:
        return "fix first", clip(f["blocking"][0], 200)
    if not structure["ok"]:
        return "fix first", "the validator reports errors"
    if f["compared"] and len(f["not_preferred"]) * 2 > f["compared"]:
        return "fix first", "on most cases the answer with the skill was not preferred over the model alone"
    if trigger and (trigger["should"] and trigger["hits"] / trigger["should"] < 0.8
                    or trigger["should_not"] and trigger["false_alarms"] / trigger["should_not"] > 0.2):
        return "fix first", "the description fires on the wrong requests"
    if f["fixes"]:
        return "ready", "the checks pass, with smaller things to fix listed below"
    return "ready", "the structure passes, the description fires where it should, and the skill changes the answers in the way it promises"


def write_report(path: str, skill: bv.Skill, args, structure: Dict, trigger: Optional[Dict], output: Optional[Dict]) -> str:
    f = findings(structure, trigger, output)
    verdict, why = verdict_of(args, structure, trigger, output, f)
    lines = [f"# Diagnosis: {skill.name} v{skill.metadata.get('version', '?')}  ({dt.date.today().isoformat()})", "",
             f"**Verdict:** {verdict}. {why[0].upper() + why[1:]}.".replace("..", "."), ""]

    lines += ["## Structure", ""]
    kind = str(skill.metadata.get("type", "")).strip()
    scope = {"meta": " A meta-skill is checked on its frontmatter, files, test cases, and changelog only.",
             "supporting": " A supporting skill is checked on its frontmatter and files only."}.get(kind, "")
    if structure["ok"]:
        lines += [f"The validator passes{', with ' + str(len(structure['warnings'])) + ' warning(s)' if structure['warnings'] else ''}.{scope}"]
    else:
        lines += [f"The validator reports {len(structure['errors'])} error(s).{scope}"]
    lines += [f"- {clip(x, 300)}" for x in structure["errors"] + structure["warnings"]] + [""]

    if trigger:
        lines += ["## Triggering", ""]
        if args.dry_run:
            lines += [f"{len(trigger['cases'])} requests would be judged against {trigger['neighbors']} other skills' descriptions.", ""]
        else:
            lines += [f"It fired on {of(trigger['hits'], trigger['should'])} requests it should take, and on "
                      f"{of(trigger['false_alarms'], trigger['should_not'])} it should leave, judged next to {trigger['neighbors']} other skills' descriptions."]
            lines += [f"- Missed ({c['source']}): \"{clip(c['phrase'], 140)}\". {clip(c['reason'], 200)}" for c in f["misses"]]
            lines += [f"- False alarm ({c['source']}): \"{clip(c['phrase'], 140)}\". {clip(c['reason'], 200)}" for c in f["alarms"]]
            lines += [""]

    if output:
        lines += ["## On the job", ""]
        shown = False
        for m, d in output["models"].items():
            for p in d["cases"]:
                head = f"**{p['name']}**" + (f" ({m})" if len(output["models"]) > 1 else "")
                if args.dry_run:
                    lines += [f"{head}: \"{clip(p['prompt'], 160)}\""]
                    continue
                n_a = len(p["assertions"])
                for label, c in p["comparisons"].items():
                    if label == "(alone)":
                        lines += [f"{head}: the checks passed {of(c['assertions_with'], n_a)}. No comparison was run."]
                        continue
                    lines += [f"{head}, with the skill against {label}: the answer with the skill was preferred in {of(c['prefer_with'], c['runs'])} run(s)"
                              f"{', tied in ' + str(c['ties']) if c['ties'] else ''}, and did what the skill promises in {of(c['keeps_promise'], c['runs'])}."
                              + (f" Checks passed: {of(c['assertions_with'], n_a)} with the skill, {of(c['assertions_other'], n_a)} with {label}." if n_a else "")
                              + f" {clip(c['difference'], 320)}"]
                    if not shown and c["excerpt_with"] and c["excerpt_other"]:
                        lines += ["", f"> With the skill: \"{clip(c['excerpt_with'], 280)}\"", ">", f"> With {label}: \"{clip(c['excerpt_other'], 280)}\""]
                        shown = True
                lines += [""]
        if args.dry_run:
            lines += [""]

    lines += ["## What to fix", ""]
    lines += [f"{i}. {x}" for i, x in enumerate(f["fixes"][:3], 1)] or ["Nothing found on these cases."]
    if len(f["fixes"]) > 3:
        lines += [f"", f"{len(f['fixes']) - 3} smaller finding(s) are in results.json."]
    lines += ["", "These are proposals. The author decides what to change, and `besci-skill-creator` helps revise.", ""]

    lines += ["## How this was run", "",
              f"By script through the API: {', '.join(args.models)}, {args.runs} run(s) per case, judged by {args.judge}. "
              "The with-skill run loads SKILL.md only, not the skill's reference files, and every case is one turn. "
              "Which answer is better is a model's judgment and not a practitioner's; expert reviews on the library site are the test of that. "
              "Full answers are in results.json beside this report."]
    text = "\n".join(lines) + "\n"
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)
    return verdict


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main(argv: Optional[List[str]] = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("skill")
    ap.add_argument("--models", nargs="+", default=[DEFAULT_MODEL])
    ap.add_argument("--judge", default=DEFAULT_MODEL)
    ap.add_argument("--runs", type=int, default=3)
    ap.add_argument("--all-cases", action="store_true", help="Run every case the skill should take, not only the default two")
    ap.add_argument("--cold", action="append", default=[], help="A cold-case request to use instead of having one written (repeatable)")
    ap.add_argument("--no-cold", action="store_true", help="Do not add a cold case")
    ap.add_argument("--skip-bare", action="store_true", help="Do not run the cases with no skill loaded (halves the cost, and loses the comparison)")
    ap.add_argument("--baseline", help="Path to an older version of the skill folder to compare against as well")
    ap.add_argument("--no-skill-baseline", action="store_true", help=argparse.SUPPRESS)  # earlier flag; the comparison is now the default
    ap.add_argument("--catalog", help="Path to catalog.md (default: besci-navigator/references/catalog.md if found)")
    ap.add_argument("--effort", default="medium", choices=["low", "medium", "high", "xhigh", "max"])
    ap.add_argument("--skip-trigger", action="store_true")
    ap.add_argument("--skip-output", action="store_true")
    ap.add_argument("--out", help="Output directory (default: <skill>-workspace/eval-<timestamp>)")
    ap.add_argument("--dry-run", action="store_true", help="Plan only; make no API calls")
    args = ap.parse_args(argv)

    skill = load_skill(args.skill)
    if not skill.name:
        sys.stderr.write("Not a skill folder (no valid SKILL.md).\n")
        return 2
    skill_md = open(os.path.join(skill.path, "SKILL.md"), encoding="utf-8").read()
    structure = check_structure(skill.path)

    catalog = args.catalog
    if not catalog:
        root = bv.find_repo_root(skill.path) or os.getcwd()
        cand = os.path.join(root, "skills", "besci-navigator", "references", "catalog.md")
        catalog = cand if os.path.exists(cand) else None
    neighbors = neighbor_descriptions(catalog, skill.name)

    others: Dict[str, str] = {}
    if not args.skip_bare:
        others["no skill"] = NO_SKILL_SYSTEM
    if args.baseline:
        old = load_skill(args.baseline)
        others[f"the older version ({old.metadata.get('version', '?')})"] = open(os.path.join(old.path, "SKILL.md"), encoding="utf-8").read()

    cases = [] if args.skip_output else output_cases(skill, args.all_cases)
    n_cold = len(args.cold) if args.cold else (0 if args.no_cold else 1)
    write_cold = 0 if (args.cold or args.no_cold) else 1
    n_out_cases = 0 if args.skip_output else len(cases) + n_cold
    if not args.skip_output and n_out_cases == 0:
        sys.stderr.write(f"{skill.name} has no test case to run and no cold case. Add a case, or drop --no-cold.\n")
        return 1
    per_run = 1 + 2 * len(others) if others else 2
    n_output = n_out_cases * len(args.models) * args.runs * per_run
    n_trigger = 0 if args.skip_trigger else len(trigger_cases(skill, [""] * n_cold))
    print(f"Plan: {skill.name} v{skill.metadata.get('version', '?')} | models {args.models} | judge {args.judge} | runs {args.runs}")
    print(f"Cases run for output: {', '.join(str(c.get('name') or c.get('id')) for c in cases) or 'none'}" + (f", plus {n_cold} cold case(s)" if n_cold and not args.skip_output else ""))
    print(f"Compared with: {', '.join(others) or 'nothing'}")
    print(f"Calls: cold case {write_cold}, trigger {n_trigger}, on the job {n_output}, total {write_cold + n_trigger + n_output}")

    if args.dry_run and not args.out:
        print("Dry run: no calls were made and nothing was written. Add --out DIR to save the plan.")
        return 0

    client = None if args.dry_run else get_client()
    cold = list(args.cold)
    if write_cold:
        cold = [write_cold_case(client, args.judge, skill, args.effort, args.dry_run)]
    if not args.skip_output:
        cases = cases + [{"id": f"cold-{i}", "name": "Cold case", "prompt": p, "expected_output": "", "assertions": []} for i, p in enumerate(cold, 1)]

    trigger = None if args.skip_trigger else check_trigger(client, args.judge, skill, neighbors, cold, args.effort, args.dry_run)
    output = None if args.skip_output else check_output(client, args.models, args.runs, args.judge, skill, skill_md, cases, others, args.effort, args.dry_run)

    stamp = dt.datetime.now().strftime("%Y%m%d-%H%M")
    out_dir = args.out or os.path.join(os.path.dirname(skill.path), f"{skill.name}-workspace", f"eval-{stamp}")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "results.json"), "w", encoding="utf-8") as fh:
        json.dump({"skill": skill.name, "version": skill.metadata.get("version"), "args": vars(args),
                   "structure": structure, "trigger": trigger, "output": output}, fh, indent=2, default=str)
    verdict = write_report(os.path.join(out_dir, "report.md"), skill, args, structure, trigger, output)
    print(f"Verdict: {verdict}")
    print(f"Wrote {out_dir}/report.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
