---
name: from-a-goal-to-a-tested-intervention
title: From a goal to a tested intervention
description: >-
  For a program team that has a goal ("more children complete their
  vaccinations") and no behavioral diagnosis yet: define one behavior, list
  and test reasons it is not happening, choose a lever for the barrier the
  interviews confirm, draft it, check its ethics, try it with a few people,
  and plan the measurement and a feasibility pilot. Ends with a draft that has
  been tried with the audience, a measurement plan with one primary outcome,
  and a pilot plan with go, amend, and stop lines. Does not cover the main
  trial's design, sample size, or analysis, or scale-up.
license: CC-BY-4.0
metadata:
  version: "0.1.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  stages: "define, diagnose, analyze, design, test"
  skills: "define-key-behavior, decompose-comb-barriers, draft-tdf-interview-guide, synthesize-interview-findings, select-intervention-levers, design-reminder-schedule, select-default-option, draft-implementation-intention-prompt, design-incentive-scheme, draft-lever-content, audit-intervention-ethics, plan-prototype-test, plan-evaluation-design, design-pilot-feasibility-study"
  tags: "com-b, behavior-change-wheel, tdf, behavior-change-techniques, experimental-design"
---

## What it is for

A team knows the outcome it wants and is tempted to jump to an intervention ("let's send a text"). This workflow puts the diagnosis before the design, puts a round of real interviews between the team's guesses and the lever, tries the draft on a few people before any pilot, and ends with a pilot that tests whether the program can run, not whether it works. Ten steps across five stages: the longest workflow in the library.

**Process it follows:** the define, diagnose, design, and test sequence of Datta and Mullainathan's *Behavioral Design* (2012).

## When to use it

- When a program goal exists but nobody has named the behavior, the barrier, or the lever
- When a team has an intervention idea and cannot say which barrier it addresses
- When you already have a barrier confirmed by your own interviews; start at step 5. When you already have a draft; start at step 7
- Not when people are held back by how they read their situation ("people like me don't belong here") rather than by cost, access, or forgetting; use the workflow "Design a wise intervention"
- Not as a substitute for checking the research; run the workflow "Check the evidence" alongside step 1

## Skills in this workflow

| Step | Skill | Version | Relationship | What carries forward | Human decision point |
|---|---|---|---|---|---|
| 1 | `define-key-behavior` | 0.2.0 | start | target behavior brief: one behavior as who does what, when, with the runners-up ranked | Commit to one behavior; if the top two are close on team guesses, ask a few people from the audience first |
| 2 | `decompose-comb-barriers` | 0.2.0 | after 1 | ranked hypotheses about why the behavior is not happening, each with a question that could rule it out | Choose the two or three hypotheses the interviews will test |
| 3 | `draft-tdf-interview-guide` | 0.2.0 | after 2 | interview guide, with a map from each question to the hypothesis it tests | Choose who is interviewed and by whom; get ethics review first if the topic is sensitive |
| 4 | `synthesize-interview-findings` | 0.2.0 | after 3, once the interviews are done | barrier diagnosis: a verdict on each hypothesis, the confirmed barriers, and what no hypothesis predicted | Decide whether one barrier is confirmed, or whether another round of interviews is needed |
| 5 | `select-intervention-levers` | 0.2.0 | after 4 | lever brief: one kind of intervention, one named technique, and ranked fallbacks | Accept the technique, and confirm the permissions and costs it needs |
| 6 | The technique skill for the chosen lever (for example `design-reminder-schedule`, `select-default-option`, `draft-implementation-intention-prompt`, `design-incentive-scheme`), or `draft-lever-content` when no technique skill fits | 0.2.0 | after 5 | intervention draft | Check that the draft delivers the one technique chosen, and settle the open questions it lists |
| 7 | `audit-intervention-ethics` | 0.2.0 | after 6 | ethics review: go, revise, or stop, with the changes required | Act on a revise or stop verdict; decide whether the ethics board sees the draft before launch |
| 8 | `plan-prototype-test` | 0.1.0 | after 7 | prototype test plan with a keep, change, or drop rule; after the sessions, the revised draft | Fix the decision rule before the first session; after the sessions, decide what changes |
| 9 | `plan-evaluation-design` | 0.2.0 | after 4, parallel with 5, 6, 7, and 8 | measurement plan: one primary outcome, its data source, when it is measured, and the smallest change worth detecting | Name who sets the smallest change worth detecting, and lock the dated outcome statement before launch |
| 10 | `design-pilot-feasibility-study` | 0.2.0 | after 8 and 9 | pilot plan with go, amend, and stop lines | Set the lines before fieldwork, and agree what each result changes in the main study |

Relationship values: `start`, `after N`, `parallel with N`, `independent`, `optional`.

## How to run it

The order is a recommendation. Start at any step if you already have what it needs, and use any of these skills on its own.

1. Run `define-key-behavior` on the goal, with who the program reaches, where, through what channel, and what is already built. It lists at least three candidate behaviors, scores them, and picks one. Look at which scores are team guesses before you commit.
2. Run `decompose-comb-barriers` on the behavior and what the team has seen or heard. Stop and choose two or three hypotheses for the interviews, using the ranking table's evidence and cost columns.
3. Run `draft-tdf-interview-guide` with the behavior, those hypotheses, and who will interview whom. Try the guide with two respondents, then run the interviews. Nothing after this point should rest on hypotheses alone.
4. Run `synthesize-interview-findings` on the transcripts or notes and the hypotheses. If no hypothesis is supported, go back to step 2 with what you learned. If two are supported, take each through the next steps separately, or ask a specialist whether another round of interviews is cheaper than a wrong pilot.
5. Run `select-intervention-levers` on one confirmed barrier and its evidence, with what the implementer controls: budget, channels, staff, partners, and what needs someone else's permission. Keep the ranked fallbacks; they are the next thing to try if this lever fails.
6. Run the skill that owns the chosen technique, giving it the confirmed barrier and its evidence from step 4 as well as the lever brief. For example, `design-reminder-schedule` when people mean to act and forget a due date; `select-default-option` when doing nothing leaves people without something they want; `draft-implementation-intention-prompt` when people say they will do a dated, one-off action and do not; `design-incentive-scheme` when the cost of acting stops people. `select-intervention-levers` lists the others. If none fits, `draft-lever-content` writes the words. A message about what other people do needs `diagnose-social-norm` before `write-social-norm-message`.
7. Run `audit-intervention-ethics` on the draft, with who delivers it, what hold they have over the audience, and what the audience will be told. Do this even for "just a message".
8. Run `plan-prototype-test` on the draft that passed the audit. Run the sessions, change the draft by the rule, and test the change again.
9. At any point after step 4, run `plan-evaluation-design` with the behavior, the data that exist and who holds them, and the confirmed barriers. The person who will decide on scale-up sets the smallest change worth detecting; until then it is marked provisional.
10. Run `design-pilot-feasibility-study` with the tested draft, the primary outcome and data source from step 9, and the pilot's people, sites, staff, and time. If the main trial's unit, size, and expected dropout are not designed yet, the pilot's lines are provisional; `choose-trial-design` and `estimate-sample-size` settle them. When the team moves to a trial, `estimate-expected-effect`, `estimate-sample-size`, and `write-pre-analysis-plan` come next.

## Worked example

This example is illustrative; the program and its details are invented.

A district health program in Bangladesh wants more children fully vaccinated. Step 1 compares candidates, among them caregivers bringing the child for each dose, health workers visiting families who missed one, and caregivers keeping the vaccination card, and selects: caregivers of children registered at the program's clinics bring the child for the second measles-rubella dose within 30 days of the due date. Step 2 writes hypotheses under all six parts of COM-B; the team chooses three to test: caregivers forget the date, the trip costs a day's wages, and the child's grandmother advises against a second injection. Step 3's guide is tried on two caregivers, then used in 18 interviews with caregivers who did and did not bring their child. Suppose step 4 supports forgetting, finds the trip cost mixed, and does not support the grandmother hypothesis. Step 5 reads the published table for that kind of barrier, scores the options against what the program controls, and names one technique: a prompt shortly before the due date. Help with the trip is kept as the first fallback. Step 6 runs `design-reminder-schedule`: two voice messages to the phone the household uses, because many caregivers share a phone and some do not read. Step 7 returns go, with one change: caregivers can stop the messages by telling their health worker. Step 8 tests the voice message with five caregivers who have their own phone and five who share one, run by a health worker from another clinic. Step 9 sets the primary outcome as the share of eligible children with the second dose recorded in the clinic register within 30 days of the due date, and the district health officer sets the smallest change worth detecting. Step 10 plans a pilot in three clinics, with go, amend, and stop lines on the share of caregivers with a working phone number, the share of messages delivered, and the share of register entries complete.

## Where it goes wrong

- Running step 5 on step 2's ranking without the interviews in steps 3 and 4. The lever then answers a guess.
- Running a technique skill before `select-intervention-levers`. The technique skills assume a confirmed barrier and a chosen technique.
- Adding a second technique while drafting ("while we're at it, add a pledge"). That is an intervention nobody diagnosed.
- Skipping step 7 because the draft is "just a message". A message can carry a loss, a deadline, or a claim about others that someone pays for.
- Reporting step 8's counts as rates. "Four of five understood" is not "80% comprehension".
- Choosing the primary outcome after the pilot shows which number moved. Step 9 dates it before launch.
- Treating the pilot as the test of whether the intervention works, and sizing the trial on its numbers. The pilot measures whether the program can run.
- Treating the order as fixed. Step 4 can send you back to step 2, and step 8 can send you back to step 6.

## When to bring in a specialist

- The behavior carries clinical, safety, or child-protection risk: a clinician or safeguarding lead reviews the interview guide (step 3) and the draft (step 6) before anyone outside the team sees them.
- Two barriers are equally supported at step 4, or the verdict rests on a few interviews: a qualitative researcher who reads the interview language designs the next round. Bring the hypotheses, the guide, and the matrix.
- Step 5 selects a payment, a penalty, a restriction, or a default that moves money: a legal or safeguarding lead, before step 6.
- A trial follows the pilot: an evaluator or statistician owns the trial design, the sample size, and the analysis plan. Bring the measurement plan from step 9 and the pilot report.
