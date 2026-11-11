---
name: analyze-heterogeneous-effects
description: >-
  Use when a trial or evaluation has its main result and someone asks "who
  did it work for?" or "did it work better for women or poorer households?",
  or wants machine learning to find who responds. Also use when a team is
  about to report a subgroup difference it never planned to test. Tests the
  subgroups the analysis plan named, labels every other split a hypothesis,
  and says what to pre-register next. Do not use before the trial, to choose
  subgroups; use write-pre-analysis-plan. Not for whether an effect will
  hold at scale; use assess-scalability.
license: CC-BY-4.0
metadata:
  title: Find out who benefited most from a program
  type: atomic
  stage: analyze
  version: "0.2.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  tested_in: not-applicable
  tags: "heterogeneity, quantitative, experimental-design"
  consumes: "analysis-plan, dataset-description"
  produces: "heterogeneity-report"
---

## What it does

Estimates how a program's effect differed across the people it reached.

**What this adds:** keeps the subgroups the analysis plan named apart from every other split, and never moves one across; corrects for testing several; fits any machine-learning search on one random half of the sample and checks it on the other; reports effects in the outcome's units; reads a null difference as "not detectable"; and refuses to turn a result into a rule for who gets the program.

A subgroup is defined by a characteristic measured before the program began, such as sex or starting score.

## When to use it

### Use it when
- A trial has an overall effect and someone asks "who did it work for?"
- The analysis plan named subgroups, and they now need testing
- Someone proposes "the main effect was null, let's check the subgroups" after seeing the results
- The team wants a causal forest or another machine-learning method to find who responds

### Do not use it when
- The subgroups are still being chosen before the trial; use `write-pre-analysis-plan`
- The question is the sample needed to detect a subgroup difference; use `estimate-sample-size`
- The question is whether the effect will hold at scale; use `assess-scalability`

## Before you start

Ask these before producing anything. Do not ask anything the user has already answered.

1. **Required.** The analysis plan (outcome, model, and the subgroups it names with their expected direction), or a statement that there is none.
2. **Required.** A description of the data: arms, unit of randomization, sample per arm, baseline characteristics, the outcome's units, and how the sample was drawn.
3. Optional. The data or regression output, and the software in use.
4. Optional. The decision the result informs: description, what to pre-register, or who gets the program.

If 2 is missing, ask and stop. With no plan, label every result exploratory. If 3 is missing, write the analysis code and leave the numbers to fill in. If 4 is missing, assume description.

## What it draws on

- Skivington, K., Matthews, L., Simpson, S. A., et al. (2021). A new framework for developing and evaluating complex interventions: update of Medical Research Council guidance. *BMJ*, 374, n2061. https://doi.org/10.1136/bmj.n2061 Supports: reporting prespecified subgroup analyses, even underpowered ones.
- Haynes, L., Service, O., Goldacre, B., & Torgerson, D. (2012). *Test, Learn, Adapt*. Cabinet Office. https://www.gov.uk/government/publications/test-learn-adapt-developing-public-policy-with-randomised-controlled-trials Supports: choosing subgroups at the outset, and treating an unexpected trend as a reason for a new trial.
- Chernozhukov, V., Demirer, M., Duflo, E., & Fernández-Val, I. (2025). Fisher–Schultz Lecture: Generic machine learning inference on heterogeneous treatment effects in randomized experiments, with an application to immunization in India. *Econometrica*, 93(4), 1121–1164. https://doi.org/10.3982/ECTA19303 Supports: the three exploratory outputs and repeated splitting.

**Where the evidence comes from:** The procedure is statistical and makes no claim about how people behave. The machine-learning method was demonstrated on an immunization trial in Haryana, India; the trial guidance comes from the United Kingdom. What is local is the sample: a result speaks for a wider population only if the trial drew its people from it at random.

**Replication status:** Not applicable to the methods; subgroups chosen after the data lack power and validity, so unplanned results are labeled hypotheses.

## How to do it

