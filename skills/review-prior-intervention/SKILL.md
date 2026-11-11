---
name: review-prior-intervention
description: >-
  Use when a team has a record of a program it already ran and must decide
  whether to retry it, change it, or drop the idea, or when someone says "we
  tried that and it didn't work" as if that settles it. Compares what was
  planned with what was delivered, checks the team's explanation against the
  data it collected, and judges whether the idea or its delivery failed, or
  whether the record cannot tell. Do not use to design the next attempt; use
  select-intervention-levers. Not for what others have tried elsewhere; use
  assess-evidence-base.
license: CC-BY-4.0
metadata:
  title: "Review a past program: bad idea or bad delivery?"
  type: atomic
  stage: analyze
  version: "0.2.0"
  status: draft
  authors: "Joe Speed, Zezhen Wu"
  org: IL
  tested_in: not-applicable
  tags: "process-evaluation, implementation, post-mortem"
  consumes: "prior-intervention-record"
  produces: "intervention-post-mortem"
---

## What it does

Judges whether a past program failed because of its idea or because of its delivery.

**What this adds:** checks delivery and whether people responded before judging the idea; labels every finding confirmed or inferred; tests the team's own explanation against its data and names an alternative the data does not rule out; asks whether a null result could rule out a useful effect; and gives one of four fixed classifications, including "cannot yet tell".

## When to use it

### Use it when
- A team has a record of a program it ran and must decide whether to retry it, change it, or drop the idea
- Someone says "we tried this before and it didn't work" as if that settles whether the idea is bad
- A funder asks why a pilot failed, and the answer so far is a story, not a reading of the data

### Do not use it when
- The team wants to design the next attempt; use `select-intervention-levers`
- The question is what others have tried elsewhere; use `assess-evidence-base`
- The team wants a plan for tracking delivery next time; use `design-fidelity-monitoring`

## Before you start

Ask these before producing anything. Do not ask anything the user has already answered.

1. **Required.** A written record of the program: what was planned, what the team believes happened, and why. Notes count; memory alone does not.
2. **Required.** What data was collected (delivery logs, attendance, outcomes, surveys), and whether each was tracked routinely or noticed in passing.
3. Optional. For a comparison with a control group, the estimate and its confidence interval.
4. Optional. The decision this review informs, and what a retry would cost.

If 1 is missing, ask the team to write down what it remembers, and stop. If 2 is missing, ask once; if there is no data, proceed and say at the top that the answer will almost certainly be "cannot yet tell". If 4 is missing, assume a retry is moderately costly.

## What it draws on

- Moore, G. F., Audrey, S., Barker, M., et al. (2015). Process evaluation of complex interventions: Medical Research Council guidance. *BMJ*, 350, h1258. https://doi.org/10.1136/bmj.h1258 Supports: the delivery dimensions, the response line (its "mechanisms of impact"), and that a program can fail through its design or its implementation.
- Durlak, J. A., & DuPre, E. P. (2008). Implementation matters: A review of research on the influence of implementation on program outcomes and the factors affecting implementation. *American Journal of Community Psychology*, 41(3–4), 327–350. https://doi.org/10.1007/s10464-008-9165-0 Supports: checking delivery first. In over 500 studies of prevention and promotion programs, the level of implementation affected outcomes.
- Kettle, S., & Persian, R. (2022). *Target, Explore, Solution, Trial, Scale: An introduction to running simple behavioural insights projects*. The Behavioural Insights Team. https://www.bi.team/wp-content/uploads/2022/11/BIT-Handbook-How-to-run-simple-BI-projects.pdf Supports: asking participants whether it reached them, the precision check on a null result, and the next steps.

**Where the evidence comes from:** The procedure makes no claim about how people behave. The MRC guidance and the BIT guide come from the United Kingdom; the review's abstract does not say where its studies were run. What is local is the record: who kept the logs, and whether anyone asked participants.

