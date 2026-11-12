# Worked example: fertilizer-timing questions for maize farmers in western Kenya

A full run of the skill on a realistic case, showing the output it should produce. The case is illustrative, not a real program.

## The request

"We have four baseline questions for smallholder maize farmers in Kakamega County, mostly women with primary schooling. Enumerators will read them aloud at home in Kiswahili; the Kiswahili version is agreed, and I give the English here. A1: 'Think about the long rains of this year. When did you buy the fertilizer you used at planting?' Options: before the previous harvest / between the harvest and planting / at planting time / I did not buy fertilizer for the long rains. It measures purchase timing for that season only. B1: 'After the harvest, how hard is it for you to put money aside for the next season's fertilizer?' Not hard / a little hard / very hard. It measures her own judgment of the difficulty, however she keeps the money. C1: 'Think of ten farmers like you in this village. How many of the ten do you think buy their fertilizer before planting time?' A number from 0 to 10. It measures what she believes other farmers do. D1: 'For the next long rains, do you plan to buy your fertilizer before planting time?' No / not sure / yes. It measures a plan for that season. B1 and C1 worry us. Two field officers can do eight interviews a week; neither has done this before."

## The output

```markdown
The script covers all four questions, with the most probing on B1 and C1, the two you were worried about. The plan is two rounds of eight interviews of about 20 minutes, run by your two field officers as a pair. The interviews can show where farmers read a question differently from what you meant; they cannot show that the answers they give are true.

# Cognitive interview script: testing whether people understand the Kakamega baseline fertilizer-timing questions

**Respondents:** smallholder maize farmers in Kakamega County, mostly women with primary schooling; interviews in Kiswahili. The script is shown in English; the translators who produced the Kiswahili questions put the probes into Kiswahili.
**When the follow-up questions (probes) are asked:** after each question, because enumerators will read the survey aloud
**Plan:** 2 rounds of 8 interviews of about 20 minutes, in pairs (one asks, one takes notes); recruit women farmers in a neighboring ward that is outside the survey sample, those with the least schooling first; try the script on two farmers before round 1
**Not tested in this script:** none; four questions at three minutes each fit the interview

## Opening (read aloud)
"Thank you for sitting with us. We are preparing questions that will be asked of many farmers, and we want to find out whether the questions are clear. We are testing the questions, not you. There are no right or wrong answers, and if a question is confusing, the question needs work. I will ask you each question and then ask a little about how you understood it. My colleague will write notes. We will not write your name. May we go on?"
Practice: "How many people ate in your home last night?" Then: "Who did you count?"

## Questions and probes
Read each question exactly as written. If she asks what a question means, say "whatever it means to you" and write down what she asked.

### A1. "Think about the long rains of this year. When did you buy the fertilizer you used at planting?" (options: before the previous harvest / between the harvest and planting / at planting time / I did not buy fertilizer for the long rains)
**Meant to measure:** purchase timing  **A correct reading is:** the timing of the purchase for this year's long rains only
- Recall: "Which season were you thinking about when you answered?"
- Meaning: "What does 'between the harvest and planting' mean to you?"
- If she asks to hear the answers again: "Which of the answers was hard to keep in mind?"
- If she says she bought at more than one time: "How did you decide which answer to give?"

### B1. "After the harvest, how hard is it for you to put money aside for the next season's fertilizer?" (options: not hard / a little hard / very hard) [flagged]
**Meant to measure:** difficulty of putting money aside  **A correct reading is:** her own judgment of the difficulty, whether she keeps the money as cash, mobile money, or grain
- Meaning: "When you hear 'put money aside', what do you think of doing?"
- Meaning: "Can you tell me this question in your own words?"
- Options: "What is the difference, for you, between 'a little hard' and 'very hard'?"
- Judgment: "How did you decide on that answer?"
- Recall: "Which harvest did you have in mind?"
- If she pauses for a long time: "What were you thinking about just then?"

### C1. "Think of ten farmers like you in this village. How many of the ten do you think buy their fertilizer before planting time?" (options: a number from 0 to 10) [flagged]
**Meant to measure:** expectation of others  **A correct reading is:** what she believes other farmers do, not what they ought to do
- Meaning: "Who came to mind when you heard 'farmers like you'?"
- Judgment: "How did you arrive at that number?"
- Recall: "Tell me about the farmers you counted as buying early. How do you know when they buy?"
- Options: "Was it easy or hard to give a number out of ten? What made it hard?"
- If she answers with a word such as "many" and not a number: "What made it hard to give a number?"

### D1. "For the next long rains, do you plan to buy your fertilizer before planting time?" (options: no / not sure / yes)
**Meant to measure:** intention  **A correct reading is:** a plan for the named season, not a general view that buying early is good
- Judgment: "How did you decide on that answer?"
- Meaning: "You said [her answer]. Tell me more about that."
- If she changes her answer: "What made you change your answer?"

## Closing
"Which of these questions was hardest to answer? Was there anything about buying fertilizer that we should have asked and did not? Thank you for your help."

## If a respondent is upset or cannot answer
Do not repeat or reword the probe. Say "That is fine, the question needs work," write "could not answer" and her words, and go to the next question. If she wants to stop, stop, thank her, and note where.

## Note sheet (one per interview)
| Question | Answer given | How the respondent read it, in their words | Problem code | Quote |
|---|---|---|---|---|
| A1 | | | | |
| B1 | | | | |
| C1 | | | | |
| D1 | | | | |

Problem codes: unclear word / wrong reading / cannot recall / options do not fit / uncomfortable / translation / none

## After each round
- Tabulate: questions as rows, interviews as columns, problem codes in the cells.
- Fix a question when: the same problem code appears in two of the eight interviews, or in one if she could not answer at all.
- Retest: every reworded question in round 2, with the same probes.
- Stop when: no question meets the fix rule in a round. Otherwise run a third round.

## What this cannot tell you
- Sixteen interviews can show that a question is misread. They cannot show that every farmer reads it correctly, or that the answers are true: whether farmers who say "yes" to D1 go on to buy early is a question for the survey data.
- If "put money aside" turns out to mean only bank or phone savings, the fault may lie in the Kiswahili wording or in the idea itself. Someone who reads both languages has to judge which.

## Where you could go from here
That's the script.
- Brief the two field officers on reading each question as written and noting, not answering, requests to explain, then run the try-out with two farmers: neither has done this before, and an officer who rephrases B1 to help has tested a different question.
- If round 1 codes "put money aside" as a translation problem, take B1 back through `translate-survey-instrument`: reviewers who know these farmers can judge whether the Kiswahili or the idea is at fault, which this script cannot.
- If C1's number out of ten proves hard to give, rewrite its answer options with `draft-survey-items`: what she believes other farmers do can stay; only the way of answering changes.
I'd lean toward the briefing and try-out, because it is the cheapest way to catch a problem in the script before it costs you a round.
Questions you could ask next: "What do we do if 'put money aside' turns out to mean only bank or phone savings?" · "How do we fit a third round into the baseline timeline?"
```
