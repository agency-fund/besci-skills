# Worked example: a savings-group endline moved to live calls in Wakiso, Uganda

A full run of the skill on a realistic case, showing the output it should produce. The case is illustrative, not a real program.

## The request

"Endline for a savings-group program with 900 peri-urban workers in Wakiso, Uganda. The result decides whether we extend the program to 40 more groups. The baseline was 50 minutes face to face: savings balance, deposits in the last month, group attendance, a 10-rung ladder for financial security, a 5-point satisfaction showcard, a card listing eight uses of savings, a 14-item household asset list, a spending module, and a question on whether anyone at home takes the respondent's savings. Our travel budget was cut, so the endline has to be live calls by our own enumerators, in Luganda and English. We have the numbers respondents gave at baseline: 85% of men and 70% of women said the phone was their own; the rest gave a spouse's or relative's number. The items we cannot do without are the balance, deposits, attendance, and the ladder. We can pay airtime and can manage about 100 face-to-face interviews for comparison. Convert it."

## The output

```markdown
# Phone version: savings-group endline, Wakiso

**Mode:** live call  **Face-to-face length:** 50 minutes  **Target call length:** 20 minutes
**Why phone:** cost; the travel budget was cut
**Decision the survey informs:** whether to extend the program to 40 more groups

## 1. Items kept and dropped
| Item or module | Decision it feeds | Keep / drop / later call | Why |
|---|---|---|---|
| Savings balance | Extend or not | Keep | Core outcome |
| Deposits in the last month | Extend or not | Keep | Core outcome |
| Group attendance in the last month | Extend or not | Keep | Core outcome |
| Financial security ladder | Extend or not | Keep, converted | Core outcome |
| Satisfaction with the group | How to run new groups | Keep, converted | One item, about a minute |
| Uses of savings (card of eight) | How to run new groups | Keep four uses, converted | Eight yes-or-no questions is too long; the four most named at baseline stay |
| Household asset list, 14 items | None at endline | Drop | Collected at baseline; assets change slowly |
| Spending module | None | Drop | Long modules tire people on a call and were not needed for the decision |
| Anyone at home takes your savings | How to run new groups | See section 6 | Sensitive on a shared phone |

## 2. Converted items
| Item | Face-to-face format | Phone format | Words as spoken |
|---|---|---|---|
| Satisfaction | Showcard, 5 points | Two steps: direction, then strength | "Overall, are you satisfied or dissatisfied with your savings group, or neither?" If satisfied or dissatisfied: "Is that very or somewhat?" |
| Financial security | Picture of a ladder, 10 rungs | Number from 1 to 10, both ends described | "Think of a ladder with ten steps. Step one means you could not find 50,000 shillings for an emergency at all. Step ten means you could find it easily. Which step are you on today? Tell me a number from one to ten." |
| Uses of savings | Card, pick all that apply | Four yes-or-no questions | "In the last month, did you use savings from the group for school fees? ... for your business? ... for a medical cost? ... for food?" |
| Deposits | Count written down by the enumerator from the passbook | Spoken count | "Since the start of last month, how many times did you put money into the group? If you have your passbook near you, please look." |

## 3. Consent and spoken instructions
"My name is [name], calling from [organization]. You answered our questions about your savings group in [month]. Am I speaking with [respondent's name]? We would like to ask you some questions again. It takes about 20 minutes. You can stop at any time, and stopping changes nothing about your place in the group. We will send 3,000 shillings of airtime to this number afterward to thank you for your time. Do you agree to take part?"

"For each question I will read the answers you can choose from. Please wait until I have read them all, and ask me to repeat anything."

## 4. Call rules
- **Attempts:** five per number, on at least three different days, covering a weekday evening, a midday, and a Sunday afternoon
- **Call-backs:** if the respondent names a better time, call then; that call starts a new set of five
- **Number retired when:** five attempts fail, or the person who answers says the respondent no longer uses the number and gives no other
- **Interviewer language:** the language recorded at baseline, Luganda or English; the respondent may switch
- **Airtime payment:** 3,000 shillings, sent within a day of the call, including for interviews stopped part-way
- **Logged for every attempt:** day, time, outcome, who answered (respondent, spouse, other adult, child), language

## 5. Who the calls will reach
- **Whose phones:** the respondent's own for 85% of men and 70% of women at baseline. The other 30% of women gave a spouse's or relative's number.
- **Who will be missing:** members who changed numbers since baseline, and, more often than others, women reached only through someone else's phone. If their call-backs fail more often, the endline will describe women who own phones better than women who do not.
- **How the intended respondent is asked for:** by name. If someone else answers, the enumerator says only that the call is about the savings group, asks when the respondent can be reached, and logs who answered. Nobody else is interviewed in her place.

## 6. Sensitive items
| Item | Keep behind the privacy check / drop / refer | Why |
|---|---|---|
| Savings balance | Keep behind the privacy check | A balance said aloud near a spouse or relative can be claimed |
| Anyone at home takes your savings | Drop when the number is not the respondent's own; keep behind the privacy check otherwise | On a spouse's phone the answer could be overheard by the person it is about |

**Privacy check as spoken:** "The next questions are about your own money. Are you somewhere you can speak without others hearing? If not, I can call back at a time you choose."

## 7. Mode check
Draw 100 respondents at random from the baseline list and interview them face to face with the phone wording of the four core items; call the rest. Compare the two groups on the share who deposited last month, attendance, and the ladder. With 100 interviews only a large gap, roughly 15 percentage points on a yes-or-no item, can be told apart from chance. A gap that large on deposits means the baseline-to-endline change is not reported as a program result. A smaller gap cannot be ruled out, and the report says so.

## 8. Converted items to test aloud
- The ladder: listen for respondents who answer "five" at once without hearing both ends
- Satisfaction in two steps: listen for respondents who answer "very" to the first question
- Deposits: listen for whether respondents count the group's weekly meeting or only the times they paid in

## What to check before relying on this
- Whether the women reached through someone else's phone are reached at all. Compare completed interviews for own-phone and other-phone numbers after the first week.
- Whether the ladder is answered differently by ear than by picture. It is the core item changed most by the move to the phone.
```
