---
name: adapt-growth-mindset-message
description: >-
  Use when students read a poor result as proof that they lack ability, the
  school gives them a way to improve, and a team wants a growth-mindset lesson
  for that setting: "a mindset session for our schools". Writes the lesson with
  local examples, the task in which students advise a younger student, and the
  check on what teachers and peers do. Do not use when nobody has established
  which question students are asking; use identify-wise-intervention-target.
  Not for doubts about belonging; use draft-belonging-story.
license: CC-BY-4.0
metadata:
  title: Adapt a growth-mindset lesson to a local school
  type: atomic
  stage: design
  version: "0.2.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  tested_in: beyond-western-differs
  tags: "growth-mindset, wise-interventions"
  consumes: "wise-intervention-target"
  produces: "intervention-draft"
---

## What it does

Adapts a short lesson teaching that ability grows with practice to one school setting.

**What this adds:** writes no lesson unless students' own words show they read a setback as fixed ability and the school gives them a way to improve; keeps the three claims and the advice-writing task of the tested lesson, replacing only the examples; allows no "try harder" wording; and states the record, a pooled effect near zero, in the output.

The method is Walton and Wilson's: a wise intervention is a short exercise that changes how people interpret themselves or their situation.

## When to use it

### Use it when
- Students' own words name the question "can I get better at this?", and what the school offers after a poor result is known
- Someone asks for "a growth mindset lesson" or "a mindset session for our students"
- A team is about to translate a US mindset script word for word

### Do not use it when
- Nobody has established which question students are asking, or that a belief is the barrier; use `identify-wise-intervention-target`
- Students' words are about whether people like them belong; use `draft-belonging-story`
- People feel judged for who they are or what they lack; use `draft-values-affirmation`

## Before you start

Ask these first, unless already answered.

1. **Required.** The behavior (who, what, when) and, in students' words with counts, evidence that they read a poor result as proof of fixed ability.
2. **Required.** What the school offers after a poor result: feedback, a second attempt, what teachers and peers say. Facts, not plans.
3. **Required.** Grade, session length, language, reading level, and who runs the lesson.
4. Optional. The outcome the program can measure.

If 1 or 3 is missing, ask and stop. If 2 is unknown, mark the check "not verified" and the lesson "not for delivery". If 4 is missing, name grades or test scores.

## What it draws on

- Walton, G. M., & Wilson, T. D. (2018). Wise interventions: Psychological remedies for social and personal problems. *Psychological Review*, 125(5), 617–655. https://doi.org/10.1037/rev0000115 Supports: the framework.
- Yeager, D. S., Hanselman, P., Walton, G. M., Murray, J. S., Crosnoe, R., Muller, C., et al. (2019). A national experiment reveals where a growth mindset improves achievement. *Nature*, 573, 364–369. https://doi.org/10.1038/s41586-019-1466-y Supports: steps 2 to 7. In this US national study, students taught the message to a struggling younger student and were not told to work hard. Grades rose 0.10 points among lower-achieving students, more where peers favored challenge.
- Macnamara, B. N., & Burgoyne, A. P. (2023). Do growth mindset interventions impact students' academic achievement? A systematic review and meta-analysis with recommendations for best practices. *Psychological Bulletin*, 149(3–4), 133–173. https://doi.org/10.1037/bul0000352 Supports: step 8. Across 63 studies the pooled effect on achievement was a twentieth of a standard deviation (d = 0.05), not significant once corrected for publication bias.

**Where the evidence comes from:** Most trials are with secondary-school students in the United States. Elsewhere, short sessions raised test scores slightly in Peru and Indonesia, a similar exercise in 202 schools in Argentina had no effect, and a longer program in rural China changed beliefs with little sign of a change in scores. Check locally whether feedback or a second attempt follows a poor result.

**Replication status:** Contested. One meta-analysis puts the average effect near zero; another finds a small one (d = 0.14) where the lesson was delivered faithfully to students expected to benefit.

## How to do it

1. **Confirm the question** from the students' words. If they point to a missing teacher, a fee, or belonging, say so and stop.
2. **Check the school, as a gate.** Write what follows a poor result. If nothing lets effort pay off, write no lesson and name what must change first; "you can improve" is false where the school gives no chance to.
3. **Keep the three claims:** ability grows with practice, as a muscle does with use; struggle and mistakes are part of learning, not a verdict; what builds ability is a new strategy or asking for help, not the same effort repeated.
4. **Replace every example** with a local one of a skill learned over time, and mark the text for a native speaker to redraft.
5. **Never tell students to work harder.** The tested lesson described how learning happens and left the conclusion to them.
6. **Write the advice task:** each student writes a letter, in their own words, to a younger student who is struggling. People come to hold an idea by explaining it ("saying is believing"). Offer a spoken version, and say truthfully where the letters go.
7. **Fix delivery and outcome:** one or two short sessions before the question becomes live; grades or scores on a named date, judged on lower-achieving students against a comparison group. A belief survey shows only that the lesson was received.
8. **State the record** and promise no effect size.

See `references/worked-example.md` for a complete run.

## Output template

```markdown
# Growth-mindset lesson, adapted

**Behavior:** <who, what, when>
**The question students are asking:** "<in their words>" (<n of N; source>)
**Who receives it:** <grade; lower-achieving students, how defined>

## What the school offers (gate)
- **After a poor result:** <feedback, retake: facts, with their source>
- **Teachers:** <what they say and do>
- **Peers:** <what they say about trying hard>
- **Verdict:** <delivers / does not deliver: what must change first, and no lesson follows / not verified: not for delivery>

## The lesson (working copy; a native speaker redrafts it)
1. **Ability grows with practice.** <the claim, with a local example>
2. **Struggle is part of learning.** <the claim, with a local example>
3. **A new strategy or help builds ability.** <named strategies; named people to ask>

## Advice task
<the prompt: a letter to a younger student who is struggling; the spoken version; where the letters go>

## Delivery
- **Sessions:** <one or two; length>
- **When:** <before which moment>
- **Run by:** <who; what they are briefed to keep and to leave out>

## How you will know
- **Outcome:** <grades or scores; date>
- **Judged on:** <lower-achieving students; the comparison group>
- **Check on delivery only:** <a belief item>

## The record
<what trials found and where; no effect size promised>

## Pre-test before use
<five to ten students restate the three claims; two teachers say whether anything contradicts their classroom; what counts as a pass>

## What to check before relying on this
- <the fact about the school most likely to be a hope>
- <the barrier this lesson does not touch>
```

## Where it goes wrong

- **A lesson in place of a teacher.** It is cheap, so it gets offered where the barrier is absent teachers or fees. Refuse to write it as a replacement for teaching.
- **An average promised for everyone.** The gains on record are among lower-achieving students.
- **A teacher who contradicts it.** One who sorts students into clever and slow undoes the lesson the same week; a retake on paper does not settle step 2.
- **Quoting the best trial:** Peru or the US study without Argentina and the pooled estimate.

## When to bring in a specialist

Tell the user to consult an education evaluator, and a psychologist with experience of school interventions, when:
- The lesson would replace teaching, remedial classes, or materials
- It is pitched as the answer to poverty or discrimination, which tells disadvantaged students the problem is their mindset
- The rollout is regional or national; an evaluator should pre-register a test first
- Students face a high-stakes exam with known distress

Bring them: the students' words, the check of the school, the lesson, and the record.
