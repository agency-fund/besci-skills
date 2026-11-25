---
name: besci-eval
description: >-
  Use when someone wants to know how good a skill in the Behavioral Science
  Skills Library is: check its structure, test whether it fires on the right
  requests and stays quiet on the wrong ones, see what it makes the AI do
  that the AI would not do alone, compare it across models, or re-test it
  after a new model is released. Trigger on "evaluate this skill", "test my
  skill", "diagnose this skill", "does this skill trigger correctly", "run
  the evals", "is this skill any use", "compare models on this skill". Do
  not use for writing or revising a skill's content (besci-skill-creator),
  for choosing which skill to use (besci-navigator), or for evaluating an AI
  product or chatbot (that is The Agency Fund's evaluation playbook, a
  different thing).
license: CC-BY-4.0
metadata:
  title: Behavioral science skill evaluator
  type: meta
  stage: other
  version: "0.4.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  tested_in: not-applicable
  tags: "meta, evaluation, regression"
  consumes: "skill-draft"
  produces: "eval-report"
---

Diagnoses one library skill: whether its structure is sound, whether it fires on the right requests, and whether it makes the AI do the job better than the AI does alone. Reports what it found on one screen.

A skill can meet every rule in the spec and still add nothing. So the main test here is a comparison: the same realistic request answered with the skill and without it. The library's claim for every skill is that it makes the AI do something it would not do unprompted, and this checks that claim.

## Before anything else

Find out which skill (a folder, a `.skill` file, or pasted text) and how you can run things here, because that sets how clean the comparison is:

1. **Fresh agents**, when you can start one. One agent gets a request and the path to the skill's folder, and is told to read its `SKILL.md`, follow it, read `references/` when the skill says to, and leave `evals/` alone. Another gets the same request and is told to answer from its own knowledge, loading no skill and reading no files, because the library may be installed where it runs. Neither sees the other or is told it is a test. Tell both that the user can answer afterwards, so an agent that would ask a question first can ask it. Use this tier whenever it is available.
2. **The script**, for repeated runs, several models, or a re-test after a model release. It calls the API and costs money, so show the plan first: `python scripts/run_evals.py <skill-folder> --dry-run` prints the number of calls and writes nothing. Run it only on the person's go-ahead. It loads `SKILL.md` alone, without the skill's reference files, so it tests a little less than a fresh agent does.
3. **In this conversation**, when there are no tools. You cannot un-read a skill, so the order of work below matters most here, and the report says the result is indicative.

**Keep this order, on every tier.** Read only the skill's `description` and the `prompt` of each test case first. In `evals.json` each prompt sits beside its expected output and assertions, so print the prompts alone or have the person paste them. Then write the cold case. Then get the baselines: start the fresh agents, or on the conversation tier write your own answer to each case. Only then read the rest of the skill. The validator can run at any point, since it shows you nothing of the body. A baseline written after reading the skill borrows its ideas and makes the skill look as if it adds less than it does.

## Three checks

**Structure.** Run `python scripts/besci_validate.py <skill-folder>` from this skill's folder, or walk `references/checklist.md` when you cannot. Report errors in plain words. A meta-skill or supporting skill is written in its own shape, so only its frontmatter and files are checked (plus test cases and a changelog for a meta-skill); say so. Structural errors do not stop the other checks unless there is no description to test.

**Triggering.** Would an AI that sees only descriptions load this skill for the right requests, and leave it alone for the wrong ones?

- Requests it should take: the bullets under "Use it when", the test cases, and the cold case. A bullet that states a condition and not a request gets turned into what a user would type.
- Requests it should leave: the bullets under "Do not use it when", the "Wrong skill" case, and any case marked `"should_trigger": false`. For a skill with no such lists, write two or three near-misses from the "do not use" clause of its description.
- Judge each one next to the neighbors: this skill's description among the descriptions of the other skills in the catalog (`skills/besci-navigator/references/catalog.md` in the repository, or the live catalog). A description that fires correctly alone can over-fire next to its neighbors. With a fresh agent, give it the list of descriptions and the requests in shuffled order, do not say which skill is under test, and ask which skill, if any, it would load for each. One agent can take all the requests.

**On the job.** Run three cases, each with the skill and without it: the "Full run" case, the "Missing context" case, and one cold case. For a skill without those names, use its first two cases. "All cases" is there if the person asks; a "Wrong skill" case is then judged on whether the skill sends the person to the right place.

The cold case is a request you write from the description alone, the way a program officer would type it: plain words, a real-sounding program, none of the method's vocabulary, and enough detail that the skill can produce its full output. The "Missing context" case already tests whether the skill asks, so the cold case should show the whole output on a request the skill has never seen. A skill's own cases were written with the skill open and tend to hand it what it asks for. A skill that does well on its own cases and poorly on the cold one has shown you its most useful finding.

For each pair of answers, settle three questions and quote the answers as you do:

1. Did the skill change what the AI did?
2. Is the change the one the skill promises? An atomic skill states its promise in the "What this adds" line; for another skill, use how it describes itself.
3. For this job, would a practitioner prefer the answer written with the skill, and why?

Then mark the case's own assertions against each answer. Three things block a skill whatever else is true: a citation that is not in the skill's sources or was not opened, a full answer to a request that lacked something the skill needs, and a missed handoff to a specialist. `references/judging.md` has the detail, and the script's judge reads the same file.

## The report

About one screen, in this order every time, so that maintainers can read reports side by side. Lead with the verdict.

```markdown
# Diagnosis: <skill-name> v<version>  (<date>)

**Verdict:** <ready | fix first | could not test>. <The finding that decided it, in one sentence.>

## Structure
<Passes, or the errors in plain words. One line when clean.>

## Triggering
<Counts in words: "It fired on 5 of 6 requests it should take, and on 1 of 4 it should leave.">
<Each miss or false alarm: the request, and the clause in the description responsible.>

## On the job
<Per case, two or three sentences: what the skill changed against the bare model, whether that is what it promises, which answer a practitioner would prefer and why, and assertions passed with and without.>
<One short side-by-side excerpt from the most telling case.>

## What to fix
<Up to three findings, most important first, each with the smallest change that would address it.>

## How this was run
<Two or three lines: fresh agents, script, or in conversation; the model; runs per case; what was not run; and that which answer is better is a model's judgment, not a practitioner's.>
```

- **Ready** means ready for a maintainer's content review. **Fix first** is where most first drafts land: a validator error, a blocking finding, a description that fires on the wrong requests, or answers that are no better with the skill on most of the cases. **Could not test** means there was nothing to run. When the verdict is "ready" and the evidence is thin, the sentence after it says so.
- Give counts in words. Precision and recall to two decimals on ten requests claim an accuracy that is not there.
- You propose and the author decides. Never edit the skill; `besci-skill-creator` helps with the revision.
- With a filesystem, save the full answers and the per-request detail to a folder named `<skill>-workspace` beside the skill's folder, so the report can stay short. The repository ignores those folders, and the script writes there itself. Model comparison appears only when more than one model ran.

## What this cannot tell you

Whether the method is right. You can see that two answers differ and which one does the job as described; you cannot settle which advice a practitioner would stand behind. Say so when two runs give different method advice, when a source cannot be checked, or when the skill touches clinical, safety, or child-protection decisions, and point to the skill's expert reviews on the library site. One run is one draw from a model that varies, so without repeats call the findings indicative.

Nothing here measures whether a program or an AI product works. That is The Agency Fund's evaluation playbook, https://eval.playbook.org.ai/.

## Manner

Plain and direct. Say what you found and what you could not test. Quote the answers rather than describe them. No praise, and no softening a "fix first" into something vaguer.
