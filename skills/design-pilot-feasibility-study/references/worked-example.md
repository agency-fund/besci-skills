# Worked example: a fertilizer voucher and SMS for maize farmers in Western Kenya

A full run of the skill on a realistic case, showing the output it should produce. The case is illustrative, not a real program.

## The request

"We're a farmer-support NGO in Western Kenya. Our intervention: an SMS two weeks before the long rains telling each registered farmer the date to top-dress their maize, plus a voucher for the local agro-dealer that is valid only that week. Next season we plan a cluster-randomized trial in 60 villages, with 15 farmers per village enrolled within 3 weeks and the outcome from a follow-up survey at harvest; our sample size assumes we reach 85% of farmers at harvest. We can pilot in 4 villages with 120 farmers over one season, with 2 field officers who can do short interviews. Our biggest worry is whether farmers will redeem the voucher at all. Design the pilot."

## The output

```markdown
# Pilot plan: top-dressing SMS and fertilizer voucher

**Intervention piloted:** two weeks before the long rains, each registered farmer gets an SMS with the date to top-dress maize and a voucher for the local agro-dealer, valid that week only.
**What it serves:** a cluster-randomized trial next season: 60 villages, 15 farmers per village enrolled within 3 weeks, top-dressing measured by a harvest survey, sample size assuming 85% of farmers reached at harvest.
**What this pilot is not for:** estimating the program's effect. Its effect estimate will not be used to size the main trial.
**Main-trial inputs it will measure:** share reached at harvest (attrition); voucher redemption (take-up); last season's top-dressing, asked at enrollment (the baseline). Not measured: the intracluster correlation, which four villages cannot estimate.

## Feasibility questions and progression criteria
| Heading | Question (rate or count, with its denominator) | Go | Amend | Stop | Why this line |
|---|---|---|---|---|---|
| Recruitment | Farmers enrolled per village within 3 weeks of starting, out of those eligible | 15 or more | 10 to 14 | Fewer than 10 | The trial needs 15 per village in 3 weeks |
| Retention | Share of enrolled farmers reached by the harvest survey | 85% or more | 70 to 84% | Below 70% | The trial's sample assumes 85% |
| Delivery | Share of enrolled farmers whose SMS arrived within 2 days of the planned date, and whose voucher was in hand before the valid week | 90% or more on both | 75 to 89% on either | Below 75% on either | A reminder after the top-dressing window is a different intervention |
| Acceptability | Share of enrolled farmers who redeemed the voucher in the valid week | 40% or more | 20 to 39% | Below 20% | Provisional: the trial's sample does not state a redemption rate. If the voucher is what changes behavior, 40% redemption needs about 6 times the sample of full redemption (1 ÷ 0.4²) and 20% needs 25 times |
| Outcome data | Share of farmers reached at harvest whose top-dressing answer matches the agro-dealer's voucher record | 90% or more | 75 to 89% | Below 75% | The trial's outcome is a survey answer; a record check shows whether it can be trusted |

## Pilot size
Redemption matters most. With 120 farmers and redemption near 40%, the 95% margin is 1.96 × √(0.40 × 0.60 ÷ 120) = ±9 points, narrower than the 20-point gap between the go and stop lines. Retention near 85% is known to ±6 points (1.96 × √(0.85 × 0.15 ÷ 120)), inside its 15-point gap. Farmers are spread over 4 villages and redemption may differ with distance to the dealer, so each village's rate is reported too. Recruitment is read village by village: 4 counts against the line of 15. One season, from enrollment 4 weeks before the rains to the harvest survey.

## Sites and conditions
Four villages chosen to span distance to the nearest agro-dealer, not the four nearest the NGO office. SMS sent from the NGO's routine platform; vouchers redeemed at the dealers who would serve the trial; no extra field visits beyond those the trial would fund. Unknown afterward: redemption in villages with no dealer within walking distance, if none of the four is one, and redemption in a season when the rains come late.

## Interviews
| Who | The one question | Asked by | When |
|---|---|---|---|
| Up to 15 farmers who did not redeem, from all 4 villages | "What stopped you using the voucher that week?" | Field officers, by phone or at home | Within a week of the voucher expiring |
| All 4 agro-dealers | "What happened when farmers came with the voucher? Did you have fertilizer in stock?" | Field officer | The last day of the valid week |
| Farmers missed by the harvest survey | "What happened?" (one call each) | Field officers | During the survey |

## What changes in the main study
| Question | If go | If amend | If stop |
|---|---|---|---|
| Recruitment | No change | Extend enrollment to 5 weeks, or enroll through farmer groups | Redesign enrollment with village leaders before any trial |
| Retention | No change | Collect a second phone number at enrollment and raise the trial's sample for the observed loss | Take the outcome from dealer records, not the survey |
| Delivery | No change | Fix the SMS schedule or voucher distribution, and check it in the trial's first week | Do not run the trial on this channel |
| Acceptability | No change | Extend validity to two weeks or add a nearer dealer, then recompute the trial's sample with the observed rate | Do not run the trial on the voucher; revisit the design with the interview reasons |
| Outcome data | No change | Add a dealer-record check to the trial's outcome | Change the outcome measure before the trial |

## Report skeleton
1. Participant flow: eligible, enrolled, sent the SMS and voucher, reached at harvest, with a usable top-dressing answer
2. Each question: line, observed rate with its margin, decision; redemption also by village
3. Interview reasons from non-redeemers, dealers, and farmers missed at harvest
4. Changes to the main study
5. Any top-dressing figures, labeled "not a basis for sizing the main trial"

## What to check before relying on this
- Whether the dealers can stock fertilizer for a whole village redeeming in one week; a stock-out would read as low acceptability.
- Whether the pilot season's rains are typical, since redemption is tied to the planting date.
```
