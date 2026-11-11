# Skill specification

This is the authoring guideline for every skill in the Behavioral Science Skills Library. The validator in `scripts/besci_validate.py` enforces everything marked **required**. `besci-skill-creator` interviews you against this spec; you can also write a skill by hand with `template/skill-template/`.

A skill is a folder:

```
skills/<name>/
├── SKILL.md                      required: frontmatter + eight sections
├── evals/evals.json              required: four named test cases
├── CHANGELOG.md                  required: one entry per version
├── references/worked-example.md  required for atomic skills
├── references/evidence.md        required for atomic skills
├── references/                   optional: other material loaded on demand
├── scripts/                      optional: code the AI can run
└── assets/                       optional: templates used in output
```

No `README.md` inside a skill folder.

## 1. What earns a place

An atomic skill stays in the library if it passes three tests.

1. **Common.** Its task is a named step or tool in two or more of the sources in `docs/canonical-sources.md`. One study's technique does not pass.
2. **Adds something.** One line can state what the skill makes the AI do that it would not do unprompted. That line goes in the skill (section 4).
3. **Distinct.** No other skill produces the same output template.

The library also carries a few frameworks by choice; `docs/canonical-sources.md` lists them. A skill built on one of them skips the first test only, and says whose method it is.

## 2. The name

**Required.** Kebab-case, 1 to 64 characters, matches the folder name, and starts with a verb from the `verbs` list in `taxonomy.yaml`. Meta-skills (`besci-*`) are exempt from the verb rule.

The verb-first name is the atomicity rule applied to the folder: if you cannot start the name with one verb, you have more than one skill.

| Good | Not this |
|---|---|
| `decompose-comb-barriers` | `comb-barrier-decomposer` |
| `define-key-behavior` | `behavior-definition` |
| `draft-cognitive-interview-script` | `cognitive-interviews` |

American spelling throughout: behavior, analyze, program.

## 3. Frontmatter

