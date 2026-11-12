---
name: define-key-behavior
description: >-
  Use when a program goal is vague ("increase savings", "build trust in the
  vaccine", "improve engagement") and no specific behavior has been chosen,
  or when a team has a list of candidate behaviors and must commit to one.
  Scores the candidates, picks one, and states it as who does what, when. Do
  not use when a specific, observable behavior is already agreed; to find out
  why it is not happening, use decompose-comb-barriers. Not for finding what
  research exists on the goal; use assess-evidence-base.
license: CC-BY-4.0
metadata:
  title: Turn a vague goal into one clear behavior
  type: atomic
  stage: define
  version: "0.3.0"
  status: draft
  authors: "Nikhil Ravichandar, Joe Speed, Zezhen Wu"
  org: IL
  tested_in: not-applicable
  tags: "behavior-change-wheel, apease, behavior-definition"
  consumes: "program-goal"
  produces: "target-behavior-brief"
---

## What it does

Turns a vague program goal into one observable behavior, stated as who does what, when.

**What this adds:** lists at least three candidate behaviors before choosing, one of them outside what the program has already built; scores every candidate on the same four criteria and labels each score as data, audience input, or team guess; refuses an outcome or a two-part action as the behavior; and keeps the runners-up, ranked, as the fallback.

## When to use it

### Use it when
- A program document, funder brief, or stakeholder states the goal as an outcome, attitude, or aspiration: "increase financial resilience", "improve engagement", "reduce stigma"
- Someone asks "what should we actually be trying to change?" or "which behavior are we targeting?"
- A team has a list of candidate behaviors and must commit to one
- A team is about to diagnose barriers or design an intervention for a goal with no named actor, action, or time window

### Do not use it when
- A specific, observable behavior with a named actor and time window is already agreed; to find out why it is not happening, use `decompose-comb-barriers`
- The team wants to know what research exists on the goal; use `assess-evidence-base`

## Before you start

Ask these before producing the choice. Do not ask anything the user has already answered.

1. **Required.** The program goal as stated, and who stated it.
2. **Required.** A rough population and setting: who the program reaches, where, through what channel, and any fixed constraints (budget, timeline, what is already built).
3. Optional. Candidate behaviors the team already has, including any it is leaning toward.
4. Optional. Evidence or data that bear on the candidates: what has been tried, how many people already do each behavior, what the audience says it would do.

If 1 or 2 is missing, ask and stop. If 3 is missing, generate the candidates. If 4 is missing, score from judgment, label every such score "team guess", and say so under "What would change this choice".

## What it draws on

- Michie, S., Atkins, L., & West, R. (2014). *The Behaviour Change Wheel: A Guide to Designing Interventions*. Silverback Publishing. Supports: the order (list behaviors, select one, specify it); the four selection criteria of impact, ease of change, spillover, and ease of measurement; and APEASE (Affordability, Practicability, Effectiveness, Acceptability, Side-effects and safety, Equity).
- Kettle, S., & Persian, R. (2022). *Target, Explore, Solution, Trial, Scale*. The Behavioural Insights Team. https://www.bi.team/wp-content/uploads/2022/11/BIT-Handbook-How-to-run-simple-BI-projects.pdf Supports: the target statement (whose behavior, what, when), and the rule that the target is a behavior, not an attitude.
- Kneebone, S., Smith, L., & Fielding, K. (2017). The Impact-Likelihood Matrix: A policy tool for behaviour prioritisation. *Environmental Science & Policy*, 70, 9–20. https://doi.org/10.1016/j.envsci.2016.11.013 Supports: scoring impact and likelihood of adoption separately.

**Where the evidence comes from:** This is a prioritization procedure and makes no claim about how people behave. Its sources come from UK health psychology and the UK's Behavioural Insights Team. What is local is the scores: which behaviors people are likely to take up is a question for members of the audience, not for staff.

**Replication status:** Not applicable. None of the sources tests whether two teams score the same candidates alike, so treat the table as reasoning made visible.

## How to do it

1. **Restate the goal** as given.
2. **List the candidates:** every behavior that could move the goal, at least three, each as who does what. At least one must sit outside the products and channels the program already has; variations on the existing app are one idea ranked three times. Reject any that is an outcome ("reduce anemia") or needs "and" to state.
3. **Score every candidate** on four criteria and write the basis beside each score: data (name the source), audience input, or team guess.
   - **Impact (1 to 5):** if the people who do not yet do this did it, how far would the goal move? Record the share already doing it; a behavior most people already do has little room left.
   - **Likelihood of change (1 to 5):** how likely the audience is to take it up, given what stands in the way.
   - **Spillover (+, 0, −):** whether doing it makes other useful behaviors more or less likely.
   - **Measurable:** how the program would observe it.
4. **Select the target** and write it as who, what, when, then as one sentence with no "and".
5. **Explain the choice** in two to four sentences that point at the deciding scores and say which are team guesses.
6. **Screen the selected behavior against APEASE** and list any concern.
7. **Rank the runners-up**, one line each on why it ranked lower.
8. **Say what would change the choice:** usually the audience's own likelihood ratings or a count of who already does the behavior, with the cheapest way to get each.

See `references/worked-example.md` for a complete run.

## Output template

```markdown
<Two or three plain sentences to the user: the behavior chosen, the score that decided it, and which scores are team guesses that the audience could overturn.>

# The behavior to target for <the goal, in a few words>

**Program goal (as given):** <the goal, verbatim or lightly cleaned>

## Candidates

| Candidate behavior | Impact (1–5) | Already doing it | Likelihood of change (1–5) | Spillover to other behaviors | Measurable by |
|---|---|---|---|---|---|
| <who does what> | <score: reason (data: <source> / audience input / team guess)> | <share or band (basis)> | <score: reason (basis)> | <+ / 0 / −: reason> | <how it would be observed> |

## Selected target behavior
- **Who:** <actor>
- **What:** <one observable action>
- **When:** <moment or window>
- **In one sentence:** <who does what, when; no "and">

## Why this one
<two to four sentences pointing at the scores that decided it; which of them are team guesses>

## Concerns about the chosen behavior (APEASE)
<any of affordability, practicability, effectiveness, acceptability, side-effects and safety, or equity that the selected behavior raises; or "None identified.">

## Runners-up, ranked
1. <candidate>: <why it ranked lower>

## What would change this choice
- <the score resting on the weakest basis, and the cheapest way to check it>

## Where you could go from here
<One line saying the choice of behavior is done.>
<Two or three next moves that fit what this run found, each with why it would help and when it fits. Candidates:
- `decompose-comb-barriers`, when the team wants to know why most of the audience is not doing the chosen behavior yet
- `audit-process-friction`, when the behavior runs through a process with steps, forms, trips, or waiting
- `diagnose-social-norm`, when whether people do it seems to depend on what others around them do or expect
- `plan-evaluation-design`, when the team needs to settle now how it will tell whether the behavior changed
- `assess-evidence-base`, when nobody has checked what has been tried for this behavior or audience
- a quick round with members of the audience, asking which candidates they would do next week, when the likelihood scores are team guesses>
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

- **Selecting what is easy to count.** App logins are easier to observe than saving that happens offline. "Measurable" is one criterion of four; it does not outrank impact.
- **A table filled in after the choice.** If one candidate wins every column, the scoring was reverse-engineered. Rescore, or say plainly that the table did not drive the choice.
- **Likelihood rated by staff.** Teams overrate how likely people are to adopt what the team can deliver. A likelihood score with no audience input is labeled a guess, and the output says how to get the audience's answer.

## When to bring in a specialist

Tell the user to consult a behavioral scientist or the program's monitoring and evaluation lead when:
- The top two candidates are close and the tie-breaker is a team guess
- A candidate carries clinical, safety, or legal consequences (medication, reporting violence, financial products with downside risk), so the side-effects line needs domain expertise
- Stakeholders disagree about what the goal means, so impact scores differently for the funder and the implementer; selection is then a governance decision

Bring them: the candidate table with its bases, the ranked runners-up, and the list of what would change the choice.
