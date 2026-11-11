# Worked example: fertilizer timing among maize farmers in western Kenya

A full run of the skill on a realistic case, showing the output it should produce. The case is illustrative, not a real program.

## The request

"We need baseline questions for a pilot that encourages smallholder maize farmers in Kakamega County to buy fertilizer before planting. Four things to measure. (A) Purchase timing: when the farmer bought the fertilizer used at planting in the last long rains. (B) Difficulty of putting money aside: how hard the farmer finds it to hold harvest money for fertilizer. (C) Expectation of others: how many similar farmers in the village the respondent believes buy before planting. (D) Intention: whether the farmer plans to buy before planting next season. Respondents are mostly women with primary schooling. Enumerators read the questions aloud at the farmer's home; translation into Kiswahili and Luhya comes later. We have room for 8 questions. From earlier interviews we know harvest money mostly goes to school fees, food, and relatives who ask for help."

## The output

```markdown
# Draft survey questions: Kakamega baseline, fertilizer-timing block

**Respondents:** smallholder maize farmers in Kakamega County, mostly women, primary schooling; drafted in English for later translation
**How they answer:** read aloud by an interviewer, at home
**Length budget:** 8 questions

## Questions by construct

### (A) Purchase timing: when the fertilizer used at planting in the last long rains was bought
**A1.** Think about the long rains of this year. When did you buy the fertilizer you used at planting?
- Options: before the previous harvest / between the harvest and planting / at planting time / I did not buy fertilizer for the long rains
- A correct reading is: the timing of the purchase for this year's long rains only, not what the farmer usually does
- Notes: report of what happened; season named; the last option keeps a non-buyer from being forced into a timing

**A2.** (If she bought) Did you buy all of it at one time, or in parts?
- Options: all at one time / in parts
- A correct reading is: whether the purchase for that season was split
- Notes: report of what happened; asked separately so that A1 holds one idea

### (B) Difficulty of putting money aside: how hard the farmer finds it to hold harvest money for fertilizer
**B1.** After the harvest, how hard is it for you to put money aside for the next season's fertilizer?
- Options: not hard at all / a little hard / somewhat hard / very hard / extremely hard
- A correct reading is: her own judgment of the difficulty, whatever the reason, and whether the money is kept as cash, mobile money, or grain
- Notes: rating of the thing itself; replaces "I find it hard to save for fertilizer: agree or disagree"; five options, because these respondents have primary schooling

**B2.** (If any answer but "not hard at all") What is the biggest reason it is hard?
- Options: the money goes to school fees / the money goes to food / other people ask me for the money / another reason (write it down)
- A correct reading is: the one main competing use of harvest money
- Notes: options from the team's earlier interviews; "another reason" recorded word for word

### (C) Expectation of others: how many similar farmers the respondent believes buy before planting
**C1.** Think of ten farmers like you in this village. How many of the ten do you think buy their fertilizer before planting time?
- Options: a number from 0 to 10
- A correct reading is: what she believes other farmers do, not whether she approves of it
- Notes: count out of ten in place of a percentage; "farmers like you" sets who to think of

### (D) Intention: whether the farmer plans to buy before planting next season
**D1.** For the next long rains, do you plan to buy your fertilizer before planting time?
- Options: no / not sure / yes
- A correct reading is: a plan for the named season, not a general view of early buying
- Notes: season named; "not sure" kept because many farmers have not decided

**D2.** (If yes) When do you plan to buy it?
- Options: right after this harvest / between the harvest and planting
- A correct reading is: the planned timing for the named season
- Notes: asked only of farmers who plan to buy early; the two periods match A1 so the answers can be set side by side

## Order
| Position | Question | Earlier question that could shape the answer |
|---|---|---|
| 1 | A1 | none |
| 2 | A2 | none |
| 3 | B1 | A1: a farmer who reported buying late may rate the difficulty higher to explain it |
| 4 | B2 | none |
| 5 | D1 | A1: a late buyer may state an early plan to look better |
| 6 | D2 | none |
| 7 | C1 | none; placed last so that thinking about other farmers does not color her own plan |

## Read-aloud script
"Now I will ask about the fertilizer you used for the long rains this year. There are no right or wrong answers."
A1. "When did you buy the fertilizer you used at planting? Was it before the previous harvest, between the harvest and planting, at planting time, or did you not buy fertilizer for the long rains?"
A2. [Ask only if she bought.] "Did you buy all of it at one time, or in parts?"
B1. "After the harvest, how hard is it for you to put money aside for the next season's fertilizer? Not hard at all, a little hard, somewhat hard, very hard, or extremely hard?"
B2. [Ask only if the answer was not "not hard at all".] "What is the biggest reason it is hard? The money goes to school fees, the money goes to food, other people ask you for the money, or another reason?" [If another reason, write her words.]
D1. "For the next long rains, do you plan to buy your fertilizer before planting time? No, not sure, or yes?"
D2. [Ask only if yes.] "When do you plan to buy it? Right after this harvest, or between the harvest and planting?"
C1. "Now think of ten farmers like you in this village. How many of the ten do you think buy their fertilizer before planting time? Give me a number from zero to ten."

## Design check
| Rule | Pass? | Rewritten or dropped |
|---|---|---|
| One idea per question | yes | A2 and B2 split from A1 and B1 |
| Asks about the thing itself, not agreement with a statement | yes | B1 rewritten from an agree/disagree statement |
| Every option in words; five for a rating, plus a three-option version where respondents cannot read | yes | B1 has five; D1 is a plan, not a rating; A1 and B2 are lists of answers |
| No "not" and no reversed question | yes | none; "did you not buy" in A1 is an answer option, not a negated question |
| Time period named | yes | A1 and D1 name the season |
| Plain, neutral words that do not push toward an answer | yes | none |
| Options cover every answer and do not overlap | yes | "another reason" added to B2 |
| No direct question on a stigmatized or illegal behavior | yes | none of the four constructs is one |

## Not written here
None.

## Untested
These are draft questions. No respondent has yet been asked what they mean.
- B1: "put money aside" may be heard as saving in a bank or on a phone only, so a farmer who keeps cash or grain back would answer "very hard".
- C1: a count out of ten of other people is an unfamiliar task for many respondents, and some will answer about what farmers should do.
- B1 has five spoken options, the most a listener is asked to hold in this block; the pretest should check that farmers can tell "a little hard" from "somewhat hard".
```
