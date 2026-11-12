# Worked example: home-visit reminders for iron-folate tablets in Malawi

A full run of the skill on a realistic case, showing the output it should produce. The case is illustrative, not a real program.

## The request

"We ran a cluster randomized trial of community health worker home-visit reminders for antenatal iron-folate adherence in 24 health centers in Mchinji and Dedza, Malawi (12 per arm): 1,600 women enrolled at treatment centers over 10 months in 2025. Effect from our pre-specified model: adherence (pill count of 80% or more at 32 weeks) was 43% against 31%, +12 percentage points (95% CI 5 to 19). Costs: 48 health workers spent about 4 hours a week for 40 weeks; they are government-stipended, so we did not pay them, and the local wage is about $0.75 an hour. Four supervisors worked 8 hours a month for 10 months at $2.50 an hour. A 2-day training for 52 people cost $2,600. We bought 48 bicycles at $90 each, with a 3-year life. Printed adherence cards cost $0.20 each; phone credit was $2 per health worker per month. Monthly meetings used clinic rooms for free (about $10 a meeting, at the 12 treatment centers). Data entry cost $600, and the endline survey and pill counts for the trial cost $9,000. No cash or in-kind transfers. The ministry wants to compare us with an SMS-only reminder program in another district, per additional adherent woman. Program perspective; USD 2025 at the average market rate. Each woman had about 10 visits of 20 minutes; value her time at $0.50 an hour if you need it."

## The output

```markdown
Each additional woman taking her tablets cost about $70 in delivery costs, and anywhere from $44 to $168 across the trial's confidence interval. The largest cost is health-worker time the program did not pay for; with that and the donated rooms at zero, the figure halves to $33.75. Before it goes beside the SMS program, keep in mind that the two measured adherence differently (pill counts here, self-report there), so the comparison is not like for like.

# What health-worker home visits in Malawi cost per additional woman taking her iron-folate tablets

**Program:** Health-worker home visits reminding pregnant women to take daily iron-folate tablets, about 10 visits per woman; 1,600 women at 12 health centers in Mchinji and Dedza, Malawi; 10 months of 2025
**Effect:** adherence (pill count of 80% or more at 32 weeks), +12 percentage points (95% CI 5 to 19), 43% against 31%; applies to 1,600 women; source: this program's evaluation. Additional adherent women: 0.12 × 1,600 = 192 (80 to 304 at the confidence bounds)
**Whose costs count (perspective):** implementer, because the ministry's comparison is built from implementer costs; the society perspective is in the sensitivity table
**Currency and year:** USD, 2025 prices; kwacha converted at the 2025 average market rate; **discount rate:** none, because all costs fall within one year
**Compared with:** SMS-only reminder program in another district; common unit: additional woman adherent at 32 weeks

## Ingredients: everything the program used, paid or not

| Category | Item | Quantity | Unit price | Cost | Paid / donated / borrowed |
|---|---|---|---|---|---|
| Staff time | Health-worker visits: 48 workers × 4 h a week × 40 weeks | 7,680 h | $0.75 an hour | $5,760 | Borrowed (government-stipended; priced at the local wage) |
| Staff time | Supervisors: 4 × 8 h a month × 10 months | 320 h | $2.50 an hour | $800 | Paid |
| Training | 2-day training for 52 people | 1 | $2,600 | $2,600 | Paid |
| Equipment | Bicycles, 48 × $90 over a 3-year life, 10 months of use | 48 | $25 | $1,200 | Paid |
| Materials | Printed adherence cards | 1,600 | $0.20 | $320 | Paid |
| Transport and communication | Phone credit, 48 workers × 10 months | 480 | $2 | $960 | Paid |
| Space | Clinic rooms for monthly meetings, 12 treatment centers × 10 | 120 | $10 | $1,200 | Donated |
| Monitoring | Data entry | 1 | $600 | $600 | Paid |
| Participants' time (society perspective only) | 1,600 women × 10 visits × 20 minutes | 5,333 h | $0.50 an hour | $2,667 | Not in the delivery total |
| **Delivery total** | | | | **$13,440** | |
| Transfers to participants | None | | | $0 | |
| Research costs (excluded) | Endline survey and pill counts | | | $9,000 | Paid |

## Cost per result
- Delivery cost per person reached: $13,440 / 1,600 = $8.40
- Cost per additional adherent woman: $13,440 / 192 = $70.00
- Additional adherent women per $100: 192 / 134.4 = 1.43

## How far the number moves (sensitivity)

| Scenario | Cost used | Effect used | Cost per additional adherent woman | Per $100 |
|---|---|---|---|---|
| Headline | $13,440 | 12 points (192 women) | $70.00 | 1.43 |
| Effect at lower confidence bound | $13,440 | 5 points (80 women) | $168.00 | 0.60 |
| Effect at upper confidence bound | $13,440 | 19 points (304 women) | $44.21 | 2.26 |
| With transfers | No transfers; same as headline | | $70.00 | 1.43 |
| Donated and borrowed inputs at zero | $6,480 | 12 points | $33.75 | 2.96 |
| Health-worker time at $1.50 an hour | $19,200 | 12 points | $100.00 | 1.00 |
| Society perspective (adds women's time) | $16,107 | 12 points | $83.89 | 1.19 |

## What limits comparing it with other programs
- Transfers: neither program made any, so this line does not separate them.
- Fixed costs: training and bicycles are $3,800, 28% of the delivery total; the cost per woman would fall if the same workers covered more women. The SMS program's fixed-cost share is not known.
- Wages and prices: health-worker time is priced at $0.75 an hour although the program did not pay it. Pricing it and the donated rooms at zero halves the ratio to $33.75; doubling the wage raises it to $100.
- Outcome measure: this trial used pill counts; the SMS program reports self-reported adherence, so the two "additional adherent woman" units are not the same measure.

## What to check before relying on this
- The health workers' hours and wage, from timesheets rather than the plan: this is the largest line and the one most likely to be mispriced.
- Whether the SMS program priced its staff time and platform fees the same way, before the two ratios go in one table.

## Where you could go from here
That's the estimate.
- Ask the SMS program's team for their ingredients list: the ministry wants both programs in one table, and that only works if they priced staff time and platform fees the same way and can say how their self-reported adherence relates to pill counts.
- Check the health workers' hours against timesheets: that line is $5,760 of the $13,440 delivery total, and it rests on the planned 4 hours a week.
- Run `assess-scalability` if the ministry is also weighing a wider rollout: training and bicycles are 28% of the cost and would fall per woman, while the health workers' time may not stay free.
I'd lean toward the SMS team's ingredients list, because without it the ministry's comparison cannot be made fairly, whatever the number here.
Questions you could ask next: "How do we present this so the $33.75 figure isn't quoted as the cost?" · "What would the cost per woman be if each health worker covered twice as many women?"
```
