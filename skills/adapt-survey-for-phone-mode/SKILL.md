---
name: adapt-survey-for-phone-mode
description: >-
  Use when a questionnaire written for face-to-face interviews has to be asked
  by voice call: "can we do the endline by phone?", "how do we ask the
  showcard questions on a call?", "how long can a phone survey be?". Cuts the
  instrument to a call length, rewrites what respondents had to see, and sets
  the call rules, who the calls will miss, and a check on whether answers
  differ by phone. Do not use when the questions are not written yet; use
  draft-survey-items. Not for testing the phone version with respondents; use
  draft-cognitive-interview-script.
license: CC-BY-4.0
metadata:
  title: Move a face-to-face survey to the phone
  type: atomic
  stage: measure
  version: "0.2.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  tested_in: beyond-western-holds
  tags: "measurement, survey-design, quantitative"
  consumes: "survey-items"
  produces: "survey-items"
---

## What it does

Converts a face-to-face questionnaire into a version that can be asked by voice call.

**What this adds:** cuts by decision to a stated call length and lists what was dropped; converts every item that relied on something seen; compares who the phone numbers reach with who the survey is about; gates sensitive items on a privacy check; and treats a change from a face-to-face round as possibly caused by the phone until a planned comparison says otherwise.

## When to use it

### Use it when
- A face-to-face questionnaire must be fielded by phone ("can we do the endline by phone?")
- A questionnaire uses showcards, ladders, or pictures that cannot be shown on a call
- Someone asks how long a phone survey can be, or whom the calls will miss

### Do not use it when
- The questions are not written yet; use `draft-survey-items`
- The questionnaire has to go into another language; use `translate-survey-instrument`
- The phone version exists and needs testing with respondents; use `draft-cognitive-interview-script`
- The question is how many numbers to call; use `estimate-sample-size`

## Before you start

Ask these before producing anything. Do not ask anything the user has already answered.

1. **Required.** The questionnaire as asked face to face, with its showcards, and its length in minutes.
2. **Required.** A live call (an interviewer phones) or IVR (recorded questions answered on the keypad), and why phone.
3. **Required.** Where the phone numbers come from, and who owns or shares those phones, by sex.
4. **Required.** The decision the survey informs, and the items it cannot do without.
5. Optional. Which items are sensitive; whether some face-to-face interviews are possible.

If 1 to 4 are missing, ask and stop. If 5 is missing, treat items on health, violence, sex, money, and politics as sensitive, and mark the face-to-face comparison "not confirmed".

## What it draws on

- Dabalen, A., Etang, A., Hoogeveen, J., Mushi, E., Schipper, Y., & von Engelhardt, J. (2016). *Mobile Phone Panel Surveys in Developing Countries: A Practical Guide for Microdata Collection*. World Bank. https://doi.org/10.1596/978-1-4648-0904-0 Supports: short questions with few answer categories; the 15 to 30 minute call, which it calls common practice, not evidence.
- Gibson, M., & Kopper, S. (2021). *Resources for conducting remote surveys*. Abdul Latif Jameel Poverty Action Lab (J-PAL). https://www.povertyactionlab.org/resource/resources-conducting-remote-surveys Supports: the 30-minute ceiling; logging every call attempt.
- Krosnick, J. A., & Presser, S. (2010). Question and questionnaire design. In P. V. Marsden & J. D. Wright (Eds.), *Handbook of Survey Research* (2nd ed., pp. 263–313). Emerald. https://web.stanford.edu/dept/communication/faculty/krosnick/docs/2010/2010%20Handbook%20of%20Survey%20Research.pdf Supports: asking a scale as two questions when read aloud.
- Greenleaf, A. R., Diakabana, H., & Lau, C. (2026). Computer-assisted mobile phone interviews in low- and middle-income countries through a total survey error framework. *Public Opinion Quarterly*, 90(3), 878–910. https://doi.org/10.1093/poq/nfag023 Supports: steps 5 and 7.

**Where the evidence comes from:** Almost all from low- and middle-income countries. A review of 36 studies in 21 of them found live-call samples under-represent women and older, rural, poorer, and less educated people. Simple yes-or-no questions were answered well, but a consumption module in Ethiopia returned 23% lower spending by phone; check locally who owns each phone.

