---
name: design-a-wise-intervention
title: Design a wise intervention
description: >-
  For a team that thinks people are held back by how they read a setback or a
  setting ("people like me don't belong here", "I'm just not good at this") and
  wants a short exercise to change that reading: name the question the audience
  is asking itself, draft the one exercise that answers it, check that the
  exercise is ethical, and plan a test with a few people from the audience,
  with an optional feasibility pilot. Ends with an exercise draft that has
  passed an ethics review, a plan to test it, and optionally a pilot plan.
  Does not cover barriers of cost, access, or process, and does not measure
  whether the exercise works.
license: CC-BY-4.0
metadata:
  version: "0.1.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  stages: "diagnose, design, test"
  skills: "identify-wise-intervention-target, adapt-growth-mindset-message, draft-belonging-story, draft-values-affirmation, audit-intervention-ethics, plan-prototype-test, design-pilot-feasibility-study"
  tags: "wise-interventions, belonging, growth-mindset, self-affirmation"
---

## What it is for

Short exercises that change how people interpret themselves or their situation are cheap, so they get proposed where the real barrier is a fee or a missing teacher. This workflow starts from the audience's own words, names the one question they are asking themselves, and checks that the setting can deliver what a new answer would promise before any exercise is written. Then it drafts only the exercise that answers that question, checks it, and tries it on a few people. Five steps in three stages; the last is optional.

**Process it follows:** Walton and Wilson's wise interventions (2018): target the specific meaning people make of their situation, and act only where the situation can support a better outcome.

## When to use it

- When a team proposes a mindset message, a belonging story, or an affirmation exercise and nobody has said which question the audience is asking itself
- When interviews show people with the same resources acting differently according to how they read a setback
- When the question is already named from the audience's own words; start at step 2
- Not when cost, access, time, information, or a process holds the behavior back; use `select-intervention-levers`, or join the workflow "From a goal to a tested intervention" at its step 5
- Not before anyone has collected the audience's own words (interview quotes, open survey answers, field notes); step 1 cannot run on the team's description of the audience

## Skills in this workflow

| Step | Skill | Version | Relationship | What carries forward | Human decision point |
|---|---|---|---|---|---|
| 1 | `identify-wise-intervention-target` | 0.2.0 | start | wise-intervention target: the one question the audience is asking, the need behind it, the moment it becomes live, and whether the setting can deliver what a new answer would promise | Accept the question; if the barrier is material or the setting cannot deliver, stop and fix that first |
| 2 | The exercise for the question named in step 1 (`adapt-growth-mindset-message` for beliefs about ability, `draft-belonging-story` for doubts about belonging, `draft-values-affirmation` for feeling judged) | 0.2.0 | after 1 | intervention draft: the lesson, story set, or affirmation script, with its setting check, delivery plan, and the record for that kind of exercise | Choose one exercise, never a bundle, and supply what it needs that step 1 did not collect |
| 3 | `audit-intervention-ethics` | 0.2.0 | after 2 | ethics review: go, revise, or stop, with the changes required | Decide what people will be told about the exercise, and act on a revise or stop verdict |
| 4 | `plan-prototype-test` | 0.1.0 | after 3 | prototype test plan with a keep, change, or drop rule; after the sessions, the revised draft | Fix the decision rule before the first session; after the sessions, decide what changes |
| 5 | `design-pilot-feasibility-study` | 0.2.0 | after 4, optional | pilot plan with go, amend, and stop lines | Decide what the pilot leads to, a trial or a rollout, and set the lines before fieldwork |

Relationship values: `start`, `after N`, `parallel with N`, `independent`, `optional`.

## How to run it

The order is a recommendation. Start at any step if you already have what it needs, and use any of these skills on its own.

