---
name: plan-evaluation-design
description: >-
  Use when a target behavior is defined but nobody has agreed what will be
  measured to show it changed, or someone asks "how will we know if this
  worked?" or "what are our indicators?". Names one primary outcome, where
  its data will come from, when it is measured, and the smallest change
  worth detecting, fixed before launch. Do not use when the goal is still
  vague; use define-key-behavior. Not for choosing the comparison or how to
  randomize (choose-trial-design), or for fixing the analysis
  (write-pre-analysis-plan).
license: CC-BY-4.0
metadata:
  title: Plan how you will measure success
  type: atomic
  stage: test
  version: "0.2.0"
  status: draft
  authors: "Joe Speed, Zezhen Wu"
  org: IL
  tested_in: not-applicable
  tags: "measurement, experimental-design"
  consumes: "target-behavior-brief"
  produces: "measurement-plan"
---

## What it does

Chooses the one outcome that will show whether a defined behavior changed, with the data source behind it.

**What this adds:** allows one primary outcome and labels any stand-in a proxy; works down a fixed order of data sources; names who confirmed every feasibility answer, refusing "assumed available"; records whose threshold the smallest change worth detecting is, or marks it provisional; and dates the outcome so it cannot be swapped after results arrive.

## When to use it

### Use it when
- A target behavior is defined and an intervention is about to launch with no named primary outcome
- Someone asks "how will we know if this worked?", or a funder asks for "the indicators" for a behavior already chosen
- A team has several candidate measures (logins, deposits, a survey score) and must pick one

### Do not use it when
- The goal is still vague, with no single behavior to measure; use `define-key-behavior`
- The question is what the outcome is compared against, or what to randomize; use `choose-trial-design`
- The outcome is chosen and the team needs the analysis or a registry entry; use `write-pre-analysis-plan`
- The question is how many people the test needs; use `estimate-sample-size`

## Before you start

Ask only what the user has not answered.

1. **Required.** The target behavior, as who does what, when.
2. **Required.** What data exist or could exist (records, logs, staff who could observe, surveys), and who controls each.
3. Optional. The smallest change that would justify scaling, and who set it.
4. Optional. The barriers believed to explain the behavior.
5. Optional. When the decision is due.

If 1 or 2 is missing, ask and stop. If 3 is missing, ask once, then mark it provisional. Without 4, list no intermediate measures. Without 5, propose a window.

## What it draws on

- Kettle, S., & Persian, R. (2022). *Target, Explore, Solution, Trial, Scale: An introduction to running simple behavioural insights projects*. The Behavioural Insights Team. https://www.bi.team/wp-content/uploads/2022/11/BIT-Handbook-How-to-run-simple-BI-projects.pdf Supports: the target behavior, not the wider objective, as the primary outcome; the four types of data in order of preference; the feasibility questions.
- Haynes, L., Service, O., Goldacre, B., & Torgerson, D. (2012). *Test, Learn, Adapt*. Cabinet Office. https://assets.publishing.service.gov.uk/media/5a7488c8e5274a7f9c586c23/TLA-1906126.pdf Supports: fixing at the outset what is measured, how, and when; measuring every group the same way; the caution about surrogate outcomes and self-reports.
- Duflo, E., Glennerster, R., & Kremer, M. (2007). Using randomization in development economics research: A toolkit. In *Handbook of Development Economics* (pp. 3895–3962). Elsevier. https://doi.org/10.1016/S1573-4471(07)04061-2 Supports: step 6.

**Where the evidence comes from:** This is a planning procedure and makes no claim about how people behave. Its sources are guides from a UK government team and from development economists whose examples come mostly from low- and middle-income countries. What is local is the data: which records exist, who holds them, and whether people would overstate the behavior.

**Replication status:** Not applicable. The sources disagree on whether to allow more than one primary outcome; this skill asks for one.

## How to do it

