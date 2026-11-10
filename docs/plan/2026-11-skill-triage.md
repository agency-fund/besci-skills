# Skill triage, November 2026

Status: reviewed by Zezhen Wu on 2026-11-10 (checkpoint 1). His decisions are recorded under each heading. Skill folders are removed in the `skills-revision` pull request, not before.
Compiled 2026-11-10 from a reading of 14 source documents and the 71 atomic skills on `main` at commit `85d8c0e`. That commit is the last one holding all 71.

## How a skill was judged

A skill stays if it passes three tests.

1. **Common.** Its task is a named step or tool in two or more of the sources below.
2. **Adds something.** One line can state what the skill makes the AI do that it would not do unprompted. This is judged at rewrite, when each skill must carry that line. A skill whose line cannot be written honestly is parked then.
3. **Distinct.** No other surviving skill produces the same output template.

A second lane holds frameworks the library chooses to carry. Skills in it skip test 1 only: wise interventions (4 skills), TAF's agency framework (2), Busara's SIFA (1), and one skill on TAF's AI evaluation playbook.

## Sources and how much of each was read

| Code | Source | Read |
|---|---|---|
| BCW | Behaviour Change Wheel: Michie, van Stralen & West (2011); the 2014 guide through open reproductions | 2011 paper in full. The book only through summaries, which disagree on its structure (8 steps, 5 steps, 6 processes) |
| BIT | Behavioural Insights Team: TESTS guide (Kettle & Persian 2022); EAST (2014 and the 2024 revision); Explore field guide and report (2022); Test, Learn, Adapt (2012) | In full, except Test, Learn, Adapt in part |
| BD | Behavioral Design: Datta & Mullainathan (CGD 2012); ideas42 Behavioral Design Teams playbook (2018) | Paper in full; playbook in part |
| OECD | BASIC toolkit (2019) | Full report obtained, read in part |
| WB | World Development Report 2015; Gauri (2018) | Overview and chapter 11 in full, chapters 1 to 3 and 10 in part; chapters 4 to 9 unread |
| IM | Intervention Mapping: Fernandez et al. (2019); Kok et al. (2017); the authors' site and workbook | Open overviews in full. The textbooks and the 1998 paper are not open |
| BUS | Busara toolkit (Groundwork No. 10, 2024), the AUDAS process | In full, except figure text |
| DBC | Designing for Behavior Change: TOPS Field Guide (2017); FSN Network curriculum (2013); Kittle, Barrier Analysis (2nd ed. 2017) | Field Guide in full; the other two in part |
| UNI | UNICEF Social and Behaviour Change Programme Guidance (2022); Petit, Behavioural Drivers Model (2019) | About half of the 2022 PDF, from an archived copy; the live site refused automated requests |
| JPAL | J-PAL Research Resources (48 pages); Glennerster & Takavarasha, Running Randomized Evaluations | Summary and headings of all 48 pages; book chapter 1 in full, chapters 2 to 9 from summaries |
| MRC | Skivington et al. (2021), MRC framework for complex interventions | In full |
| SUR | Survey methods: DIME Analytics, Development Research in Practice (2021); Groves et al., Survey Methodology (2009) | DIME chapter 4 in full, the rest in part; Groves from its table of contents only |
| EXP | WHO and ExpandNet: Nine steps (2010); Beginning with the end in mind (2011) | Both in full |
| WW | Walton & Wilson (2018), Wise interventions | In full, with the supplement tables |

Corrections the reading produced:

- **AUDAS** stands for Align, Understand, Design, Assess, Share. `taxonomy.yaml` and `docs/taxonomy.md` map the stages to "Assess, Understand, Design, Assess, Scale", which is wrong. A primary source exists (DOI 10.62372/WQSB6195); the October dossier said none did.
- **Gauri (2018)** is single-authored and names no eMBeD cycle. The four-part cycle is figure 11.1 of the World Development Report 2015. The dossier's item B15 cites "Gauri et al."
- **EAST's four-step project method** is only in the 2014 edition. The 2024 revision drops it and points to the TESTS guide.
- **ideas42** now names its process IDEAS (Identify, Diagnose, Engineer, Assess, Scale). Its method pages are empty, so the 2012 paper and the 2018 playbook are the readable sources.
- **The DBC Practical Field Guide** is dated 2017 and published by TOPS. The 2013 document is the curriculum.
- **Neither survey-methods book covers translation.** J-PAL's survey design page does, with a four-step procedure. The Cross-Cultural Survey Guidelines (University of Michigan) probably do, but the site refused the fetch, so that is unverified.

The extracted tables, about 1,340 rows, are working files and are not in the repository.

## Task table

Each row is a task, in normalized wording, with the sources that name it as a step, tool, or technique. "Claimed" means the topic is on the colleagues' tracker.

