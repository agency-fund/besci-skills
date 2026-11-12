---
name: design-incentive-scheme
description: >-
  Use when a team has decided to reward people for one behavior and needs the
  terms: "how much should we pay", "cash or food", "conditional or not", "what
  happens when the money stops". Specifies the verification, the size against
  the cost of acting, the condition, the end date, and what to monitor. Do not
  use when the stake is the person's own money, put up by choice; use
  design-commitment-device. Not for removing the steps that make the behavior
  costly; use audit-process-friction.
license: CC-BY-4.0
metadata:
  title: Design a reward for one verifiable behavior
  type: atomic
  stage: design
  version: "0.3.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  tested_in: beyond-western-holds
  tags: "incentives, conditional-cash-transfers"
  consumes: "barrier-diagnosis"
  produces: "intervention-draft"
---

## What it does

Specifies the terms of a reward or penalty that a program attaches to one verifiable behavior.

**What this adds:** stops if supply is unreliable or only the recipient can vouch for the behavior; sizes the reward against the cost of acting, shown as a share of a day's income; names who the condition excludes; requires an end date with a measurement after it; and checks for a motive that payment could displace.

## When to use it

### Use it when
- A confirmed barrier is a cost of acting now (a fare, lost wages, a queue) for a later benefit, and the team asks "how much should we pay?" or "conditional or not?"
- A reward amount is about to be set by what the budget allows
- An incentive is running and the team wants to end it, or sees its effect fading

### Do not use it when
- The stake is the person's own money, put up by choice; use `design-commitment-device`
- The cost of acting comes from steps that could be removed (forms, trips, queues); use `audit-process-friction`

## Before you start

Ask these before producing the scheme. Do not ask anything the user has already answered.

1. **Required.** The behavior (who, what, when) and the confirmed barrier, with the evidence that a cost of acting stops people and that the service is there when they come.
2. **Required.** How someone other than the recipient would verify the behavior.
3. Optional. Who pays, and until when.
4. Optional. A typical day's income for the audience and the cost of acting (fare, lost wages, fees).
5. Optional. Whether recipients are staff, public servants, or volunteers, and whether some people already act unpaid.

If 1 or 2 is missing, ask and stop. If 3 is missing, make the end date the first open question. If 4 is missing, give the size as a multiple of the cost of acting. If 5 is missing, assume community members and say so.

## What it draws on

- Banerjee, A. V., Duflo, E., Glennerster, R., & Kothari, D. (2010). Improving immunisation coverage in rural India: clustered randomised controlled evaluation of immunisation campaigns with and without incentives. *BMJ*, 340, c2220. https://doi.org/10.1136/bmj.c2220 Supports: steps 1 and 4. Full immunization reached 39% with reliable camps plus small gifts, 18% with camps alone, and 6% with neither.
- Baird, S., Ferreira, F. H. G., Özler, B., & Woolcock, M. (2014). Conditional, unconditional and everything in between: a systematic review of the effects of cash transfer programmes on schooling outcomes. *Journal of Development Effectiveness*, 6(1), 1–43. https://doi.org/10.1080/19439342.2014.890362 Supports: step 5. Across 35 studies, enrollment rose most where the condition was explicit, monitored, and enforced; effects on test scores were small at best.
- Saunders, M. J., Pereboom, M., Alvarez, J. L., Sherlock, M., & Gadroen, K. (2025). Incentives in immunisation campaigns in low- and middle-income countries: a scoping review mapping evidence on effectiveness and unintended consequences. *BMJ Global Health*, 10(6), e019662. https://doi.org/10.1136/bmjgh-2025-019662 Supports: steps 6 to 8. In 40 studies from 19 countries, most incentives raised uptake modestly; several found lower uptake once they were withdrawn.

**Where the evidence comes from:** Reviews of cash transfers and health incentives cover Africa, Asia, and Latin America as well as wealthy Western countries, and mostly find that a reward raises the rewarded action while it is paid; one found no effect on immunization coverage. Check locally what amount reads as fair, whether cash or goods are acceptable, and whether paying staff is legal.

**Replication status:** Replicated for raising the rewarded action while it is paid. Mixed afterward: effects on health habits fade within months of the last payment, and some immunization studies report lower uptake once payment stops.

## How to do it

