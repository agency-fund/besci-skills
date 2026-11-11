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
  version: "0.3.0"
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

**What this adds:** writes at least one hypothesis under each of COM-B's six sub-components; moves any capability barrier that would vanish with information or access to opportunity; pairs every question with the answers that tell rival reasons apart; ranks on evidence so far and cost of checking; and keeps the ranking provisional until field answers exist.

COM-B is Michie and colleagues' model: a behavior needs capability, opportunity, and motivation.

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

Ask these before producing the list. Do not ask anything the user has already answered.

1. **Required.** The behavior as who does what, when. If it contains "and" or lacks an actor or a time window, ask for one behavior.
2. **Required.** What is known about the setting: where the behavior happens, and anything the team has observed or heard from the audience.
3. Optional. What the team already believes is the cause.
4. Optional. How the team can check: interviews, observation, records, or nothing yet.

If 1 is missing, ask and stop. If 2 is missing, ask once; if the answer is still thin, proceed and write "none" as the evidence. If 4 is missing, assume one short round of interviews.

## What it draws on

- Michie, S., van Stralen, M. M., & West, R. (2011). The behaviour change wheel: A new method for characterising and designing behaviour change interventions. *Implementation Science*, 6, 42. https://doi.org/10.1186/1748-5908-6-42 Supports: the three components, their six sub-components, and the definition of opportunity.
- Schmidtke, K. A., & Drinkwater, K. G. (2021). A cross-sectional survey assessing the influence of theoretically informed behavioural factors on hand hygiene across seven countries during the COVID-19 pandemic. *BMC Public Health*, 21, 1432. https://doi.org/10.1186/s12889-021-11491-4 Supports: ranking from local evidence only.

**Where the evidence comes from:** COM-B was first applied to English tobacco and obesity policy. A review of 79 nutrition studies in sub-Saharan Africa sorted interventions with it, and the seven-country survey found that the components predicting children's handwashing differed by country (capability alone in Australia, Indonesia, and South Africa; capability and opportunity in India).

**Replication status:** COM-B is a way of sorting, so there is no effect to replicate. Two coders in the original paper agreed on 79% to 88% of classifications; no study tests whether a COM-B diagnosis leads to a better intervention.

## How to do it

1. **Restate the behavior** as given.
2. **Write at least one hypothesis under each of the six sub-components** in the template, specific enough that an answer could rule it out. List two where two distinct ones compete.
3. **Run the persistence test on every capability hypothesis** and write the answer: would the barrier remain if the setting gave full information, full access, and no social cost? If not, move it to opportunity. "Was never told" is opportunity; "was told and still cannot do it" is capability. One is fixed by training, the other by changing the environment.
4. **Write one question for each hypothesis, then say how the answer tells it apart:** the answer this hypothesis predicts and the different answer a named rival predicts. A question that gets the same answer either way tests nothing; change it. Ask what the person did last time, or observe, before asking why.
5. **Mark team beliefs.** Label a hypothesis that restates the team's own view "team belief"; a belief is not evidence, however it is reworded.
6. **Rank every hypothesis in one table** on evidence so far, with its source, and cost of checking.
7. **Say where you would start:** the one or two the table puts first, and why, labeled provisional. Propose no interventions; the diagnosis is made in the field.

See `references/worked-example.md` for a complete run.

## Output template

