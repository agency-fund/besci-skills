---
name: identify-wise-intervention-target
description: >-
  Use when a team proposes a mindset message, a belonging story, or an
  affirmation exercise and nobody has said which question the audience is
  asking itself, or when someone asks "is this a mindset problem or a real
  barrier?". Names that question from the audience's own words and checks that
  the setting can deliver what a new answer would promise. Do not use when the
  barrier is cost, access, or a process; use select-intervention-levers. Not
  for writing the exercise itself.
license: CC-BY-4.0
metadata:
  title: Find the question a wise intervention must answer
  type: atomic
  stage: diagnose
  version: "0.2.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  tested_in: beyond-western-differs
  tags: "wise-interventions, belonging, growth-mindset, self-affirmation"
  consumes: "qualitative-data"
  produces: "wise-intervention-target"
---

## What it does

Names the question about themselves or their situation that an audience is asking, before any brief psychological exercise is drafted.

**What this adds:** works only from the audience's own words; tests each interpretation for a material barrier first; names one question under one of three needs; checks that the setting can deliver what a new answer would promise; and states the replication record for that kind of intervention without promising an effect.

The method is Walton and Wilson's. A wise intervention is a short exercise that changes how people interpret themselves or their situation, so that a cycle of setback, withdrawal, and further setback can turn.

## When to use it

### Use it when
- A team proposes a mindset message, a belonging story, or an affirmation exercise and nobody has said which question the audience is asking itself
- Interviews show people with the same resources acting differently according to how they read a setback: "math is not for people like me"
- Someone asks "is this a mindset problem or a real barrier?"

### Do not use it when
- The barrier is cost, access, time, information, or a process, so that removing it would fix the behavior; use `select-intervention-levers`
- The question is already named and the team wants the exercise; use `draft-values-affirmation` for self-integrity, `draft-belonging-story` for belonging, or `adapt-growth-mindset-message` for beliefs about ability

## Before you start

Ask these before producing anything. Do not ask anything the user has already answered.

1. **Required.** The behavior (who, what, when) and the evidence that a belief, not a material barrier, is holding it back.
2. **Required.** How the audience reads the situation, in their words: quotes from interviews, open survey answers, or field notes.
3. **Required.** What the setting offers after any message: can people improve (feedback, a second attempt), will they be included, is the institution on their side?

If 1 or 2 is missing, ask and stop. If 3 is unknown, name the question, mark the check "not verified", and say the exercise should not be built until it is.

## What it draws on

- Walton, G. M., & Wilson, T. D. (2018). Wise interventions: Psychological remedies for social and personal problems. *Psychological Review*, 125(5), 617–655. https://doi.org/10.1037/rev0000115 Supports: the whole method. An intervention targets a specific meaning; people make meaning to meet three needs (to understand, for self-integrity, to belong); and the capacity for better outcomes must already be present in the situation and in people.
- Walton, G. M., Murphy, M. C., Logel, C., et al. (2023). Where and with whom does a brief social-belonging intervention promote progress in college? *Science*, 380(6644), 499–505. https://doi.org/10.1126/science.ade4420 Supports: step 5. Among 26,911 students at 22 US institutions, the intervention worked only where students' groups had real opportunities to belong.
- Macnamara, B. N., & Burgoyne, A. P. (2023). Do growth mindset interventions impact students' academic achievement? A systematic review and meta-analysis with recommendations for best practices. *Psychological Bulletin*, 149(3–4), 133–173. https://doi.org/10.1037/bul0000352 Supports: step 6. Across 63 studies the pooled effect on achievement was a twentieth of a standard deviation (d = 0.05).

**Where the evidence comes from:** Most trials are with students in the United States. Elsewhere, short growth-mindset sessions raised test scores slightly in Peru and Indonesia and had no effect in Argentina, and a bundle of affirmation, gratitude, and aspirations exercises changed none of its target outcomes in Kenya. Check locally whether the question makes sense in the local idiom and whether the setting backs the message.

**Replication status:** Contested, and different for each kind. Belonging: replicated at scale in the US, under the condition above. Growth mindset: a pooled effect near zero. Self-affirmation: a large school replication found no effect.

## How to do it

1. **Tabulate how the audience reads the situation**, in their words: three to six interpretations, each with how many people said it.
2. **Test each interpretation for a material barrier.** If the cost, access, time, information, or process behind it were fixed, would the behavior follow? If yes, it is not a target here, however psychological it sounds. Otherwise mark it "meaning".
3. **Name one question, under one need.** To understand: "can I get better at this?". Self-integrity: "am I a good and capable person?". To belong: "do people like me belong here?". Choose one primary question and say why the others are secondary; two primary questions are two interventions to test separately.
4. **Name the moment the question becomes live:** a transition, a first failure, an evaluation, a visible comparison. A wise intervention is timed for the start of it.
5. **Check what the setting offers.** Write what a new answer would promise and, against it, what the setting provides. If the setting cannot deliver, say what would have to change first.
6. **State the record for that kind of intervention**, from "What it draws on". Promise no effect size.
7. **Stop.** Do not draft the story, the message, or the exercise.

See `references/worked-example.md` for a complete run.

## Output template

```markdown
# Wise-intervention target

**Behavior:** <who, what, when>
**Evidence that a belief is the barrier:** <...>
**Audience's words used:** <n interviews or responses; who; when>

## How the audience reads the situation

| Interpretation, in their words | Said by | Material barrier behind it | If that were fixed, would the behavior follow? | Verdict |
|---|---|---|---|---|
| <quote or close paraphrase> | <n of N> | <cost, access, time, information, process, or none> | <yes / no: why> | <material / meaning / both: which part is which> |

## The question
- **Need:** <to understand / self-integrity / to belong>
- **Question, in the audience's words:** "<...>"
- **Why this one and not the others:** <...>
- **When it becomes live:** <the transition, failure, evaluation, or comparison>

## What the setting offers
- **A new answer would promise:** <...>
- **The setting provides:** <facts, with their source>
- **Verdict:** <delivers / does not deliver: what must change first / not verified>

## The record for this kind of intervention
<belonging / beliefs about ability / self-affirmation: what trials found and where; no effect size promised>

## What to check before relying on this
- <the interpretation that rests on the fewest people>
- <the fact about the setting most likely to be a hope>
```

## Where it goes wrong

- **Picking the famous one.** Growth mindset gets chosen because the team has heard of it. The question comes from the table, never from the program's preference.
- **A message in place of a fix.** A belief exercise is cheap, so it is tempting where the real barrier is a missing teacher or a fee. If step 2 says "material", say so even when the team asked for a message.
- **A bundle.** Combining affirmation, belonging, and mindset content hides which part, if any, worked.

## When to bring in a specialist

Tell the user to consult a psychologist with intervention experience, together with a local qualitative researcher, when:
- The audience includes people in clinical distress, because an exercise about self-worth or belonging can raise a threat without resolving it
- The threat involves stigma or a protected characteristic (HIV status, caste, ethnicity, disability), because the setting itself may be what excludes people
- The decision is a regional or national rollout; an evaluator should pre-register a test before any scaling

Bring them: the table of interpretations with quotes, the check of what the setting offers, and the scale of the decision.
