---
name: plan-agency-measurement
description: >-
  Use when a team building or evaluating a digital or AI tool has said what
  agency means for its users and must decide how to measure it: "what do we
  ask in the app and what in the phone survey?", "which scales could we
  use?", "can a model score agency in our chat logs?". Gives each chosen
  cell of The Agency Fund's 2x2 agency framework a measure on the platform
  and one off it, with the checks each needs. Do not use when nobody has
  said what agency means here; use define-agency-construct. Not for writing
  the questionnaire; use draft-survey-items.
license: CC-BY-4.0
metadata:
  title: Plan how to measure agency in a digital tool
  type: atomic
  stage: measure
  version: "0.2.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  tested_in: beyond-western-differs
  tags: "agency, measurement, psychometrics, survey-design, ai-eval"
  consumes: "agency-definition"
  produces: "measurement-plan"
---

## What it does

Plans how to measure a defined agency construct for the users of a digital or AI tool.

**What this adds:** gives each focus cell of the 2x2 agency framework one measure on the platform and one off it, each tied to a moment; keeps usage and ratings out of the grid; quotes scale items only from a source opened in the session; and sizes the testing to the claim, with the result that would mean keep, revise, or drop.

The method is The Agency Fund's, written with Google Jigsaw. On-platform data come from inside the tool (in-app questions, logs, digital traces); off-platform data from outside it (surveys, observation, interviews, records).

## When to use it

### Use it when
- A team has named its agency constructs and asks what to measure, in the app and off it
- A team asks which published scales fit, and what their items are
- A team proposes a measure (an in-chat question, a borrowed scale, a model scoring chats) and asks whether it will hold up

### Do not use it when
- Nobody has said what agency means for these users; use `define-agency-construct`
- The team wants the questionnaire written; use `draft-survey-items`
- The question is an impact evaluation's outcome, comparison, or sample; use `plan-evaluation-design`

## Before you start

Ask only what the user has not answered, one question at a time, with a suggested answer.

1. **Required.** The agency definition: named constructs, each placed in a cell of the 2x2 agency framework, and the cells in focus.
2. **Required.** The decision the plan supports: improve the product, compare versions, report to a funder, or publish. It sets how much testing is enough.
3. Optional. The data the team has, and what more it can afford.
4. Optional. Published items found by search, or drafted examples?
5. Optional. What users consented to for logs, and whether scores will be compared across groups, languages, or sites.

If 1 or 2 is missing, ask and stop; a measure with no construct ("GPT will score agency 1 to 5") lacks 1, so ask what it should capture. For 3 to 5, assume and say so: on-platform data plus one small off-platform round; drafted examples; no consent to analyze conversations; no comparison.

## What it draws on

- Wu, Z., Goldberg, B., & Xu, R. (2026, July 1). *Measuring agency in a digital context*. The Agency Fund. https://theagencyfund.substack.com/p/measuring-agency-in-a-digital-context Supports: the whole method. The grid is the post's figure "Measuring agency: data collected on- and off-platform".
- Wu, Z., On, R., Walsh, J., Korley, E., Madon, T., & Wong, L. (2025). *AI Evaluation in the Social Sector: A Living Playbook*. https://eval.playbook.org.ai/ Supports: step 3, three in-app items or fewer, asked in the chat right after a task.
- Laajaj, R., & Macours, K. (2021). Measuring skills in developing countries. *Journal of Human Resources*, 56(4), 1254–1295. https://doi.org/10.3368/jhr.56.4.1018-9805R1 Supports: step 5; measures validated mostly in high-income countries carried systematic error in Kenya.

**Where the evidence comes from:** Agency measures were mostly built in wealthy Western countries. Tested elsewhere they behave unevenly: four agency scales held up in six African countries, but small changes to decision questions changed conclusions in Ecuador, Uganda, and Yemen. Check that users read each item as intended, in their language and channel.

