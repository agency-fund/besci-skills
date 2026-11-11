# Manual validation checklist

Use when the validator script cannot run. Each line mirrors a rule in `scripts/besci_validate.py`; the code in brackets is what the script would report.

## Folder and files
- [ ] Folder name is kebab-case, 1 to 64 characters, no leading, trailing, or double hyphens, and equals `name` in the frontmatter. [E003, E004]
- [ ] For atomic skills, the name starts with a verb from the taxonomy's list (define, decompose, draft, design, measure, map, score, select, adjust, analyze, assess, audit, build, choose, cluster, compare, diagnose, estimate, evaluate, find, generate, identify, plan, prioritize, propose, review, simulate, specify, summarize, synthesize, test, translate, validate, write). [E005]
- [ ] `SKILL.md`, `evals/evals.json`, and `CHANGELOG.md` exist. No `README.md` in the folder. [E001, E029, E030, W033]
- [ ] Atomic skills have `references/worked-example.md` (headings: The request; The output) and `references/evidence.md` (headings: Sources; Where it has been tested; Replication; What to check locally). [E045, W046]
- [ ] Neither `SKILL.md` nor a reference file says how the skill was drafted or checked; that goes in `CHANGELOG.md`. [W050]
- [ ] Only allowed file types; nothing over 2 MB; folder under 10 MB. [E034]
- [ ] Every `references/`, `scripts/`, or `assets/` path mentioned in SKILL.md exists. [E032]
- [ ] SKILL.md is under 500 lines, and about 1,000 words not counting the output template. [W031, W043]

## Frontmatter
- [ ] Only these top-level keys: name, description, license, compatibility, allowed-tools, metadata. [E035]
- [ ] `description` is 1 to 1024 characters (aim for about 500, no citations), has no `<` or `>`, contains a "use when" clause and a "do not use when" clause. [E006, E007, E008, W044]
- [ ] `license` is CC-BY-4.0 (or MIT for code-only skills). [E009]
- [ ] `metadata` has type, stage, version, status, authors, org, all as plain strings. [E010]
- [ ] type is atomic or meta; stage is one of the seven or other; version is quoted semver; status is draft, published, or deprecated. [E011, E012, E014, E015]
- [ ] Atomic skills have `tested_in` set to one of: beyond-western-holds, beyond-western-differs, mainly-western, not-applicable. [E018, E040]
- [ ] `consumes` and `produces` use ids from the taxonomy's io types. Atomic skills name exactly one `produces`; `consumes` lists only the inputs the skill cannot run without. [W019, E049]

## Body
- [ ] Exactly these level-2 headings, in this order: What it does; When to use it; Before you start; What it draws on; How to do it; Output template; Where it goes wrong; When to bring in a specialist. [E020, E021]
- [ ] No section is empty. [E022]
- [ ] Only "Before you start" and "When to bring in a specialist" may read "Not applicable: <reason>", and the reason is a real sentence. [E023]
- [ ] First sentence of "What it does" has no "and", and the section has a line starting `**What this adds:**`. [W024, E041]
- [ ] "When to use it" has `### Use it when` with at least three bullets and `### Do not use it when` with at least two. [E025, E026]
- [ ] "What it draws on" has at least one real citation (year, DOI, or URL), a note starting `**Where the evidence comes from:**`, and a note starting `**Replication status:**`. [W027, E042]
- [ ] "Before you start" asks for each input by what it is, not by the skill that made it. [W051]
- [ ] Every skill or workflow named anywhere in SKILL.md exists in the library. [E056]
- [ ] "Output template" contains a fenced code block. [W028]
- [ ] The template opens with a plain lead-in, uses labels a program designer would use, and ends with a "Where you could go from here" closing: two or three next moves with reasons, and questions the user could ask next. [W054]
- [ ] No "Next action", "Check first", or "Next steps" line in the template. [W055]
- [ ] After the template, the "Output template" section carries the shared voice block between the markers, identical to `template/shared/voice.md`. [W053; check_sync]
- [ ] The closing's placeholder lists candidate next moves, each with the condition under which it fits, including one step outside the library.

Codes E040 to E049 and E056 are errors, except the warnings W043, W044, and W046; W050 to W055 are warnings too, and W053 to W055 become errors when the library has been revised to the voice standard.

## Evals and changelog
- [ ] `evals.json` has `skill_name` equal to the name, and each case has id, prompt, expected_output. [E029]
- [ ] Atomic skills have four cases named, in order, Full run, Missing context, Near the escalation point, Wrong skill; any later case is named "From an expert review #<issue>". [E047]
- [ ] Each case has three to six assertions and a one-sentence expected_output. [E048, W052]
- [ ] `CHANGELOG.md` top entry is `## <version> - <date>` matching `metadata.version`. [E030]