**Replication status:** Not applicable: this is a structured judgment, and no source tests whether two reviewers classify the same record alike.

## How to do it

1. **Condense the record** at the top.
2. **Write what was planned:** the target behavior, how the program was meant to change it, and the intended delivery.
3. **Write what was delivered:** fidelity (as designed?), dose (how much, against the plan?), reach (what share of the intended people?), and context (what changed around it?). Label each "confirmed by the record" or "inferred". The record's reason for a choice ("the hall was free only at 2pm") does not show the choice caused an outcome ("low attendance") unless the record connects them.
4. **Write whether people responded as planned:** did those reached open, understand, or use it? Without this, a flat outcome cannot separate an idea that failed from one nobody noticed.
5. **Record the outcome as observed**, with its strength: a routinely tracked measure outweighs an informal observation. For a comparison, say whether the confidence interval rules out an effect worth having; a wide interval around zero means the test was too small.
6. **Check the team's explanation.** Quote it, say whether the data supports it (yes, no, or partly, naming the data point), and name an alternative the data does not rule out.
7. **Classify:** implementation failure, idea failure, both, or cannot yet tell. Idea failure needs adequate delivery and response; a null result with thin delivery data is "cannot yet tell", however detailed the brief. An approximate figure ("roughly 15%") is enough to decide its own dimension. For idea failure, say whether the doubt is about the activity or the barrier it targeted.
8. **List what to address before any retry**, and the next steps the evidence leaves open. Do not redesign.

See `references/worked-example.md` for a complete run.

## Output template

```markdown
# Intervention post-mortem brief

**Prior intervention (as given):** <verbatim or lightly cleaned account>

## What was planned
<target behavior; how the program was meant to change it; intended delivery>

## What was actually delivered
- **Fidelity:** <delivered as designed, or how it diverged> **Basis:** <confirmed by the record / inferred>
- **Dose:** <how much was delivered, against the plan> **Basis:** <confirmed by the record / inferred>
- **Reach:** <what share of the intended people it got to> **Basis:** <confirmed by the record / inferred>
- **Context:** <what changed around the program; no cause presented as confirmed unless the record connects it> **Basis:** <confirmed by the record / inferred>
- **Response:** <whether people reached opened, understood, or used it; or "no data"> **Basis:** <confirmed by the record / inferred>

## Outcome as observed
<what was measured, and how strong it is: routinely tracked or noticed in passing; for a comparison, the estimate, its interval, and whether it rules out an effect worth having>

## Causal claim check
- **Team's stated reason for the outcome:** <verbatim or closely paraphrased>
- **Does the collected data support it?** <yes / no / partly: the data point that does or does not>
- **Alternative explanation the data does not rule out:** <...>

## Implementation failure vs. idea failure
**Classification:** <implementation failure / idea failure / both / cannot yet tell>
<why, from the findings above; for idea failure, whether the doubt is about the activity or the barrier it targeted>

## Factors to address before any retry
- <what this review found unaddressed, for whoever designs the next attempt>

**Next steps the evidence leaves open:** <any of: run it again as designed / run it with more people or in another population / change the design / try another approach to the same behavior / choose another behavior>
```

## Where it goes wrong

- **Praise taken as receipt.** Participants asked afterward may say they liked a message they never read. Ask what they did with it, and check it against the logs.
- **One review treated as universal.** A post-mortem speaks for the population, channel, and period it covered; a retry elsewhere needs its own check.
- **Drifting into redesign.** A brief that ends "here is what we should build instead" has become intervention design.

## When to bring in a specialist

Tell the user to consult an implementation or process evaluator, and where relevant an independent evaluator or a statistician, when:
- The record is thin on delivery and the retry would be large or costly
- The program involved harm (health, safety, financial loss), so attribution matters to participants
- The team's explanation is contested inside the organization or with a funder
- The past attempt was a formal evaluation and the question is whether its analysis was sound

Bring them: the record, the delivery logs and outcome data, and this brief.