**Replication status:** Mixed. Methods for testing a scale are long established; whether agency measures carry across countries is contested.

## How to do it

1. **Check each construct** is named for a task ("confidence deciding what to plant", not "agency") and placed in a cell; place any that is not, and say so.
2. **Map existing data onto the grid**, marked "(have)". Usage, retention, and ratings go in no cell: they measure engagement or satisfaction.
3. **Give each focus cell one on-platform and one off-platform measure, each tied to a moment**, from `references/measurement-options.md`. Look past surveys to logs, observation, rated work, and what users can do without the tool. Keep in-app checks to three items or fewer, asked when the construct is live (after a decision or a setback). Mark model coding of conversations "experimental": its errors can follow who the user is.
4. **Fill the details.** Quote published items only from a source opened in this session; otherwise give the citation, "not accessed", and a search query, or draft items labeled "drafted example, not from the literature".
5. **Say use, adapt, or build.** A scale built elsewhere is "adapt" until users here have said what its items mean.
6. **Size the testing to the claim** with `references/validation.md`: the cheapest check that supports it, and the result that means keep, revise, or drop.
7. **Name what should not go ahead as proposed** (a sensitive question in a chat on a shared phone; country averages from an untested scale) and what to report instead.
8. **Stop.** Do not write the questionnaire or design the comparison.

See `references/worked-example.md` for a complete run.

## Output template

```markdown
# Agency measurement plan: <tool>

**Definition:** <the working definition, the constructs, and the focus cells, as the team gave them>
**Decision this plan supports:** <improve the product / compare versions / funder report / published claim>
**Assumed:** <anything assumed because the team could not say; or "nothing">
**Do not go ahead as proposed:** <what is unsafe or cannot support the claim, and what to report instead; or "nothing">

## Measures on the 2x2 agency framework
| | With respect to the end goal: <goal> | With respect to the digital tool: <tool> |
|---|---|---|
| **Internally experienced** (thoughts and feelings) | **On-platform:** <measure, moment> (#1)<br>**Off-platform:** <measure, moment> (#2) | <... or "not in focus"> |
| **Externally expressed** (choices and actions) | <...> | <...> |

Data the team already collects is marked "(have)".
**In no cell:** <each usage, retention, or rating metric the team tracks, and what it measures>

## Measure details
| # | Instrument | Items | Source | Evidence, and what to check here | Use, adapt, or build |
|---|---|---|---|---|---|
| 1 | <name, length, response format> | <items quoted from a source opened in this session; or "not accessed: <reason>"; or "drafted example, not from the literature: ..."> | <theory; authors, year, link> | <tested with whom and where; what to check with these users> | <which, and how> |

## Testing, sized to the claim
| # | Check | Keep if | Revise or drop if |
|---|---|---|---|
| 1 | <the cheapest check that supports the claim> | <result> | <result, and what to do then> |

**Specialist to bring in:** <who, for what; or "none for this claim">

## What to find out next
- <an open measurement question>: "<a search query ready to paste>"
```

## Where it goes wrong

- **A scale chosen for its name.** A scale titled "agency" or "empowerment" can measure something other than the team's construct; let the construct's theory pick the instrument.
- **The tool asking about itself.** "Has this app made you more confident?" invites users who like the app to say yes whatever changed. Ask about the task and the person, not the product.
- **Opposite signals averaged.** When a log signal and a self-report move apart, report both. Users who feel more capable while leaning harder on the tool are what the grid exists to catch.

## When to bring in a specialist

Tell the user to bring in:
- A psychometrician or survey methodologist, when the claim goes to a funder or a journal, or scores will be compared across groups or languages
- A researcher who has checked model coding against human coders, when a model will code conversations
- An ethics board and a researcher in women's safety, before asking women, girls, or minors who decides at home; asking can put them at risk
- A data protection lead, before analyzing conversations of minors or about health

Bring them the definition, this plan, and a description of the users and their consent.
