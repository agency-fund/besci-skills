---
name: design-list-experiment
description: >-
  Use when a program needs the share of a group that does something people
  hide (missed doses, bribes, sex without a condom) and expects denial if
  asked directly: "nobody will admit that", "our self-reports look too good".
  Decides whether a list experiment is worth its cost in sample, then writes
  the two lists, the counting script, the direct question, and the checks. Do
  not use when a direct question would be answered honestly or the sample is
  a few hundred; use draft-survey-items. Not for what people think others do
  or approve of; use draft-norms-vignette.
license: CC-BY-4.0
metadata:
  title: Measure a sensitive behavior without asking directly
  type: atomic
  stage: measure
  version: "0.2.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  tested_in: beyond-western-differs
  tags: "list-experiment, survey-design, measurement, quantitative"
  consumes: "measurement-plan"
  produces: "survey-items"
---

## What it does

Designs a survey question that estimates how common a hidden behavior is without any respondent admitting to it.

**What this adds:** decides go or no-go against published thresholds; picks control statements so few people can answer none or all; requires a practice list and a private way to count; fields the direct question alongside; and names the checks that show whether it worked.

In a list experiment, half the respondents say how many of a few harmless statements are true for them, not which; the other half get the same list plus the sensitive statement. The difference in average counts estimates the share for whom it is true.

## When to use it

### Use it when
- A program needs the share of a group that does something people hide, and direct questions look too good
- Someone says "nobody will admit that on a survey" or asks for an "item count" or "list experiment" question
- A team wants to know how much people under-report a sensitive outcome

### Do not use it when
- A plainly worded direct question would be answered honestly; use `draft-survey-items`
- The sample is a few hundred, or the estimate is needed for small subgroups: ask directly, in private; use `draft-survey-items`
- The question is what people think others do or approve of; use `draft-norms-vignette`
- The question is how many respondents are needed; use `estimate-sample-size`

## Before you start

Ask these before producing anything. Do not ask anything the user has already answered.

1. **Required.** The behavior: who, what, over what period, and why people here would hide it.
2. **Required.** The respondents (schooling, language) and whether the survey is face to face, by phone, or self-completed.
3. **Required.** How many respondents are affordable, and whether the estimate is for everyone, for subgroups, or for comparing groups.
4. Optional. What direct questions have returned, and what the team believes the true figure is.

If 1 to 3 are missing, ask and stop. If 4 is missing, assume under-reporting below 10 percentage points, the usual finding.

## What it draws on

- Blair, G., Coppock, A., & Moor, M. (2020). When to worry about sensitivity bias: A social reference theory and evidence from 30 years of list experiments. *American Political Science Review*, 114(4), 1297–1315. https://doi.org/10.1017/S0003055420000374 Supports: the thresholds in step 1, and privacy as the first alternative.
- Blair, G., & Imai, K. (2012). Statistical analysis of list experiments. *Political Analysis*, 20(1), 47–77. https://doi.org/10.1093/pan/mpr048 Supports: the control statements and the checks in step 7.
- Kramon, E., & Weghorst, K. (2019). (Mis)measuring sensitive attitudes with the list experiment. *Public Opinion Quarterly*, 83(S1), 236–263. https://doi.org/10.1093/poq/nfz009 Supports: private counting, and checking that respondents can do the task.

**Where the evidence comes from:** A meta-analysis of 264 list experiments finds direct questions usually off by less than 10 percentage points; its 19 on vote buying are from developing countries. Field results disagree: more vote buying by list in Nicaragua and more partner violence in Nigeria, no difference in Peru, and worse than direct questions against known HIV status in South Africa. Check locally whether respondents can keep count in their head.

**Replication status:** Mixed. Two further meta-analyses find lists raise reported rates on average with wide variation; in Kenya, Cameroon, and Côte d'Ivoire many respondents did not follow the task.

## How to do it

