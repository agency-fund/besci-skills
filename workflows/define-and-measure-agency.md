---
name: define-and-measure-agency
title: Define and measure agency
description: >-
  For a team building or evaluating a digital or AI tool that wants to say
  whether the tool builds its users' agency: define what agency means for these
  users, plan one measure inside the tool and one outside it for each part the
  team cares about, and, if the plan calls for new questions, write them. Ends
  with an agency definition placed on The Agency Fund's 2x2 agency framework, a
  measurement plan with the check each measure needs, and optionally draft
  survey questions. Does not test the questions with users, design a
  comparison, or analyze results.
license: CC-BY-4.0
metadata:
  version: "0.1.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  stages: "define, measure"
  skills: "define-agency-construct, plan-agency-measurement, draft-survey-items"
  tags: "agency, measurement, ai-eval, survey-design"
---

## What it is for

A team says its chatbot or app "builds agency" or "empowers users", and the evidence offered is usage, retention, or ratings. This workflow makes the team say first, in its own words, what agency means for its users, and then plans how to measure exactly that, inside the tool and outside it. Two steps in two stages, with an optional third that writes the survey questions.

**Process it follows:** The Agency Fund's agency framework (Wu, Goldberg, & Xu, 2026, *Measuring agency in a digital context*): define agency as named constructs on a 2x2 grid, then measure each chosen cell both on and off the platform.

## When to use it

- When a team wants to measure, claim, or improve its users' agency and has not said what agency means for them
- When a report credits a tool with building agency or empowerment on the strength of active users or ratings
- When the constructs are already named and placed on the grid; start at step 2
- Not when the program targets one offline behavior, such as attending a clinic; use `define-key-behavior` and the workflow "From a goal to a tested intervention" instead
- Not when the question is whether the tool changed agency compared with no tool; that needs a comparison, which starts with `choose-trial-design` once the measures are set

## Skills in this workflow

| Step | Skill | Version | Relationship | What carries forward | Human decision point |
|---|---|---|---|---|---|
| 1 | `define-agency-construct` | 0.2.0 | start | agency definition: the team's own words, named constructs, their place on the 2x2 agency framework, the cells in focus, and the signs that the tool is wearing agency down | Choose which cells of the grid to focus on, and say why; the other cells stay open on purpose |
| 2 | `plan-agency-measurement` | 0.2.0 | after 1 | measurement plan: one on-platform and one off-platform measure for each focus cell, each marked use, adapt, or build, with the check that would mean keep, revise, or drop | Accept what the plan says not to run as proposed, and choose which measures need questions written or adapted |
| 3 | `draft-survey-items` | 0.2.0 | after 2, optional | draft survey questions, each with the reading it should get, a read-aloud script, and a design check | Approve the questions for a test with users; until users have said what they mean, they are untested |

Relationship values: `start`, `after N`, `parallel with N`, `independent`, `optional`.

## How to run it

The order is a recommendation. Start at any step if you already have what it needs, and use any of these skills on its own.

1. Run `define-agency-construct` with a description of the tool and its users (what it does, for whom, where, in what language) and the goal it serves in users' lives off the platform. Then answer the hard question in the team's own words: what would a user with more agency think, feel, choose, or do differently? If the team cannot say, the skill offers one example per cell and asks which comes closest. It will not write the definition for you.
2. Stop and choose the focus cells. Covering all four commits the team to measuring things it does not care about. If users are women, girls, or minors, say who else shapes their decisions; a decision made with family is not less agency by default.
3. Run `plan-agency-measurement` on the definition, and name the decision the measures will support: improving the product, comparing versions, reporting to a funder, or publishing. A funder report or a paper needs more testing than a product change. Say what data the team already has and what users agreed to when they shared their conversations.
4. Stop and read the plan's "Do not go ahead as proposed" line and its testing table. A scale built elsewhere stays marked "adapt" until users here have said what its items mean.
5. If the plan calls for questions the team must write or adapt, run `draft-survey-items`. Give it each construct's one-line definition from the agency definition, and the respondents and channel from the plan's off-platform measures. Leave a published scale the plan marks "use" in its published wording.
6. Before any question reaches users at scale, check that they read it as intended with `draft-cognitive-interview-script`, and use `translate-survey-instrument` if it must work in another language.

## Worked example

This example is illustrative; the tool and its details are invented.

A team runs a WhatsApp chatbot that gives smallholder farmers in western Kenya planting and pest advice in Swahili. Its funder report says weekly users doubled and calls this growing agency. Step 1 sets usage aside as a measure of engagement and records what the team means: farmers who decide for themselves what and when to plant, and who can explain their choice. That becomes two constructs: confidence deciding what to plant (thoughts and feelings, about the farming goal) and making the planting decision with the bot as one source among several (choices and actions, about the tool). The team focuses on those two cells and leaves the other two open. Erosion would look like a farmer who asks the bot to choose and cannot say why. Step 2 gives the confidence cell a one-question check in the chat right after a planting question, plus a phone survey at the end of the season; the decision cell gets a measure from the chat logs (how often a farmer asks the bot to choose for them) and questions in the same phone survey. The plan marks the phone survey "build" and says not to compare scores between the two counties until farmers in both have been asked what the questions mean. Step 3 writes the phone survey's questions as counts over the season, every answer option in words for an interviewer to read aloud, and names the question most likely to be misread.

## Where it goes wrong

- Letting usage or ratings stand for agency. Heavy use and high ratings can go with a loss in what people can do without the tool.
- Treating the team's definition as the users'. The definition is a guess until users have been asked how they would describe it.
- Choosing a scale for its name. A scale called "empowerment" may measure something other than the team's construct; the construct picks the instrument.
- Letting the tool ask about itself. "Has this app made you more confident?" invites users who like the app to say yes, whatever changed.
- Adding step 3's draft questions into one score. Untested questions have no shown reliability.

## When to bring in a specialist

- The claim goes to a funder or a journal, or scores will be compared across groups, languages, or sites: a psychometrician or survey methodologist. Bring the definition, the plan, and a description of the users.
- The plan would ask women, girls, or minors who decides at home: an ethics board and a researcher in women's safety, before any question is asked, because asking can put them at risk.
- A model will score users' conversations: a researcher who has checked model coding against human coders, and a data protection lead if users are minors or the chats are about health.
