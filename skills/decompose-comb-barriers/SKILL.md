---
name: decompose-comb-barriers
description: >-
  Use when one behavior is defined (who does what, when) and the question is
  why people are not doing it, or when a team is about to pick an
  intervention ("let's send a reminder") without naming the barrier it
  addresses. Lists competing capability, opportunity, and motivation
  hypotheses, each with a question that could rule it out, and ranks them.
  Do not use when the goal is still vague; use define-key-behavior. Not for
  choosing what to do about a confirmed barrier; use
  select-intervention-levers.
license: CC-BY-4.0
metadata:
  title: Find out why people are not doing a behavior
  type: atomic
  stage: diagnose
  version: "0.2.0"
  status: draft
  authors: "Nikhil Ravichandar, Joe Speed, Zezhen Wu"
  org: IL
  tested_in: beyond-western-differs
  tags: "com-b, behavior-change-wheel, diagnosis"
  consumes: "target-behavior-brief"
  produces: "comb-barrier-hypotheses"
---

## What it does

Lists competing reasons why one defined behavior is not happening, each with a question that could rule it out.

**What this adds:** writes at least one hypothesis under each of the six COM-B sub-components; makes every capability hypothesis pass a persistence test or moves it to opportunity; states, for each question, the answer this hypothesis predicts against the answer a rival predicts; ranks the hypotheses on evidence so far and cost of checking; and labels the ranking provisional until field answers exist.

COM-B is Michie, van Stralen and West's model: a behavior happens when a person has the capability, opportunity, and motivation for it.

## When to use it

### Use it when
- A behavior is stated as who does what, when, and someone asks "why isn't this happening?" or "what are the barriers?"
- A team is about to choose an intervention ("let's send a reminder text") without naming the barrier it addresses
- Several explanations are in the air ("maybe they forgot", "maybe it costs too much") with no way to tell them apart

### Do not use it when
- The goal is still an outcome or an aspiration ("improve maternal health"); use `define-key-behavior`
- The team wants its own beliefs about the audience checked before diagnosing; use `audit-researcher-bias`
- Hypotheses exist and the team needs the interview questions that test them; use `draft-tdf-interview-guide`
- Field evidence has confirmed the barrier and the question is what to do; use `select-intervention-levers`

## Before you start

Ask these before producing anything. Do not ask anything the user has already answered.

1. **Required.** The behavior as who does what, when. If it contains "and" or lacks an actor or a time window, ask for one behavior.
2. **Required.** What is known about the setting: where the behavior happens, and anything the team has observed or heard from the audience.
3. Optional. What the team already believes is the cause.
4. Optional. How the team can check: interviews, observation, records, or nothing yet.

If 1 is missing, ask and stop. If 2 is missing, ask once; if the answer is still thin, proceed and write "none" in every evidence cell. If 4 is missing, assume one short round of interviews.

## What it draws on

- Michie, S., van Stralen, M. M., & West, R. (2011). The behaviour change wheel: A new method for characterising and designing behaviour change interventions. *Implementation Science*, 6, 42. https://doi.org/10.1186/1748-5908-6-42 Supports: the three components, their six sub-components, and opportunity defined as everything outside the person that makes the behavior possible.
- Schmidtke, K. A., & Drinkwater, K. G. (2021). A cross-sectional survey assessing the influence of theoretically informed behavioural factors on hand hygiene across seven countries during the COVID-19 pandemic. *BMC Public Health*, 21, 1432. https://doi.org/10.1186/s12889-021-11491-4 Supports: ranking from local evidence only.

**Where the evidence comes from:** COM-B was built from 19 earlier frameworks and first applied to English tobacco and obesity policy. A review of 79 nutrition studies in sub-Saharan Africa sorted interventions with it, and the seven-country survey found that the components predicting children's handwashing differed by country (capability alone in Australia, Indonesia, and South Africa; capability and opportunity in India). Never carry a diagnosis over from another place.

