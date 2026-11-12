---
name: select-intervention-levers
description: >-
  Use when field evidence has confirmed why a behavior is not happening and
  the team must decide what kind of intervention to try: "given this barrier,
  what could we do?", or a team about to "just send a text". Lists the kinds
  of intervention a published table links to that kind of barrier, scores
  each for feasibility, and names one technique with ranked fallbacks. Do not
  use when the barrier is still a guess; use decompose-comb-barriers. Not for
  writing the content; use draft-lever-content.
license: CC-BY-4.0
metadata:
  title: Choose interventions for a confirmed barrier
  type: atomic
  stage: design
  version: "0.3.0"
  status: draft
  authors: "Joe Speed, Zezhen Wu"
  org: IL
  tested_in: not-applicable
  tags: "behavior-change-wheel, behavior-change-techniques, apease"
  consumes: "barrier-diagnosis"
  produces: "intervention-levers"
---

## What it does

Chooses the kind of intervention that fits one confirmed barrier.

**What this adds:** reads the eligible kinds of intervention from the Behaviour Change Wheel's published table, bundled with the skill, instead of brainstorming; says whether the team's own idea is on that list; scores each kind on six feasibility criteria, with practicability judged against what the implementer controls; names one technique, not a category; and ranks the kinds that lost as fallbacks.

## When to use it

### Use it when
- Field evidence has confirmed why a behavior is not happening, and someone asks "given this barrier, what could we do?"
- A team is about to commit to an idea ("let's send a text") without checking that it can change this kind of barrier
- A pilot aimed at this barrier failed and the team wants the next thing to try

### Do not use it when
- The barrier is a guess nobody has checked; use `decompose-comb-barriers`
- The kind of intervention is chosen and has its own skill: `select-default-option`, `design-reminder-schedule`, `choose-delivery-moment`, `choose-message-frame`, `design-commitment-device`, `design-incentive-scheme`, `write-social-norm-message`, `design-feedback-report`, `draft-implementation-intention-prompt`, or `select-messenger`
- The intervention is chosen and the team needs the words, script, or sign; use `draft-lever-content`

## Before you start

Ask these before making the choice. Do not ask anything the user has already answered.

1. **Required.** The one confirmed barrier, with the evidence: who was asked or observed, and what they said or did.
2. **Required.** The behavior the barrier blocks: who does what, when.
3. **Required.** What the implementer controls: budget, channels, staff, partners, and what needs someone else's permission.
4. Optional. An intervention idea the team already favors.

If 1 or 2 is missing, or the barrier is one of several untested guesses, ask and stop. If 3 is missing, ask once; then mark every practicability score "?" and put the constraints first in the list to confirm.

## What it draws on

- Michie, S., van Stralen, M. M., & West, R. (2011). The behaviour change wheel: A new method for characterising and designing behaviour change interventions. *Implementation Science*, 6, 42. https://doi.org/10.1186/1748-5908-6-42 Supports: the six kinds of barrier, the nine kinds of intervention ("intervention functions"), and the table linking them, reproduced in `references/function-matrix.md`.
- Michie, S., Atkins, L., & West, R. (2014). *The Behaviour Change Wheel: A Guide to Designing Interventions*. Silverback Publishing. Supports: choosing the kind before the technique, and the six APEASE criteria.
- Michie, S., Richardson, M., Johnston, M., et al. (2013). The behavior change technique taxonomy (v1) of 93 hierarchically clustered techniques: Building an international consensus for the reporting of behavior change interventions. *Annals of Behavioral Medicine*, 46(1), 81–95. https://doi.org/10.1007/s12160-013-9486-6 Supports: naming one technique, the smallest part of an intervention that can be described and repeated.

**Where the evidence comes from:** This is a selection procedure, not a finding about how people behave. Its table is its authors' judgment and comes from UK health psychology; a search found no study testing whether choosing this way leads to better interventions. Every feasibility score is local: cost, who must agree, what the audience accepts.

**Replication status:** Not applicable. Coders classifying existing strategies with the wheel agreed on 79% to 88% of items, which tests the labels, not the choice.

## How to do it

