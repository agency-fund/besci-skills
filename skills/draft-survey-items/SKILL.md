---
name: draft-survey-items
description: >-
  Use when a team knows what it wants to measure and needs the survey
  questions written ("write items for our baseline"), or when a draft leans
  on agree/disagree statements or number-only scales. Writes one-idea
  questions with every answer option in words, the script an interviewer
  reads, and a check against fixed wording rules. Do not use when the
  questions exist and you need to know whether respondents understand them;
  use draft-cognitive-interview-script. Not for putting questions into
  another language; use translate-survey-instrument.
license: CC-BY-4.0
metadata:
  title: Write survey questions people can answer
  type: atomic
  stage: measure
  version: "0.3.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  tested_in: beyond-western-differs
  tags: "measurement, survey-design, quantitative"
  consumes: "measurement-plan"
  produces: "survey-items"
---

## What it does

Writes survey questions with fixed answer options for defined constructs (a construct is the one thing a question is meant to measure).

**What this adds:** writes no question for a construct without a definition; asks about the thing itself with every answer option in words, never agreement with a statement; states beside each question what a correct reading is; runs a fixed eight-rule check and rewrites the failures; leaves a stigmatized behavior unwritten; and labels the result untested.

## When to use it

### Use it when
- A team has named what it wants to measure and asks for the questions
- A draft uses agree/disagree statements, number-only scales, or reverse-worded items
- Interviewers report respondents saying yes to everything

### Do not use it when
- The questions exist and the need is to check that respondents understand them; use `draft-cognitive-interview-script`
- The questions are needed in another language; use `translate-survey-instrument`
- The questionnaire is moving to phone; use `adapt-survey-for-phone-mode`
- The team needs the rate of a stigmatized or illegal behavior; use `design-list-experiment`
- The team has not decided what to measure; use `plan-evaluation-design`

## Before you start

Ask these before producing the questions. Do not ask anything the user has already answered.

1. **Required.** The constructs, each defined in a sentence. "Savings" is a topic; "whether the household put money aside last month" is a construct.
2. **Required.** The respondents (schooling, language) and how they answer: read aloud by an interviewer, by phone, or on a form.
3. Optional. The length budget.
4. Optional. Any question that must match an earlier round or a published scale.
5. Optional. Tested questions on these constructs from earlier local surveys.

If 1 or 2 is missing, ask and stop. Otherwise assume at most three questions per construct and nothing fixed; without tested questions, write new ones and tell the user to look for tested ones first.

## What it draws on

- Krosnick, J. A., & Presser, S. (2010). Question and questionnaire design. In P. V. Marsden & J. D. Wright (Eds.), *Handbook of Survey Research* (2nd ed., pp. 263–313). Emerald. https://web.stanford.edu/dept/communication/faculty/krosnick/docs/2010/2010%20Handbook%20of%20Survey%20Research.pdf Supports: the wording rules, words on every scale point, and direct questions in place of agree/disagree statements.
- Kopper, S., & Parry, K. (2023). *Survey design*. J-PAL Research Resources. https://www.povertyactionlab.org/resource/survey-design Supports: time-bound questions; reusing tested surveys; facts before attitudes; indirect methods for sensitive topics.
- Laajaj, R., & Macours, K. (2021). Measuring skills in developing countries. *Journal of Human Resources*, 56(4), 1254–1295. https://doi.org/10.3368/jhr.56.4.1018-9805R1 Supports: the caution about yea-saying (agreeing whatever the statement says) among respondents with little schooling; keeping reversed items in a fixed scale.
- Clingain, C., Donald, A., & Hernandez-de-Benito, M. (2026). *Measuring agency through psychological constructs in lower-income settings* (Policy Research Working Paper No. 11401). World Bank. https://documents.worldbank.org/curated/en/099218506012639611/pdf/IDU-7ec4d5d3-ea71-4e8f-b9e1-71c807cfd354.pdf Supports: five answer options by default.

**Where the evidence comes from:** The wording rules and the experiments on agree/disagree statements come from the United States and Europe; a study in Kenya found yea-saying rises as schooling falls. On answer options studies split: five were too many for non-readers studied by a team in Brazil and rural women in India, but beat three when randomized in six African countries. Check locally which options respondents can tell apart.

**Replication status:** Yea-saying is replicated. The gain from direct questions over agree/disagree statements is mixed, and the number of options non-readers can use is contested.

## How to do it

