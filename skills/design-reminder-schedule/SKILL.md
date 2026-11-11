---
name: design-reminder-schedule
description: >-
  Use when people mean to do something with a due date (a vaccine dose, a
  clinic visit, a loan installment, a deposit) and miss it because it slips
  their mind, or when a team is about to "text everyone" without deciding how
  many messages, when, by what channel, and when they stop. Specifies each
  send, the ceiling, the stop rule, and what to monitor. Do not use when
  choosing the moment for one ask or offer; use choose-delivery-moment. Not
  for a plan the person makes; use draft-implementation-intention-prompt.
license: CC-BY-4.0
metadata:
  title: Plan when and how often to remind
  type: atomic
  stage: design
  version: "0.2.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  tested_in: beyond-western-holds
  tags: "reminders, behavior-change-techniques, sms"
  consumes: "barrier-diagnosis"
  produces: "intervention-draft"
---

## What it does

Specifies the reminders a program sends about one action people already intend to take.

**What this adds:** stops if the confirmed barrier is not forgetting; ties every send to a date the program knows; picks the channel from who holds the phone and who can read; gives every send a ceiling and a stop rule; requires a line on what a message could reveal to others; and sets the levels that trigger a review.

## When to use it

### Use it when
- A confirmed barrier is forgetting: people intend to do something with a due date (a vaccine dose, a loan installment) and say it slipped their mind
- A team is about to "text everyone" and has not decided how many messages, when, or by which channel
- Reminders already go out and nobody knows whether their number and timing are right

### Do not use it when
- The question is when to make one ask or offer; use `choose-delivery-moment`
- The person is to state their own plan for acting; use `draft-implementation-intention-prompt`
- The barrier is cost, supply, or distrust; use `select-intervention-levers`
- The team needs the wording of the message; use `draft-lever-content`

## Before you start

Ask these before producing anything. Do not ask anything the user has already answered.

1. **Required.** The behavior (who, what, when) and the confirmed barrier, with the evidence that people intend to act and forget.
2. **Required.** The due dates: one date, a window, or a recurring cycle, and how the program knows each person's date.
3. **Required.** Phone access: who holds the phone, whether it is shared, whether the person reads, and in which language.
4. Optional. Whether the action concerns a health condition, a debt, or anything else people keep private.

If 1, 2, or 3 is missing, ask and stop. If 4 is unclear, treat the action as private.

## What it draws on

- Eze, P., Lawani, L. O., & Acharya, Y. (2021). Short message service (SMS) reminders for childhood immunisation in low-income and middle-income countries: a systematic review and meta-analysis. *BMJ Global Health*, 6(7), e005035. https://doi.org/10.1136/bmjgh-2021-005035 Supports: the direction, and the number of sends before a dated action.
- Horvath, T., Azman, H., Kennedy, G. E., & Rutherford, G. W. (2012). Mobile phone text messaging for promoting adherence to antiretroviral therapy in patients with HIV infection. *Cochrane Database of Systematic Reviews*, 2012, CD009756. https://doi.org/10.1002/14651858.CD009756 Supports: the weekly ceiling for a recurring action.
- Banerjee, A., Chandrasekhar, A. G., Dalpath, S., Duflo, E., Floretta, J., Jackson, M. O., Kannan, H., Loza, F., Sankar, A., Schrimpf, A., & Shrestha, M. (2025). Selecting the most effective nudge: Evidence from a large-scale experiment on immunization. *Econometrica*, 93(4), 1183–1223. https://doi.org/10.3982/ECTA19739 Supports: asking whether reminders are enough alone.

**Where the evidence comes from:** A review of 18 studies in 11 low- and middle-income countries found that text reminders raised childhood immunization coverage; in two Kenyan trials weekly texts improved adherence to HIV treatment and daily texts did not. Trials in Cameroon, Uganda, and India found no effect, and in Haryana, India, reminders were cost-effective only alongside local ambassadors. Check locally who holds the phone and whether forgetting is the barrier.

**Replication status:** Replicated in direction across several reviews, with large differences between studies and several null trials.

## How to do it

1. **Check that the barrier is forgetting.** If the evidence points to stock-outs, fees, distance, or distrust, say a reminder is the wrong tool and stop.
2. **Map the dates:** the first and last day the action counts, and how the program learns each person's date. If it cannot, stop: a reminder on the wrong day costs trust.
3. **Choose the channel** from who holds the phone: a text where the person holds it and reads, a voice call where they do not read, a visit by someone already making rounds where no phone reaches.
4. **Place each send before the action can be done,** leaving time to arrange transport or time off.
5. **Set the ceiling:** two or three sends per due date and one at most after a missed date; for a recurring action, no more than one a week.
6. **Give every send a stop rule:** the action is recorded, the person opts out in one free step, or the ceiling is reached.
7. **List what each message must name:** the action, the date, the place, and the person's own goal where one is on record.
8. **Write the privacy line:** what the message reveals to anyone else who reads or hears it. On a shared phone it names no health condition and no debt.
9. **Say whether reminders are enough alone.** If people also need information from someone they trust, or help with a cost, say what must sit beside the schedule.
10. **Set the monitoring:** delivery rate, opt-out rate, and the share of reminded people who act, with the levels that trigger a review.
11. **State what the evidence supports:** the direction. Do not promise an effect size.

See `references/worked-example.md` for a complete run.

## Output template

```markdown
# Reminder schedule

**Behavior:** <who, what, when>
**Confirmed barrier:** <the evidence that people intend to act and forget; how cost, supply, and trust were ruled out>
**Due dates:** <one date / a window / recurring; first and last day the action counts; how the program knows each person's date>

## Sends
| # | When, relative to the due date | Channel | Must name | Stops when |
|---|---|---|---|---|
| 1 | <e.g. 3 days before> | <text / voice call / visit> | <action, date, place, the person's goal> | <action recorded / opt-out / ceiling> |

## Limits
- **Ceiling:** <most sends per due date or per week, and why>
- **After a missed date:** <one send naming the next date; or none>
- **Opt-out:** <the one step, at no cost>

## Channel
- **Why this channel:** <who holds the phone, who reads, which language>
- **Who it does not reach:** <who, and what they get instead>

## Privacy
- **What a message reveals to someone else:** <...>
- **How that is handled:** <what the message leaves out; or "privacy review needed before any send">

## Are reminders enough alone?
<yes, because ...; or no: what else people need, such as a trusted person or help with the cost>

## Monitoring
- **Measures:** <delivery rate, opt-out rate, share of reminded people who act; how often checked>
- **Review if:** <the opt-out rate or the fall in response that triggers a review, and who reviews>

## What the evidence supports
<the direction, and the nearest evidence with where it was run; no effect size promised>

## What to check before relying on this
- <the assumption most likely to be wrong>
```

## Where it goes wrong

- **Counting sent as received.** Numbers change, phones are off, and a husband's phone is not the mother's. A schedule judged by messages sent can reach a minority.
- **Answering a fading effect with more messages.** A fall in response may mean forgetting was never the main barrier; more sends teach people to ignore the sender.
- **A dosing instruction by text.** "Take your two tablets now" is clinical advice sent without knowing the person's regimen. Name the visit, not the dose.

## When to bring in a specialist

Tell the user to consult a specialist before the first send when:
- The message concerns medication: a clinician or pharmacist approves what it names
- The message could reveal a health condition or a debt on a phone others use: a privacy or safeguarding lead reviews the wording and the channel
- People have not agreed to be contacted: a data-protection lead confirms the consent required

Bring them: the sends table, the privacy line, and the phone-access facts.
