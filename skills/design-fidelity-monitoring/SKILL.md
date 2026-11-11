---
name: design-fidelity-monitoring
description: >-
  Use when a program is about to roll out, or is rolling out, and the team
  needs to know whether it is being delivered as designed: which parts to
  watch, what counts as delivered, who checks, how often, and what happens
  when delivery slips. Plans the indicators, data sources, thresholds, and
  feedback to the people delivering it. Do not use when the program is over
  and the question is why it failed; use review-prior-intervention. Not for
  writing down what the intervention is; use draft-intervention-description.
license: CC-BY-4.0
metadata:
  title: Monitor whether a program is delivered as designed
  type: atomic
  stage: implement
  version: "0.2.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  tested_in: not-applicable
  tags: "implementation-science, process-evaluation, implementation"
  consumes: "intervention-description"
  produces: "fidelity-plan"
---

## What it does

Plans how a team will check fidelity, the degree to which a running program is delivered as designed.

**What this adds:** names the parts that carry the mechanism before choosing what to count; separate indicators for adherence, dose, and quality; a source the deliverer does not keep for each essential part, with back-checks for contact only; an owner for every threshold; and an agreement with the evaluator on corrections during a trial.

## When to use it

### Use it when
- A rollout is starting or under way and the only check on delivery is the deliverers' own log
- A funder or evaluator asks for a fidelity or implementation-monitoring plan
- Someone asks "how do we know the health workers are saying the right thing?"

### Do not use it when
- The program is over and the question is whether the idea or its delivery failed; use `review-prior-intervention`
- The team needs an item-by-item account of what the intervention is; use `draft-intervention-description`
- Known changes need judging against what makes the program work; use `specify-intervention-adaptations`

## Before you start

Ask these before producing anything. Do not ask anything the user has already answered.

1. **Required.** The program's parts, who delivers each, to whom, how often. If the account is only "health workers counsel mothers", ask what the counseling contains.
2. **Required.** Who delivers, how many, and who supervises them.
3. **Required.** What the data are for: support, an evaluation, or also appraisal, pay, or discipline.
4. Optional. Existing records, whether they are filled in at delivery, and the budget.

If 1 or 2 is missing, ask and stop. If 3 is missing, ask once, then assume support only and flag it. If 4 is missing, treat records as unchecked and plan for a small team.

## What it draws on

- Carroll, C., Patterson, M., Wood, S., et al. (2007). A conceptual framework for implementation fidelity. *Implementation Science*, 2, 40. https://doi.org/10.1186/1748-5908-2-40 Supports: adherence (content, coverage, frequency, duration) as the core measure, and naming the essential components first.
- Moore, G. F., Audrey, S., Barker, M., et al. (2015). Process evaluation of complex interventions: Medical Research Council guidance. *BMJ*, 350, h1258. https://doi.org/10.1136/bmj.h1258 Supports: fidelity, dose, and reach; independent monitors; deciding whether findings correct delivery as problems appear.
- Gibson, M. (2021). *Implementation monitoring*. J-PAL Research Resources. https://www.povertyactionlab.org/resource/implementation-monitoring Supports: administrative data, unannounced visits, and back-checks as sources; tracking compliance, spillovers, and contamination for an evaluation.
- OECD (2019). *Tools and Ethics for Applied Behavioural Insights: The BASIC Toolkit*. https://doi.org/10.1787/9ea76a8f-en Supports: watching features that look unimportant to the people delivering, because those get dropped.

**Where the evidence comes from:** The method makes no claim about how people behave. Its frameworks come from health research, and J-PAL's guidance from field trials, many in low- and middle-income countries. Studies of the monitoring methods from Nigeria, Zambia, India, and the United States are in `references/evidence.md`; check locally whether registers are filled in at the visit.

**Replication status:** Not applicable; this is method guidance. How far delivery may vary before it is a different program is unresolved, so the plan logs changes for judgment.

## How to do it