### Define and diagnose

| Task | Named in | Count | Current skill |
|---|---|---|---|
| Review existing evidence before designing | BIT, BUS, IM, UNI, EXP, OECD | 6 | `assess-evidence-base` |
| Judge whether evidence applies in a new context | JPAL, MRC, WW, IM | 4 | `assess-evidence-transferability` |
| State the problem as behaviors and list candidates | BCW, BIT, OECD, BD, DBC, IM, UNI | 7 | `define-key-behavior` |
| Prioritize among candidate behaviors | BCW, BIT, OECD, DBC | 4 | `score-candidate-behaviors`, `define-key-behavior` |
| Specify the target behavior (who, what, when) | BCW, BIT, OECD, DBC, IM, BD | 6 | `define-key-behavior` |
| Describe the audience and the context | IM, DBC, UNI, MRC, BIT, BUS, OECD, WW | 8 | `map-audience-context` |
| Write a theory of change or logic model | BUS, UNI, MRC, IM, BCW, JPAL, WB | 7 | `draft-theory-of-change` |
| Document the team's own assumptions before research | BIT, BUS, WB, BD | 4 | `audit-researcher-bias` |
| Map the steps of the behavior (journey or behavioral map) | BIT, BUS, OECD, UNI, BD | 5 | none (claimed) |
| Map stakeholders | BIT, MRC, EXP, UNI, IM, OECD | 6 | none |
| Diagnose barriers with a behavioral framework | BCW, BIT, BUS, UNI, OECD, BD, WB | 7 | `decompose-comb-barriers` |
| Write an interview or focus-group guide for diagnosis | BIT, BCW, IM, BUS, UNI, WB | 6 | `draft-tdf-interview-guide` |
| Observe or experience the service in the field | BIT, OECD, WB, UNI, BUS | 5 | none |
| Audit friction and hassle in a process | BIT, BD, OECD, WB | 4 | `audit-process-friction` |
| Establish whether a social norm is at play | WB, UNI | 2 | `diagnose-social-norm` |
| Identify the reference or influencing group | WB, UNI, DBC, BIT | 4 | `map-reference-network` |
| Barrier Analysis, or Doer and Non-Doer study | DBC | 1 | `draft-barrier-analysis-questionnaire`, `analyze-doer-nondoer-differences` |
| Positive deviance inquiry | DBC | 1 | `identify-positive-deviants` |
| Assess scarcity or cognitive load | BD and WB treat it as a lens or a timing technique, not a step | 0 | `assess-scarcity-load` |
| Synthesize qualitative data into findings | BUS, UNI, JPAL | 3 | `synthesize-interview-findings` |
| Review why a past intervention did or did not work | BIT, BUS, MRC, DBC, WB | 5 | `review-prior-intervention` |
| Pre-mortem or risk review | BIT, OECD, UNI, WB | 4 | none (claimed) |
| Personas or segmentation | BIT, UNI, BUS | 3 | none (claimed) |

### Design

| Task | Named in | Count | Current skill |
|---|---|---|---|
| Match interventions to diagnosed barriers and prioritize | BCW, BIT, OECD, WB, BUS, DBC, IM, UNI | 8 | `select-intervention-levers` |
| Draft messages, materials, and scripts | IM, BIT, DBC, BCW, OECD | 5 | `draft-lever-content` |
| Prototype and user-test before piloting | BIT, BUS, OECD, UNI, IM, BD | 6 | none (`plan-trials-of-improved-practices` covers one method) |
| Ethics review of an intervention | OECD, BIT, WW, JPAL, WB | 5 | `audit-intervention-ethics` |
| Technique: defaults | BIT, OECD, WB, BD, UNI | 5 | `select-default-option` |
| Technique: reminders and prompts | OECD, BD, WB, UNI, BIT | 5 | `design-reminder-schedule` |
| Technique: timing, choosing the moment | BIT, OECD, WB, WW, BD | 5 | `choose-delivery-moment` |
| Technique: framing | BIT, OECD, WB, BD, UNI, WW | 6 | `choose-message-frame` |
| Technique: commitment devices | BIT, OECD, WB, BD, UNI, WW | 6 | `design-commitment-device` |
| Technique: incentives | BIT, BD, WB, BCW, WW | 5 | `design-incentive-scheme` |
| Technique: social norm messages | BIT, OECD, WB, BD, UNI, WW | 6 | `write-social-norm-message` |
| Technique: feedback and social comparison | OECD, WB, UNI, BIT, BD | 5 | `design-feedback-report` |
| Technique: implementation intentions | BIT, OECD, BD, UNI, WW | 5 | `draft-implementation-intention-prompt` |
| Technique: messenger or source | BCW, WW, WB, each loosely | 3 | `select-messenger` |
| Technique: simplification | BIT, WB, OECD | 3 | none (partly in `draft-lever-content`) |
| Technique: salience and personalization | BIT, OECD | 2 | none |
| Technique: habit formation | WB; BCW loosely | 1 | `design-habit-anchor` |
| Technique: labeling (mental accounting) | WB | 1 | `specify-earmark-label` |
| Technique: social image or recognition | BIT | 1 | `design-social-recognition` |
| Community-level norm change by public declaration | WB and UNI describe community norm change; neither names a pledge | 0 | `plan-collective-pledge` |

