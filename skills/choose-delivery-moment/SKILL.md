---
name: choose-delivery-moment
description: >-
  Use when an ask or offer is already chosen and the question is when to make
  it: "before or after harvest", "payday or mid-month", "is the new year a
  good time to launch". Also use when a team is about to schedule an offer by
  its own calendar. Picks one moment from when people have the money, the
  attention, and the chance to act, and names who that moment leaves out. Do
  not use when deciding how many reminders to send and how often; use
  design-reminder-schedule. Not for a plan the person makes; use
  draft-implementation-intention-prompt.
license: CC-BY-4.0
metadata:
  title: Pick the moment to deliver an ask
  type: atomic
  stage: design
  version: "0.2.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  tested_in: beyond-western-holds
  tags: "choice-architecture, behavior-change-techniques, timing"
  consumes: "barrier-diagnosis"
  produces: "intervention-draft"
---

## What it does

Picks the moment at which one ask or offer reaches people.

**What this adds:** stops if no moment could make the action possible; builds the money calendar from what the user reports, never from general knowledge of a country; tests every candidate moment on three questions (money in hand, attention free, action possible then); treats a landmark such as a new year as untested; allows a deadline only where delay is a confirmed barrier; and names who the moment leaves out.

## When to use it

### Use it when
- A confirmed barrier is a bad moment: people want what is offered and are asked when they have no cash, time, or way to act
- Someone asks "before or after harvest?", "payday or mid-month?", or "is the new year a good time to launch?"
- A team is about to schedule an ask by its own calendar (the quarter start, a staff visit)

### Do not use it when
- The question is how many reminders to send and how often; use `design-reminder-schedule`
- The person is to state when and where they will act; use `draft-implementation-intention-prompt`
- People are to lock money or a choice until a later date; use `design-commitment-device`

## Before you start

Ask these before producing anything. Do not ask anything the user has already answered.

1. **Required.** The ask (who does what) and what it costs the person at that moment: cash, time, thought.
2. **Required.** The confirmed barrier, with the evidence that people want the thing and that the moment stops them.
3. **Required.** When money comes in and goes out for these people: harvests, paydays, transfers; fees, festivals, lean months, debts.
4. **Required.** When the action can be done: a season, an enrollment period, opening hours, or any time.
5. Optional. Dates or life changes that people there treat as a new beginning.
6. Optional. Whether delay (putting the action off) is a confirmed barrier.

If any of 1 to 4 is missing, ask and stop. If 5 is missing, consider no landmark. If 6 is missing, attach no deadline.

## What it draws on

- Duflo, E., Kremer, M., & Robinson, J. (2011). Nudging farmers to use fertilizer: Theory and experimental evidence from Kenya. *American Economic Review*, 101(6), 2350–2390. https://doi.org/10.1257/aer.101.6.2350 Supports: making the offer while money is in hand, and the deadline rule.
- Casaburi, L., & Willis, J. (2018). Time versus state in insurance: Experimental evidence from contract farming in Kenya. *American Economic Review*, 108(12), 3778–3813. https://doi.org/10.1257/aer.20171526 Supports: moving a payment to the moment money arrives.
- Mani, A., Mullainathan, S., Shafir, E., & Zhao, J. (2013). Poverty impedes cognitive function. *Science*, 341(6149), 976–980. https://doi.org/10.1126/science.1238041 Supports: the attention question.
- The Behavioural Insights Team (2024). *EAST: Four simple ways to apply behavioural insights* (revised and updated edition). https://bi.team/wp-content/uploads/2014/04/BIT-EAST.pdf Supports: landmarks and life changes as candidate moments.

**Where the evidence comes from:** Field trials in Kenya and Colombia found that an offer or payment timed to when people hold cash, or to when a bill falls due, did more than the same thing at another time. Evidence on calendar landmarks comes from the United States; the one trial found elsewhere, in South Africa, was inconclusive. Build the calendar from local reports; treat any landmark as a guess.

**Replication status:** Mixed. The money finding recurs across three field trials; the attention finding held in India and not in the United States; landmark framing has one positive field experiment.

## How to do it

1. **Check that a moment can fix it.** If the thing is out of stock, unaffordable all year, or unwanted, say timing is the wrong tool and stop.
2. **Build the money calendar** from what the user reported: each period, money in, money out, and whether people are flush or short. Mark a row "assumed" where the user gave nothing; harvest and pay dates vary by crop and employer.
3. **List the candidate moments:** the program's current one, each point when money arrives, and any landmark the user named.
4. **Test each candidate on three questions.** Is money in hand, if the ask costs money? Is attention free: not the lean season, peak work, or the week a large bill falls due? Can the action be completed then?
5. **Choose the moment that passes all three,** and name what it relies on: money in hand, free attention, or a new beginning. If none passes, ask whether the payment can move to when money arrives.
6. **Decide on a deadline.** Attach a short one only where delay is a confirmed barrier, since a deadline shuts out people who need longer.
7. **Name who the moment leaves out** (no harvest, paid on other days, away for work) and give them a second moment.
8. **State what the evidence supports:** the direction, with any landmark marked "untested here". Do not promise an effect size.

See `references/worked-example.md` for a complete run.

## Output template

```markdown
# Delivery moment specification

**The ask:** <who is asked to do what; what it costs the person at that moment: cash, time, thought>
**Confirmed barrier:** <the evidence that people want it and that the moment stops them>
**When the action can be done:** <season, enrollment period, opening hours; or "any time">

## Money calendar
| Period | Money in | Money out | Position | Source |
|---|---|---|---|---|
| <week, month, or season> | <harvest sale, payday, transfer> | <fees, festival, lean-season food, debt> | <flush / short / neutral> | <user report / assumed> |

## Candidate moments
| Moment | Money in hand? | Attention free? | Action possible then? | Verdict |
|---|---|---|---|---|
| <the program's current moment> | <yes / no / not needed> | <yes / no> | <yes / no> | <chosen / rejected: why> |

## Chosen moment
- **When:** <stated relative to an event, e.g. "within two weeks of the main harvest sale">
- **Relies on:** <money in hand / free attention / a new beginning>
- **Why this setting supports it:** <the local fact>

## Deadline
<none, because ...; or how long the offer stays open, what happens after, and the evidence that people put the action off>

## Who this moment leaves out
- **Who:** <people with no money, time, or access at that moment>
- **Second moment for them:** <when>

## What the evidence supports
<the direction, and the nearest field evidence with where it was run; no effect size promised; "untested here" for any landmark>

## What to check before relying on this
- <the calendar row most likely to be wrong>
```

## Where it goes wrong

- **A landmark on an expensive day.** The new year, a festival, and the start of a school term are often the year's largest spending days. A "fresh start" message then asks for money when people have least.
- **The seller's best moment.** The day people hold the most cash is also the day a paid product is easiest to sell and hardest to judge. Timing for take-up alone can leave people over-committed.
- **Copying the study's moment, not its logic.** "Right after harvest" worked for farmers in western Kenya because they held cash then. For wage workers or herders the matching moment is elsewhere.

## When to bring in a specialist

Tell the user to consult a specialist before any pilot when:
- The ask is a loan, insurance, or another paid financial product timed to when people hold the most cash: a consumer-protection specialist checks affordability and disclosure
- The dates are set by clinical need (vaccine due dates, antenatal visits): a clinician sets them
- The moment is a religious period, a birth, or a bereavement: a local faith or community leader confirms the ask is welcome

Bring them: the money calendar, the candidate table, and who is left out.
