# Worked example: village-randomized sanitation triggering in Indonesia

A full run of the skill on a realistic case, showing the output it should produce. The case is illustrative, not a real program.

## The request

"We are testing community-led total sanitation triggering in a district in East Nusa Tenggara, Indonesia. Villages will be randomized to two arms, and we will survey 40 households per village. The outcome is whether a household uses an improved latrine at 12 months, verified in the survey; the district health office puts the baseline at 35%. Our effect-size benchmark says to plan on 6 percentage points, the smallest effect worth acting on, with a central expected effect of 8. We have no local intracluster correlation. Triggering reaches every assigned village; we expect 10% of households not to be found at endline, and we will use baseline latrine ownership as a covariate, with an R² around 0.10. We can afford 60 villages. How many do we need, and what can 60 detect?"

## The output

```markdown
Sixty villages are not enough to detect the 6-point effect you plan on: at the assumed ICC of 0.05 it needs 76 villages per arm, and 30 per arm can detect about 9.6 points. The answer rests most on the ICC, which is a guess here; across the range tested, the villages needed move by a factor of six. The options below would change the verdict, and none of them assumes a bigger effect.

# How big the sample must be: sanitation triggering, East Nusa Tenggara

**Design:** randomized by village; two arms; 1:1; 40 households surveyed per village
**Effect planned on:** 6 percentage points; the smallest effect worth acting on, from the team's effect-size benchmark (central expected effect 8 points)

## Inputs
| Input | Value | Source |
|---|---|---|
| Alpha, two-sided (the accepted chance of a false alarm) | 0.05 | Convention (assumption) |
| Power (the chance of detecting a true effect) | 0.80 | Convention (assumption) |
| Outcome, baseline | Yes-or-no; 35% use an improved latrine | District health office records |
| People per group | 40 households per village | Survey plan |
| ICC (how alike people in one group are) | No local estimate; 0.05 used, 0.01 to 0.20 in the sensitivity table | Assumption |
| Take-up (treatment, control) | 1.0, 0 | Triggering reaches every assigned village |
| Attrition (people lost before measurement) | 0.10 | Team's estimate (assumption) |
| Covariate R² (the share of variation a baseline measure explains) | 0.10 | Baseline latrine ownership (assumption) |

## Calculation
- Script: `python3 scripts/power_calc.py --outcome binary --p0 0.35 --p1 0.41 --icc 0.05 --cluster-size 40 --attrition 0.10 --r2 0.10 --clusters-per-arm 30 --sensitivity --true-effect 0.06`
- Sample per arm before adjustments: 1,026.2
- Multipliers: design effect for randomizing groups 1 + (40 − 1) × 0.05 = 2.95; take-up ÷ 1.0; attrition ÷ 0.90; covariates × 0.90
- **Required:** 3,028 households enrolled per arm; 76 villages per arm (152 in total)

## Smallest effect the feasible sample can detect (minimum detectable effect)
30 villages per arm (1,200 households enrolled per arm): 9.6 percentage points (0.20 SD of the baseline outcome), against a planned effect of 6

## Sensitivity: how the answer moves with the guesses
Villages needed per arm:

| ICC \ effect | 3.0 points | 4.5 points | 6.0 points | 9.0 points |
|---|---|---|---|---|
| 0.01 | 141 | 63 | 36 | 17 |
| 0.05 | 299 | 134 | 76 | 35 |
| 0.10 | 496 | 222 | 126 | 57 |
| 0.20 | 890 | 399 | 226 | 102 |

Detectable effect with 30 villages per arm, by ICC: 6.5 points at 0.01; 9.6 at 0.05; 12.4 at 0.10; 16.7 at 0.20.

## Wrong sign and exaggeration (Type S and Type M risk), when the expected effect is below the detectable effect
At a true effect of 6 points: power 0.42; chance a significant result has the wrong sign 0.000; exaggeration 1.52, so a significant result would overstate a true 6-point effect by about half. At the central expected effect of 8 points: power 0.65; exaggeration 1.24.

## Verdict
Cannot detect the planned effect with the feasible sample, because at an ICC of 0.05 a 6-point effect needs 76 villages per arm and 30 per arm detect 9.6 points. Options that change it: fund 152 villages; collect a fuller baseline to raise R² above 0.10; accept that 60 villages can confirm only an effect of about 10 points or more, and say so in the registration; or run a smaller study of feasibility instead of the effect test. Spreading the same budget across more, smaller villages helps only a little: 50 villages per arm at 20 households detect 8.5 points.

## What to check before relying on this
- The ICC. A baseline survey of latrine use in 20 villages would replace the 0.01 to 0.20 range with an estimate; across that range the villages needed move by a factor of six.
- The 35% baseline, which comes from administrative records that may overstate use compared with a verified survey.
- The 10% attrition, which is the team's estimate rather than a figure from an earlier round.

## Where you could go from here
That's the calculation.
- Measure the ICC with a baseline survey of latrine use in 20 villages: at 6 points the villages needed run from 36 to 226 per arm across the range tested, so this one figure decides whether 60 villages are close or far off. The same survey would check the 35% baseline against verified use.
- Take the options in the verdict to whoever holds the budget: funding 152 villages and registering that 60 can confirm only about 10 points are different decisions, and the district or the funder has to make them.
- If the 60-village study goes ahead, fix the analysis with `write-pre-analysis-plan`: it is where to state, before any data arrive, that the study can confirm only an effect of about 10 points or more, and to name the baseline covariate counted on here.
I'd lean toward the ICC survey, because the verdict rests on a number that is a guess today, and the survey checks the baseline at the same time.
Questions you could ask next: "What would a smaller feasibility study look like instead of the effect test?" · "How do we explain to the funder that 60 villages can confirm only about 10 points?"
```