1. **Restate the barrier with its evidence.** If nothing confirmed it, stop: an intervention chosen for the wrong barrier wastes a pilot.
2. **Classify the barrier as one of six kinds**, defined in `references/function-matrix.md`, and quote the evidence that puts it there. A barrier that fits two kinds is two barriers; run each separately.
3. **Read that row of the table.** List only the kinds of intervention it links to this kind of barrier, marking any that only the authors' later table links. Add none from intuition. Name the kind of the team's own idea and say whether it is in the row.
4. **Give each eligible kind a form for this setting:** what would change, and who would change it.
5. **Score each kind on APEASE:** affordability, practicability, effectiveness, acceptability, side-effects and safety, equity. Use +, 0, −, or ? (not known), with a reason in every cell. Score practicability against what the implementer controls: a kind needing a permission, partner, or system they lack gets −, not a hopeful 0.
6. **Select one kind**, pointing to the cells that decided it. Do not select a kind with a − unless you state the change that removes it.
7. **Name the technique:** the specific thing that changes, who does it, where, and when. Add its taxonomy number and name; mark a label given from memory "label to check".
8. **Rank the kinds that lost**, each with why it lost and what would make it worth trying.
9. **List what to confirm before design starts:** permissions, costs, and every "?".

See `references/worked-example.md` for a complete run.

## Output template

```markdown
<Two or three plain sentences to the user: the kind of intervention and the technique you would pick, the scores that decided it, and what has to be confirmed (a permission, a cost) before anyone designs it.>

# Choosing an intervention for <the barrier, in a few words>

**Behavior:** <who does what, when>
**Confirmed barrier:** <the barrier, as the team stated it>
**Evidence that confirmed it:** <who was asked or observed; what they said or did>
**Kind of barrier:** <one of the six>, because <the evidence that puts it there>

## Kinds of intervention the Behaviour Change Wheel's table links to this barrier

| Kind | Form it would take here |
|---|---|
| <kind from the row> | <what would change, and who would change it> |

**The team's own idea:** <the idea, its kind, and whether that kind is in the row; or "none given">

## How feasible each one is here (APEASE)

| Kind | Affordability | Practicability | Effectiveness | Acceptability | Side-effects and safety | Equity |
|---|---|---|---|---|---|---|
| <kind> | <+ / 0 / − / ?: reason> | <...> | <...> | <...> | <...> | <...> |

## The kind I'd choose, and the technique
- **Kind:** <one kind>, because <the cells that decided it>
- **Technique:** <the specific thing that changes; who does it; where and when>
- **Label in the behavior change technique taxonomy:** <number and name; or "label to check: <label>">

## If it fails: the other kinds, ranked
1. <kind>: <why it lost; what would make it worth trying>

## What to confirm before design starts
- <a permission, a cost, or a "?" that could change the selection>

## Where you could go from here
<One line saying the choice is made.>
<Two or three next moves that fit what this run found, each with why it would help and when it fits. Candidates:
- `draft-lever-content`, when the technique needs words (a message, a script, a sign) and what is listed to confirm is in hand
- a skill made for the chosen technique, such as `select-default-option`, `design-incentive-scheme`, or `design-reminder-schedule`, when the technique is one of those
- `plan-prototype-test`, when a sketch of the technique could be shown to a few people from the audience before anything is built
- `draft-tdf-interview-guide`, when the barrier was confirmed only once, at one site, and checking it elsewhere costs less than a pilot
- the people whose permission, money, or cooperation the choice depends on, when a practicability score is − or ?>
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

- **Eligible read as effective.** The table says a kind of intervention could change this kind of barrier, not that it will here. The effectiveness score is usually a guess; say so in the cell.
- **Education as the reflex.** Information is the cheapest thing to produce, so it gets proposed for every barrier. The table links education to two kinds only: psychological capability and reflective motivation.
- **A table filled in to crown the favorite.** If the team's idea wins every column, rescore from the stated constraints, or say the table did not drive the choice.

## When to bring in a specialist

Tell the user to consult a behavioral scientist, and the program's legal or safeguarding lead where noted, when:
- The selected kind or the first fallback is coercion, restriction, or a payment or penalty, which can backfire or be unlawful (legal or safeguarding lead)
- The barrier sits in a policy or another organization's process, so every eligible kind needs someone else's cooperation; the first move may be partnership, not a technique
- The barrier was confirmed once, at one site, and the pilot is costly; more diagnosis may be cheaper

Bring them: the barrier with its evidence, the feasibility table, and the list to confirm.
