---
name: plan-prototype-test
description: >-
  Use when a draft of an intervention exists (a message, form, script, product
  change, or a practice to try at home) and the team wants to try it with a
  few people from the audience before any pilot: "show it to some users
  first", "pretest the materials". Plans what to learn, with whom, how, and
  the rule for what is kept, changed, or dropped. Do not use when the question
  is whether the program can be delivered at small scale; use
  design-pilot-feasibility-study. Not for pretesting survey questions; use
  draft-cognitive-interview-script.
license: CC-BY-4.0
metadata:
  title: Test a draft with a few people before the pilot
  type: atomic
  stage: design
  version: "0.1.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  tested_in: beyond-western-differs
  tags: "qualitative, prototyping, user-testing"
  consumes: "intervention-draft"
  produces: "prototype-test-plan"
---

## What it does

Plans a test of a draft intervention with a few people from the audience, before any pilot.

**What this adds:** ties every learning question to the barrier the draft should remove; has people use the draft, since "do you understand?" gets a polite yes; sets people per group and a second round; keeps the draft's author out of the tester's seat; fixes the keep, change, or drop rule before the first session; reports counts, never percentages.

## When to use it

### Use it when
- A draft exists and someone asks to "show it to a few people first", "user test it", or "pretest the materials"
- A draft is about to enter a pilot that nobody from the audience has seen
- A team has only a sketch and asks whether the idea is worth building
- A program wants households to try a new practice at home before promoting it

### Do not use it when
- The draft is not written yet; use `draft-lever-content`
- The draft is a set of survey questions; use `draft-cognitive-interview-script`
- The question is whether the program can recruit, keep, and serve people at small scale; use `design-pilot-feasibility-study`

## Before you start

Ask these before producing anything. Do not ask anything the user has already answered.

1. **Required.** The draft: what it is, how finished it is, the behavior it should change (who does what, when), and the barrier it should remove.
2. **Required.** The audience: who the draft is for, which groups may react differently, how many people the team can reach, in which language, and who can run sessions.
3. Optional. What the team is least sure of.

If 1 or 2 is missing, ask and stop. If the barrier is unknown, test understanding and use only, and say the mechanism (how the draft changes the behavior) goes untested. If 3 is missing, take the questions from the steps of using the draft.

## What it draws on

- Kettle, S., & Persian, R. (2022). *Target, Explore, Solution, Trial, Scale: An introduction to running simple behavioural insights projects*. The Behavioural Insights Team. https://www.bi.team/wp-content/uploads/2022/11/BIT-Handbook-How-to-run-simple-BI-projects.pdf Supports: learning questions tied to barriers; having people use the draft; five as the least for a group of similar people.
- Dell, N., Vaidyanathan, V., Medhi, I., Cutrell, E., & Thies, W. (2012). "Yours is better!" Participant response bias in HCI. *Proceedings of the SIGCHI Conference on Human Factors in Computing Systems*, 1321–1330. https://doi.org/10.1145/2207676.2208589 Supports: not saying who made the draft; a local tester.
- Dickin, K., Griffiths, M., & Piwoz, E. (1997). *Designing by Dialogue: A Program Planners' Guide to Consultative Research for Improving Young Child Feeding*. Academy for Educational Development. https://web.archive.org/web/20241203073137/https://pdf.usaid.gov/pdf_docs/PNACE296.pdf Supports: the home trial.

**Where the evidence comes from:** The planning steps come from a practitioner guide written from work with the governments of Bangladesh, Guatemala, and Indonesia; the home trial from child-feeding programs in Africa, Asia, and Latin America. In Bangalore, India, people were about 2.5 times as likely to prefer technology they believed the interviewer had built, and thinking aloud drew fewer comments from Indian and Kenyan users than from British ones. Check locally whom people will criticize a draft in front of.

**Replication status:** Mixed. Small tests surface problems, but how many varies: in one study from a United States university, random groups of five software users found between 55% and 99% of the known problems.

