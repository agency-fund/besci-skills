---
name: define-agency-construct
description: >-
  Use when a team building or evaluating a digital or AI tool wants to
  measure, claim, or improve its users' agency but has not said what agency
  means for those users: "how do we measure agency for our app?", "is this
  empowerment or just engagement?". Turns the team's own meaning into named
  constructs placed on The Agency Fund's 2x2 agency framework. Do not use
  when the constructs are named and the question is how to measure them; use
  plan-agency-measurement. Not for a program that targets one offline
  behavior; use define-key-behavior.
license: CC-BY-4.0
metadata:
  title: Define what agency means for a tool's users
  type: atomic
  stage: define
  version: "0.3.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  tested_in: beyond-western-differs
  tags: "agency, social-cognitive-theory, self-determination-theory, measurement, ai-eval"
  consumes: "ai-product-account"
  produces: "agency-definition"
---

## What it does

Turns what a team means by its users' agency into named constructs (defined, measurable ideas such as self-efficacy) placed on The Agency Fund's 2x2 agency framework.

**What this adds:** starts from the team's own words; refuses usage and ratings as evidence of agency; matches each part to a named construct or keeps it as a local one; shows which of four cells the definition leaves open; does not count a shared decision as less agency by default; and lists observable signs that the tool is wearing agency down.

The method is The Agency Fund's, written with Google Jigsaw. It treats agency as "a person's capability to navigate toward the future they want", directed at the end goal or at the digital tool, and experienced internally (thoughts and feelings) or expressed externally (choices and actions).

## When to use it

### Use it when
- A team asks "how do we measure agency for our chatbot?" or "does our AI make people more capable or more dependent?" without saying what agency means for its users
- A report says the tool builds agency or empowerment, and the evidence offered is active users, retention, or ratings
- A team's idea of agency involves decisions made with a spouse, parents, or the community

### Do not use it when
- The constructs are named and the question is which measures or items to use; use `plan-agency-measurement`
- The tool targets one offline behavior; use `define-key-behavior`

## Before you start

Ask only what the user has not answered, one question at a time, each with a suggested answer inferred from what they said.

1. **Required.** The tool and its users: what it does, for whom, where, in what language.
2. **Required.** The end goal in users' lives, off the platform.
3. **Required.** What the team means by agency: what would a user with more of it think, feel, choose, or do differently?
4. Optional. What the tool wearing agency down would look like.
5. Optional. Who else shapes users' decisions. Ask whenever users are women, girls, or minors.

If 1 or 2 is missing, ask and stop. If the team cannot answer 3, offer one example per cell for this tool and ask which comes closest; never supply the definition yourself. If 4 is missing, propose signs marked "proposed; confirm".

## What it draws on

- Wu, Z., Goldberg, B., & Xu, R. (2026, July 1). *Measuring agency in a digital context*. The Agency Fund. https://theagencyfund.substack.com/p/measuring-agency-in-a-digital-context Supports: the whole method.
- Bandura, A. (2001). Social cognitive theory: An agentic perspective. *Annual Review of Psychology*, 52(1), 1–26. https://doi.org/10.1146/annurev.psych.52.1.1 Supports: step 8. Agency can be exercised through a proxy, so relying on a tool is not lost agency in itself.
- Bastani, H., Bastani, O., Sungu, A., Ge, H., Kabakcı, Ö., & Mariman, R. (2025). Generative AI without guardrails can harm learning: Evidence from high school mathematics. *Proceedings of the National Academy of Sciences*, 122(26), e2422633122. https://doi.org/10.1073/pnas.2422633122 Supports: step 2. With an unguarded AI tutor, practice grades rose 48%; once access was removed, students scored 17% below those who never had it.

**Where the evidence comes from:** Agency measures were often developed in wealthy countries and then applied elsewhere, mostly in sub-Saharan Africa and South Asia. Results across countries are uneven: a self-efficacy scale did not measure equivalently in Brazil, Colombia, and Germany, and spouses in Bangladesh disagreed about who decides. Check with users what counts as acting on their own goals.

**Replication status:** Contested. Reviews find no agreed definition or standard measure of agency, and evidence on agency toward AI tools is recent and thin.

## How to do it

