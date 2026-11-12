---
name: assess-evidence-transferability
description: >-
  Use when a team has one study in hand and asks "will this work here?",
  "does this apply to our population?", or "can we expect the same effect?".
  Also use when a proposal quotes a study's result as what a program will
  achieve somewhere else. Reads the study, compares what its effect depended
  on with your setting, and gives a verdict with the assumptions to test
  locally. Do not use to find what evidence exists; use assess-evidence-base.
  Not for the effect size to plan a sample on; use estimate-expected-effect.
license: CC-BY-4.0
metadata:
  title: Check whether a study's finding applies in your setting
  type: atomic
  stage: define
  version: "0.3.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  tested_in: not-applicable
  tags: "evidence-synthesis, generalizability"
  consumes: "evidence-scan-brief"
  produces: "transferability-assessment"
---

## What it does

Judges whether one published finding is likely to hold in a named setting.

**What this adds:** reads the study itself and takes the estimate from its results, not from memory or the abstract alone; compares the study with your setting on what the effect depended on, step by step; gives one of five fixed verdicts, including "no evidence to assess" when no study tests the claim; and turns every unknown into a local check.

## When to use it

### Use it when
- A team has a study and asks "will this work here?", "does this apply to our population?", or "they got 40 points in Afghanistan; what about Bangladesh?"
- A proposal or pitch quotes a study's effect as what the program will achieve in a different country, population, or channel
- An evidence scan has turned up a promising finding from somewhere else

### Do not use it when
- The question is what evidence exists on a topic; use `assess-evidence-base`
- The team needs a number to plan a sample size on; use `estimate-expected-effect`
- The team wants to adapt an intervention it has already decided to run; use `specify-intervention-adaptations`

## Before you start

Ask these before producing the assessment. Do not ask anything the user has already answered.

1. **Required.** The finding: one study or review, as a link, a file, or a full citation. A claim with no study behind it cannot be assessed.
2. **Required.** The user's setting: who the program would reach, where, what would be delivered, by whom, and which outcome matters.
3. Optional. The decision this informs: a pilot, a scale-up, a number in a proposal.
4. Optional. Other studies of the same intervention in other places.

If 1 or 2 is missing, ask and stop. If 3 is missing, assume a pilot decision and say so. If 4 is missing, treat the finding as tested in one setting.

## What it draws on

- Bates, M. A., & Glennerster, R. (2017). The generalizability puzzle. *Stanford Social Innovation Review*, 15(3), 50–54. https://doi.org/10.48558/EYY5-3S89 Supports: the four questions the assessment walks through: the theory behind the program, whether local conditions hold for it, how strong the evidence is for the behavior change, and whether it can be implemented well.
- Vivalt, E. (2020). How much can we generalize from impact evaluations? *Journal of the European Economic Association*, 18(6), 3045–3089. https://doi.org/10.1093/jeea/jvaa019 Supports: comparing who delivered the intervention. Across impact evaluations, programs run by governments had smaller effects than those run by academics or NGOs.
- DellaVigna, S., & Linos, E. (2022). RCTs to scale: Comprehensive evidence from two nudge units. *Econometrica*, 90(1), 81–116. https://doi.org/10.3982/ECTA18709 Supports: not carrying a published number into a plan. Nudge trials in academic journals averaged 8.7 percentage points; trials run by two US government nudge units averaged 1.4.

**Where the evidence comes from:** The procedure makes no claim about how people behave. Its framework comes from cases of moving programs between low- and middle-income countries; the lead example takes a result from Kenya to Rwanda.

**Replication status:** Not applicable; this is a structured judgment. None of the sources tests whether two teams reach the same verdict on the same study.

## How to do it

1. **Read the study itself**, following `references/citing-sources.md`. Record the effect from the results, with its unit, and who was studied. If you can reach only the abstract, write "abstract only" and say what that leaves unknown.
2. **If no study tests the claim, stop.** Write "No evidence to assess", list the nearest related studies you were given or opened, and say how each differs from the claim. Give no verdict.
3. **Write why the effect happened**, as the authors state it: the steps between the intervention and the outcome. If they do not say, write "not stated by the authors" and treat every difference as one that may matter.
4. **List what each step depended on** and compare the study with the user's setting on each: who took part, what was delivered, what was measured, and the institutions and channel around it. Mark each "holds", "does not hold", or "unknown", and say what would settle an unknown. Only differences that touch a step count.
5. **Note whether the same response has been seen elsewhere**, from studies the user supplied or you opened. None means a single-setting finding.
6. **Compare who delivered it**: the study's implementer and resources against the user's.
7. **Give the verdict.** "Cannot tell" is correct when the authors state no mechanism or two or more conditions are unknown.
8. **Turn each "unknown" and "does not hold" into an assumption to test locally**, with the cheapest check: a survey item, a few interviews, a small trial arm.