1. **Decide go or no-go.** A list estimate is about 14 times as variable as a direct question. With 1,000 respondents it is the better estimate only if under-reporting exceeds about 5.5 percentage points; with 2,000, about 4. Telling two groups apart takes a gap near 20 points even with 2,000. If no-go, recommend a direct question asked in private or self-completed, and stop. A list may still be right where asking directly would endanger respondents.
2. **Write the sensitive statement:** one plain sentence about one behavior, over the same period as the direct question.
3. **Choose three or four control statements:** harmless, some true for few people and some for most, with one pair that rarely go together. A respondent for whom every statement is true, or only the sensitive one, has no cover and may lie.
4. **Assign respondents at random,** half to each list, by the survey software.
5. **Write the script:** the instruction ("tell me how many, not which"); a practice list; a private way to count, such as marks on a card the interviewer does not see; what the interviewer says when a respondent names a statement.
6. **Add the direct question** on the same behavior after the list, so the gap is measured, not assumed.
7. **Name the checks to run on the data:** the share of the short-list group counting none or all; the design-effect test (did adding the sensitive statement change answers to the others; in the R package `list`); the list estimate minus the direct one.
8. **Fix the reporting rule before fielding:** which estimate is primary if the checks pass, and if they fail.

See `references/worked-example.md` for a complete run.

## Output template

```markdown
# List experiment design: <behavior>

**Behavior:** <who, what, over what period>
**Why people would hide it here:** <...>
**Respondents and mode:** <who; schooling; language; face to face / phone / self-completed>
**Affordable sample:** <n>  **Estimate needed for:** <everyone / subgroups / comparing groups>

## Go or no-go
- **Plausible under-reporting:** <percentage points, and what that rests on>
- **What this sample can show:** <against the thresholds>
- **Decision:** <go / go on conditions / no-go: ask directly, in private>

## Statements
**Sensitive statement (long list only):** "<...>"
**Control statements (both lists):**
1. "<...>" (expected to be true for <few / about half / most>)
2. "<...>" (<...>)
3. "<...>" (<...>)

**Why few respondents will count none or all:** <the rare statement, the common one, the pair that rarely go together>
**Order in the long list:** <...>

## Random assignment
<unit; how generated; what is recorded; what the interviewer sees>

## Script
- **Instruction as read:** "<...>"
- **Practice list:** <statements; what the interviewer checks>
- **Private way to count:** <...>
- **If a respondent names a statement:** <...>

## Direct question
"<...>" asked of <whom>, <where in the survey>

## Checks on the data
- **Short-list group counting none or all:** <the share that raises concern>
- **Design-effect test:** <how it is run>
- **List estimate minus direct estimate:** <with its confidence interval>

## Reporting rule
<which estimate is primary if the checks pass; if they fail>

## For the sample-size calculation
<expected share; spread of the short-list count; groups to compare>

## What to check before relying on this
- <the control statement most likely to be near-universal, rare, or sensitive here>
- <whether respondents in this mode can keep count>
```

## Where it goes wrong

- **A lower list estimate read as honesty.** In Kenya a list showed less support for political violence than the direct question did. An estimate below the direct one, or below zero, means the list failed.
- **Individual answers inferred.** The design gives a share for a group. Refuse to score, target, or follow up individuals from it.
- **Under-reporting borrowed from elsewhere.** Across 19 vote-buying studies the gap ran from 24 points of under-reporting to 5 points of over-reporting. A prior is a guess that the direct question tests.

## When to bring in a specialist

Tell the user to consult, before fielding:
- An ethics reviewer, when the behavior is illegal or dangerous to disclose even for a group (drug use, same-sex relations, opposition politics), or results will be reported for small areas: a group figure can be used against the group
- A survey statistician, when the list estimate is the main outcome of an evaluation or must be compared across arms or subgroups

Bring them: the statements, the plausible under-reporting, the sample, the mode, and the checks.
