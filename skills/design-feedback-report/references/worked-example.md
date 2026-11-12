# Worked example: a monthly report on record completeness for health facilities in Nigeria

A full run of the skill on a realistic case, showing the output it should produce. The case is illustrative, not a real program.

## The request

"We support 85 primary health facilities in Ekiti State, Nigeria, to keep complete patient records. Behavior: each facility's record officer completes every outpatient record (date, diagnosis, treatment, age, sex) on the day of the visit. We interviewed 30 officers: 24 could not say how complete their own registers were, and most guessed 'about the same as everyone'. Registers and pens are in stock, and officers say time is not the problem. The state health information system gives us, for each facility and month, the share of outpatient visits with a complete record; the data are good except at three facilities with intermittent power. About 20 facilities are above 90%, 30 are between 60 and 75%, and the rest are below 50%. We want to send a monthly text to each record officer. The local government monitoring officer would also like to see the numbers. Design the report."

## The output

```markdown
Each record officer gets a monthly text with their facility's share of complete records, set against the state's 90% standard and their own last month; facilities under 50% get a nearer step of 60% instead. No peer average or rank is shown, because officers meet at review meetings and would read "the average" as named colleagues. The monitoring officer sees counts only, no facility named, and I haven't promised an effect for Ekiti.

# A feedback report for record officers in Ekiti State

**Behavior:** The record officer at each of 85 primary health facilities in Ekiti State completes every outpatient record on the day of the visit.
**Confirmed barrier:** Officers do not know how complete their registers are: 24 of 30 interviewed could not say, and most guessed "about the same as everyone", while completeness runs from under 50% to over 90%. Supplies and time are ruled out by the officers' own account, and completing a record is in the officer's hands.
**Data:** The state health information system: share of outpatient visits with a complete record, by facility and month. Reliable except at three facilities with intermittent power, which get no report until their data are fixed.

## Metric
- **Headline:** The share of last month's outpatient visits at the officer's facility with a complete record.
- **Not shown:** Disease counts and patient numbers, which the officer cannot change.

## Comparison
- **Compared with:** A standard of 90%, with the officer's own previous month as a second line, because about a quarter of facilities (20 of 85) already meet 90%, so it is within reach. No peer average is shown: officers meet at review meetings, and "the average facility in your area" would be read as named colleagues.
- **Which standard or group:** "90% complete", the level the state already uses at review meetings.

## What each group sees
- **At or above the comparison:** This month's share, last month's share, and the words "On target". No other figure.
- **Below it:** This month's share, last month's share, the 90% standard, and the field most often left blank at that facility.
- **Far below:** For facilities under 50%, a next step of 60% in place of the 90% standard, and one action: fill the most-missed field before the patient leaves the desk.

## What the report says
"Records, [month]: [n]% of outpatient visits had a complete record (last month: [m]%). [On target. | Target: [90% or next step]. Most often blank: [field]. Fill it before the patient leaves the desk.] Next report: [date]."

## Who sees it
- **The person:** The record officer, by text message.
- **Anyone else:** The local government monitoring officer sees how many facilities are on target, below, and far below, with no facility named. Facility figures are not shared.

## How often, and when it stops
- **Sent:** Monthly, in the week after the information system closes the month.
- **When reports stop:** Expect completeness to slide back over time. Check it three and six months after the last report.

## Monitoring
- **Results read separately for:** The 20 facilities that started above 90%, and the roughly 35 that started below 50%.
- **Review if:** Average completeness in either group falls by 5 points over two months; the program lead and the state records lead review the comparison and the wording.

## Specialist review
A monitoring and evaluation specialist, for the three facilities with intermittent power, before they receive any report. If the monitoring officer asks for facility figures, a human-resources specialist and program management must first agree in writing what the figures may be used for.

## What the evidence supports
That feedback to health workers on their own practice improves it on average, more where the starting level is low and where the report gives a benchmark and an action; this comes from 292 trials, 26 of them in low- or middle-income countries (Ivers et al., 2025). Comparison with peers lowered the performance of weaker health worker trainees in Zambia (Ashraf, Bandiera & Lee, 2014), which is why no peer figure is shown. No effect size is promised for Ekiti.

## What to check before relying on this
- Whether officers believe the system's figure. Show five of them their number and their register side by side before the first report.
- Whether "On target" reads as approval in a text from the program.

## Where you could go from here
That's the report design.
- Show five officers their number beside their own register, and the draft text, with `plan-prototype-test`: the design rests on officers trusting the system's figure, and the same session shows whether "On target" reads as approval.
- Ask a monitoring and evaluation specialist to fix the data at the three facilities with intermittent power: they get no report until then.
- Settle in writing with the monitoring officer what the figures are for, before anyone asks for them by facility: once facility figures reach supervisors, the report can turn into an appraisal tool.
I'd lean toward the session with five officers first, because if they don't believe the number, nothing else in the design matters.
Questions you could ask next: "What should the text say to a facility that drops below 90% after being on target?" · "How will we know whether completeness holds after the reports stop?"
```