### Measure, test, analyze, implement

| Task | Named in | Count | Current skill |
|---|---|---|---|
| Choose outcome measures and data sources | BIT, OECD, IM, MRC, BUS, DBC, UNI, JPAL | 8 | `plan-evaluation-design` |
| Write survey questions | SUR, JPAL, BIT, BUS | 4 | `draft-survey-items` |
| Pretest a questionnaire, including cognitive interviews | SUR, JPAL, DBC, BUS, IM | 5 | `draft-cognitive-interview-script` |
| Translate an instrument | JPAL, BUS, DBC | 3 | `translate-survey-instrument` |
| Choose or adapt the survey mode | SUR, JPAL, BIT | 3 | `adapt-survey-for-phone-mode` |
| Ask about sensitive behavior indirectly | WB, JPAL, SUR | 3 | `design-list-experiment` |
| Measure social norms, including vignettes | WB, UNI, BUS | 3 | `draft-norms-vignette` |
| Find a validated measure | BIT, BUS, IM, UNI | 4 | none (claimed) |
| Mystery shopping | BIT and BUS list it as a way to explore a service, not as a measurement protocol | 0 | `design-mystery-client-protocol` |
| Sampling plan | BIT, JPAL, SUR, DBC | 4 | none |
| Choose the evaluation design and unit of randomization | BIT, OECD, JPAL, MRC, BUS, SUR, IM | 7 | `choose-trial-design` |
| Choose a quasi-experimental design | OECD, BUS, BD, SUR, JPAL | 5 | none |
| Set the effect size to plan for | BIT, JPAL | 2 | `estimate-expected-effect` |
| Power and sample size | BIT, OECD, JPAL, SUR, BUS | 5 | `estimate-sample-size` |
| Pre-analysis plan and registration | JPAL, SUR, BIT, OECD, BUS | 5 | `write-pre-analysis-plan` |
| Feasibility or pilot study | MRC, OECD, JPAL, IM, UNI, EXP | 6 | `design-pilot-feasibility-study` |
| Adaptive allocation across message variants | MRC | 1 | `design-adaptive-message-experiment` |
| Subgroup and heterogeneity analysis | MRC, BIT, OECD, BUS, WW | 5 | `analyze-heterogeneous-effects` |
| Adjust for multiple outcomes | JPAL | 1 | `adjust-for-multiple-comparisons` |
| Cost-effectiveness analysis | JPAL, MRC, BD, EXP | 4 | `estimate-cost-effectiveness` |
| Check AI-assigned qualitative codes | none | 0 | `audit-llm-qualitative-coding` |
| Communicate results | BIT, BUS, OECD, JPAL | 4 | none |
| Monitor fidelity of delivery | MRC, JPAL, BIT, OECD, BCW, DBC | 6 | `design-fidelity-monitoring` |
| Describe the intervention so it can be repeated | BCW, MRC, OECD, WW, DBC, EXP, IM | 7 | `draft-intervention-description` |
| Record and judge adaptations | MRC, EXP, IM, BCW, WW | 5 | `specify-intervention-adaptations` |
| Assess scalability | EXP, BIT, WW | 3 | `assess-scalability` |
| Plan the scale-up strategy | EXP, BIT, OECD, BD, IM | 5 | `plan-scale-up-strategy` |

## Verdicts

Totals: 53 keep, 1 merge, 1 rework, 12 park, 4 cut. That leaves 54 atomic skills.

### Keep (53)

