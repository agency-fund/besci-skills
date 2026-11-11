---
name: estimate-expected-effect
description: >-
  Use when a team needs the effect size to plan a test on and has published
  estimates in hand: "the paper found 12 points, what should we plan for?",
  "what effect goes in the power calculation?", "is d = 0.45 realistic for
  us?". Reads the studies, puts each estimate in the test's units, corrects
  for selective publication and delivery at scale, and returns a range and
  one number to plan on. Do not use to judge whether one study applies to
  your setting; use assess-evidence-transferability. Not for the sample size;
  use estimate-sample-size.
license: CC-BY-4.0
metadata:
  title: Set a realistic effect size to plan for
  type: atomic
  stage: test
  version: "0.2.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  tested_in: beyond-western-holds
  tags: "evidence-synthesis, experimental-design, quantitative"
  consumes: "evidence-scan-brief"
  produces: "effect-size-benchmark"
---

## What it does

Sets the effect size a test should plan on from the published estimates a team supplies.

**What this adds:** each estimate taken from the study's results and converted with the arithmetic shown; no size carried from lab studies; bias-corrected meta-analytic figures; a low end from unselected results or one sixth of the high end; the smallest effect worth acting on kept separate.

## When to use it

### Use it when
- Someone asks "what effect should we plan for?" or "is that paper's number realistic for us?"
- A proposal or power calculation treats a published effect as the program's expected effect
- A scan of the evidence turned up several estimates and the team needs one number

### Do not use it when
- The question is whether one study's finding applies to the user's setting; use `assess-evidence-transferability`
- The team has an effect to plan on and needs the sample size; use `estimate-sample-size`

## Before you start

Ask these before producing anything. Do not ask anything the user has already answered.

1. **Required.** Each study behind the estimate (link, file, or full citation) and the number taken from it.
2. **Required.** The test's outcome, unit, and baseline: the control-group rate, or the mean and standard deviation (SD).
3. **Required.** Who will deliver the intervention, to how many people, and the decision it informs.
4. Optional. The smallest effect the program would act on, or its cost and the outcome's value.
5. Optional. Take-up: the share offered the intervention who will receive it.

If 1, 2, or 3 is missing, ask and stop. If 4 is missing, write "not set". If 5 is missing, assume the source's take-up and say so.

## What it draws on

- Kettle, S., & Persian, R. (2022). *Target, Explore, Solution, Trial, Scale: An introduction to running simple behavioural insights projects*. The Behavioural Insights Team. https://www.bi.team/wp-content/uploads/2022/11/BIT-Handbook-How-to-run-simple-BI-projects.pdf Supports: the check on the central value. Communication interventions "often don't bring about a change that is larger than 2-3 percentage points".
- Gupta, S., & Kopper, S. (2021). *Power calculations*. J-PAL Research Resources. https://www.povertyactionlab.org/resource/power-calculations Supports: diluting the effect by take-up; planning on the smallest gain the implementer would act on.
- DellaVigna, S., & Linos, E. (2022). RCTs to scale: Comprehensive evidence from two nudge units. *Econometrica*, 90(1), 81–116. https://doi.org/10.3982/ECTA18709 Supports: the low end. Nudge trials (reminders, defaults, and similar changes to how a choice is presented) in journals averaged 8.7 percentage points; all trials of two US government nudge units averaged 1.4.

**Where the evidence comes from:** The one comparison of published with unselected results covers two US nudge units, so the one-sixth ratio is a US figure. A meta-analysis of tax-compliance nudges, a third run in low- and middle-income countries, found selective reporting and, tentatively, smaller effects there; a Kenyan teacher-contract program worked under an NGO, not under the government. The gap's size in any one setting is unknown.

**Replication status:** The direction held in every comparison found. The size is contested: corrected nudge averages run from about zero to 0.31 SD, by method.

## How to do it

