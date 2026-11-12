# Worked example: reminders for monthly immunization camps in Udaipur district, India

A full run of the skill on a realistic case, showing the output it should produce. The case is illustrative, not a real program.

## The request

"We support monthly immunization camps in 48 villages in Udaipur district, Rajasthan. Each village's camp runs on a fixed day each month, 9am to 2pm, at the anganwadi center. Our register holds every enrolled child's next due dose and the camp date. We ran exit interviews at 12 camps and surveyed 600 mothers: 64% of mothers whose child missed a dose said they did not know the camp was that day or that week. Vaccine stock has been reliable for two years, the vaccines are free, and nobody mentioned distrust of the nurse. About 60% of households have a phone, usually held by the husband. Many mothers cannot read a Hindi text. The ASHA, the village health worker, visits each hamlet once a week. Our call center can place voice calls in Mewari. Some mothers told us at enrollment that they want all doses done by the first birthday. Design the reminder schedule."

## The output

```markdown
Each mother gets a voice call in Mewari three days before her village's camp, a word from the ASHA on her round that week, and one call after a missed camp: three contacts a month at most. Calls reach only the 60% of households with a phone, usually through the husband, so the ASHA visits households without one first, and the calls are not enough alone. I haven't promised an effect for Udaipur.

# Reminder schedule

**Behavior:** Mothers of enrolled children under two in the 48 villages bring the child to the monthly camp at the anganwadi center in the month the next dose is due.
**Confirmed barrier:** Forgetting the camp day. 64% of mothers whose child missed a dose said they did not know the camp was that day or that week (exit interviews at 12 camps, survey of 600 mothers). Supply, cost, and trust are ruled out: stock has been reliable for two years, vaccines are free, and no distrust was reported.
**Due dates:** Recurring, one fixed camp day a month per village, 9am to 2pm. The action counts only on that day; a missed camp means a month's delay. The register holds each child's due dose and the camp date.

## The reminders
| # | When, relative to the due date | Channel | Must name | Stops when |
|---|---|---|---|---|
| 1 | 3 days before the camp | Voice call in Mewari to the household phone, asking for the mother | The child's name, the dose due, the camp day and date, the anganwadi center, the hours; "all doses by the first birthday" where the mother said so at enrollment | Dose recorded; household opts out; ceiling reached |
| 2 | On the ASHA's hamlet round in the week of the camp | ASHA in person, to the mother | The same | Dose recorded; mother declines |
| 3 | The day after a missed camp | Voice call in Mewari | That the dose is still due, and the date of the next camp | Dose recorded; household opts out |

## Limits
- **Ceiling:** Two contacts before each camp and one after a miss, three a month at most. After three missed camps in a row the calls stop and the ASHA asks the mother why, because forgetting is then unlikely to be the reason.
- **After a missed date:** One call naming the next camp date.
- **Opt-out:** Say "stop the calls" on any call, or tell the ASHA. It takes effect that month and costs nothing.

## Channel
- **Why this channel:** Many mothers cannot read a Hindi text, so the call is spoken, in Mewari. The phone is usually the husband's, so the call asks for the mother and otherwise leaves the date with whoever answers.
- **Who it does not reach:** The roughly 40% of households with no phone. The ASHA's visit is their only reminder, so she visits those households first.

## Privacy
- **What a message reveals to someone else:** That a named child has a routine vaccine due on a given day.
- **How that is handled:** The call names the child, the dose, the day, and the place, and nothing else about the family's health. No privacy review is needed for a routine childhood vaccine.

## Are reminders enough alone?
No. A call reaches about 60% of households, often through the husband. The ASHA's visit sits beside the calls so that every mother hears the date from someone she knows. No incentive is added, because no cost barrier was found.

## Monitoring
- **Measures:** Each month, from the call log and the register: calls answered and by whom, opt-outs, and the share of due children vaccinated at the camp.
- **Review if:** Fewer than half of calls are answered, opt-outs pass 10% of households, or the share of due children vaccinated falls for two months running. The program lead and the ASHA supervisor review.

## What the evidence supports
That reminders before a due date raise timely childhood immunization. A review of 18 studies in 11 low- and middle-income countries found higher coverage and timeliness, more so with more than two reminders. In Haryana, India, text reminders taken separately disappointed, and reminders paired with local ambassadors were the most cost-effective combination, which is why the ASHA stays in this schedule. No effect size is promised for Udaipur.

## What to check before relying on this
- Whether "I did not know the day" is the real reason or a polite one for distance or a lost day's wage. Ask 15 mothers on a camp day.
- Whether the call reaches the mother or stops with the husband. Test it with 20 households before the first full month.
- Whether the register's due-dose data is current; a call about the wrong dose costs more trust than no call.
- Whether the ASHA's round falls before the camp in every hamlet.

## Where you could go from here
That's the reminder schedule.
- Test the call with 20 households using `plan-prototype-test`: whether it reaches the mother or stops with the husband decides whether the calls are worth their cost.
- Ask 15 mothers on a camp day why their child last missed a dose: if "I didn't know the day" is standing in for distance or a lost day's wage, reminders won't fix it, and `select-intervention-levers` would fit better.
- Check the register's due-dose data at a few camps before the first call: a call about the wrong dose costs more trust than no call.
I'd lean toward the 20-household test, because it has to happen before the first full month anyway, and the camp-day conversations can run in the same week.
Questions you could ask next: "What should the call say if the husband answers?" · "How should the ASHA order her visits to households without a phone?"
```