## How to do it

1. **State what the draft must do:** who should do what, and which barrier the draft removes. The test checks that claim, not whether people like the draft.
2. **Match the version to the question.** A sketch or role play shows whether the idea is worth building; a working version shows where it breaks.
3. **Write three to five learning questions.** Tie each to the barrier or a step of use, and name what will be observed: an action, or the person's own words. Include one that checks the barrier itself.
4. **Choose who and how many.** List the groups likely to react differently (schooling, language, who decides at home) and the staff who will deliver the draft. Plan about five people per group per round, and two rounds, because a fix is itself untested.
5. **Choose the method:** show and tell back, for a sketch; use while observed, for anything a person handles; role play, for a script or service; home trial (Trials of Improved Practices), for a practice done at home over days, following `references/trials-of-improved-practices.md`.
6. **Write the session guide.** Say the draft is on trial, not the person; do not say who made it. Give a task, watch, then have the person say what the draft asks of them. Where thinking aloud (narrating while using the draft) is awkward, walk back through the task afterward.
7. **Name the tester:** someone who did not write the draft and speaks the participants' language, plus a note-taker.
8. **Fix the decision rule** per learning question, in counts: keep, change and retest, or drop, plus what stops the test at once.
9. **Say what the test cannot show.**

See `references/worked-example.md` for a complete run.

## Output template

```markdown
# Prototype test plan

**Draft under test:** <what it is; version shown: idea / sketch / mock-up / working version>
**What it must do:** <who does what, when; the barrier the draft removes>
**Decision this test feeds:** <what the team will decide with the result, and by when>

## Learning questions
| # | Question | Tied to | What will be observed |
|---|---|---|---|
| 1 | <...> | <barrier / step of use> | <an action, or the person's own words> |

## Who and how many
| Group | Why they may react differently | People per round | How they are found |
|---|---|---|---|
| <...> | <...> | <number> | <...> |

- **Rounds:** <number; what happens between them>
- **Not reached:** <who is left out, and what that could hide>

## Method
- **Method:** <show and tell back / use while observed / role play / home trial>
- **Why this one:** <the learning question it answers>
- **Setting:** <where, with what materials, how long>
- **Run by:** <tester and note-taker; neither wrote the draft; language>

## Session guide
1. <opening: the draft is on trial, not the person; who made it is not said; consent>
2. <task, in the words the tester will use>
3. <what the note-taker watches for>
4. <tell back: "In your own words, what is this asking you to do?">
5. <closing questions>

## Recording sheet
| Person | Group | Learning question | What they did | What they said (their words) | Problem? | Safety concern? |
|---|---|---|---|---|---|---|

## Decision rule (fixed before the first session)
| Learning question | Keep if | Change and retest if | Drop if |
|---|---|---|---|
| <#> | <count> | <count> | <count> |

- **Stop at once if:** <a sign of harm from any one person>
- **Stop testing when:** <a round turns up nothing the rule says to change; or the round limit>

## What this test cannot show
- <whether the behavior changes; how many people in the audience would respond>

## What to check before relying on this
- <the assumption most likely to be wrong>
```

## Where it goes wrong

- **Counts reported as rates.** "Four of five understood" becomes "80% comprehension" in a proposal. Five people show that a problem exists, never how common it is.
- **Understanding mistaken for the mechanism.** People can read the card, so the draft passes; nobody learned whether the barrier it removes is the one stopping them.
- **Every comment becomes a change.** One person's taste gets built in, and the line the technique depends on gets cut.

## When to bring in a specialist

Tell the user to consult a specialist before the first session when:
- The draft changes how people take medication, feed an infant, or handle money: a clinician, nutritionist, or financial compliance lead approves what participants will be asked to try
- Participants are children, patients, or people who depend on the organization for a service: an ethics reviewer or safeguarding lead decides what consent is needed

Bring them: the plan, the session guide, and the decision rule.