1. **Write the intended reading first.** Beside each question write "a correct reading is ...", because a comprehension test scores answers against that line.
2. **Reuse before writing.** Adapt tested questions the user supplied. Leave any that must match another survey unchanged, marked fixed.
3. **Choose the question type from the construct:** a count over a named period ("in the last 7 days, on how many days ..."), a rating of the thing itself, or a count out of ten for a belief about other people.
4. **Ask about the thing itself.** Write "How hard is it to put money aside each week?", not "I find it hard to save: agree or disagree?", because people agree with statements they have not followed.
5. **Put every option in words,** five for a rating. Where respondents cannot read, add a three-option version for the pretest to choose between.
6. **Keep one idea per question, with no "not" and no reversed wording** (where "yes" means less of the construct). In a fixed agree/disagree scale, keep the reversed items: they are the only way to see yea-saying in the data.
7. **Name the time:** a recent period or local event ("since the last market day"), never "usually".
8. **Leave stigmatized or illegal behavior unwritten.** Better wording does not remove the pressure to give the acceptable answer; say it needs a private or indirect method.
9. **Order** facts before opinions, then write the read-aloud script with options spoken every time.
10. **Run the design check** and rewrite or drop each failing question.

See `references/worked-example.md` for a complete run.

## Output template

```markdown
<Two or three plain sentences to the user: how many questions you wrote for which constructs, anything left unwritten and why, and that the questions are untested until respondents are asked what they mean.>

# Draft survey questions: <survey or block name>

**Respondents:** <who, schooling, language>
**How they answer:** <read aloud by an interviewer / phone / self-completed>
**Length budget:** <questions or minutes; "assumed" if not given>

## Questions, by what each one measures

### <Construct>: <one-sentence definition>
**<ID>.** <the question as asked>
- Options: <every option in words; or the number range>
- A correct reading is: <...>
- Notes: <question type; time period; source if reused; "fixed, wording unchanged" if so>

## Order
| Position | Question | Earlier question that could shape the answer |
|---|---|---|
| <1> | <ID> | <none / ID, because ...> |

## Read-aloud script
<verbatim: the transition, each question with its options, interviewer instructions in brackets>

## Design check
| Rule | Pass? | Rewritten or dropped |
|---|---|---|
| One idea per question | <yes/no> | <...> |
| Asks about the thing itself, not agreement with a statement | <yes/no> | <...> |
| Every option in words; five for a rating, plus a three-option version where respondents cannot read | <yes/no> | <...> |
| No "not" and no reversed question | <yes/no> | <...> |
| Time period named | <yes/no> | <...> |
| Plain, neutral words that do not push toward an answer | <yes/no> | <...> |
| Options cover every answer and do not overlap | <yes/no> | <...> |
| No direct question on a stigmatized or illegal behavior | <yes/no> | <...> |

## Not written here
<constructs left out and why: no definition / stigmatized behavior / clinical screener; or "None.">

## Untested
These are draft questions. No respondent has yet been asked what they mean.
- <the question most likely to be misread, and why>
- <the answer scale most likely to fail with these respondents>

## Where you could go from here
<One line saying the draft questions are done.>
<Two or three next moves that fit what this run found, each with why it would help and when it fits. Candidates:
- `draft-cognitive-interview-script`, when the questions, especially those listed as most likely to be misread, are ready to try with a few respondents before fielding
- `translate-survey-instrument`, when the questions will be asked in a language other than the one they were drafted in
- `adapt-survey-for-phone-mode`, when the questions will be asked by phone
- `design-list-experiment`, when a stigmatized or illegal behavior was left unwritten and the sample is more than a few hundred
- tested questions from earlier surveys of the same population, when none were supplied and a question that has been fielded before could replace a new one
- a survey methodologist (a clinician for a clinical construct), when questions are to be added into a score that drives a decision, or compared across rounds or languages>
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

- **A score nobody validated.** The model offers to add several questions into an index. Draft questions have no shown reliability; refuse.
- **Frequency words standing in for counts.** "Never, sometimes, often" passes the words rule, but people mean different numbers by the same word. Ask for the count.
- **Answer lists borrowed from elsewhere.** Reasons copied from another country's survey miss the local answer. Take options from interviews, or add "other (specify)" and flag the list.
- **Repairing a published scale.** Rewording a validated scale to pass the check breaks comparison with its other uses. Show which rules it fails; the user decides.

## When to bring in a specialist

Tell the user to consult a survey methodologist (a clinician for a clinical construct) when:
- A construct is clinical (depression, anxiety, disability) and needs a validated screener
- Several questions are to be added into one score that drives a decision
- Scores must be compared across rounds, languages, or with a published scale
- A stigmatized or illegal behavior is a main outcome

Bring them: the construct definitions, the questions with their intended readings, and the design check.
