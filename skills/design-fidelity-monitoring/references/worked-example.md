# Worked example: iron-folate counseling at four rural clinics in Malawi

A full run of the skill on a realistic case, showing the output it should produce. The case is illustrative, not a real program.

## The request

"We support four rural antenatal clinics in one district of Malawi with a package to help pregnant women take their iron-folate tablet every day. Nausea was the main barrier in our interviews. At each antenatal visit a nurse gives a three-message script: why daily, take it with food at night to limit nausea, and what to do after a missed day. The session opens with a group song. Each woman gets a pictorial tick calendar with her 30-tablet supply. Within three weeks of each antenatal visit a Health Surveillance Assistant (a government community health worker) visits her at home, counts the pills, checks the calendar, and repeats the night-with-food advice. There are 8 nurses, 2 per clinic, supervised by each clinic's in-charge, and 24 assistants, 6 per clinic, supervised by the district coordinator. Nurses keep the antenatal register; assistants keep visit books. Two comparison clinics get usual care for our evaluation. The data are for learning and support, and that is in our memorandum with the District Health Office. We have one district monitor with a motorbike and a phone budget. What should the fidelity monitoring look like?"

## The output

```markdown
# Fidelity monitoring plan: iron-folate counseling package, four rural clinics

**Delivered by:** 8 antenatal nurses (2 per clinic), supervised by each clinic's in-charge; 24 Health Surveillance Assistants (6 per clinic), supervised by the district coordinator
**Use of the data:** Learning and support, and the evaluation with two comparison clinics. Stated in the memorandum with the District Health Office.

## Essential parts
| Part | Mechanism it carries | Essential or adaptable | Why |
|---|---|---|---|
| Three-message nurse script | Tells the woman how to take the tablet without nausea and what to do after a missed day | Essential | Nausea was the main barrier; the night-with-food message is the part that addresses it |
| Tick calendar handed over with the tablets | A daily cue and a record she keeps herself | Essential | Without it there is no daily prompt between visits |
| Home visit within three weeks | Checks the pills, repeats the advice, notices problems early | Essential | It is the only contact between clinic visits |
| Group song opening the session | Rapport | Adaptable | Can vary by clinic without loss |
| Time of day of the home visit | None | Adaptable | Set by the assistant's route |

## Indicators
| Part | Dimension | Indicator | Source | Sample and frequency | Collected by |
|---|---|---|---|---|---|
| Nurse script | Adherence | Each of the three messages said (yes or no per message) | Unannounced observation of a session | 2 sessions per nurse per month | District monitor, not the in-charge |
| Nurse script | Quality | Woman restates the night-with-food advice correctly when asked at the end of the session | Same observation | Same sessions | District monitor |
| Tick calendar | Dose | Share of women enrolled that month who received a calendar | Back-check by phone or home visit | 10 women per clinic per month, drawn at random from the register by the monitor | District monitor |
| Home visit | Dose | Share of enrolled women visited within three weeks | Visit books, checked against the back-check ("did an assistant come, and when?") | All entries; the same 10 women per clinic | Coordinator compiles; monitor runs the back-check |
| Home visit | Adherence | Pills counted and advice repeated (yes or no each) | Monitor accompanies an assistant, unannounced | 2 visits per assistant per quarter | District monitor |
| Tick calendar | Responsiveness | Days ticked since the last visit | Recorded by the assistant; checked on accompanied visits | All visits; 2 checked per assistant per quarter | Assistant; monitor |

## Thresholds and actions
| Indicator | Expected level | Act when | Action | Who acts |
|---|---|---|---|---|
| All three messages said | 90% of observed sessions (assumed) | Below 70% at a clinic in a month | Half-day refresher with the script cards; observe again the next month | In-charge with the program trainer |
| Calendar received | 95% (assumed) | Below 85% | Check that calendars are packed with the tablets, not stored separately | Program logistics officer |
| Visited within three weeks | 80% (assumed) | Below 60% at a clinic | Review routes with the assistants; reschedule visits rather than add a backlog | District coordinator |
| Visit book disagrees with the back-check | Under 10% of checked women | Above 20% | Meeting with the clinic team as a group to review how the book is filled in | Monitor with the in-charge |

## Feedback to the people delivering
- **Who sees what, how often:** each clinic team gets a one-page sheet each month with its four indicators, the gap to the expected level, and one next step; the District Health Office gets a four-clinic summary.
- **Rule:** clinic-level results only; no names, no ranking of clinics; not used for appraisal, pay, or discipline. Written in the memorandum and said at launch.
- **Their channel back:** in the coordinator's monthly phone round, each assistant is asked what stopped them that month; answers go on the back of the sheet.
- **During an evaluation:** agreed with the evaluator: refreshers and route reviews are allowed, because routine supervision at scale would do the same; each is recorded in the change log as part of what was delivered.

## Change log
A page at the back of each visit book and a column on the monitor's observation form: date, what changed, who changed it, why, and which part it touches. Collected monthly by the monitor.

## What an evaluation needs caught
- **Assigned but not reached:** enrolled women with no home visit, from the visit books and back-checks
- **Comparison group reached:** comparison-clinic women who report receiving a tick calendar, from a short question in the comparison clinics' exit interviews
- **Spillover:** assistants whose routes also cover villages served by the comparison clinics, from the coordinator's route list
- **Dropout:** women who miss the next antenatal visit, from the register

## How to read the results
If the script is delivered and calendars and visits are on target but tablets are still not being taken, question the package, starting with whether nausea is the barrier the night-with-food advice assumes. If the night-with-food message is the one most often skipped, the trial is not yet testing the package as designed.

## What to check before relying on this
- Whether nurses fill in the register during the visit; if it is written up at the end of the day, the back-check sample is drawn from a list that may be wrong.
- Whether the home visit is essential or whether the calendar alone carries the daily cue; the evaluation's process data should settle this before scale-up.
```
