# Worked example: missed HIV treatment doses at six clinics in Kisumu, Kenya

A full run of the skill on a realistic case, showing the output it should produce. The case is illustrative, not a real program.

## The request

"We run an SMS adherence program for people on antiretroviral treatment (ARVs) at six clinics in Kisumu, Kenya. At every visit the nurse asks 'did you miss any doses this week?' and 95% say no. Pharmacy records show about one patient in four collecting a refill late, so nobody believes the 95%. We want the real share who missed doses on two or more days in the past 7 days. Interviews are face to face in Dholuo or Swahili, on tablets, by our own enumerators, not clinic staff. Respondents are adults, many with primary schooling only. We can afford about 1,800 interviews at endline, and the estimate is for the whole sample, not by clinic. We will keep a direct question too. Can you design the list experiment?"

## The output

```markdown
# List experiment design: missed ARV doses

**Behavior:** Adults on ARVs at the six clinics; did not take their ARVs on two or more days; past 7 days
**Why people would hide it here:** Patients are told at every visit that missing doses is dangerous, and they connect any survey about treatment with the clinic that supplies it.
**Respondents and mode:** Adults, many with primary schooling only; Dholuo or Swahili; face to face with a program enumerator, answers entered on a tablet
**Affordable sample:** 1,800  **Estimate needed for:** everyone

## Go or no-go
- **Plausible under-reporting:** More than 10 percentage points. 5% admit a missed dose to the nurse, and about 25% collect refills late. A late refill is not the same as two missed days, so this is a rough guide.
- **What this sample can show:** With 1,800 respondents the list is the better estimate if under-reporting is above roughly 4 to 5.5 points, which looks likely. The list estimate will be imprecise: expect a margin of about 8 or 9 points either way, to be confirmed by a sample-size calculation. The sample cannot show reliably that the list and direct figures differ unless the gap is well above 10 points, and it cannot compare clinics.
- **Decision:** Go on conditions: the counting test with a few respondents passes, and the estimate is reported for the whole sample only.

## Statements
**Sensitive statement (long list only):** "In the past 7 days, there were two or more days when I did not take my ARVs."
**Control statements (both lists):**
1. "In the past 7 days, I ate fish." (expected to be true for most)
2. "In the past 7 days, I traveled outside Kisumu County." (few)
3. "In the past 7 days, I worked for pay on five or more days." (about half)
4. "In the past 7 days, I spent a whole day resting at home." (about a third)

**Why few respondents will count none or all:** Eating fish is true for most people here, so few will count zero. Travel outside the county is rare, so few will count four. Working five days and resting a whole day at home pull against each other, which keeps most counts at one, two, or three. These shares are guesses until the test with respondents.
**Order in the long list:** 1, 3, the sensitive statement, 4, 2.

## Random assignment
Individual respondents, half to each list. The tablet assigns the list from a schedule made before fieldwork, split evenly within each enumerator. The list heard is stored with the interview. The enumerator sees only the statements to read.

## Script
- **Instruction as read:** "I am going to read some statements. Please do not tell me which ones are true for you. I only want to know how many are true. Here is a card and a pencil. Make one mark for each statement that is true for you, and keep the card where I cannot see it. At the end, tell me the number of marks. The card is yours to keep."
- **Practice list:** "I have a brother. I was born in Kisumu. I have been to Nairobi. I own a bicycle." The enumerator checks that the respondent answers with a number, repeats the instruction once if not, and records that a repeat was needed.
- **Private way to count:** Marks on a blank card that the respondent keeps.
- **If a respondent names a statement:** The enumerator says "Thank you. Please tell me only the number", reads the whole list again, and records that the instruction was repeated. Nothing is recorded about which statement was named.

## Direct question
"In the past 7 days, were there two or more days when you did not take your ARVs?" asked of everyone by the enumerator, after the list and at least five unrelated questions.

## Checks on the data
- **Short-list group counting none or all:** concern if more than one respondent in ten counts zero or four
- **Design-effect test:** the test in the R package `list`, run on the counts from the two lists
- **List estimate minus direct estimate:** reported with its confidence interval, which will be wide

## Reporting rule
If the checks pass and the list estimate is above the direct one, report the list estimate as primary, with its interval and the direct figure beside it. If the design-effect test fails, if more than one in ten short-list respondents count zero or four, or if the list estimate is below the direct one, report the direct figure as primary and say the list did not work.

## For the sample-size calculation
Expected share 20 to 30%, the team's guess from refill records. The spread of the short-list count, to be taken from the test with respondents. No groups to compare.

## What to check before relying on this
- Whether "ate fish" is close to universal near the lake, which would push every count up, and whether "worked for pay" embarrasses respondents without work.
- Whether respondents with primary schooling can keep marks for five statements read aloud. Test with eight to ten respondents before fielding.
```