Only the keys allowed by the [Agent Skills spec](https://agentskills.io/specification) may appear at the top level. Everything the catalog needs goes under `metadata` as plain strings. Lists are comma-separated strings, because the spec allows string values only.

```yaml
---
name: decompose-comb-barriers
description: >-
  Use when one behavior is already defined (who does what, when) and you
  need to know why it is not happening. Lists competing capability,
  opportunity, and motivation barriers with a question that tests each.
  Do not use when the goal is still vague; use define-key-behavior. Not
  for choosing interventions; use select-intervention-levers.
license: CC-BY-4.0
metadata:
  title: Find out why people are not doing a behavior
  type: atomic
  stage: diagnose
  version: "0.2.0"
  status: draft
  authors: "Nikhil Ravichandar"
  org: IL
  tested_in: beyond-western-differs
  tags: "com-b, behavior-change-wheel"
  consumes: "target-behavior-brief"
  produces: "comb-barrier-hypotheses"
---
```

| Field | Required | Rule |
|---|---|---|
| `name` | yes | See section 2. |
| `description` | yes | The compressed trigger rule. It must contain a "Use when ..." clause and a "Do not use when ..." clause naming the nearest adjacent intent, and no `<` or `>`. This is the only text the AI reads before deciding to load the skill. Aim for about 500 characters and leave citations out; `besci-navigator` does the routing, so the description need not hold every phrasing. The validator warns above 600 characters and fails above 1024. |
| `license` | yes | `CC-BY-4.0` for skill content. `MIT` only for a skill that is code with no method content. |
| `metadata.title` | no | Human-readable name for the catalog. Defaults to the name. |
| `metadata.type` | yes | `atomic` or `meta`. |
| `metadata.stage` | yes | One of `define`, `diagnose`, `design`, `measure`, `test`, `analyze`, `implement`, or `other`. The seven are strong recommendations; `other` is accepted with a warning. See the crosswalk in `docs/taxonomy.md`. |
| `metadata.version` | yes | Semver, quoted: `"0.2.0"`. Bump in the same change as the CHANGELOG entry. |
| `metadata.status` | yes | `draft`, `published`, or `deprecated`. Submit as `draft`; a maintainer sets `published` on merge. |
| `metadata.authors` | yes | Names or GitHub handles, comma-separated. |
| `metadata.org` | yes | `TAF`, `IL`, or `community`. |
| `metadata.tested_in` | atomic only | Where the evidence has been tested: `beyond-western-holds`, `beyond-western-differs`, `mainly-western`, or `not-applicable`. The value follows from the evidence scan (section 7). |
| `metadata.tags` | no | Free-form, comma-separated. See `suggested_tags` in `taxonomy.yaml` for consistent spelling. |
| `metadata.consumes` | no | The inputs the skill cannot run without, as ids from `io_types` in `taxonomy.yaml`. It matches the "Required" questions in "Before you start". Leave optional inputs out. |
| `metadata.produces` | atomic only | Exactly one `io_types` id: the thing the output template is. |
| `metadata.reviewed_by` | no | Set by the reviewer at merge. |

`consumes` and `produces` draw the arrows on the site's map. An arrow says one skill's output can feed another; it is a suggestion for building a workflow, not a rule about where an input must come from.

## 4. The eight sections

**Required**, in this order, each as a level-2 heading with exactly this text. The validator fails on a missing, empty, or reordered section.

Keep `SKILL.md` to about 1,000 words, not counting the output template. Apply one test to every sentence: it stays only if deleting it would change what the AI does or what the reader decides. The validator warns above 1,000 words.

### `## What it does`

One sentence, no "and". Then one labeled line:

```markdown
**What this adds:** <what the skill makes the AI do that it would not do unprompted>
```

The line names concrete behavior: a fixed output, a required check, a decision rule, verified sources, or a search or script call. "Structured" and "rigorous" do not count. The site shows this line at the top of the skill's page.

### `## When to use it`

The full trigger rule. The `description` is the compressed version that fires the skill; this section is the complete list, read by people on the site and by `besci-eval`, which turns every bullet into a trigger test. Two level-3 subheadings, exactly:

```markdown
### Use it when
- (at least three) user intents or phrasings that should invoke this skill
### Do not use it when
- (at least two) adjacent intents that should not, each naming where to go instead
```

"Do not use it when" is the one place a skill names another skill.

### `## Before you start`

The questions the skill asks the user before it produces anything. A skill should not produce output on a guess it could have checked with one question. List the questions, say which are required, and say what the skill assumes if an answer is missing.

Ask for an input by what it is ("a confirmed barrier, from interviews or any diagnosis"), not by which skill made it. People bring inputs from anywhere.

**May be "Not applicable: <reason>"** when the skill does not need to ask, for instance because it transforms an input the user has already supplied in full. The reason must be a real sentence.

### `## What it draws on`

The evidence base: the framework, paper, or practice the skill puts to work. List each source as a full citation with a link, followed by one line on what it supports in the skill. Then two labeled notes:

```markdown
**Where the evidence comes from:** <three sentences at most>

**Replication status:** <one sentence>
```

- **Where the evidence comes from** says which countries and populations were studied, what was found outside wealthy Western countries, and what to check where the user works.
- **Replication status** says replicated, mixed, contested, or single-study.

The fuller account goes in `references/evidence.md`. "Common sense" or "general best practice" is not an evidence base. If the skill encodes a practitioner's method, say so and name the practitioner.

### `## How to do it`

The procedure, step by step, in the imperative. Explain why a step matters where it isn't obvious; a model follows a reasoned instruction better than a bare command. Point to `references/` files for detail, one level deep.

### `## Output template`

The exact shape of the response, in a fenced `markdown` block, with placeholders in angle brackets. A user and a reviewer should be able to tell from this block alone whether a run of the skill did its job.

### `## Where it goes wrong`

Known failure modes and out-of-scope cases: what the model tends to do wrong with this method, what inputs break it, what it must refuse to do. A failure mode that only repeats a step from "How to do it" does not belong here.

### `## When to bring in a specialist`

The escalation point: the conditions under which the skill tells the user the question has outgrown the tool. Be concrete ("if the behavior involves clinical risk", "if the sample is below 200 and the effect size is unknown"). Say what kind of specialist and what to bring to them.

**May be "Not applicable: <reason>"** for a narrow technical skill with no judgement call the user could get wrong. Same rule: a real reason.

## 5. Test cases: `evals/evals.json`

**Required.** Four cases, named and in this order. The format extends the one Anthropic's skill-creator uses.

| `name` | What the case tests |
|---|---|
| `Full run` | A realistic request with enough context. The skill produces the whole output template. |
| `Missing context` | A request that lacks a required input. The skill asks its "Before you start" questions and produces nothing else. |
| `Near the escalation point` | A request that meets a condition under "When to bring in a specialist". The skill does what it safely can and names the specialist. |
| `Wrong skill` | A request that belongs to a neighboring skill. The skill says where to go and does not produce its output. |

```json
{
  "skill_name": "decompose-comb-barriers",
  "evals": [
    {
      "id": 1,
      "name": "Full run",
      "prompt": "A realistic request a user would actually type, with the context they'd actually give.",
      "expected_output": "One sentence on what a good answer is.",
      "files": [],
      "assertions": [
        "A statement a reviewer can tick yes or no.",
        "Another, about what must be present.",
        "Another, about what must not be present."
      ]
    }
  ]
}
```

- `expected_output` is one sentence.
- `assertions` holds three to six short statements, each one check. `besci-eval` grades a run against them.
- Write prompts the way your users talk, not the way the skill talks.

**A fifth case where a review reported a failure.** When an expert review reports that the skill got something wrong, the version that answers it adds a case that reproduces the failure, named `From an expert review #<issue number>`.

Trigger tests are not written here. `besci-eval` derives them from `## When to use it`.

## 6. Reference files

**Required for atomic skills:** `references/worked-example.md` and `references/evidence.md`, with the headings below. Other reference files are allowed when `SKILL.md` points to them; each opens with one line saying what it is for.

### `references/worked-example.md`

```markdown
# Worked example: <the case in a few words>

A full run of the skill on a realistic case, showing the output it should produce. The case is illustrative, not a real program.

## The request

<what the user gave>

## The output

<the filled output template, in one fenced block>
```

Use the case that fits the skill. Leave out who drafted the example and where it was ported from.

### `references/evidence.md`

```markdown
# Evidence: <skill title>

## Sources

- <full citation with a link>. Supports: <what it supports in the skill>.

## Where it has been tested

Searched <month and year>.

| Source | Type | Countries | Finding |
|---|---|---|---|
| <citation with a link> | <review or single study> | <...> | <...> |

<one or two sentences: which part of the mechanism depends on local conditions>

## Replication

<what held, what failed, what is contested>

## What to check locally

1. <...>
```

## 7. The evidence scan

Every atomic skill that makes a claim about how people behave runs this scan before it is written or revised, and records the result in `references/evidence.md`.

1. **Reviews first.** Look for systematic reviews or meta-analyses of the technique. Record whether they include samples outside wealthy Western countries, how many, and whether the effect differs by region or income level.
2. **Then individual studies.** Find the two or three strongest studies from low- and middle-income or non-Western settings, with field trials ahead of lab studies.
3. **Then the explicit null.** If neither step finds anything, say so and name what was searched.
4. **State what depends on local conditions.** Name the part of the mechanism that could differ (literacy, formal accounts, who decides in the household, trust in the sender) and the one thing to check locally.

About five searches per skill is enough. This is a scan, not a systematic review.

The result sets `metadata.tested_in`:

| Value | Label | What earns it |
|---|---|---|
| `beyond-western-holds` | Tested beyond wealthy Western countries; results hold | A systematic review, or at least two field studies outside wealthy Western countries, point the same way as the original evidence. |
| `beyond-western-differs` | Tested beyond wealthy Western countries; results differ | Studies outside wealthy Western countries exist, and their results differ from the original evidence or from each other. |
| `mainly-western` | Tested mainly in wealthy Western countries | The scan found fewer than two field studies outside wealthy Western countries. |
| `not-applicable` | Not applicable | The skill is a procedure that makes no claim about how people behave. |

When a review pools studies from outside wealthy Western countries, its overall result decides between "holds" and "differs"; record single trials that went the other way in the table.

**Verify every source.** Resolve the DOI or open the page, and confirm author, year, and title, before the source goes into a skill. Leave out anything that cannot be verified; do not flag it and keep it. Never write a citation from memory.

## 8. Skills that search for or read studies

A skill whose job at run time is to find studies, or to read the studies it is given, carries `references/citing-sources.md`, a shared file that `scripts/check_sync.py` keeps identical across those skills. Its rules: open every source before citing it; take effect sizes from the results, and say "abstract only" when that is all that was read; never output a link that was not opened; say "no evidence found" when no study addresses the claim, and do not issue a verdict; and when no search tool is available, say so first and give no links or effect sizes.

## 9. Version history: `CHANGELOG.md`

**Required.** Newest first. The top entry must contain the current `metadata.version`.

```markdown
# Changelog

## 0.2.0 - 2026-11-10
Addresses expert review #42 (Jane Doe): the first run now checks every link before showing it.
```

Patch for wording, minor for new behavior, major when the output template changes shape. Name the reviewer in the entry that marks a skill `published`. An entry that answers an expert review cites the issue in the form above; the site uses it to mark the review answered. The changelog is also where a note on how a version was drafted belongs, including any use of AI.

## 10. Files

Allowed types: markdown, text, JSON, YAML, CSV, Python, R, shell, HTML, CSS, JavaScript, PNG, JPG, SVG, GIF. 2 MB per file, 10 MB per skill. Every path `SKILL.md` mentions under `references/`, `scripts/`, or `assets/` must exist.

## 11. Style

- Write for a program designer or M&E lead who has never met a behavioral scientist. Define a term the first time you use it.
- Use plain words for where evidence comes from: "wealthy Western countries", not the acronym WEIRD.
- Imperative mood in "How to do it". Explain the why in one clause when a step is not obvious.
- Ask before producing. A skill that gives a confident answer to an underspecified request is a failure mode, not a feature.
- Name the mechanism, not just the tactic. "Send a reminder" is a tactic; "reduce the attention cost at the moment of action" is a mechanism.
- Cite what you draw on, and only what you have verified.
- Keep notes on how the skill was drafted or checked out of `SKILL.md` and `references/`. They go in `CHANGELOG.md`.

## 12. Running the validator

```bash
uv run scripts/besci_validate.py skills/<name>     # one skill
uv run scripts/besci_validate.py                    # all skills
uv run scripts/besci_validate.py --json             # for tools
```

Exit 0 means the structure is right. Content review by a maintainer is still required before merge.

The rules added in November 2026 (the "what this adds" line, the two labeled evidence notes, `tested_in`, the two reference files, the four named test cases with assertions, one `produces`) are errors, E040 to E049. The length limits and the note on drafting language are warnings.
