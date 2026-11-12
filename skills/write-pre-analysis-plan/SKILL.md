---
name: write-pre-analysis-plan
description: >-
  Use when a trial's design and primary outcome are set and the team must
  fix, before any outcome data arrive, how results will be analyzed: "write
  our pre-analysis plan", "PAP", "what do we put in the AEA registry?", "how
  much do we pre-specify?". Writes the hypotheses, estimator, outcome
  families, subgroups, decision rules, and registration. Do not use when the
  primary outcome or smallest change worth detecting is open
  (plan-evaluation-design) or the comparison is open (choose-trial-design).
license: CC-BY-4.0
metadata:
  title: Write the analysis plan before the data arrive
  type: atomic
  stage: test
  version: "0.3.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  tested_in: not-applicable
  tags: "research-transparency, experimental-design, multiple-comparisons"
  consumes: "evaluation-design, measurement-plan"
  produces: "analysis-plan"
---

## What it does

Writes down how a trial's results will be analyzed before anyone sees the outcome data.

**What this adds:** asks first whether anyone has seen outcome data by arm; carries the design and primary outcome over unchanged; gives every secondary outcome a family and a named way of handling multiple tests; requires a reason and a status for each subgroup; writes a decision for each range of the primary result; and checks which registry applies.

## When to use it

### Use it when
- A trial is about to launch and nobody has written down how its results will be analyzed
- Someone asks "what goes in a pre-analysis plan?" or "what do we put in the AEA registry?"
- A team proposes subgroups ("look at women too") and wants to commit before the data exist

### Do not use it when
- The primary outcome or the smallest change worth detecting is still open; use `plan-evaluation-design`
- The comparison or the unit of randomization is still open; use `choose-trial-design`
- The data are in and the question is how effects differ by subgroup; use `analyze-heterogeneous-effects`

## Before you start

Ask only what the user has not answered.

1. **Required.** The design: comparison, unit of randomization, arms, strata, timing.
2. **Required.** The primary outcome, with its source, window, and smallest change worth detecting.
3. **Required.** Whether anyone has seen outcome data by arm, even on a dashboard. Baseline data are fine.
4. Optional. Secondary outcomes, and each proposed subgroup with its reason.
5. Optional. Who has a stake in the result; the registry, deadline, and baseline variables.

If 1, 2, or 3 is missing, ask and stop; if outcome data by arm have been seen, go to the specialist note. Without 4, write a primary-only plan. Without 5, assume the implementer and funder have a stake.

## What it draws on

- Duru, M., Sautmann, A., Turitto, J., & Welch, K. (2023). *Pre-analysis plans* and *Trial registration*. J-PAL Research Resources. https://www.povertyactionlab.org/resource/pre-analysis-plans and https://www.povertyactionlab.org/resource/trial-registration Supports: when to file, a "concise and focused" plan, edits, and the populated plan; the registry rules in step 8.
- Banerjee, A., Duflo, E., Finkelstein, A., Katz, L., Olken, B., & Sautmann, A. (2020). *In praise of moderation: Suggestions for the scope and use of pre-analysis plans for RCTs in economics* (NBER Working Paper 26993). https://doi.org/10.3386/w26993 Supports: step 6, where detail is worth adding.
- Brodeur, A., Cook, N. M., Hartley, J. S., & Heyes, A. (2024). Do preregistration and preanalysis plans reduce p-hacking and publication bias? Evidence from 15,992 test statistics and suggestions for improvement. *Journal of Political Economy Microeconomics*, 2(3), 527–561. https://doi.org/10.1086/730455 Supports: writing the plan, not only the registry entry.

**Where the evidence comes from:** This is a procedure and makes no claim about how program participants behave. Its sources are economists' guidance and papers on trials in many countries, and a study of trials in leading economics journals. What is local is which registry the funder or journal requires, and whether ethics approval comes first.

**Replication status:** Contested on detail. Banerjee and colleagues argue the registry's fields usually suffice; Brodeur and colleagues found no sign that registration alone reduced p-hacking (trying analyses until one is significant), but signs that registration with a plan did.

## How to do it

