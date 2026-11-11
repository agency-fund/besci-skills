# Worked example: an SMS reminder for business permit renewals in a Kenyan county

A full run of the skill on a realistic case, showing the output it should produce. The case is illustrative, not a real program.

## The request

"We're the revenue unit of a county government in Kenya. About 40,000 small businesses must renew their single business permit by 31 March; last year 30% renewed on time, from our own records. We want to test an SMS from the county revenue office two weeks before the deadline that states the late-renewal penalty and says enforcement visits follow. About 80% of permits have a working phone number on file. Our proposal quotes the Mexico tax SMS trial in BIT's TESTS guide, where on-time declarations rose from 24% to 33%. We also have Antinyan and Asatryan's meta-analysis of tax nudges, https://doi.org/10.1093/ej/ueae088. The revenue director says she would send the SMS to every permit holder for a gain of 1 percentage point or more; each SMS costs KSh 1. What effect should we plan the test on?"

## The output

```markdown
# Effect-size benchmark: deterrence SMS on on-time permit renewal

**Decision this informs:** whether to send the SMS to every permit holder each year
**Outcome, unit, baseline:** permit renewed by 31 March; percentage points; baseline 30% from last year's county records
**Delivered by, at what scale:** the county revenue office, by SMS, to about 40,000 permit holders

## Estimates read
| Source | How read | Label | Delivered by | Reported effect | In the test's units |
|---|---|---|---|---|---|
| Kettle & Persian (2022), Mexico case study, https://www.bi.team/wp-content/uploads/2022/11/BIT-Handbook-How-to-run-simple-BI-projects.pdf | Full text of the guide; the trial's own paper not read | Published field trial, picked for the guide as an exception to its 2–3 point experience | Government: the Mexican tax authority, with BIT; 748,499 businesses | Deterrence SMS: on-time declarations 24% to 33%, +9 points (+37.5%) | +9 points, kept as points because the meta-analysis below works in points at a similar baseline. At 30%, 1 SD = √(0.30 × 0.70) = 0.458, so 9 points = 0.20 SD |
| Antinyan & Asatryan (2025), https://doi.org/10.1093/ej/ueae088 | Full text of the authors' July 2024 discussion-paper version | Meta-analysis of tax-nudge experiments, not corrected for publication bias | Tax authorities, usually working with academics or nudge units | From a baseline of about 25%: reminders +2.7 points; deterrence messages +3.2 more, so +5.9 | +5.9 points = 0.13 SD at 30% |

## Corrections
1. Lab or online study: not applied; none was supplied.
2. Selective publication: the meta-analysis found reported results selected for their sign and significance but gives no corrected figure, so 5.9 points is a ceiling. The Mexico trial was picked for the guide because its effect was large, and it sits above the pooled figure, so it does not set the high end.
3. Take-up: applied. About 80% of permits have a working number; neither source says how many messages arrived, so their take-up counts as complete: × 0.8.
4. Who delivers it: the same kind as the sources, a government tax office. The meta-analysis found smaller effects in low- and middle-income countries, which its authors call suggestive, so the central value sits below the midpoint.

## Planning range
| | Percentage points | SD | Where it comes from |
|---|---|---|---|
| High | 4.7 | 0.10 | The meta-analysis's deterrence estimate × take-up: 5.9 × 0.8 = 4.72 |
| Central | 2.0 | 0.04 | The meta-analysis's reminder estimate × take-up (2.7 × 0.8 = 2.2), rounded down for the smaller effects found in low- and middle-income countries; within BIT's 2–3 points for messages |
| Low | 0.8 | 0.02 | No unselected estimate supplied: one sixth of the high end, 4.72 ÷ 6 = 0.79, the ratio of the nudge-unit average to the journal average (1.4 to 8.7) |

## Smallest effect worth acting on
1 percentage point, set by the revenue director: the 40,000 messages cost KSh 40,000 a year, and 1 point is 400 more permits renewed on time.

## Effect to plan on
1 percentage point (0.022 SD at the 30% baseline), because the director has set it and it lies inside the range. A test that can detect 1 point will also detect the central 2 points. If the true effect is at the low end, 0.8 points, the test will probably miss it, and the director would not act on it anyway.

## What to check before relying on this
- Whether the county has sent reminders before, and what every one of them did, including those that changed nothing. That record is an unselected estimate and would replace the one-sixth low end.
- How many of the 40,000 phone numbers are current. Below 80%, every value above falls in proportion.
- The 30% baseline, which rests on one year of records; compare it with the year before.
- Whether 40,000 permit holders are enough to detect 1 point; the sample-size calculation comes next.
```
