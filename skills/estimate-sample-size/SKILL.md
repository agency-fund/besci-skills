---
name: estimate-sample-size
description: >-
  Use when someone asks "how many people, villages, or clinics do we need?",
  "is 400 enough?", or "what could we detect with the sample we have?", or
  when a funder wants a power calculation. Runs a script for the sample size
  or the smallest detectable effect, adjusting for group randomization,
  take-up, attrition, and covariates, and says whether the feasible sample
  can detect the planned effect. Do not use to decide what effect to plan on;
  use estimate-expected-effect. Not for choosing the unit of randomization;
  use choose-trial-design.
license: CC-BY-4.0
metadata:
  title: Work out how big the sample must be
  type: atomic
  stage: test
  version: "0.2.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  tested_in: not-applicable
  tags: "experimental-design, quantitative"
  consumes: "effect-size-benchmark, evaluation-design"
  produces: "power-calculation"
---

## What it does

Computes the sample a test needs to detect a planned effect, or the smallest effect a fixed sample can detect.

**What this adds:** every number comes from `scripts/power_calc.py`, command shown; the smallest detectable effect beside the required sample; named multipliers for groups, take-up, attrition, and covariates; a sensitivity table for guessed inputs; Type S and M risk when underpowered; a verdict that never raises the effect to fit the budget.

## When to use it

### Use it when
- Someone asks "how many people do we need?", "how many clinics or villages?", or "is our sample big enough?"
- A funder, ethics board, or registry asks for a power calculation
- The sample is fixed by budget and the team asks what it could detect

### Do not use it when
- Nobody has decided what effect to plan on, or the only number is a published headline; use `estimate-expected-effect`
- The unit of randomization is still open ("people or villages?"); use `choose-trial-design`

## Before you start

Ask these before producing anything. Do not ask anything the user has already answered.

1. **Required.** The effect to plan on, with its unit, and whether it is the expected effect or the smallest worth acting on.
2. **Required.** The outcome's baseline: the control-group rate for a yes-or-no outcome, or the mean and standard deviation (SD), with their source.
3. **Required.** The unit of randomization; for groups (villages, clinics), the number measured per group and any intracluster correlation (ICC: the share of outcome variation lying between groups).
4. **Required.** The feasible sample the program can reach and afford.
5. Optional. Take-up in each arm; attrition (people lost before measurement); the share of variation a baseline measure explains (R²); alpha and power (the chance of detecting a true effect), if a protocol fixed them.

If 1, 2, or 3 is missing, ask and stop. If 4 is missing, mark the verdict "not assessed". For anything in 5, assume full take-up, no attrition, no covariates, alpha 0.05 two-sided, and power 0.80, labeled as assumptions.

## What it draws on

- Gupta, S., & Kopper, S. (2021). *Power calculations*. J-PAL Research Resources. https://www.povertyactionlab.org/resource/power-calculations Supports: the script's formulas, including the design effect 1 + (m − 1) × ICC and dilution by take-up; taking the ICC from data "preferably in the same or a similar population"; the sensitivity table.
- Kettle, S., & Persian, R. (2022). *Target, Explore, Solution, Trial, Scale: An introduction to running simple behavioural insights projects*. The Behavioural Insights Team. https://www.bi.team/wp-content/uploads/2022/11/BIT-Handbook-How-to-run-simple-BI-projects.pdf Supports: running the calculation both ways, and strengthening the intervention, enlarging the sample, or accepting less power when the detectable effect is unrealistic.
- Gelman, A., & Carlin, J. (2014). Beyond power calculations. *Perspectives on Psychological Science*, 9(6), 641–651. https://doi.org/10.1177/1745691614551642 Supports: the Type S and Type M report.

**Where the evidence comes from:** The arithmetic makes no claim about how people behave; its inputs are local. One ICC compilation uses national samples of US schools; others, for school achievement in 15 sub-Saharan African countries and perinatal outcomes in India, Bangladesh, and Malawi, find the ICC varies by country and outcome. The script's default ICC range, 0.01 to 0.20, comes from no compilation.

**Replication status:** Not applicable; the formulas are standard approximations, and the script's normal approximation understates the sample when groups are few.

## How to do it

