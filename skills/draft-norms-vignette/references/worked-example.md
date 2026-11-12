# Worked example: a vignette on iron-folate tablets in pregnancy, rural Malawi

A full run of the skill on a realistic case, showing the output it should produce. The case is illustrative, not a real program.

## The request

"Practice: pregnant women enrolled at four rural health centers in Mchinji district, Malawi, take one iron-folate tablet every day from the first antenatal visit. We interviewed 28 pregnant women alone. Most said the tablets are good for the baby, yet many stop. When we asked whose opinion matters, they named the husband and his mother; most said they would take the tablets if those two told them to, and most believe those two are against 'hospital medicine' in pregnancy. Several also said they watch what other pregnant women in the village do. We want to test this in our baseline survey before designing anything. Respondents: about 600 pregnant women aged 18 to 40 at antenatal visits, most with primary schooling, each interviewed alone in a private room, in Chichewa, by a female surveyor who reads the questions aloud from a tablet computer. Taking the tablets is not illegal or shameful here. Please write the vignette."

## The output

```markdown
The story asks each woman to predict whether Chikondi, a pregnant woman like her in another district, takes her tablet this morning. Its four versions change only what other pregnant women in Chikondi's village do and what her husband and his mother think she should do. The answers will show what respondents expect of someone like them, not whether they take the tablets themselves.

# Survey story (vignette): daily iron-folate tablets in pregnancy

**Practice and moment of decision:** A pregnant woman given a month's supply of iron-folate tablets at her first antenatal visit decides each morning at home whether to take one.
**Why expectations are thought to matter:** In 28 interviews most women said the tablets are good for the baby, yet many stop. Most said they would take them if their husband or his mother told them to, and most believe those two are against "hospital medicine" in pregnancy.
**Whose behavior and approval the story names:** Empirical cue: other pregnant women in her village. Normative cue: her husband and his mother.
**Respondents and how they are surveyed:** About 600 pregnant women aged 18 to 40 at antenatal visits; most with primary schooling; Chichewa; read aloud by a female surveyor to one respondent at a time in a private room.
**Sensitivity:** None stated. Wording given in full.

## Base story (the same in every version)
"Chikondi is 24 years old and four months pregnant with her second child. She lives in a farming village in Kasungu district with her husband and his mother. They grow maize and groundnuts and go to church on Sundays, like most families there. At her first visit to the health center, the nurse gave her a packet of tablets for her blood and told her to take one every morning until the baby is born. The packet is in the house. This morning Chikondi is deciding whether to take a tablet."

## The sentences that change (cues)
| | Version A | Version B |
|---|---|---|
| Empirical: what others do | "Most pregnant women in Chikondi's village take the tablets every day." | "Most pregnant women in Chikondi's village do not take the tablets." |
| Normative: what others approve | "Chikondi's husband and his mother think a pregnant woman should take the tablets from the health center." | "Chikondi's husband and his mother think a pregnant woman should not take the tablets from the health center." |

## Versions
1. Base story + empirical A + normative A
2. Base story + empirical A + normative B
3. Base story + empirical B + normative A
4. Base story + empirical B + normative B

## Questions after the story
1. **What she will do:** "What do you think Chikondi will do this morning?" Answers: take the tablet; not take the tablet; cannot say
2. **What might lead her to, and not to (open):** "What might lead Chikondi to take the tablet? What might lead her not to take it?" The surveyor writes the answer in the respondent's words.
3. **Whether she should, in the respondent's view:** "Do you yourself think Chikondi should take the tablets every day?" Answers: yes; no; it is up to her
4. **Check that the cue was heard:** "In the story, what do most pregnant women in Chikondi's village do about the tablets?" Answers: take them; do not take them; do not remember. "And what do her husband and his mother think she should do?" Answers: take them; not take them; do not remember

## Random assignment
One version for each respondent. The tablet computer draws the version from a schedule made before fieldwork, with the four versions in equal numbers for each surveyor. The version is stored with the interview. The surveyor reads the version shown and cannot choose it.

## How the answers will be read
- **Outcome:** share answering "take the tablet" to question 1, by version
- **What others do:** versions 1 and 2 against 3 and 4
- **What others approve:** versions 1 and 3 against 2 and 4
- **What each result would mean:** If the share rises only when most pregnant women in the village take the tablets, what other women do is enough to move a woman: a descriptive norm. If it rises when the husband and his mother approve, their expectation matters as well: a social norm. If neither moves it and most respondents say she should take them, something other than expectations is stopping women, such as side effects, supply, or forgetting. If neither moves it and many respondents fail question 4, the cues did not register and the story needs rewriting.
- **Sample:** about 150 respondents per version, so 300 on each side of each comparison. Whether that is enough for the size of shift the team cares about has not been checked.

## What to ask when trying out the story
- Ask what "most pregnant women do not take the tablets" told the respondent: something about what women do, or something about whether the tablets are safe.
- Ask "when you answered, were you thinking of Chikondi or of yourself?", and whether Chikondi's home seemed like the respondent's own.

## Where you could go from here
That's the vignette.
- Have the Chichewa version made with `translate-survey-instrument`: the four versions must stay identical except for the cue sentences, in Chichewa as in English, and "hospital medicine" and "tablets for her blood" need words these women use.
- Try the story with a few pregnant women using `draft-cognitive-interview-script`: the riskiest point is "most pregnant women do not take the tablets" being heard as "the tablets are unsafe", which would change what the comparison on what others do means.
- Check the 150 per version with `estimate-sample-size`: nobody has yet asked whether 300 on each side can detect a shift big enough to change what you design.
I'd lean toward the Chichewa version and the try-out together, because the try-out is what tells you how the "do not take" cue is heard, and it has to be heard in Chichewa to tell you that.
Questions you could ask next: "What would we design differently if only the husband-and-mother cue moves the answers?" · "Can we repeat this story after the program to see whether expectations changed?"
```
