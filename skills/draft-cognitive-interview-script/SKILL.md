---
name: draft-cognitive-interview-script
description: >-
  Use when draft survey questions exist and a team wants to check, before
  fielding, that respondents understand them as intended ("pretest our
  survey", "cognitive testing", "do these questions make sense to people").
  Writes the interview script: open follow-up questions for each survey
  question, a note sheet, and a rule for which questions to fix. Do not use
  when the questions are not written yet; use draft-survey-items. Not for
  interviews about why people do or do not do something; use
  draft-tdf-interview-guide.
license: CC-BY-4.0
metadata:
  title: Test whether people understand your survey questions
  type: atomic
  stage: measure
  version: "0.3.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  tested_in: beyond-western-holds
  tags: "measurement, qualitative, survey-design"
  consumes: "survey-items"
  produces: "interview-guide"
---

## What it does

Writes the script for cognitive interviews, in which a few respondents answer draft survey questions one at a time while an interviewer asks how they understood each one.

**What this adds:** requires each question's intended meaning before writing a probe (a follow-up about the survey question); writes only open probes that do not contain the intended answer; scripts probes in place of asking respondents to think aloud (say their thoughts as they answer); budgets three minutes per question; supplies a note sheet with fixed problem codes; and sets the rule for which questions get fixed before any interview.

## When to use it

### Use it when
- A team has draft survey questions and asks "will people understand these?"
- Someone asks for cognitive testing, cognitive interviews, or think-aloud testing of a questionnaire
- A questionnaire translated or borrowed from another country is about to be fielded untested

### Do not use it when
- The questions are not written yet; use `draft-survey-items`
- The questions are not yet in the interview language; use `translate-survey-instrument`
- The interviews are to learn why people do or do not do something; use `draft-tdf-interview-guide`

## Before you start

Ask these before producing the script. Do not ask anything the user has already answered.

1. **Required.** The questions exactly as respondents will hear or read them, with answer options.
2. **Required.** What each question is meant to measure, a phrase each.
3. **Required.** The respondents: schooling, language, and whether the survey is read aloud or self-completed.
4. Optional. The questions that worry the team most.
5. Optional. How many interviews are possible.

If 1, 2, or 3 is missing, ask and stop. If 4 is missing, flag every question with an abstract word, a rating scale, a time period, or a hypothetical. If 5 is missing, plan two rounds of eight.

## What it draws on

- Willis, G. B., & Artino, A. R. (2013). What do our respondents think we're asking? Using cognitive interviewing to improve medical education surveys. *Journal of Graduate Medical Education*, 5(3), 353–356. https://doi.org/10.4300/JGME-D-13-00154.1 Supports: scripted probes asked after each question; the four things a respondent must do (understand, recall, judge, fit the answer to the options); small repeated rounds.
- Scott, K., Ummer, O., & LeFevre, A. E. (2021). The devil is in the detail: reflections on the value and application of cognitive interviewing to strengthen quantitative surveys in global health. *Health Policy and Planning*, 36(6), 982–995. https://doi.org/10.1093/heapol/czab048 Supports: probing over thinking aloud, pairs, recruiting those most likely to struggle, three minutes per question.
- Conrad, F. G., & Blair, J. (2009). Sources of error in cognitive interviews. *Public Opinion Quarterly*, 73(1), 32–55. https://doi.org/10.1093/poq/nfp013 Supports: probing only on what the respondent said or did.

**Where the evidence comes from:** Field studies in India, Bangladesh, Ethiopia, Kenya, and Uganda found that the interviews exposed misread questions, including ones respondents had answered without hesitation. In Ethiopia and Kenya the first round was stopped because the probes distressed participants; a revised script worked. Check locally whether respondents are at ease explaining an answer to a stranger.

**Replication status:** That the interviews expose misread questions is replicated. Which problems they find is mixed: judges agree fairly well on which questions most need repair, poorly on which single answers show a problem, and in one experiment a reworded question gave no clearly better data than the draft.

## How to do it

1. **Write the yardstick.** For each question: "meant to measure X; a correct reading is Y." Probes and notes are judged against it.
2. **Script probes; do not ask for thinking aloud,** which confuses many respondents with little schooling. Ask the probes straight after each question, or after the whole questionnaire when respondents will fill it in alone.
3. **Budget three minutes per question.** If they do not fit, test the flagged ones and list the rest as untested.
4. **Choose two or three probes per question** from `references/probe-bank.md` by where it can fail: a word, a time period, a rating scale, a sensitive topic. Flagged questions get two more.
5. **Keep every probe open.** Write "What time period were you thinking about?", never "Did you think of the last seven days?"
6. **Add cue probes,** asked only on a pause, a request to repeat, a changed answer, or an answer that fits no option; probing on a hunch finds problems that are not there.
7. **Write the stop rule:** when a respondent is upset or cannot answer, the interviewer drops the probe, notes it, and moves on.
8. **Set the plan and the fix rule before fieldwork.** Recruit from the survey's population, outside its sample, those with the least schooling first. Try the script on two people. Fix a question when one problem appears in two interviews of a round, or once if the respondent could not answer (this skill's own rule); retest every reworded question.