1. **Fill the inputs table**, each value with its source; label any input without one an assumption.
2. **Run `python3 scripts/power_calc.py`** and paste the command and output. Never do the arithmetic yourself; the printed multipliers let a reader check it.
   - Yes-or-no outcome: `--outcome binary --p0 <control rate> --p1 <rate with the effect>`; for a decrease add `--direction decrease`.
   - Measured outcome: `--outcome continuous --effect` in SD, or in raw units with `--sd`.
   - Groups: `--icc` and `--cluster-size`. Report groups per arm; more groups raise power more than more people per group.
   - `--takeup`, `--control-takeup`, `--attrition`, `--r2`. State each multiplier in words: half take-up means four times the sample.
3. **If the sample is fixed**, add `--n-per-arm` or `--clusters-per-arm` and report the minimum detectable effect (the smallest true effect detected at the stated power), in units and SD, beside the planned effect.
4. **Add `--sensitivity`** whenever the ICC, take-up, or effect is a guess. Cells whose rate would fall outside 0 to 1 print "n/a".
5. **If the expected effect is below the detectable one**, add `--true-effect`. Report the power, the chance a significant result has the wrong sign (Type S), and how much it would overstate the truth (Type M).
6. **Give the verdict:** "can detect" or "cannot detect the planned effect with the feasible sample", with what would change it: more groups rather than bigger ones, a baseline measure, higher take-up, a stronger intervention, or not testing. Never raise the effect to fit the sample.

See `references/worked-example.md` for a complete run.

## Output template

```markdown
# Power calculation: <test>

**Design:** <individual or group randomized; arms; allocation>
**Effect planned on:** <value, unit>; <expected effect / smallest effect worth acting on>, from <source>

## Inputs
| Input | Value | Source |
|---|---|---|
| Alpha (two-sided) | <0.05> | <convention / protocol> |
| Power | <0.80> | <convention / protocol> |
| Outcome, baseline | <yes-or-no, control rate / measured, mean and SD> | <...> |
| People per group | <...> | <...> |
| ICC | <value, or "no local estimate; range used"> | <...> |
| Take-up (treatment, control) | <...> | <...> |
| Attrition | <...> | <...> |
| Covariate R² | <...> | <...> |

## Calculation
- Script: `python3 scripts/power_calc.py <arguments>`
- Individual-level sample per arm: <n>
- Multipliers: design effect <...>; take-up ÷ <...>; attrition ÷ <...>; covariates × <...>
- **Required:** <n enrolled per arm>; <groups per arm, if grouped>

## Minimum detectable effect for the feasible sample
<feasible sample>: <value, unit> (<SD>), against a planned effect of <...>

## Sensitivity
| ICC \ effect | <...> | <...> | <...> | <...> |
|---|---|---|---|---|
| <...> | <groups or people per arm> | <...> | <...> | <...> |

## Type S and Type M risk (when the expected effect is below the detectable effect)
At a true effect of <...>: power <...>; chance a significant result has the wrong sign <...>; exaggeration <...>

## Verdict
<Can / Cannot> detect the planned effect with the feasible sample, because <...>. Options that change it: <...>

## What to check before relying on this
- <the ICC source, or that none exists>
- <the baseline or SD source>
- <the take-up and attrition assumptions>
```

## Where it goes wrong

- **Counting people instead of groups.** Four clinics per arm with 300 clients each is not a trial of 2,400 people; above an ICC of zero, the clinics set the power.
- **A borrowed ICC used as fact.** One figure from another country or outcome, with no range, hides the input the answer moves most on.
- **Reading "powered" as "will find it".** At power 0.80, one test in five misses a true effect of the planned size, and in an underpowered test the significant results are the overstated ones.

## When to bring in a specialist

Tell the user to consult a statistician or an evaluation methodologist when:
- Fewer than 30 groups are feasible; with 10, the script understates the sample by about 30%
- The outcome is rare (baseline below 5% or above 95%), a count, or a time until an event
- The design is stepped-wedge, factorial, or has unequal arms or group sizes; the script assumes two equal arms of equal groups
- An ethics board or registry will review the calculation

Bring them: the inputs table, the script output, the sensitivity table, and the design.
