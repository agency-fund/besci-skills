---
name: design-commitment-device
description: >-
  Use when people intend a behavior, have the means, and give way at the moment
  of action ("I meant to save it but it was gone by evening"), and a team wants
  to offer a restriction people choose for themselves: a locked account, a
  deposit lost on failure, a public promise. Specifies the device, the cap on
  what anyone can lose, the offer, and the plan for people who commit and fail.
  Do not use when people get the option without choosing it; use
  select-default-option. Not for a reward or penalty the program sets; use
  design-incentive-scheme.
license: CC-BY-4.0
metadata:
  title: Help people tie their own hands against temptation
  type: atomic
  stage: design
  version: "0.2.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  tested_in: beyond-western-differs
  tags: "commitment-devices, present-bias, savings"
  consumes: "barrier-diagnosis"
  produces: "intervention-draft"
---

## What it does

Specifies a restriction on future choices that a person opts into to keep a plan they have made.

**What this adds:** stops if the barrier is not giving way at the moment of action; picks a soft or hard device by whether the goal can be checked and a loss afforded; caps what anyone can lose; requires a plan for people who commit and fail; and sets a failure rate that triggers review.

A commitment device is an arrangement a person chooses that makes a later change of mind costly: locked money, a deposit lost on failure, a public promise.

## When to use it

### Use it when
- A confirmed barrier is giving way at the moment of action: people intend the behavior, have the means, and say "I meant to save it but it was gone by evening"
- A team proposes a lock box, a locked savings account, a quit contract, or "a deposit they lose if they don't"
- People already hand cash to a treasurer to hold, and the team wants a formal version

### Do not use it when
- People would get the option without choosing it, as in automatic enrollment; use `select-default-option`
- The program sets or pays the stake (a reward, a fine); use `design-incentive-scheme`
- The plan is "when X happens, I will do Y" with nothing restricted; use `draft-implementation-intention-prompt`

## Before you start

Ask these before producing anything. Do not ask anything the user has already answered.

1. **Required.** The behavior (who, what, when) and the confirmed barrier, with the evidence that people intend it, have the means, and give way at the moment of action.
2. **Required.** Whether someone other than the person can check that the goal was met, and who would hold any money.
3. **Required.** The audience's income pattern: lean months, debts, what loss would cause hardship.
4. Optional. What people already do to bind themselves.

If 1 is missing, ask and stop. If the user cannot answer 2, specify a soft device. If the user cannot answer 3, specify no forfeit and make the income pattern the first open question.

## What it draws on

- Bryan, G., Karlan, D., & Nelson, S. (2010). Commitment devices. *Annual Review of Economics*, 2(1), 671–698. https://doi.org/10.1146/annurev.economics.102308.124324 Supports: the definition, and the choice between soft and hard in step 2.
- Abdul Latif Jameel Poverty Action Lab (2021). *Commitments to Save*. J-PAL Policy Bulletin. https://www.povertyactionlab.org/publication/commitments-save Supports: steps 4 and 5. A review of twelve randomized trials of 21 savings commitment products in seven countries in Africa and Asia.
- John, A. (2020). When commitment fails: Evidence from a field experiment. *Management Science*, 66(2), 503–529. https://doi.org/10.1287/mnsc.2018.3236 Supports: steps 4 and 6. Savers chose their own penalty for missed deposits; 55% defaulted and lost money.

**Where the evidence comes from:** Most field trials were run in low- and middle-income countries. Fourteen of the 21 savings products in the review raised balances at the bank offering them; contracts for doctor visits in India changed nothing, and many who paid for one lost the money. Check locally whether the holder of the money is trusted to return it and whether a lock would fall in a lean season.

**Replication status:** Mixed. Higher savings balances recur across trials, yet many who open a commitment account never use it, and where savers set their own penalty more than half paid it.

## How to do it

1. **Check that the barrier is giving way at the moment of action.** If people lack the money, the access, or the skill, say a commitment device is the wrong tool and stop.
2. **Choose soft or hard.** A soft device costs only regret or reputation on failure: a promise, a box the person can open. A hard device removes access or takes money. Choose hard only when someone else can check the goal and the person can afford the loss.
3. **Set the goal and the check:** a date or amount the person picks, and who verifies it.
4. **Set the stake and its cap.** The person chooses what to put up, within a range. Cap the most anyone can lose below what a household can spare in its leanest month. Send forfeited money away from the program, which must never gain when a person fails. Add an emergency release.
5. **Make the offer a choice:** separate from credit, wages, or any service the person cannot refuse. Expect many to decline.
6. **Plan for people who commit and fail:** what they lose, how they are told, and whether they may try again.
7. **Set the monitoring:** who takes up, the share of committers who fail or lose their stake above which the device is reviewed, and what is checked after it ends.
8. **Name the specialist** if the device holds or takes money or the behavior is clinical.
9. **State what the evidence supports:** the direction. Promise no effect size.

See `references/worked-example.md` for a complete run.

## Output template

```markdown
# Commitment device specification

**Behavior:** <who, what, when>
**Confirmed barrier:** <the evidence that people intend it, have the means, and give way at the moment of action>
**What people already do to bind themselves:** <the informal practice; or "none known">

## The device
- **Type:** <soft / hard>, because <whether the goal can be checked and a loss afforded>
- **Goal:** <the date or amount the person sets>
- **Checked by:** <who, how, at what cost; or "cannot be checked, so the device is soft">
- **What the person puts up:** <access, money, or reputation, and the range they choose within>
- **Cap:** <the most anyone can lose, and the lean-month fact it rests on>
- **Where forfeited money goes:** <not to the program; or "nothing is forfeited">
- **Emergency release:** <how a person gets out, and what it costs them>

## The offer
- **Who is offered it, and how:** <...>
- **How a person says no:** <...>
- **Kept separate from:** <credit, wages, or any service the person cannot refuse>

## People who commit and fail
- **What they lose:** <...>
- **How they are told, and whether they can try again:** <...>
- **Who is most likely to fail:** <...>

## Monitoring
- **Take-up:** <how it is counted, and who is expected to take up>
- **Review if the share of committers who fail or lose their stake exceeds:** <rate, and who reviews>
- **After the device ends:** <what is checked>

## Specialist review
<not needed / <who>, because the device holds or takes money, or the behavior is clinical>

## What the evidence supports
<the direction, and the nearest field evidence with where it was run; no effect size promised>

## What to check before relying on this
- <the assumption most likely to be wrong>
```

## Where it goes wrong

- **Reading sign-ups as proof.** People sign contracts they cannot keep, out of optimism about their future selves. Judge the device by how committers fare.
- **Stricter taken for stronger.** In trials in Kenya and Uganda the looser version of a savings device was used more.
- **An average that hides the losers.** Average savings can rise while most committers pay a penalty. Report both.

## When to bring in a specialist

Tell the user to consult the relevant specialist before any pilot when:
- The device holds, locks, or forfeits money: a financial consumer-protection specialist sets the cap, confirms the holder is regulated, and checks the disclosure
- The behavior is clinical (smoking, alcohol, medication): a clinician chooses the test and what a person who fails is told
- A lender or employer would offer it: a lawyer checks that it cannot work as collateral or a wage deduction

Bring them: the specification, the cap with the income pattern behind it, and the plan for people who fail.