1. **Carry the design and primary outcome over** word for word.
2. **Write the hypotheses**: the primary one with direction, outcome, and comparison arm; then one per secondary family.
3. **Fix the primary outcome for analysis**: any transformation, and the rule for missing values. Two primaries become a family with a correction, so "one of two moved" is not reported as success.
4. **Group secondary outcomes into families** by what they measure, and name how each handles multiple tests: a summary index, or a false discovery rate correction (Benjamini–Hochberg). Outcomes outside a family are exploratory.
5. **Specify the estimator**: the effect of assignment, whether or not people took part (intention to treat); covariates, including strata, named now; standard errors clustered at the unit randomized, if groups were; exclusions by one rule for every arm; and a test of whether drop-out differs by arm.
6. **List subgroups** with the variable and cut, the reason the effect should differ, and a status, confirmatory or exploratory; drop any with no reason. Add detail where the outcome could be built several ways, a subgroup matters, or a party has a stake; keep the rest short. Commit to a populated plan: a later report of every pre-specified test and deviation.
7. **Write the decision rules**: what the team will do, and who decides, if the primary result is at or above the smallest change worth detecting, positive but below it, or null or negative; and which harm would stop adoption regardless.
8. **Plan the registration** in the registry the funder or journal requires; health and medical journals that follow ICMJE rules require an approved clinical trial registry, even for a social science trial. Register before the intervention starts, attach this plan, and name who holds the outcome data until then.

See `references/worked-example.md` for a complete run.

## Output template

```markdown
<Two or three plain sentences to the user: what the plan commits to (the primary test and what each result would lead to), where it adds detail because someone has a stake, and that it must be registered before anyone sees outcome data by arm.>

# Pre-analysis plan: <trial>

**Date fixed:** <date>
**Outcome data by arm (each group compared) seen before this date:** <none / what, by whom, when>
**Registry:** <name; id when issued>

## 1. Design (carried over)
<comparison; unit of randomization; arms and allocation; strata; timing; sample>

## 2. Hypotheses
- **H1 (primary):** <the change, its direction, on which outcome, against which arm>
- **H2 to Hn:** <one per secondary family>

## 3. Primary outcome
<carried over: measure, source, window; for analysis: transformation, missing-value rule; smallest change worth detecting and who set it>

## 4. Secondary outcome families: outcomes tested as a group
| Family | Outcomes | How multiple tests are handled | Why grouped |
|---|---|---|---|
| <...> | <...> | <summary index / false discovery rate correction / reported without a test> | <...> |

## 5. How the effect is estimated (the estimator)
- **Effect estimated:** <intention to treat, by assigned arm>
- **Model:** <outcome on arm indicators, strata, named baseline covariates>
- **Standard errors (how uncertainty is computed):** <robust / clustered at <unit>, the unit randomized>
- **Exclusions:** <rule, applied to every arm>
- **Drop-out:** <test for differences between arms>

## 6. Subgroups
| Subgroup | Variable and cut | Why the effect should differ | Status |
|---|---|---|---|
| <...> | <...> | <...> | <confirmatory / exploratory> |

## 7. Decision rules
| Primary result | What the team will do | Who decides |
|---|---|---|
| At or above <smallest change worth detecting> | <...> | <...> |
| Positive but below it | <...> | <...> |
| Null or negative | <...> | <...> |

**Would stop adoption whatever the primary shows:** <a harm, and its threshold>

## 8. Where this plan is detailed, where it is flexible
<detail added for which stake, subgroup, or outcome, and why; what is left flexible; the commitment to a populated plan>

## 9. Registration
<registry and why; plan attached and dated; hidden until completion: yes / no; who holds the outcome data until registration is confirmed>

## Open questions
- <...>

## Where you could go from here
<One line saying the pre-analysis plan is done.>
<Two or three next moves that fit what this run found, each with why it would help and when it fits. Candidates:
- `estimate-sample-size`, when nobody has checked that the sample can detect the smallest change worth detecting, or a confirmatory subgroup difference
- `analyze-heterogeneous-effects`, after the outcome data arrive, when the plan names subgroups to test
- the registry the funder or journal requires, when the entry is not yet filed: it must be dated before the intervention starts, with this plan attached
- whoever holds the outcome data, when an open question is about how the records are kept, or when they must agree to share no tables by arm until registration is confirmed
- an independent evaluator to hold the plan, when the implementer, funder, or research team has a stake in the result
- a statistician, when the design is clustered, stepped-wedge, or adaptive>
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

- **Writing it after a peek.** A midline table or a dashboard glance by arm shapes what gets pre-specified, however honest the team.
- **The registry entry as the plan.** A few registry fields leave the estimator, families, and subgroups open until the data arrive.
- **A deviation shown as the result.** A new specification reported without the pre-specified one beside it, each labeled, reads as the plan's answer.

## When to bring in a specialist

Tell the user to consult a statistician or evaluation methodologist, with an independent evaluator to hold the plan where a party has a stake, when:
- Outcome data by arm have been seen: what can still be pre-specified needs judgment, and the registry entry must say what was seen and when
- The design is clustered, stepped-wedge, or adaptive, so the estimator is not the standard case
- The primary outcome decides eligibility for benefits or health care

Bring them: the design, the draft plan, and a description of the data.
