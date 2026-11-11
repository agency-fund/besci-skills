---
name: choose-trial-design
description: >-
  Use when a team knows what it wants to test but not how to compare:
  "should we randomize people or villages?", "everyone has to get it
  eventually", "which of our components matter?", or a plan says "RCT" with
  no unit named. Chooses the design and unit of randomization from the
  program's constraints, names a runner-up, and says when no randomized
  design fits. Do not use for choosing the outcome or its data source
  (plan-evaluation-design), the analysis (write-pre-analysis-plan), or the
  sample size (estimate-sample-size).
license: CC-BY-4.0
metadata:
  title: Pick how to randomize the test
  type: atomic
  stage: test
  version: "0.2.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  tested_in: not-applicable
  tags: "experimental-design, quantitative"
  consumes: "experiment-intent"
  produces: "evaluation-design"
---

## What it does

Chooses the comparison for one test: which randomized design, at which unit.

**What this adds:** marks unstated constraints "unknown" instead of guessing; rules six designs in or out, each against a named constraint; requires a recorded random draw and a named person who agreed to any delay; names a runner-up; and says plainly when no randomized design fits.

## When to use it

### Use it when
- Someone asks "individuals or villages?" or "how do we test this when everyone must get it eventually?"
- People reached through one channel (a health worker, a WhatsApp group) would mix with others
- The intervention has separable components or versions, and the decision needs to know which matter

### Do not use it when
- The outcome or its data source is still open; use `plan-evaluation-design`
- The design is chosen and the team needs the estimator or a registry entry; use `write-pre-analysis-plan`
- The design is set and the question is how many units; use `estimate-sample-size`
- The team must first learn whether the program can be delivered at all; use `design-pilot-feasibility-study`

## Before you start

Ask only what the user has not answered. Each required answer decides a branch: if one is missing, ask and stop.

1. **Required.** The change, who gets it, the outcome, and the decision the result informs.
2. **Required.** How the change could reach people not assigned it (talk, a shared worker or phone).
3. **Required.** Must every unit get it by a date; how many can start per period; can some wait, and who decides.
4. **Required.** Can the program decide who receives it, or only who is offered it?
5. **Required.** How many components or versions, and whether the decision needs each one's value.
6. Optional. Unit counts at each level, and periods; without them, feasibility is unchecked.

## What it draws on

- Haynes, L., Service, O., Goldacre, B., & Torgerson, D. (2012). *Test, Learn, Adapt*. Cabinet Office. https://assets.publishing.service.gov.uk/media/5a7488c8e5274a7f9c586c23/TLA-1906126.pdf Supports: people, institutions, or areas as the unit; a random order for a staggered rollout; a draw nobody with a stake can steer.
- Kopper, S., & Sautmann, A. (2023). *Randomization*. J-PAL Research Resources. https://www.povertyactionlab.org/resource/randomization Supports: the delivery unit, or one containing spillovers, as the unit; stratification; a replicable draw.
- Duflo, E., Glennerster, R., & Kremer, M. (2007). Using randomization in development economics research: A toolkit. In *Handbook of Development Economics* (pp. 3895–3962). Elsevier. https://doi.org/10.1016/S1573-4471(07)04061-2 Supports: phase-in, encouragement, and factorial designs, and how each fails.
- Hemming, K., Haines, T. P., Chilton, P. J., Girling, A. J., & Lilford, R. J. (2015). The stepped wedge cluster randomised trial: rationale, design, analysis, and reporting. *BMJ*, 350, h391. https://doi.org/10.1136/bmj.h391 Supports: the stepped-wedge row.

**Where the evidence comes from:** This is a design procedure and makes no claim about how people behave. Its sources are UK guides, J-PAL's research guidance, and a toolkit by development economists with many examples from Kenya and India. The constraints that decide the design (phased rollouts, shared workers, few administrative units) are local facts.

**Replication status:** Not applicable: these are design methods, not interventions. Their limits are stated with each design below.

## How to do it