1. **Copy the plan's subgroups verbatim** into the confirmatory table with their expected direction. Every other split is exploratory, whatever it shows.
2. **State the overall effect first**, from the plan's model, in the outcome's units with its confidence interval and standard errors clustered at the unit of randomization.
3. **Test each named subgroup** by adding its interaction with treatment (a term that lets the effect differ by group) to that model. Report the effect in each group and the difference, in outcome units. Correct for testing several (Benjamini-Hochberg, or Bonferroni if the plan says so) and show corrected and uncorrected p-values.
4. **For exploration, split the sample at random**, by unit of randomization, into halves. On one, fit a causal forest or other flexible model of the effect on baseline characteristics only. On the other, estimate the best linear predictor (its heterogeneity coefficient is near 1 if predicted differences are real, near 0 if noise), the average effect in each fifth of predicted benefit, and the characteristics of the most and least affected fifths. Repeat over many splits and report medians (R: grf or GenericML; Python: econml).
5. **State the power limits.** The trial was sized for the overall effect; a difference between subgroups needs a much larger sample, so a null difference is "not detectable here", not "the same for everyone".
6. **Label every exploratory result a hypothesis**, and list what to pre-register next, with the expected direction.
7. **Stop before targeting.** Turn no result into a rule for who gets the program.

See `references/worked-example.md` for a complete run.

## Output template

```markdown
# Heterogeneous effects report

**Trial:** <name; arms; unit of randomization; sample per arm>
**Primary outcome:** <outcome, in its units>
**Overall effect:** <estimate in outcome units (95% CI), from the plan's model>
**Sample:** <random sample of <population> / reached by convenience: <who>>; results speak for <whom>
**Decision this informs:** <describe / pre-register next / targeting (see the specialist note)>
**Plan status:** <plan dated <date> names <n> subgroups / no plan: everything below is exploratory>

## Named subgroups (confirmatory)

| Subgroup (verbatim from the plan) | Expected direction | Effect in each group (units, 95% CI) | Difference (units, 95% CI) | Uncorrected p | Corrected p (<method>, <n> tests) |
|---|---|---|---|---|---|
| <subgroup> | <...> | <group A: ...; group B: ...> | <...> | <...> | <...> |

<one or two sentences: which differences hold after correction, in which direction>

## Exploratory splits (hypotheses only)
- **Method and software:** <causal forest / generic machine learning; package>
- **Sample splitting:** <fit half / test half, split by <unit>; <n> repeated splits; medians reported>
- **Characteristics used:** <baseline only: list>
- **Best linear predictor:** heterogeneity coefficient <estimate (95% CI)>; <reads as: real differences detected / not distinguishable from noise>
- **Average effect by fifth of predicted benefit:**

  | Group | Effect (units, 95% CI) |
  |---|---|
  | Least affected fifth | <...> |
  | <middle fifths> | <...> |
  | Most affected fifth | <...> |
  | Most minus least | <...> |

- **Most and least affected compared:** <characteristic: mean in most affected, mean in least affected, difference; three to six rows>

## Power limits
<what the trial was sized for; why a null difference means "not detectable here"; which subgroups, if any, the plan sized for>

## What to pre-register next time
- <subgroup>, expected <direction>, because <the result here>

## What to check before relying on this
- <who this sample can speak for>
- <that every exploratory result keeps its label wherever the report is read>
- <that no rule for who gets the program has been drawn from it>
```

## Where it goes wrong

- **An unplanned split reported as a finding.** "It worked for women", from a split no plan named, reaches the funder's summary unlabeled.
- **Fishing after a null.** "The overall effect was null, so check the subgroups" is the usual route to a false positive.
- **A characteristic read as a cause.** Girls benefiting more does not mean being a girl caused it; the characteristic may stand in for something unmeasured.
- **A convenience sample speaking for a population.** If the sample is whoever could be reached, the most-affected fifth describes who among them responded, not who in the district would.

## When to bring in a specialist

Tell the user to consult a statistician or econometrician with trial experience when:
- A subgroup result would decide who gets or loses the program: that needs a confirmatory test in a sample sized for it, and a review of who would be excluded
- There are few clusters, since subgroup differences become unreliable well before the overall effect does
- The machine-learning results disagree across splits and the team wants to act on them
- There is no plan and the result will feed a funding decision

Bring them: the plan, the data description, and this report.