| Stage | Skills |
|---|---|
| Define (6) | `assess-evidence-base`, `assess-evidence-transferability`, `define-agency-construct` (lane), `define-key-behavior`, `draft-theory-of-change`, `map-audience-context` |
| Diagnose (7) | `audit-process-friction`, `audit-researcher-bias`, `decompose-comb-barriers`, `diagnose-social-norm`, `draft-tdf-interview-guide`, `identify-wise-intervention-target` (lane), `map-reference-network` |
| Design (16) | `adapt-growth-mindset-message` (lane), `audit-intervention-ethics`, `choose-delivery-moment`, `choose-message-frame`, `design-commitment-device`, `design-feedback-report`, `design-incentive-scheme`, `design-reminder-schedule`, `draft-belonging-story` (lane), `draft-implementation-intention-prompt`, `draft-lever-content`, `draft-values-affirmation` (lane), `select-default-option`, `select-intervention-levers`, `select-messenger`, `write-social-norm-message` |
| Measure (7) | `adapt-survey-for-phone-mode`, `design-list-experiment`, `draft-cognitive-interview-script`, `draft-norms-vignette`, `draft-survey-items`, `plan-agency-measurement` (lane), `translate-survey-instrument` |
| Test (7) | `choose-ai-eval-level` (lane, rewritten), `choose-trial-design`, `design-pilot-feasibility-study`, `estimate-expected-effect`, `estimate-sample-size`, `plan-evaluation-design`, `write-pre-analysis-plan` |
| Analyze (4) | `analyze-heterogeneous-effects`, `estimate-cost-effectiveness`, `review-prior-intervention`, `synthesize-interview-findings` |
| Implement (6) | `assess-scalability`, `design-fidelity-monitoring`, `draft-intervention-description`, `draft-sifa-declaration` (lane), `plan-scale-up-strategy`, `specify-intervention-adaptations` |

Three keeps rest on thin support and are the first to check against test 2 at rewrite: `select-messenger` (three sources, each naming it loosely), `diagnose-social-norm` (two sources), `estimate-expected-effect` (two sources).

Two overlaps to remove at rewrite, under test 3:

- `assess-evidence-transferability` has a "discounted expected effect" section that repeats the job of `estimate-expected-effect`. The section comes out.
- `plan-evaluation-design`, `choose-trial-design`, and `write-pre-analysis-plan` each touch the comparison condition. Each keeps one job: outcome and data source, design and unit, analysis.

### Merge (1), approved

| Skill | Into | Why |
|---|---|---|
| `score-candidate-behaviors` | `define-key-behavior` | The template of `define-key-behavior` already has a candidate scoring table and a ranked shortlist. Its scoring criteria move over. |

### Rework (1), approved for this batch

| Skill | Becomes | Why |
|---|---|---|
| `plan-trials-of-improved-practices` | A skill for planning a user test of a prototype | Trials of Improved Practices is named in one source. The wider task, testing a prototype with a few people before a pilot, is named in six and no skill covers it. |

### Park (12)

| Skill | Test it failed | Rebuild candidate |
|---|---|---|
| `assess-scarcity-load` | Common: sources use scarcity as a lens inside diagnosis and as a timing technique, which `choose-delivery-moment` covers | Maybe |
| `identify-positive-deviants` | Common: one source | Yes |
| `design-habit-anchor` | Common: one source, plus one loose mention | Yes |
| `design-social-recognition` | Common: one source | Maybe |
| `plan-collective-pledge` | Common: no source names a pledge; public commitments sit in `design-commitment-device` | Maybe |
| `specify-earmark-label` | Common: one source | Maybe |
| `design-mystery-client-protocol` | Common: the two sources that mention mystery shopping mean experiencing a service, not measuring providers | Maybe |
| `design-adaptive-message-experiment` | Common: one source for adaptive allocation; multi-arm tests sit in `choose-trial-design` | Yes |
| `draft-barrier-analysis-questionnaire` | Common: one source family (DBC). Considered for the lane and declined for now | Yes, with the next row |
| `analyze-doer-nondoer-differences` | Common: one source family (DBC) | Yes |
| `adjust-for-multiple-comparisons` | Common: one source (JPAL). Held for a possible later batch on analysis, statistics, and methods | Yes, in that batch |
| `audit-llm-qualitative-coding` | Common: no source; the practice is newer than all of them | Yes |

### Cut by decision (4)

`build-user-funnel`, `diagnose-funnel-weak-link`, `design-golden-dataset`, `design-evidential-experiment`. These are the AI evaluation set, removed on 2026-11-10.

One note for the rebuild: the task under `diagnose-funnel-weak-link`, finding where people drop off along a mapped process, is named in four sources (BD, BUS, BIT, WB). It overlaps the journey map that is claimed on the tracker.

## Gaps

Tasks named in two or more sources that no skill covers.

| Gap | Named in | Status |
|---|---|---|
| Prototype and user-test before piloting | 6 | Built in this batch as the rework above |
| Observe or experience the service in the field | 5 | Logged, not built in this batch |
| Choose a quasi-experimental design | 5 | Logged, not built in this batch |
| Map stakeholders | 6 | Logged; general project practice |
| Sampling plan | 4 | Logged |
| Communicate results | 4 | Logged |
| Technique: simplification | 3 | Logged; partly in `draft-lever-content` |
| Technique: salience and personalization | 2 | Logged |
| Journey or behavioral map | 5 | Claimed on the tracker |
| Pre-mortem or risk review | 4 | Claimed on the tracker |
| Find a validated measure | 4 | Claimed on the tracker |
| Personas or segmentation | 3 | Claimed on the tracker |