1. **Read each study** following `references/citing-sources.md`, recording the effect from its results with unit, baseline, population, deliverer, and design.
2. **Label each estimate:** lab or online; published field trial, including cases picked for a guide; meta-analysis (pooled studies), corrected for publication bias or not; or unselected: every trial an organization ran, whatever it found.
3. **Put each estimate in the test's units** at its baseline, showing the arithmetic: one SD of a yes-or-no outcome is √(p(1 − p)); odds ratios convert through the baseline odds; percentage points are not percent change.
4. **Correct**, marking each correction applied or not:
   - Lab or online: direction only (loss-framed incentives: 0.33 SD in the lab, 0.02 in the field).
   - Meta-analysis: use the bias-corrected figure if the paper or a re-analysis gives one (a nudge average of 0.43 SD fell to 0.04); otherwise it is a ceiling.
   - Take-up: multiply by the user's take-up over the source's. Unreported take-up counts as complete.
   - Delivery: if researchers or an NGO ran the source and a government will run the test, lower the central value: government-run programs show smaller effects.
5. **Set the range** in the test's units and in SD. High: the largest corrected estimate; a meta-analysis outranks single trials above it. Low: the closest unselected estimate, or else one sixth of the high end, never applied to an unselected or corrected figure. Central: a reasoned judgment between them; for a letter, SMS, or email, above 3 points needs a stated reason.
6. **Name the effect to plan on:** the smallest effect worth acting on, if set, otherwise the central value. Report the two apart: one comes from the decision and its cost, the other from the studies. If the first is above the high end, say the program is unlikely to reach it, so the question is whether to test at all. Compute no sample size.

See `references/worked-example.md` for a complete run.

## Output template

```markdown
# Effect-size benchmark: <intervention> on <outcome>

**Decision this informs:** <pilot / scale-up / policy / funder report>
**Outcome, unit, baseline:** <outcome>; <unit>; baseline <rate, or mean and SD> from <source>
**Delivered by, at what scale:** <who will deliver it in the test, to how many people>

## Estimates read
| Source | How read | Label | Delivered by | Reported effect | In the test's units |
|---|---|---|---|---|---|
| <authors, year, link> | <full text / abstract only> | <lab or online / published field trial / meta-analysis, corrected or not / unselected> | <researchers / NGO / government> | <effect, unit, baseline> | <points and SD, with the arithmetic> |

## Corrections
1. Lab or online study: <applied or not, and why>
2. Selective publication: <bias-corrected figure used / treated as a ceiling / not needed, because unselected>
3. Take-up: <ratio applied, or assumed equal to the source's>
4. Who delivers it: <same kind as the source / smaller effect expected, because ...>

## Planning range
| | <Unit> | SD | Where it comes from |
|---|---|---|---|
| High | <...> | <...> | <the estimate and correction behind it> |
| Central | <...> | <...> | <the judgment, in one sentence> |
| Low | <...> | <...> | <the unselected estimate, or one sixth of the high end> |

## Smallest effect worth acting on
<value and unit, who set it and on what basis; or "Not set: <who must set it>">

## Effect to plan on
<value, unit, SD>, because <it is the smallest effect worth acting on / the central value>. <What a true effect at the low end would mean for the test.>

## What to check before relying on this
- <the input that would move the range most, and the cheapest way to check it>
```

## Where it goes wrong

- **Cohen's labels as a plan.** "Small, 0.2 SD" sounds safe, but the labels come from lab experiments with undergraduates.
- **A pilot's estimate as the plan.** It is imprecise, and a pilot that persuaded the team to continue was selected for looking good: a published field trial, not unselected.
- **Correcting twice.** The one-sixth ratio applied to a nudge-unit average or a corrected figure shrinks a realistic number to nearly zero.
- **One average for every intervention.** Once corrected, information-only nudges showed evidence of no effect, while changes to how options are structured, such as defaults, stayed undecided. Use the kind being tested.

## When to bring in a specialist

Tell the user to consult an evaluation methodologist, or a behavioral scientist who knows the setting, when:
- The decision is a scale-up, a policy, or a large budget, and no estimate comes from delivery like the user's
- The low end is near zero and the test is expensive
- The outcome carries clinical or financial risk, so the smallest effect worth acting on has a harm side

Bring them: the estimates table, the corrections, the range, and the decision.