1. **Carry the target behavior over** word for word.
2. **Name one primary outcome** that observes the behavior itself, not the program's wider objective, which other things also move. Define what is counted, out of whom, per what period. Count everyone eligible, not only participants, since the program changes who participates.
3. **Choose the data source** by working down this order, taking the first that records the behavior for each person or unit:
   - records already collected routinely;
   - the same records with a field added, or a paper process made digital;
   - observation or a survey run for this purpose;
   - a proxy, which must change when the behavior changes; name the gap it leaves. A self-report is a weak proxy when people want to please the asker.
4. **Check feasibility**, writing who confirmed each answer: who holds the data; individuals or totals; how often recorded; format; consent and approvals; whether it is recorded alike for everyone compared; and how the record could change without the behavior changing, as when staff are paid on that number. Unconfirmed answers go under "Open questions".
5. **Set when it is measured**: a baseline before launch, then a window long enough for the behavior to show and short enough for the decision.
6. **State the smallest change worth detecting**, in the outcome's units, with who set it: the smallest change that would make the intervention worth its cost at scale. It is what the program needs to see, not what a study can detect.
7. **List other measures**, five at most: one intermediate measure per barrier supplied, to explain a null result, and anything that must not get worse.
8. **Write the outcome statement**: one dated sentence naming the primary outcome, source, window, and smallest change worth detecting.

See `references/worked-example.md` for a complete run.

## Output template

```markdown
# Measurement plan

**Target behavior:** <who does what, when; carried over word for word>

## Primary outcome
- **Measure:** <one measure>
- **Defined as:** <what is counted, out of whom, per what period>
- **Observes the behavior directly:** <yes / proxy: what it stands in for, the gap it leaves, why it should track the behavior>
- **Could be distorted by:** <how the record could change without the behavior changing; or "nothing identified">

## Data source

| Option | Available here? | Verdict |
|---|---|---|
| Records already collected | <...> | <chosen / rejected: why> |
| Records with a field added | <...> | <...> |
| Observation or survey | <...> | <...> |
| Proxy | <...> | <...> |

**Chosen source:** <...>

## Feasibility

| Check | Answer | Confirmed by |
|---|---|---|
| Who holds the data and grants access | <...> | <name or role / not confirmed> |
| Individuals or totals | <...> | <...> |
| How often recorded, against when needed | <...> | <...> |
| Format | <...> | <...> |
| Consent and approvals | <...> | <...> |
| Recorded the same way for everyone compared | <...> | <...> |

## When it is measured
<baseline period; outcome window; the decision date it serves>

## Smallest change worth detecting
<value in the outcome's units; who set it and why / "Provisional: nobody has set a threshold; <who> must decide">

## Other measures

| Measure | Role | Source |
|---|---|---|
| <...> | <intermediate: which barrier / must not get worse> | <...> |

## Outcome statement
As of <date>, the primary outcome is <...>, from <source>, measured <window>; the smallest change worth detecting is <...>.

## Open questions
- <each feasibility answer nobody has confirmed, and who can confirm it>
```

## Where it goes wrong

- **Data only the program generates.** App logs and attendance sheets exist only for people the intervention reached, leaving nothing to compare them with.
- **A borrowed threshold.** A number from a statistics template or a published study is not what this program needs to see.
- **Sliding into the comparison.** "We will compare before and after" creeps in; the comparison is a separate decision.
- **Editing the outcome in place.** If the source fails after launch, write a new dated statement and keep the old. A silent edit looks like choosing the measure that moved.

## When to bring in a specialist

Tell the user to consult:
- **A research ethics board**, when the outcome concerns health, safety, or benefits eligibility, or the data come from children or other vulnerable people
- **A survey methodologist**, when the only feasible measure is a self-report of a sensitive behavior, or a state of mind that needs a tested scale
- **An evaluation methodologist**, when the result will decide a national rollout, or the only source is an untested proxy

Bring them: this plan with its open questions, any baseline figures, and who holds the data.