See `references/worked-example.md` for a complete run.

## Output template

```markdown
<Two or three plain sentences to the user: the verdict, the one condition that decided it, and what that means for the number or plan they had in mind.>

# Would <the finding, in a few words> hold in <their setting, in a few words>?

**Decision this informs:** <pilot / scale-up / proposal number / go or no-go>
**Finding:** <authors, year, link>; <effect with its unit, from the results>; <where and with whom>
**How the study was read:** <full text / abstract only / the user's summary, not checked>

## 1. Why the effect happened
<the steps between the intervention and the outcome, as the authors state them; or "not stated by the authors">

## 2. Do the conditions hold in your setting?

| What the effect depended on | In the study | In your setting | Holds? |
|---|---|---|---|
| <condition> | <...> | <...> | <holds / does not hold / unknown: what would settle it> |

## 3. Has the same response been seen elsewhere?
<each other study, with where it was run and what it found; or "None supplied or found: a single-setting finding.">

## 4. Can it be delivered as it was?
<who delivered it in the study and with what; who would deliver it here; the difference>

## Verdict
<Likely to hold / Likely to hold with changes / Unlikely to hold / Cannot tell / No evidence to assess>, because <the rows that decided it>.

## Assumptions to test locally
1. <a statement that could turn out false>: <the cheapest check>

## What to check before relying on this
- <the unknown that would change the verdict most>

## Where you could go from here
<One line saying the assessment is done.>
<Two or three next moves that fit this verdict, each with why it would help and when it fits. Candidates:
- `estimate-expected-effect`, when the verdict is likely to hold and the team needs an effect size to plan a test on, since the study's own number is not a forecast
- `assess-evidence-base`, when the verdict is "no evidence to assess", or the finding has been seen in one setting only and the team wants to know what else has been tried
- `specify-intervention-adaptations`, when the verdict is likely to hold with changes and the team will change the intervention for its setting
- `plan-prototype-test`, when an assumption to test is how the audience will read or respond to the draft, which a few people can show before any pilot
- the full text of the study, its authors, or a researcher who knows the local setting, when the assessment rests on the abstract or the condition in doubt is institutional or legal>
Questions you could ask next: "<question>" · "<question>"
```

<!-- shared: template/shared/voice.md. Edit it there, then run scripts/check_sync.py --fix. -->
**How to talk with the user**

- If the user asked a question rather than asked for this skill's output, answer the question first, in a few plain sentences. Then offer the run and say what it would add.
- Mark the run. When it starts, say so in one line: the skill, and what it will produce. When the output is done, say the run is finished. The user should always know when the library's method is in force.
- Talk with the person, not at them. Use their words for their program and the people in it, say why you ask each question, and say what you are unsure of. No praise, no filler.
- Say where each claim comes from: this skill's sources, your general knowledge, or nothing in the library. A number the sources do not give, such as how many interviews to run, is your judgment; say so, and why you chose it.
- End with the template's closing: two or three next moves that fit what this run found, each with its reason and when it fits, and one or two questions the user could ask next. Say which move you would lean toward and why; the user decides.
<!-- /shared -->

## Where it goes wrong

- **A verdict from the abstract.** An abstract gives the headline number and seldom the conditions behind it. If that is all that was read, the "How the study was read" line says so, and section 2 lists what could not be compared.
- **A verdict on a claim nobody tested.** "Does cutting corruption raise trust in government?" is a question, not a finding. Without a study that measures it, the answer is "No evidence to assess" plus the nearest studies.
- **Judging by surface likeness.** The same country or sector does not mean the conditions hold, and a different continent does not mean they fail. Only section 2 decides.
- **Carrying the number.** A verdict of "likely to hold" is about direction. The study's effect size is not a forecast for the user's program.

## When to bring in a specialist

Tell the user to consult a researcher who knows the local setting, and an evaluator, when:
- The decision is a scale-up or a large budget and the verdict is "cannot tell"
- The condition in doubt is institutional or legal (who may deduct from pay, who may give consent), which a local expert can settle faster than a study
- The study's own design is disputed, so the finding may not hold even where it was run

Bring them: the assessment, the study, and the list of unknowns.
