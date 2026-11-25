# Worked example: community health workers and a digital job aid

A full run of the skill on a realistic case, showing the output it should produce. The case is illustrative, not a real program.

## The request

"We interviewed 12 community health workers in two districts about the job-aid app we rolled out last year. I did eight of the interviews myself and our field officer did four. They were in Kiswahili; we have English transcripts, translated by the field officer. I don't have hypotheses. I want to understand how the workers make sense of the app in their daily visits, for a report to the ministry. Do the analysis with me. Transcripts attached."

The user chose to run it with them. At checkpoint 1 they confirmed a data-driven analysis of the whole data set at the level of surface meaning. At checkpoint 2 they merged two candidate themes about supervision and sent "phone problems" to the set-aside pile. At checkpoint 3 they renamed one theme.

## The output

```markdown
I built three themes with you from the 12 interviews: the app is experienced as a second supervisor, it lends workers authority at the doorstep while costing them their own voice, and it pushes unpaid work into their evenings. You made the calls at all three checkpoints. The thing to check first is the second theme, which rests on translated phrases about "voice" that your field officer should read in Kiswahili. The report is `thematic-analysis/report.docx` and the map is `thematic-analysis/thematic-map.png`; the working files are in `thematic-analysis/working/`.

# How community health workers make sense of a digital job aid

**Question:** How do community health workers make sense of a digital job aid in their daily visits?
**Data set:** 12 individual interviews with community health workers in two districts; 8 conducted by the program lead and 4 by a field officer; held in Kiswahili; English transcripts translated by the field officer
**How it was run:** with the program lead deciding at three checkpoints

## Introduction
The program introduced a job-aid app to guide household visits and record them. Use of the app is high in the program's records, and the program wanted to know what that use means to the workers before reporting to the ministry. No prior literature was supplied for this report.

## Method
### Data
The data set is all 12 worker interviews. Interviews with supervisors, collected in the same round, were left out because the question concerns the workers' own accounts.
### Analytic approach
We conducted a thematic analysis following the six phases of Braun and Clarke (2006). The analysis was data-driven, because the program had no hypotheses and little is known about this group. It describes the whole data set and works at the level of surface meaning. We treated what workers said as a report of their experience, read with attention to their working conditions. Prevalence is counted in interviews.
### Procedure
An AI system (Claude, November 2026) read each transcript twice and coded it in full, with one reader per transcript, then collated 214 extracts under 41 codes and drafted candidate themes. The program lead set the question and the analytic choices, merged two candidate themes, set one aside, and approved the final definitions and names. Themes were reviewed against all extracts and then against each full transcript. Braun and Clarke consider reflexive thematic analysis a human practice and reject generative AI for it (Jowsey et al., 2026). We report the division of work so readers can judge the analysis with that in mind.
### Quality checks
All 214 extracts were checked against the transcripts by script; 3 had been shortened without a mark and were corrected. Criterion 1 is not met: the translations were not checked against the recordings.

## Findings
The workers described an app that does three things to their work. It watches them, it speaks for them, and it follows them home. The first two are in tension: the same record that lets a supervisor see them is what makes families listen.

![Figure 1. Thematic map of how community health workers make sense of the job aid](../thematic-map.png)

*Note.* Solid lines join a theme to its sub-themes. The dashed line marks a relationship between themes. Codes about phone hardware were set aside.

| Theme | Central idea | Sub-themes | Appears in |
|---|---|---|---|
| The app as a second supervisor | The record is read as surveillance, and workers act for the record | Being watched through the data; Entering visits to look busy; Praise that never arrives | 10 of 12 interviews |
| Borrowed authority at the doorstep | The phone makes families listen, and the worker's own judgment recedes | The phone says so; Families trust the screen; Losing my own voice | 8 of 12 interviews |
| Work that spills past the visit | Keeping the app fed is unpaid evening work | Syncing at night; Paying for my own data | 7 of 12 interviews |

### The app as a second supervisor
This theme covers accounts of the app as a means by which supervisors see and judge workers. It does not cover complaints about supervisors that do not involve the record.

Workers spoke of the dashboard as the thing their supervisor looks at, in place of the visit.

> I enter the visit even when nobody was home, because the dashboard is what she looks at. (CHW-03)

The worker does not describe this as cheating. The entry is presented as what the job now requires, which suggests the record has become the work that counts. Two workers said the opposite, that the record protects them when a supervisor doubts a visit took place (CHW-07, CHW-11).

### Borrowed authority at the doorstep
This theme covers how the phone changes the worker's standing with families. It does not cover the content of the advice.

> When I read it from the phone they listen. When I say it from my own head, they ask who told me. (CHW-05)

The authority belongs to the device, and the worker knows it. Several described this as useful and as a loss in the same breath, most plainly in accounts of no longer giving advice the app does not contain. This reading leans on the translated word "voice" and should be checked in Kiswahili.

### Work that spills past the visit
This theme covers work the app creates outside paid visits. It does not cover the length of the visits themselves.

> I sync at night when the network is better. That is my own bundle. Nobody asks about that. (CHW-09)

The cost is in time and in money, and "nobody asks" marks it as unseen by the program.

## Discussion
High recorded use sits alongside an account in which the record is partly kept for the supervisor's eyes. For the ministry report, recorded visits should not be read as a plain count of visits made. The analysis cannot say how common false entries are, and it reflects twelve workers in two districts, chosen by the program.

## What to check before relying on this
- "Borrowed authority at the doorstep" rests most on interpretation and on translation; the field officer should read CHW-05 and CHW-08 in Kiswahili against it
- All transcripts are translations that were not checked against the recordings
- Supervisors' accounts were left out, so "being watched" is the workers' view only

## References
Braun, V., & Clarke, V. (2006). Using thematic analysis in psychology. *Qualitative Research in Psychology*, *3*(2), 77–101. https://doi.org/10.1191/1478088706qp063oa

Jowsey, T., Braun, V., Clarke, V., Lupton, D., & Fine, M. (2026). We reject the use of generative artificial intelligence for reflexive qualitative research. *Qualitative Inquiry*, *32*(10), 931–935. https://doi.org/10.1177/10778004251401851

## Where you could go from here
The thematic analysis is done.
- I would lean toward having your field officer read CHW-05 and CHW-08 in Kiswahili first, because the second theme turns on a translated word and the ministry report will quote it.
- `decompose-comb-barriers` would fit if you want to turn "entering visits to look busy" into testable reasons why accurate recording is not happening.
- `draft-sifa-declaration` would fit before the report goes to the ministry, so readers can see what you decided and what the AI system did.
Questions you could ask next: "Which extracts go against each theme?" · "What would this analysis look like if we included the supervisor interviews?"
```
