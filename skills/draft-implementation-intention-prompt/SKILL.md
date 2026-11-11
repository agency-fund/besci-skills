---
name: draft-implementation-intention-prompt
description: >-
  Use when people say they will do a dated, one-off action (get a vaccine,
  attend a visit, collect a document, redeem a voucher) and many do not
  follow through, or when a team wants to add "when and where will you do
  it?" to a contact that already happens. Writes an if-then prompt in which
  the person names the time and place they will act, limited to options that
  exist. Do not use when the program wants to send messages on a schedule;
  use design-reminder-schedule. Not for choosing when to make an offer; use
  choose-delivery-moment.
license: CC-BY-4.0
metadata:
  title: Ask people to plan when and where
  type: atomic
  stage: design
  version: "0.2.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  tested_in: beyond-western-differs
  tags: "implementation-intentions, behavior-change-techniques, planning-prompts"
  consumes: "barrier-diagnosis"
  produces: "intervention-draft"
---

## What it does

Writes a prompt that asks a person to name the moment they will carry out one action they already intend to take.

**What this adds:** stops if nothing shows that people already intend to act; writes the prompt as an if-then plan, called an implementation intention ("If it is Tuesday at 10 and I am leaving the market, then I go to the clinic"); requires a time and a place from options that exist; has the person say the plan back; names who else sees it; and requires a pretest.

## When to use it

### Use it when
- A confirmed barrier is an intention not acted on: people say they will do a one-off, dated action (get a vaccine, collect a document) and many do not
- A team wants to add "when and where will you do it?" to a message, visit, or form
- A date is fixed and many who said they would come do not

### Do not use it when
- The program is to send messages on dates it chooses, as for a daily action people forget; use `design-reminder-schedule`
- The question is when to make an offer; use `choose-delivery-moment`
- People want to bind themselves with a penalty or a lock; use `design-commitment-device`

## Before you start

Ask these before producing anything. Do not ask anything the user has already answered.

1. **Required.** The behavior (who, what, when) and the confirmed barrier, with the evidence that people intend to act and that cost, access, and trust do not stop them.
2. **Required.** Whether the action happens once or is repeated.
3. **Required.** The real options: dates, hours, and places where the action can be done.
4. **Required.** The contact the prompt rides on: which message, visit, or form, and who delivers it.
5. Optional. Whether the time and place are the person's to choose, and who else would see or hear the plan.

If any of 1 to 4 is missing, ask and stop. If 5 is missing, make it the first open question.

## What it draws on

- Sheeran, P., Listrom, O., & Gollwitzer, P. M. (2025). The when and how of planning: Meta-analysis of the scope and components of implementation intentions in 642 tests. *European Review of Social Psychology*, 36(1), 162–194. https://doi.org/10.1080/10463283.2024.2334563 Supports: the form of the prompt (if-then, a time and a place, said back once).
- Milkman, K. L., Beshears, J., Choi, J. J., Laibson, D., & Madrian, B. C. (2011). Using implementation intentions prompts to enhance influenza vaccination rates. *Proceedings of the National Academy of Sciences*, 108(26), 10415–10420. https://doi.org/10.1073/pnas.1103170108 Supports: asking for more than a date.
- Abel, M., Burger, R., Carranza, E., & Piraino, P. (2019). Bridging the intention-behavior gap? The effect of plan-making prompts on job search and employment. *American Economic Journal: Applied Economics*, 11(2), 284–301. https://doi.org/10.1257/app.20170566 Supports: use outside wealthy Western countries.

**Where the evidence comes from:** Most of the 642 tests were run in the United Kingdom, Germany, and the United States. Elsewhere field results differ: a job-search plan raised employment among unemployed youth in South Africa, while plan prompts made little or no difference to HIV testing in Uganda or to reporting HIV self-test results in South Africa. Check locally whether the time and place are the person's to choose.

**Replication status:** Replicated in direction, with smaller effects in the field than the lab and substantial publication bias; the meta-analysis found no reliable effect on vaccination or voting, and a field trial for gym visits found none.

## How to do it

1. **Check that the intention exists.** If people do not want the thing, cannot reach it, or cannot afford it, say a plan prompt is the wrong tool and stop: it creates no intention.
2. **Check the action is one dated occasion.** For a repeated behavior, write the prompt for the next occasion only and say the field evidence there is weak.
3. **List the real options:** dates, hours, places. The blanks accept only these.
4. **Write the prompt as an if-then plan** with a time and a place: "If it is [day] at [time] and I am [where I will be just before], then I will [action] at [place]."
5. **Add nothing by default.** Add a way to get there, or one obstacle and its answer, only where evidence shows that stops people; extra detail lowered the effect.
6. **Attach it to the existing contact:** who asks, and how close to the action date.
7. **Have the person say the plan back once.** Rehearsal raised effects in the meta-analysis and writing the plan down lowered them; a card is optional and theirs to keep.
8. **Say who else sees or hears the plan,** and whether that could expose the person.
9. **Specify the pretest:** five to ten people answer the prompt cold; it passes if every answer names a day, a time, and a real place.
10. **State what the evidence supports:** the direction. Do not promise an effect size.

See `references/worked-example.md` for a complete run.

## Output template

```markdown
# Implementation intention prompt

**Behavior:** <who, what, when>
**Confirmed barrier:** <the evidence that people intend to act and do not; how cost, access, and trust were ruled out>
**Action:** <one dated occasion / the next occasion of a repeated behavior>
**Real options:** <dates, hours, places>

## The prompt
<the literal words, with blanks: "If it is <day> at <time> and I am <where>, then I will <action> at <place>.">

## Why each part is there
- **If (time and cue):** <...>
- **Then (action and place):** <...>
- **Anything added:** <a way to get there or one obstacle, and the evidence for adding it; or "nothing">

## Delivery
- **Rides on:** <the existing message, visit, or form>
- **Asked by:** <who>
- **When:** <how long before the action, and why>
- **Said back:** <how the person repeats the plan once>
- **What the person keeps:** <nothing; or a card or message that stays with them>

## Who else sees or hears the plan
<who; whether that could expose the person; "specialist review needed" where it could>

## Pretest
<how many people, how, and what counts as a pass>

## What the evidence supports
<the direction, and the nearest field evidence with where it was run; no effect size promised>

## What to check before relying on this
- <the assumption most likely to be wrong>
```

## Where it goes wrong

- **A polite yes read as an intention.** People tell a health worker they will come. A prompt built on that yields filled blanks and no change.
- **The program's plan in the person's mouth.** A worker who fills in the blanks for people, or assigns a slot, has delivered an appointment; one who collects the cards has turned a private aid into monitoring.
- **Crediting the prompt for what an explanation did.** In South Africa a plan-and-commit prompt did no better than a clear explanation of how to report a result.

## When to bring in a specialist

Tell the user to consult a specialist before use when:
- Others learning of the planned action could put the person at risk (an HIV test, telling a partner): a clinician or safeguarding lead reviews who sees the plan and what support follows
- Someone else sets the person's time and place (a husband's permission, an employer's shifts): a local qualitative researcher checks whether asking for a plan is realistic or shaming

Bring them: the prompt, the evidence of intention, the real options, and who sees the plan.