1. **Record the team's meaning** in their words.
2. **Set engagement aside, if it was offered.** Say what each metric measures. Heavy use and high ratings can go with a loss in what people can do alone.
3. **Make the meaning concrete.** For each part: whose agency, over which decision or goal, in which part of life. Stop when a person could report each part or someone could observe it. Where users span settings, say where the definition may differ.
4. **Match each part to a construct and its theory**, using `references/frameworks.md`, and define the construct in one plain line. Where nothing fits, keep the team's wording as a "local construct".
5. **Do not mark shared decisions down.** A decision made with a spouse or family is not less agency by default. Ask whether the person wants a say in it.
6. **Place the constructs on the grid.** Mark each open cell with one example for this tool.
7. **Ask which cells to focus on.** Record the team's reason and what the open cells would catch. If the first message answers the required questions, draft the whole document with the focus marked "proposed; confirm".
8. **Write the signs of erosion** (the tool wearing agency down) for the chosen cells, as things a user could be seen doing. Relying on the tool by choice, while able to act without it, is not one.
9. **Stop.** Do not choose instruments or write survey items.

See `references/worked-example.md` for a complete run.

## Output template

```markdown
<Two or three plain sentences to the user: the working definition in plain words, which cells of the grid it covers and which it leaves open, and that it stays a hypothesis until users have been asked.>

# What agency means for <tool>'s users

**Context:** <users, the end goal in their lives, and the tool's role, in one or two sentences>
**In your words:** "<the team's own description of agency>"
**Working definition:** <one or two sentences: whose agency, over which decisions or goals, where>
**What your usage numbers measure instead:** <only if usage metrics were offered as evidence: each metric and what it measures>

## Your definition, matched to theory
| # | What you said | Construct (a defined, measurable idea) | Theory |
|---|---|---|---|
| 1 | "<their words>" | <construct, defined in one plain line> | <theory or framework; or "local construct: no established match"> |

## Where it sits in the 2x2 agency framework
| | With respect to the end goal: <goal> | With respect to the digital tool: <tool> |
|---|---|---|
| **Internally experienced** (thoughts and feelings) | <construct name (#), or "open: e.g., <example>"> | <...> |
| **Externally expressed** (choices and actions) | <...> | <...> |

**Focus:** <the cells the team chose, and why, in their words; or "proposed; confirm">
**Not covered by this focus:** <what the open cells would catch>
**Signs the tool is wearing agency down:** <observable signs in the chosen cells; and one example of chosen reliance that is not one>

## What to check before relying on this
- <the part of the definition the team was least sure of>
- <whether users themselves would describe agency this way, and how to ask them>

## Where you could go from here
<One line saying the definition is done.>
<Two or three next moves that fit what this run found, each with why it would help and when it fits. Candidates:
- `plan-agency-measurement`, once the team has confirmed the focus and wants measures for these constructs
- `choose-ai-eval-level`, when the team or its funder also needs to know which kind of evaluation of the tool comes next
- `define-key-behavior`, when the definition comes down to one thing users should do off the platform rather than agency
- a few users, asked what someone "in charge" of the goal does differently, when the team is unsure users would describe agency this way
- a psychologist, economist, or anthropologist who knows the setting, when a part found no match in theory or decisions are shared with family>
Questions you could ask next: "<question>" · "<question>"
```

<!-- shared: template/shared/voice.md. Edit it there, then run scripts/check_sync.py --fix. -->
**How to talk with the user**

- If the user asked a question rather than asked for this skill's output, answer the question first, in a few plain sentences. Then offer the run and say what it would add.
- Mark the run. When it starts, say so in one line: the skill, and what it will produce. When the output is done, say the run is finished. The user should always know when the library's method is in force.
- Talk with the person, not at them. Use their words for their program and the people in it, say why you ask each question, and say what you are unsure of. No praise, no filler.
- Say where each claim comes from: this skill's sources, your general knowledge, or nothing in the library. A number the sources do not give, such as how many interviews to run, is your judgment; say so, and why you chose it.
- End with the template's closing: two or three next moves that fit what this run found, each with its reason and when it fits, and one or two questions the user could ask next. Say which move you would lean toward and why; the user decides.
<!-- /shared -->

## Where it goes wrong

- **Filling every cell.** Covering all four cells commits the team to measuring things it does not care about. An open cell is a result, not a gap.
- **A general trait where the team meant a task.** "Confident deciding what to plant" is not general self-confidence. Keep the task in the construct's name.
- **The team's definition treated as the users'.** The document is a hypothesis until users have been asked.

## When to bring in a specialist

Tell the user to bring in a specialist when:
- The team is unsure how to define agency in its domain, or step 4 finds no match: a psychologist or economist who has defined or measured agency in that domain
- Agency here is shaped by custom or contested (family decisions, norms about who may decide): a psychologist, economist, or anthropologist who knows the setting

Bring them: the definition document, the team's own words, and a description of the users and setting.