1. Collect the audience's own words about how they read their situation: interview quotes, open survey answers, or field notes, with how many people said each thing.
2. Run `identify-wise-intervention-target` with the behavior (who, what, when), the evidence that a belief rather than a practical barrier holds it back, those words, and what the setting offers after any message: feedback and a second attempt, people who include newcomers, an institution on their side.
3. Stop and read the table of interpretations. An interpretation that would disappear once a cost, access, time, information, or process problem were fixed is not a target for this workflow. If the setting check says "does not deliver", no exercise follows until the setting changes; if it says "not verified", find out before going on.
4. Choose the exercise from the need step 1 named, and run only that one. Each skill checks the setting again as a gate and writes nothing if it fails.
   - To understand, "can I get better at this?": `adapt-growth-mindset-message`. It is written for school students and needs the grade, session length, language, and who runs the lesson.
   - To belong, "do people like me belong here?": `draft-belonging-story`. It is for newcomers at a transition and needs older peers of the same group who can be interviewed; it will not invent stories.
   - Self-integrity, "am I a good and capable person?": `draft-values-affirmation`. It needs the moment the judgment is felt and a way to give the exercise in private before it.
5. Run `audit-intervention-ethics` on the draft, with who delivers it, what hold they have over the audience, and what the audience will be told. Expect the transparency check to need a decision. The exercises are introduced as ordinary activities (an affirmation is never announced as help, because that marks people as needing it), while the audit asks whether the exercise would still work if people read a plain statement of its purpose. A person on the team, or the ethics board, decides what people are told.
6. Run `plan-prototype-test` on the draft that passed the audit. The growth-mindset and belonging skills each end with a short pre-test; the prototype plan turns it into groups, rounds, a tester who did not write the draft, and a decision rule fixed in advance. For an affirmation, test whether people understand the prompts; nobody reads what they write.
7. Run the sessions, change the draft by the rule, and test the change again.
8. If the exercise is going to a trial or a rollout, run `design-pilot-feasibility-study` with the revised draft, what the pilot leads to, and the pilot's resources. Take the outcome and the comparison group from the exercise draft's "How you will know" section. The pilot tests whether the exercise can be delivered as designed, at the right moment, to the right people; it does not test whether it works.

## Worked example

This example is illustrative; the college and its details are invented.

A nursing college in Rwanda sees first-year students from rural districts leave after their first ward placement. Staff collect open answers from 40 first-years about the placement. Step 1 tabulates the readings. "The fees are due before the bursary arrives" is material, a payment date, so it goes to the finance office instead. "Everyone else seems to know what they are doing" and "students from my district do not become nurses" are about meaning. Step 1 names one question under the need to belong, "do people like me belong here?", live in the first week of placement. The setting check finds that every student has an assigned clinical mentor and that none of the students asked reported harassment, so the verdict is "delivers". Step 2 runs `draft-belonging-story`: it plans interviews with eight second-year students from rural districts, edits their accounts with their approval, and writes the task in which first-years write a letter to the next intake. Step 3 rates transparency a concern, because the session would be introduced only as older students sharing their experience. The team decides to tell first-years that the session is meant to help newcomers settle in, and with that change the verdict is go. Step 4 plans two rounds with five rural and five urban first-years, run by a tutor who did not edit the stories. The college then wants to compare two intakes, so step 5 plans a pilot in one intake with go, amend, and stop lines on attendance at the session, letters written, and whether enrollment records can be pulled for every student.

## Where it goes wrong

- Picking the famous exercise. Growth mindset gets chosen because people have heard of it; the question has to come from the audience's words in step 1.
- An exercise in place of a fix. If step 1 finds a fee, a missing teacher, or exclusion, an exercise would ask people to doubt a reading that is correct.
- A bundle. Combining affirmation, belonging, and mindset content hides which part, if any, worked.
- Delivering an illustration. A belonging story the skill wrote to show the shape is labeled "illustration, not for delivery"; presented as real, it is a deception.
- Promising an effect. Each exercise skill states the record for its kind of exercise and promises no effect size; the workflow promises none either.
- Reading step 4 as a result. Five people per group show whether the exercise is understood and lands at the right moment, not whether it changes outcomes.

## When to bring in a specialist

- The audience includes people in clinical distress, minors, or people who have lived through recent conflict or disaster: a psychologist with intervention experience, or a counselor, reviews the exercise before step 4.
- The threat involves stigma or a protected characteristic (HIV status, caste, ethnicity, disability): a local qualitative researcher and a safeguarding lead, because the setting itself may be what excludes people.
- The plan is a regional or national rollout: an evaluator registers a test in advance, before anything scales.

Bring them the table of interpretations with its quotes, the setting check, the draft, and the ethics review.
