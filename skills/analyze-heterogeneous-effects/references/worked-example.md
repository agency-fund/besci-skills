# Worked example: a growth-mindset session in Peruvian public schools

A full run of the skill on a realistic case, showing the output it should produce. The case is illustrative, not a real program.

## The request

"We ran a cluster randomized trial of a one-session growth-mindset program in 180 public secondary schools in three regions of Peru (90 treatment, 90 control, about 12,000 grade-8 students; schools were randomized). Primary outcome: end-of-year national math score, in points (regional mean about 50, standard deviation about 12). The pre-analysis plan, registered before baseline, names two subgroups: baseline math tercile (we expected a larger effect for the bottom tercile) and school poverty index above or below the median (larger effect expected in poorer schools). It powered the trial for an overall effect of 1.5 points. Overall effect from the plan's model: 1.8 points (95% CI 0.3 to 3.3). Baseline covariates: sex, age, baseline math and reading, mother's education, school size, urban or rural, poverty index. Schools were a random sample of public secondary schools in the three regions. The funder wants to know who benefited most and what to pre-register in the next trial, and asked whether to run it only in rural schools next year. We use R; the data are attached."

## The output

```markdown
# Heterogeneous effects report

**Trial:** Growth-mindset session, three regions of Peru; treatment vs control; randomized by school; 90 schools (6,050 students) vs 90 schools (5,950 students)
**Primary outcome:** End-of-year national math score, points
**Overall effect:** 1.8 points (95% CI 0.3 to 3.3), from the plan's model, standard errors clustered by school (about 0.15 standard deviations)
**Sample:** random sample of public secondary schools in three regions; results speak for grade-8 students in public schools in those regions, not private schools or other regions
**Decision this informs:** describe who benefited; choose what to pre-register next. Running it only in rural schools would be targeting (see the last section).
**Plan status:** plan registered before baseline names 2 subgroups

## Named subgroups (confirmatory)

| Subgroup (verbatim from the plan) | Expected direction | Effect in each group (points, 95% CI) | Difference (points, 95% CI) | Uncorrected p | Corrected p (Benjamini-Hochberg, 2 tests) |
|---|---|---|---|---|---|
| Baseline math tercile | Larger for the bottom tercile | Bottom 3.1 (0.8 to 5.4); middle 1.6 (-0.4 to 3.6); top 0.6 (-1.5 to 2.7) | Bottom minus top 2.5 (0.5 to 4.5) | 0.01 | 0.03 |
| School poverty index above or below the median | Larger in poorer schools | Poorer 2.4 (0.3 to 4.5); less poor 1.1 (-0.9 to 3.1) | 1.3 (-1.6 to 4.2) | 0.38 | 0.38 |

The baseline-tercile difference holds after correction, in the expected direction: the effect is concentrated among students who started in the bottom tercile. The poverty difference is not detectable at this sample; its interval runs from below zero to more than twice the overall effect.

## Exploratory splits (hypotheses only)
- **Method and software:** causal forest, grf in R
- **Sample splitting:** half to fit, half to test, split by school; 100 repeated splits; medians reported
- **Characteristics used:** baseline only: sex, age, baseline math, baseline reading, mother's education, school size, urban or rural, poverty index
- **Best linear predictor:** heterogeneity coefficient 0.6 (95% CI 0.1 to 1.1); reads as real differences detected, with predicted differences more spread out than the real ones
- **Average effect by fifth of predicted benefit:**

  | Group | Effect (points, 95% CI) |
  |---|---|
  | Least affected fifth | 0.2 (-1.8 to 2.2) |
  | Second fifth | 1.0 (-0.9 to 2.9) |
  | Third fifth | 1.6 (-0.3 to 3.5) |
  | Fourth fifth | 2.3 (0.3 to 4.3) |
  | Most affected fifth | 4.1 (1.9 to 6.3) |
  | Most minus least | 3.9 (0.9 to 6.9) |

- **Most and least affected compared:** baseline math, 38 vs 61 (-23 points); share girls, 0.58 vs 0.45 (+0.13); mother's education primary or less, 0.47 vs 0.29 (+0.18); rural school, 0.52 vs 0.31 (+0.21). These describe whom the model picked out; they are hypotheses, not confirmed subgroups.

## Power limits
The trial was sized for an overall effect of 1.5 points. Neither subgroup was sized for, and a difference between subgroups of that size needs a much larger sample. The poverty result is "not detectable at this sample", not "the same in poorer and less poor schools". Each exploratory fifth is estimated on half the sample, so its interval is wide; the least affected fifth's interval includes the overall effect.

## What to pre-register next time
- Baseline math tercile, expected larger for the bottom tercile, because the difference held after correction here
- Sex, expected larger for girls, because girls were more common in the most affected fifth
- Rural school, expected larger in rural schools, from the exploratory split only

## What to check before relying on this
- These schools were a random sample of public secondary schools in three regions; the results do not speak for private schools or other regions.
- The findings on girls and rural schools must keep their exploratory label in the funder's summary; only the baseline-tercile result is confirmatory.
- Running the program only in rural schools would exclude urban students on an exploratory result. Take this report to a statistician before any such decision.
```