1. **Fill the constraints table.** Mark anything not stated "unknown"; do not guess.
2. **Rule each design in or out** against a named constraint, and note what each surviving one costs:
   - **Individual:** delivered to individuals, no spillovers, some can go without for the study period.
   - **Cluster:** the change is delivered to, or spreads within, a group (a class, a clinic). Randomize the smallest unit that contains the spread; it needs more people for the same precision.
   - **Stepped-wedge (randomized phase-in):** everyone must get it and capacity forces phases. Randomize the order, measure every unit in every period, and model time.
   - **Factorial:** separable components whose separate value the decision needs. Cross them so each unit gets one combination.
   - **Multi-arm:** several versions of one change, and the decision is which. Each arm splits the sample; similar versions need many units to tell apart.
   - **Encouragement:** the program controls only the offer. Randomize the offer; it works only if the offer changes take-up a lot.
3. **Choose one**, naming the deciding constraints. If nothing can be randomized, not even the order or the offer, write "No randomized design fits" and give the specialist note.
4. **Specify it**: unit, arms and allocation, timing, and what to stratify on (a variable that predicts the outcome, or a subgroup the decision cares about).
5. **Say how assignment is drawn** (software with a recorded seed, or a public lottery where fairness must be seen; by someone with no stake; filed before launch), and who agreed to any delay or withholding, on what grounds.
6. **Name the runner-up** and the condition that would make it the choice.

See `references/worked-example.md` for a complete run.

## Output template

```markdown
# Trial design choice: <test>

**Change tested:** <what, for whom>
**Outcome:** <as given>
**Decision this informs:** <...>

## Constraints
| Constraint | Answer | Source |
|---|---|---|
| Spillovers | <none / within <group> via <channel> / unknown> | <who said so> |
| Delivered to | <individuals / <group>> | <...> |
| Rollout | <all at once / <n> units per <period> / unknown> | <...> |
| Withholding | <some can go without for <period> / all by <date> / none> | <...> |
| Control | <assigns who receives it / only the offer> | <...> |
| Components or versions | <n>; decision needs each one's value: <yes / no> | <...> |
| Units available | <people, groups at each level, periods / unknown> | <...> |

## Designs ruled in or out
| Design | Verdict | Because | What it costs |
|---|---|---|---|
| Individual | <in / out> | <constraint> | <...> |
| Cluster | <...> | <...> | <...> |
| Stepped-wedge | <...> | <...> | <...> |
| Factorial | <...> | <...> | <...> |
| Multi-arm | <...> | <...> | <...> |
| Encouragement | <...> | <...> | <...> |

## Chosen design: <name, or "No randomized design fits">
- **Unit of randomization:** <...>
- **Arms and allocation:** <...>
- **Stratified by:** <variable: why>
- **Timing:** <periods, steps, dates>
- **How assignment is drawn:** <method, seed or witness, who draws, when filed>
- **Delay or withholding agreed by:** <name or role; grounds>

## Runner-up: <name>
<the condition that would make it the choice>

## Open questions
- <each "unknown" constraint and how it could change the design>
```

## Where it goes wrong

- **Few clusters treated as a trial.** Eight districts, four per arm, is not a trial, however many people live there.
- **A phase-in that measures nothing.** The later group starts before the effect can show, or holds back once told the program is coming.
- **An assignment nobody follows.** Staff treat whoever seems neediest, or procurement keeps its usual order. Prefer a simpler design the partner will hold to.
- **A factorial read for interactions.** A design sized to estimate each component cannot say whether they work better together.

## When to bring in a specialist

Tell the user to consult an evaluation methodologist, with an ethics board and the implementing authority where relevant, when:
- No randomized design fits: a quasi-experimental design (a comparison built from data, such as a matched group or an eligibility cutoff) is needed, and a specialist should choose it
- The unit is an administrative area and there are few of them
- A stepped-wedge is chosen; its time model needs a statistician before the first step
- A ministry, community leaders, or a funder contest the randomization

Bring them: the constraints and designs tables, unit counts, and the rollout calendar.