**Replication status:** Replicated for who is missed; mixed for whether answers differ by phone.

## How to do it

1. **Cut by decision.** Keep the items the decision needs; mark the rest "drop" or "later call". Target 30 minutes or less for a live call, less for IVR. Reading faster is not a cut.
2. **Convert every item that relied on something seen.** Ask a rating scale in two steps, direction then strength ("satisfied or dissatisfied?", then "very or somewhat?"), because a long scale is hard to hold when read aloud. Describe both ends of a ladder in words. Turn a card list into yes-or-no questions. Record each item's old and new format, and flag it for testing aloud.
3. **Rewrite instructions for the ear:** short sentences, choices repeated in every question; for IVR, one idea and few choices per prompt.
4. **Write the call rules:** spoken consent; attempts spread over times and days; call-backs; when a number is retired; the airtime payment; a log of every attempt with day, time, and who answered.
5. **Compare who the numbers reach with who the survey is about.** State who owns or shares the phones and who will be missing. Ask for the intended respondent by name; never interview whoever answers.
6. **Gate sensitive items.** Before each, ask whether the respondent is alone and can speak freely; call back if not. On a shared phone, drop an item whose answer could harm the respondent if overheard.
7. **Plan the mode check.** A change since a face-to-face round may come from the phone. Interview a random subsample face to face on the core items and name the difference that would change the conclusion, or state what cannot be claimed without it.

See `references/worked-example.md` for a complete run.

## Output template

```markdown
# Phone version: <survey name>

**Mode:** <live call / IVR>  **Face-to-face length:** <minutes>  **Target call length:** <minutes>
**Why phone:** <cost / access / safety / timing>
**Decision the survey informs:** <...>

## 1. Items kept and dropped
| Item or module | Decision it feeds | Keep / drop / later call | Why |
|---|---|---|---|
| <...> | <...> | <...> | <...> |

## 2. Converted items
| Item | Face-to-face format | Phone format | Words as spoken |
|---|---|---|---|
| <...> | <showcard, 5 points> | <two steps: direction, then strength> | <exact words> |

## 3. Consent and spoken instructions
<consent as read; how the respondent is identified; the instruction that precedes the questions>

## 4. Call rules
- **Attempts:** <number, spread over which times and days>
- **Call-backs:** <rule>
- **Number retired when:** <rule>
- **Interviewer language:** <...>
- **Airtime payment:** <amount; when sent>
- **Logged for every attempt:** <day, time, outcome, who answered, language>

## 5. Who the calls will reach
- **Whose phones:** <own / shared / someone else's, by sex and wealth where known>
- **Who will be missing:** <...>
- **How the intended respondent is asked for:** <...>

## 6. Sensitive items
| Item | Keep behind the privacy check / drop / refer | Why |
|---|---|---|
| <...> | <...> | <...> |

**Privacy check as spoken:** <...>

## 7. Mode check
<the face-to-face subsample and how it is drawn; items compared; the difference that would change the conclusion; or what cannot be claimed without it>

## 8. Converted items to test aloud
<items, and what to listen for>

## What to check before relying on this
- <the group the numbers are most likely to miss>
- <the converted item most likely to be answered differently by phone>
```

## Where it goes wrong

- **Weights offered as the fix.** Reweighting a phone sample to match the population mostly failed to remove the bias in four African countries. Report who is missing anyway.
- **Long modules moved intact.** A detailed consumption module or a household roster tires people on a call. Collect it face to face or leave it out.
- **IVR treated as a cheap live call.** In Nigeria the response rate was 3% for IVR against 15% for live calls.

## When to bring in a specialist

Tell the user to consult, before fielding:
- An ethics reviewer and a survey methodologist with phone experience, when the survey asks about HIV status, partner violence, or illegal income and phones are shared: they decide whether to ask by phone at all
- A sampling statistician, when the people the program is for are those least likely to have a phone
- Someone who has fielded IVR there, when IVR is planned for respondents with little schooling and no pilot has run

Bring them: the source of the numbers, who owns the phones, the sensitive items, the call rules, and the mode check.