**Replication status:** COM-B is a way of sorting, so there is no effect to replicate. Two coders in the original paper agreed on 88% and 79% of classifications; no study was found that tests whether a COM-B diagnosis leads to a better intervention.

## How to do it

1. **Restate the behavior** as given.
2. **Write at least one hypothesis under each sub-component**, specific enough that an answer could rule it out. List two where two distinct ones compete.
   - **Capability:** physical (bodily skill) and psychological (knowledge, understanding, memory, planning).
   - **Opportunity:** physical (time, money, distance, materials) and social (what the people around the person do, expect, and allow).
   - **Motivation:** reflective (evaluations and plans) and automatic (emotion, impulse, habit).
3. **Run the persistence test on every capability hypothesis** and write the answer: would the barrier remain if the setting gave full information, full access, and no social cost? If not, move it to opportunity. "Was never told" is opportunity; "was told and still cannot do it" is capability. One is fixed by training, the other by changing the environment.
4. **Write one question for each hypothesis, then a "discriminates because" line:** the answer this hypothesis predicts and the different answer a named rival predicts. A question that gets the same answer whichever is true tests nothing; change it. Ask what the person did last time, or observe, before asking why.
5. **Mark team beliefs.** Label a hypothesis that restates what the team already believes "team belief"; a belief is not evidence, however it is reworded.
6. **Rank every hypothesis in one table** on evidence so far, with its source, and cost of checking.
7. **Name the one or two to check first**, labeled provisional, and stop. Propose no interventions; the diagnosis is made in the field.

See `references/worked-example.md` for a complete run.

## Output template

```markdown
# COM-B barrier hypotheses

**Behavior:** <who does what, when; as given>
**Evidence used:** <what is known about the setting, and where it comes from; or "none yet">

## Capability
### Physical
- **Hypothesis:** <a specific barrier>
  **Persistence test:** <would it remain with full information, full access, and no social cost? yes, because ...>
  **Question:** <what to ask or observe>
  **Discriminates because:** <the answer this hypothesis predicts; the different answer a named rival predicts>
### Psychological
- **Hypothesis:** <...>
  **Persistence test:** <...>
  **Question:** <...>
  **Discriminates because:** <...>

## Opportunity
### Physical
- **Hypothesis:** <...>
  **Question:** <...>
  **Discriminates because:** <...>
### Social
- **Hypothesis:** <...>
  **Question:** <...>
  **Discriminates because:** <...>

## Motivation
### Reflective
- **Hypothesis:** <...>
  **Question:** <...>
  **Discriminates because:** <...>
### Automatic
- **Hypothesis:** <...>
  **Question:** <...>
  **Discriminates because:** <...>

## Ranking, pending field answers

| Hypothesis | Evidence so far | Cost of checking |
|---|---|---|
| <sub-component: hypothesis> | <high / medium / low / none: what supports it, and its source; "team belief" if that is all> | <low / medium / high: what it takes> |

**Check first:** <the one or two hypotheses the table puts first, and why>. Provisional until the questions above are answered in the field.

## What to check before relying on this
- <the hypothesis that rests on the weakest evidence, and the cheapest way to check it>
```

## Where it goes wrong

- **Motivation as the default.** "They are not motivated" needs no evidence, so it fills every gap. A motivation hypothesis names the belief, the feeling, or the habit.
- **The ranking read as a diagnosis.** The table orders guesses; sending its first row to intervention design skips the fieldwork.
- **A diagnosis imported from elsewhere.** What limits a behavior in one district is only a hypothesis in the next.

## When to bring in a specialist

Tell the user to consult a behavioral scientist or an experienced qualitative researcher when:
- The behavior carries clinical, safety, or legal risk (medication, violence, child protection, sexual health): some questions cannot be asked directly, and the set needs ethical review before fieldwork
- The hypotheses cluster under social opportunity in a setting the team does not know; a local researcher should shape the questions and say who asks them
- Field answers support two hypotheses equally; a study designed to separate them comes next

Bring them: the hypotheses, the ranking table, and any field answers so far.