See `references/worked-example.md` for a complete run.

## Output template

```markdown
<Two or three plain sentences to the user: how many questions the script covers and which get the most probing, the plan in rounds and interviews, and that the interviews can show a question is misread but not that the answers are true.>

# Cognitive interview script: testing whether people understand <questionnaire name>

**Respondents:** <who, schooling, language of the interview>
**When the follow-up questions (probes) are asked:** <after each question / after the whole questionnaire, and why>
**Plan:** <rounds> rounds of <n> interviews of about <minutes> minutes, in pairs (one asks, one takes notes); recruit <who and where: the survey's population, outside its sample>
**Not tested in this script:** <questions left out for time, or "none">

## Opening (read aloud)
<purpose; "we are testing the questions, not you"; consent to notes or recording; practice question and probe>

## Questions and probes
<instruction to the interviewer: read each question as written; if asked what it means, do not explain, and note the request>

### Q<n>. "<exact question text>" (options: <...>)
**Meant to measure:** <...>  **A correct reading is:** <...>
- <what the probe tests: meaning / recall / judgment / options>: <probe>
- <...>: <probe>
- If <cue>: <probe>

## Closing
<which question was hardest; anything missing; thanks>

## If a respondent is upset or cannot answer
<the stop rule, in words an interviewer can follow>

## Note sheet (one per interview)
| Question | Answer given | How the respondent read it, in their words | Problem code | Quote |
|---|---|---|---|---|
| Q1 | | | | |

Problem codes: unclear word / wrong reading / cannot recall / options do not fit / uncomfortable / translation / none

## After each round
- Tabulate: questions as rows, interviews as columns, problem codes in the cells.
- Fix a question when: <rule>
- Retest: <every reworded question, in the next round>
- Stop when: <rule>

## What this cannot tell you
- <the limit that matters most for this questionnaire>

## Where you could go from here
<One line saying the script is done.>
<Two or three next moves that fit what this run found, each with why it would help and when it fits. Candidates:
- `translate-survey-instrument`, when the questions or probes are not yet in the interview language, or problems coded "translation" cluster after a round
- `draft-survey-items`, when a round shows a question's answer options do not fit and need rewriting (not when the idea itself does not exist for respondents)
- a briefing and a try-out with two people, when the interviewers have not run these interviews before, since an interviewer who explains a question tests a different one
- a psychometrician or survey methodologist, when the questions belong to a validated scale or the answers will decide referral or eligibility>
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

- **A quiz.** Probes that ask for a definition ("what is a balanced diet?") make respondents guess the right answer. Ask what the words meant to them when they answered.
- **Rewording when the fault is the idea.** If respondents cannot restate a question however it is put, as with "consent" in rural India, the idea may not exist for them in that form. Report it; do not offer another wording.
- **Interviewers who explain.** An interviewer who rephrases a question to help tests a different question. The script has them read it as written and note the request.

## When to bring in a specialist

Tell the user to consult a psychometrician (who tests whether scores mean what they claim) or a survey methodologist when:
- The questions belong to a validated scale and the interviews point to rewording, which can break comparison with its other uses
- Answers will decide something for a person (eligibility, referral, diagnosis); testing comprehension does not validate a score or a cut-off
- Problems cluster on sensitive questions, which points to the way of asking, not the wording

Bring them: the questions with their intended meanings, the tabulated problem codes, and quotes for each problem question.