```markdown
<Two or three plain sentences to the user: how many possible reasons you found, which one the evidence so far points to, and that none is confirmed until people in the field are asked.>

# Possible reasons <the behavior, in a few words> isn't happening

**The behavior:** <who does what, when; as given>
**What we know so far:** <what is known about the setting, and where it comes from; or "nothing yet">

## Capability: can they do it?
### Physical capability: the bodily skill
- **Possible reason:** <a specific barrier>
  **Still a barrier with full information, full access, and no social cost?** <yes, because ...>
  **What to ask or watch:** <the question or observation>
  **How the answer tells it apart:** <what we would hear if this is the reason; what we would hear instead if <a named rival> is>
### Psychological capability: knowledge, understanding, memory, planning
- **Possible reason:** <...>
  **Still a barrier with full information, full access, and no social cost?** <...>
  **What to ask or watch:** <...>
  **How the answer tells it apart:** <...>

## Opportunity: does their situation let them?
### Physical opportunity: time, money, distance, materials
- **Possible reason:** <...>
  **What to ask or watch:** <...>
  **How the answer tells it apart:** <...>
### Social opportunity: what the people around them do, expect, and allow
- **Possible reason:** <...>
  **What to ask or watch:** <...>
  **How the answer tells it apart:** <...>

## Motivation: do they want to, at the moment it counts?
### Reflective motivation: their judgments and plans
- **Possible reason:** <...>
  **What to ask or watch:** <...>
  **How the answer tells it apart:** <...>
### Automatic motivation: habits, emotions, and impulses
- **Possible reason:** <...>
  **What to ask or watch:** <...>
  **How the answer tells it apart:** <...>

## Which to check first (a provisional order)

| Possible reason | Evidence so far | Cost of checking |
|---|---|---|
| <part of COM-B: the reason> | <high / medium / low / none: what supports it, and where that comes from; "team belief" if that is all> | <low / medium / high: what it takes> |

**Where I'd start:** <the one or two reasons the table puts first, and why>. This order is a best guess until the questions above are answered in the field.

## What to check before relying on this
- <the reason that rests on the weakest evidence, and the cheapest way to check it>

## Where you could go from here
<One line saying the list of possible reasons is done.>
<Two or three next moves that fit what this run found, each with why it would help and when it fits. Candidates:
- `draft-tdf-interview-guide`, when the team can interview people and wants a guide built on these questions
- `audit-researcher-bias`, when the list leads with team beliefs, or the team is sure of the answer before asking anyone
- `audit-process-friction`, when the leading reasons are steps, forms, trips, or waiting
- `diagnose-social-norm`, when the leading reason is what other people do or expect
- `select-intervention-levers`, once field answers have confirmed a reason, and not before
- records the team already holds (usage logs, attendance, ratings), when they could rule a reason out before anyone goes to the field>
Questions you could ask next: "<question>" · "<question>"
```

<!-- shared: template/shared/voice.md. Edit it there, then run scripts/check_sync.py --fix. -->
**How to talk with the user**

- If the user asked a question rather than asked for this skill's output, answer the question first, in a few plain sentences. Then offer the run and say what it would add.
- Mark the run. When it starts, say so in one line: the skill, and what it will produce. When the output is done, say the run is finished. The user should always know when the library's method is in force.
- Talk with the person, not at them. Use their words for their program and the people in it, say why you ask each question, and say what you are unsure of. No praise, no filler.
- Say where each claim comes from: this skill's sources, your general knowledge, or nothing in the library. A number the sources do not give, such as how many interviews to run, is your judgment; say so, and why you chose it.
- End with the template's closing: two or three next moves that fit what this run found, each with its reason and when it fits, and one or two questions the user could ask next. Say which move you would lean toward and why; the user decides.
<!-- /shared -->

## Where it goes wrong

- **Motivation as the default.** "They are not motivated" needs no evidence, so it fills every gap. A motivation hypothesis names the belief, the feeling, or the habit.
- **The ranking read as a diagnosis.** The table orders guesses; designing for its first row skips the fieldwork.
- **A diagnosis imported from elsewhere.** What limits a behavior in one district is only a hypothesis in the next.

## When to bring in a specialist

Tell the user to consult a behavioral scientist or an experienced qualitative researcher when:
- The behavior carries clinical, safety, or legal risk (medication, violence, child protection, sexual health): some questions cannot be asked directly and need ethical review before fieldwork
- The hypotheses cluster under social opportunity in a setting the team does not know; a local researcher should shape the questions and say who asks them
- Field answers support two hypotheses equally; a study designed to separate them comes next

Bring them: the hypotheses, the ranking table, and any field answers so far.
