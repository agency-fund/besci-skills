---
name: map-audience-context
description: >-
  Use when a program names its audience only by a broad label ("smallholder
  farmers", "first-time mothers") and nobody has said where and when those
  people make the decision, or who else has a say. Names a specific group,
  the decision moment, the channels that already reach them, and the
  assumptions nobody has checked locally. Do not use when the audience and
  setting are already described and the team must choose a behavior; use
  define-key-behavior. Not for what published research says about the
  population; use assess-evidence-base.
license: CC-BY-4.0
metadata:
  title: Map your audience and their setting
  type: atomic
  stage: define
  version: "0.2.0"
  status: draft
  authors: "Joe Speed, Zezhen Wu"
  org: IL
  tested_in: not-applicable
  tags: "audience, context, cultural-psychology"
  consumes: "program-goal"
  produces: "audience-context-brief"
---

## What it does

Replaces a broad audience label with a specific group of people at the moment they make the decision the program cares about.

**What this adds:** labels every claim by its source (seen by the team, told by someone who lives it, or general knowledge of the country or sector); lists only channels that reach the group today; refuses to name a place the input never mentioned; and checks, every time, for assumptions carried over from wealthy Western settings, including the assumption that the named person decides alone.

## When to use it

### Use it when
- A program goal names its population the way a funder would ("smallholder farmers", "gig workers") with nothing on where or when the choice is made
- Someone asks "who exactly are we talking about, and where does this decision actually happen for them?"
- A team is about to assume bank accounts, smartphones, literacy, or a person who decides alone, for a population nobody on the team has observed

### Do not use it when
- The group, the decision moment, and the channels are already described and the team must choose a behavior; use `define-key-behavior`
- The question is what published research says about the population; use `assess-evidence-base`
- The team wants a channel or message for a future intervention; use `select-intervention-levers`

## Before you start

Ask these before producing anything. Do not ask anything the user has already answered.

1. **Required.** The program goal as stated, and whatever is known about the population and setting.
2. **Required.** Where that knowledge comes from: which sites the team has visited, who told them what, which reports.
3. Optional. What the input already assumes about infrastructure or about who decides.
4. Optional. Whether the population holds groups with different decision moments (men and women, fixed and itinerant traders).

If 1 is missing, ask and stop. If 2 is missing, ask once; if the user does not know, label every claim "general knowledge" and say so under open questions. If 3 or 4 is missing, proceed and list the gaps under open questions.

## What it draws on

- Jang, C., Koki, E., Nyaga, R., Okafor, A., Singh, J., Vang, A., & Wendel, S. (2024). *The Busara toolkit: leveraging behavioral science for development*. Busara Groundwork No. 10. https://doi.org/10.62372/WQSB6195 Supports: describing context as people, a place, a moment, and an activity together; recording what the team knows as insiders or as outsiders.
- The TOPS Program (2017). *Designing for Behavior Change: A Practical Field Guide*. https://web.archive.org/web/20180329030310/http://fsnnetwork.org/sites/default/files/designing_for_behavior_change_a_practical_field_guide.pdf Supports: describing the group by its daily routine as well as its demographics; naming the people who approve or disapprove of the behavior.
- Henrich, J., Heine, S. J., & Norenzayan, A. (2010). The weirdest people in the world? *Behavioral and Brain Sciences*, 33(2–3), 61–83. https://doi.org/10.1017/S0140525X0999152X Supports: the assumption check. On many behavioral measures, people in Western, industrialized, rich societies are often outliers.

**Where the evidence comes from:** This is a description procedure and makes no claim about how people behave. Its sources are a research group based in Kenya, a field guide from a US-funded food security program, and a review of comparisons across societies. Everything in a brief is local; what a reader checks is the source label on each claim.

**Replication status:** Not applicable. No source tests whether two teams would describe the same audience alike. The source labels are this skill's own.

## How to do it

Give every claim one source label: **seen by the team** (say where), **told by someone who lives it**, or **general knowledge** of the country or sector.

1. **Restate the goal** as given.
2. **Narrow the population.** Write the label as given, then the narrowest group the input supports: role, age range, site, daily routine. If the input supports only a region, say so. Never name a district, clinic, or market the input did not mention; a wrong specific misleads more than a named gap.
3. **Describe the decision moment:** where the person is, what they are doing, and what they have in hand when the choice is made. A time of day is not enough.
4. **Name who else is there or has a say:** who watches, who approves or disapproves, who receives the result.
5. **List the channels that reach the group today**, each with how often. Leave out any channel that does not yet exist.
6. **State the constraints at that moment:** physical, social, or economic.
7. **Run the assumption check**, and write "none found" if that is the result. Cover two kinds:
   - **Infrastructure:** formal bank accounts, phones and connectivity, literacy, formal institutions.
   - **Who decides:** the named person treated as deciding alone when a spouse, elder, household, or group can say no.

   For each assumption, say whether it is confirmed locally and what to check.
8. **Write the open questions:** every inference, every site not visited, every claim that rests on one visit or one informant.

See `references/worked-example.md` for a complete run.

## Output template

```markdown
# Audience and context brief

**Program goal (as given):** <the goal, verbatim or lightly cleaned>

## Population
- **As named:** <the funder's or stakeholder's label, verbatim>
- **Narrowed to:** <the narrowest group the input supports; or "the input supports only <region>", with the gap listed under open questions>

## Decision moment
- **Where and when the choice is made:** <place, activity, what is in hand>. **Source:** <seen by the team: where / told by someone who lives it / general knowledge>
- **Who else is there or has a say:** <...>. **Source:** <...>

## Channels that reach them today
- <channel>: <how often it reaches them>. **Source:** <...>

## Constraints at the decision moment
- <physical, social, or economic constraint>. **Source:** <...>

## Assumptions carried over from wealthy Western settings
- **Infrastructure:** <assumption in the input, or "none found">. **Confirmed locally?** <yes / no / unknown>. **What to check:** <...>
- **Who decides:** <assumption in the input, or "none found">. **Confirmed locally?** <yes / no / unknown>. **What to check:** <...>

## Open questions
- <what the brief inferred, which site is unconfirmed, or which claim rests on one visit; and how to check it>
```

## Where it goes wrong

- **A longer label.** "Smallholder farmers in rural areas who grow crops" is the same abstraction with more words.
- **Sliding into segments.** Where the input covers groups with different decision moments, describe the one it supports best and list the rest as an open question; do not write personas.
- **The opposite stereotype.** "The husband decides" is as much an assumption as "she decides alone". Neither is confirmed until someone from the setting says so.

## When to bring in a specialist

Tell the user to consult a local researcher, a social scientist who knows the setting, or a member of the population when:
- Who decides is unknown and the behavior touches household money, health, fertility, or gender roles
- Every claim is labeled "general knowledge" and nobody on the team has been there; the brief is then a list of hypotheses
- The input covers groups with different decision moments and does not say which the program is for

Bring them: the brief with its source labels, the assumption check, and the open questions.