1. **Name the essential parts.** For each part, write the mechanism it carries and mark it essential (dropping it removes the mechanism) or adaptable. Look hardest at details deliverers think trivial, such as a script's wording; they go first. If nobody knows which parts are essential, monitor them all.
2. **Write separate indicators per essential part:** adherence (content delivered as specified), dose (how many intended people, how often, how long), quality, and, where visible, participants' responsiveness, each worded so two monitors would record the same value.
3. **Give every essential part a source the deliverer does not keep.** Logs give dose but are kept by the person checked; unannounced observation gives adherence and quality; a back-check of a random sample of participants confirms contact, not content, because people recall what was said poorly.
4. **Set the sample and schedule:** how many per round, drawn at random by the monitor, how often, by whom. Check often what fails fast, such as stock; mark what to cut first.
5. **Set each threshold:** expected level, trigger level, action, and who acts. Say what a shortfall would mean; delivery on target with no change in behavior points to the design.
6. **Decide the feedback:** who sees which results, how often, as the gap and one next step, by team or site, ranking no one. Put in writing that the data stay out of appraisal, pay, and discipline, and give deliverers a channel back. In an effectiveness trial, agree with the evaluator before launch whether results may correct delivery.
7. **Keep a change log** of each unplanned change as it happens: date, what, who, why, part touched.
8. **For an evaluation, also track** people assigned but not reached, comparison-group people reached, spillover, and dropout.

See `references/worked-example.md` for a complete run.

## Output template

```markdown
# Fidelity monitoring plan: <program>

**Delivered by:** <who, how many, supervised by whom>
**Use of the data:** <support only / also an evaluation / appraisal, pay, or discipline: see the specialist note>; <"assumed; confirm with <organization> before launch" if not stated>

## Essential parts
| Part | Mechanism it carries | Essential or adaptable | Why |
|---|---|---|---|
| <part> | <what it changes for the person receiving it> | <essential / adaptable> | <dropping it removes the mechanism / it can vary without loss> |

## Indicators
| Part | Dimension | Indicator | Source | Sample and frequency | Collected by |
|---|---|---|---|---|---|
| <part> | <adherence / dose / quality / responsiveness> | <what two monitors would record alike> | <log / observation / back-check / exit interview> | <n per round, drawn how, how often> | <role; not the person checked> |

## Thresholds and actions
| Indicator | Expected level | Act when | Action | Who acts |
|---|---|---|---|---|
| <indicator> | <from a pilot, or "assumed"> | <level> | <concrete step> | <role> |

## Feedback to the people delivering
- **Who sees what, how often:** <roles, results, form>
- **Rule:** <by team or site; no ranking; not used for appraisal, pay, or discipline; where it is written down>
- **Their channel back:** <how deliverers report what stops them>
- **During an evaluation:** <corrections allowed or not, as agreed with the evaluator; or "no evaluation">

## Change log
<where unplanned changes are recorded and by whom: date, what changed, who, why, part touched>

## What an evaluation needs caught
<assigned but not reached, comparison group reached, spillover, dropout: an indicator for each; or "no evaluation planned">

## How to read the results
<what a shortfall on each essential part would mean; on target with no change in behavior points to the design>

## What to check before relying on this
- <the assumption most likely to be wrong, such as registers filled in at the visit>
- <the part the team is least sure is essential>
```

## Where it goes wrong

- **Punitive drift.** Support becomes a league table or a bonus trigger, and records then show what protects their keepers. When an Indian district punished nurses' absence, the health administration appears to have undermined the scheme by granting "exempt days"; after 18 months it had no effect.
- **Freezing the program.** Every deviation is treated as failure, or every change excused as "local adaptation"; the log exists so each is judged.
- **Monitoring heavier than delivery.** Deliverers spend more time being checked than delivering, and the plan is dropped after the first quarter.

## When to bring in a specialist

Tell the user to consult a specialist when:
- The data will feed appraisal, pay, or discipline: an implementation researcher and the human-resources lead, to redesign the feedback before launch
- A government partner delivers and nothing written says who may observe whom: the partner's data-governance office and counsel
- Monitoring observes clinical care, children, or stigmatized services, or uses mystery clients (people posing as clients): an ethics reviewer
- The plan must double as a process evaluation: an implementation researcher, for mechanisms and context

Bring them: the essential-parts and indicator tables, and the data-use answer.
