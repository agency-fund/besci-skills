---
name: draft-norms-vignette
description: >-
  Use when a team wants survey questions that test whether a practice (latrine
  use, tablets in pregnancy, girls' schooling) follows what others do or
  approve of: "write a vignette", "scenario questions for our norms survey".
  Writes one short story about a fictional person in versions that differ
  only in what others do and approve of, with the questions and how to read
  the answers. Do not use when nobody has yet asked whether others'
  expectations matter; use diagnose-social-norm. Not for the respondent's own
  hidden behavior; use design-list-experiment.
license: CC-BY-4.0
metadata:
  title: Write scenarios that measure what others do and approve
  type: atomic
  stage: measure
  version: "0.3.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  tested_in: beyond-western-holds
  tags: "social-norms, survey-design, measurement, experimental-design"
  consumes: "social-norm-diagnosis"
  produces: "survey-items"
---

## What it does

Writes a short survey story in versions that differ only in what other people are said to do or approve of.

**What this adds:** names in every cue whose behavior or approval it is, never "people"; changes only the cue sentences between versions; assigns versions at random; asks fixed questions about the fictional person; says in advance what each pattern of answers would mean; and withholds the wording for a harmful practice until a local researcher has seen it.

The method is Bicchieri's. An empirical expectation is what a person believes others do; a normative expectation, what they believe others think they should do. Respondents predict what a fictional person will do when these change, because people resist "what if everyone stopped?" questions about themselves.

## When to use it

### Use it when
- Interviews or a diagnosis suggest a practice depends on what others do or approve of, and the team wants a survey test
- Someone asks to "write a vignette" or for "scenario questions for the norms survey"
- A program wants a measure of expectations to repeat after a norms activity

### Do not use it when
- Nobody has yet asked the people concerned whether others' expectations matter; use `diagnose-social-norm`
- Whose behavior and approval people track is a guess; use `map-reference-network`
- The question is how common the respondent's own hidden behavior is; use `design-list-experiment`

## Before you start

Ask these before producing the vignette. Do not ask anything the user has already answered.

1. **Required.** The practice and the moment of decision (who does what, when), with the evidence that others' expectations may matter.
2. **Required.** Whose behavior and whose approval people track for this practice, as respondents named them.
3. **Required.** The respondents and the mode: schooling, language, read aloud or self-read, alone or in a group.
4. **Required.** Whether the practice is harmful, illegal, or stigmatized.
5. Optional. How many respondents the survey will have.

If 1 to 3 are missing, ask and stop. If 4 is missing, treat the practice as sensitive. If 5 is missing, say the sample has not been checked.

## What it draws on

- Bicchieri, C., Lindemans, J. W., & Jiang, T. (2014). A structured approach to a diagnostic of collective practices. *Frontiers in Psychology*, 5, 1418. https://doi.org/10.3389/fpsyg.2014.01418 Supports: the design and the questions.
- Bicchieri, C., & Penn Social Norms Training and Consulting Group (2016). *Why Do People Do What They Do? A Social Norms Manual for Viet Nam, Indonesia and the Philippines*. UNICEF Office of Research – Innocenti. https://repository.upenn.edu/pennsong/12 Supports: a fictional person who resembles the respondents.
- Bicchieri, C., Das, U., Gant, S., & Sander, R. (2022). Examining norms and social expectations surrounding exclusive breastfeeding: Evidence from Mali. *World Development*, 153, 105824. https://doi.org/10.1016/j.worlddev.2022.105824 Supports: step 7.

**Where the evidence comes from:** The design was set out with child marriage as its example and taught in UNICEF courses in Southeast Asia. In Mali, mothers more often predicted that a fictional mother would breastfeed exclusively when told most mothers in her community did; vignette studies of norms have also run in Ghana, Benin, and Zambia. Check locally that respondents will reason about a made-up person.

**Replication status:** Used repeatedly in low- and middle-income countries with interpretable results; none found there checked the answers against what people then did.

## How to do it

1. **Write the base story:** a named fictional person like the respondents in sex, age, and situation, at one moment of decision, told briefly. Set it in a similar community that is not their own, because people reject a cue about neighbors they know. State details respondents would otherwise fill in differently (religion, wealth, who she lives with).
2. **Write the empirical cue in two versions** with the same quantifier: "Most pregnant women in her village take the tablets" and "... do not".
3. **Write the normative cue in two versions,** naming who approves: "Her husband and his mother think a pregnant woman should take them" and "... should not".
4. **Combine them into four versions** that match in every other word.
5. **Write the questions,** all about the fictional person: what she will do (fixed answers); what might lead her to do it, and not to (open); whether the respondent thinks she should. Add a check that the cue was heard.
6. **Assign one version to each respondent at random,** by the survey software. Giving a respondent several versions needs a planned design; do not improvise it.
7. **Say how the answers will be read,** before fielding. The outcome is the share predicting she follows the practice, by version. A shift with what others do alone points to a descriptive norm; with what others approve, to a social norm. No shift means people would act the same whatever others did, or the cue did not register; the check question tells which.
8. **For a harmful, illegal, or stigmatized practice, stop before wording:** give the design, the cues in outline, and the questions, and name the review needed.

See `references/worked-example.md` for a complete run.

## Output template

```markdown
<Two or three plain sentences to the user: what the story asks respondents to predict, whose behavior and whose approval the versions change (or, for a harmful practice, that the wording waits for review), and that the answers are predictions about a made-up person, not what respondents do.>

# Survey story (vignette): <practice>

**Practice and moment of decision:** <who does what, when>
**Why expectations are thought to matter:** <the diagnosis or interview evidence>
**Whose behavior and approval the story names:** <whose behavior the empirical cue names; whose approval the normative cue names>
**Respondents and how they are surveyed:** <who; schooling; language; read aloud or self-read; alone or in a group>
**Sensitivity:** <none stated / sensitive: wording withheld, and the review required>

## Base story (the same in every version)
"<named fictional person; a similar community elsewhere; the details that matter; one moment of decision>"

## The sentences that change (cues)
| | Version A | Version B |
|---|---|---|
| Empirical: what others do | "<Most ... do>" | "<Most ... do not>" |
| Normative: what others approve | "<... think she should>" | "<... think she should not>" |

## Versions
1. Base story + empirical A + normative A
2. Base story + empirical A + normative B
3. Base story + empirical B + normative A
4. Base story + empirical B + normative B

## Questions after the story
1. **What she will do:** "<...>" Answers: <...>
2. **What might lead her to, and not to (open):** "<...>"
3. **Whether she should, in the respondent's view:** "<...>" Answers: <...>
4. **Check that the cue was heard:** "<...>"

## Random assignment
<unit; how generated; what is recorded; what the interviewer sees>

## How the answers will be read
- **Outcome:** share answering "<follows the practice>" to question 1, by version
- **What others do:** versions 1 and 2 against 3 and 4
- **What others approve:** versions 1 and 3 against 2 and 4
- **What each result would mean:** <shift with what others do alone / with what others approve / with neither, and what each would mean here>
- **Sample:** <respondents per version; whether that has been checked>

## What to ask when trying out the story
- <whether the cue is heard as an expectation or as news about the practice>
- <whether respondents answer for the fictional person or for themselves>

## Where you could go from here
<One line saying the vignette is done.>
<Two or three next moves that fit what this run found, each with why it would help and when it fits. Candidates:
- `draft-cognitive-interview-script`, when the story is ready to try with a few respondents, to check the cues are heard as expectations and the person is like them
- `translate-survey-instrument`, when the story must be asked in another language, since the versions must still match in every word but the cues
- `estimate-sample-size`, when the respondents per version have not been checked against the smallest shift that would change the program
- `map-reference-network`, when whose behavior or approval people track is still a guess, or the try-out shows respondents look to someone the cues do not name
- a local qualitative researcher and an ethics reviewer, when the practice is harmful, illegal, or stigmatized, or respondents are minors>
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

- **A cue heard as news about the practice.** "Most women do not take the tablets" can be heard as "the tablets are harmful"; the shift then reflects a belief about the tablets, not an expectation.
- **A fictional person unlike the respondents.** Respondents answer by imagining themselves in her place. Make her richer, older, or of another faith and they describe a stranger.
- **Predictions reported as behavior.** The answers are what respondents expect of a fictional person; report them as that.

## When to bring in a specialist

Tell the user to consult, before any wording is fixed:
- A local qualitative researcher who knows the practice and an ethics reviewer, when the practice is harmful, illegal, or stigmatized (child marriage, partner violence), respondents are minors, or the people the cues name could overhear: a story can distress, and a version in which others approve can read as endorsement
- A survey statistician, when four versions and the subgroups wanted leave few respondents per version

Bring them: the base story, the cues, the questions, and the sampling plan.