1. **Check that the barrier is a cost of acting and that supply works.** If the clinic has no stock or the school no teacher, say an incentive is the wrong tool and stop.
2. **Fix the behavior and its verification:** one action, checked by someone other than the recipient. If only the recipient can report it, the payment buys the report: propose a nearby action that can be checked.
3. **Size the reward** against the cost of acting. Show it as a multiple of that cost and as a share of a day's income; a reward above a day's income is hard to refuse.
4. **Choose form and timing:** cash, goods, or airtime; certain; handed over at verification.
5. **Decide the condition:** enforced, or announced and not enforced. Name who it excludes and what happens to them.
6. **Plan the end:** the date, how people are told, and a measurement some months after.
7. **Check for a motive that payment could displace:** people who already act unpaid, volunteers, staff beside unrewarded colleagues. Where one exists, say what is watched, or choose a reward that is not cash.
8. **Set the monitoring:** claims without the behavior, complaints from people not rewarded, and the level at which the scheme is reviewed.
9. **State what the evidence supports:** the direction. Promise no effect size.

See `references/worked-example.md` for a complete run.

## Output template

```markdown
<Two or three plain sentences to the user: what is paid for which checked action, how the amount compares with the cost of acting and a day's income, what happens when the payment ends, and that no effect is promised.>

# An incentive for <the behavior, in a few words>

**Behavior:** <who, what, when>
**Confirmed barrier:** <the cost of acting, with the evidence; and the evidence that supply works>
**Verification:** <who checks, how, cost per check; what is not rewarded because it cannot be checked>

## The reward
- **Size:** <amount; as a multiple of the cost of acting; as a share of a day's income>
- **Form:** <cash / goods / airtime; certain>
- **Timing:** <when it is handed over, relative to verification>
- **Recipient:** <who receives it>

## The condition
- **Rule:** <the exact condition; enforced, or announced only>
- **Who it excludes:** <and what happens to them>

## The end
- **End date:** <date, and who funds until then>
- **How people are told:** <...>
- **Measured after the end:** <what, and how many months after>

## Motives that payment could displace
- **Who already acts unpaid, or works beside unrewarded colleagues:** <...; or "none identified">
- **What is done about it:** <...>

## Monitoring
- **Claims without the behavior:** <how they are caught>
- **Review if:** <the level, and who reviews>

## Ethics check
- **Can a person refuse it:** <the reward as a share of a day's income>
- **Who is left out:** <...>
- **Specialist review:** <not needed / <who>, because <reason>>

## What the evidence supports
<the direction, and the nearest field evidence with where it was run; no effect size promised>

## What to check before relying on this
- <the assumption most likely to be wrong>

## Where you could go from here
<One line saying the scheme is done, or, if supply is unreliable or the behavior cannot be checked, why no scheme was set.>
<Two or three next moves that fit what this run found, each with why it would help and when it fits. Candidates:
- `audit-intervention-ethics`, when the reward is large next to a day's income, the behavior is clinical, or recipients work beside colleagues who are not rewarded
- `plan-prototype-test`, when nobody has asked people whether the amount reads as fair or whether cash or goods are acceptable
- `audit-process-friction`, when part of the cost of acting comes from steps the program could remove instead of paying for
- `design-pilot-feasibility-study`, once the terms are set, to find out whether checking and paying can run as planned before any trial
- an ethics committee, a clinician, or a human-resources and legal review, when the reward exceeds a day's income, the behavior is clinical, or recipients are staff or volunteers: before any pilot
- the people who run the service, when it is not confirmed that supply is reliable at every site>
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

- **The reward moves the measure.** Teachers in Kenya paid on test scores raised scores on the rewarded exams and on no other.
- **A fine read as a price.** Day-care centers that fined late parents got more lateness, which stayed after the fine ended.
- **Money added to something that works.** In India, reports comparing a household's electricity use with its peers cut use; adding a cash reward erased the cut.

## When to bring in a specialist

Tell the user to consult the relevant specialist before any pilot when:
- The reward exceeds a day's income for poor households: an ethics committee judges whether people can freely refuse
- The behavior is clinical (testing, medication, immunization): a clinician checks the verification and the harms a payment can induce, such as repeat testing
- Recipients are public servants, health workers, teachers, or volunteers: a human-resources and legal review covers what the law allows and what unrewarded colleagues are told

Bring them: the specification, the sizing arithmetic, and the plan for the end.
