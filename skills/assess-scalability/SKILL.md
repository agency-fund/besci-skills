---
name: assess-scalability
description: >-
  Use when a pilot or trial showed an effect and someone asks "will this work
  at scale?", "can the ministry run it?", or "what breaks when we go from 20
  clinics to 2,000?", or when a proposal carries a pilot result straight into
  a scale-up budget. Compares the pilot as it was run with the delivery
  planned at scale, gives a verdict, and names what to test first. Do not use
  when the decision to scale is made and the question is how to get there;
  use plan-scale-up-strategy. Not for a study run elsewhere; use
  assess-evidence-transferability.
license: CC-BY-4.0
metadata:
  title: Check whether a pilot effect will survive scale-up
  type: atomic
  stage: implement
  version: "0.3.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  tested_in: not-applicable
  tags: "scaling, implementation-science, implementation"
  consumes: "intervention-description"
  produces: "scalability-assessment"
---

## What it does

Judges whether an effect found in a pilot is likely to survive delivery at scale.

**What this adds:** compares the pilot as run with delivery at scale on seven fixed rows; counts any difference the pilot did not test as a minus; adds up no total score; gives one of three fixed verdicts; and names the one test to run first, under routine conditions.

## When to use it

### Use it when
- A pilot showed an effect and someone asks "will this work at scale?" or "can the ministry run it?"
- A government or larger partner wants to adopt a program on the strength of one evaluation
- A proposal carries the pilot's result straight into a scale-up budget
- Who delivers, how, or to whom will change on the way to scale

### Do not use it when
- The decision to scale is made and the question is how to get there; use `plan-scale-up-strategy`
- The question is which changes to the intervention are allowed; use `specify-intervention-adaptations`
- The finding is from a study elsewhere and nothing has been piloted here; use `assess-evidence-transferability`
- The question is cost per outcome; use `estimate-cost-effectiveness`

## Before you start

Ask these before producing the assessment. Do not ask anything the user has already answered.

1. **Required.** The pilot's result: outcome, effect and comparison, design, sample size, who took part.
2. **Required.** How the pilot was delivered: by whom, how they were trained, supervised, and paid, what extra support a project team gave, the channel, the cost per person.
3. **Required.** The proposed scale-up: how many people or sites, who would deliver, through what system, what would change, the budget.
4. Optional. Whether the decision can be reversed; results by subgroup; delivery records.

If 1, 2, or 3 is missing, ask and stop. If 4 is missing, assume a reversible decision, say so, and mark the rows it bears on "more information needed".

## What it draws on

- World Health Organization & ExpandNet (2010). *Nine steps for developing a scaling-up strategy*. https://www.who.int/publications/i/item/9789241500319. With World Health Organization & ExpandNet (2011). *Beginning with the end in mind*. https://www.who.int/publications/i/item/9789241502320 Supports: comparing the pilot with routine delivery, and testing "under the routine operating conditions and existing resource constraints" before scaling.
- Kettle, S., & Persian, R. (2022). *Target, Explore, Solution, Trial, Scale: An introduction to running simple behavioural insights projects*. The Behavioural Insights Team. https://www.bi.team/wp-content/uploads/2022/11/BIT-Handbook-How-to-run-simple-BI-projects.pdf Supports: five rows, from its SCALE factors (Sponsorship, Cost/benefit, Accountability, Logistics, Evidence).
- Walton, G. M., & Wilson, T. D. (2018). Wise interventions: Psychological remedies for social and personal problems. *Psychological Review*, 125(5), 617–655. https://doi.org/10.1037/rev0000115 Supports: the rows on what is delivered and how.
- Milat, A., Lee, K., Conte, K., et al. (2020). Intervention Scalability Assessment Tool: A decision support tool for health policy makers and implementers. *Health Research Policy and Systems*, 18, 1. https://doi.org/10.1186/s12961-019-0494-2 Supports: the three verdicts, and adding up no total score.

**Where the evidence comes from:** This is a judgment procedure and makes no claim about how people behave. The ExpandNet guides grew out of health programs in Africa, Asia, and Latin America; the scalability tool was built with Australian policy makers. What is local is each row's answer, above all whether the staff who would deliver at scale can do what the pilot's staff did.

**Replication status:** Not applicable; no source tests whether teams using these questions scale more successfully.

## How to do it

1. **Write the pilot and the scale version** in one line each, on the same fields: effect and comparison, outcome, design, who is reached, who delivers with what support, cost. Write "not reported" in any blank.
2. **Fill the seven rows of the table.** For what is delivered, ask what each pilot extra (a follow-up call, a supervisor's visit) was doing, because routine budgets drop extras first.
3. **Mark each row** plus (the same, or different and tested), minus (different and untested, or a known problem), or more information needed. An untested difference is a minus even when it looks minor, because pilots succeed on inputs routine delivery lacks. Add no total: one minus can decide the verdict.
4. **Give one verdict.** *Recommended for scale-up:* a credible effect, no minus. *Promising: test first:* a credible effect, at least one minus or unknown. *Does not yet merit scale-up:* no comparison group or one small study alone, a scale version without what the effect depended on, or no one who would deliver it wants it.
5. **Name the first test:** the minus whose failure would change the verdict most, run by the organization that would deliver at scale, with its own staff and budget, in a few sites, against a comparison group.
6. **List what must be true** for the effect to survive, each a statement that could prove false.

See `references/worked-example.md` for a complete run.

## Output template

```markdown
<Two or three plain sentences to the user: the verdict, the one difference between the pilot and delivery at scale that decided it, and that this says whether the effect is likely to hold, not how large it will be.>

# Will <the program, in a few words> keep its effect at scale?

**Pilot:** <effect and its comparison> on <outcome>; <design, sample size>; among <who, where>; delivered by <whom>, with <extra support>; at <cost per person or site>
**At scale:** <how many people or sites>; delivered by <whom>, through <what system>; changes: <...>; budget: <...>
**Decision this informs:** <...>; reversible: <yes / no / assumed yes>

## The pilot compared with delivery at scale

| What we compared | In the pilot | At scale | Did the pilot test the scale version? | Mark |
|---|---|---|---|---|
| Strength of the effect | <comparison group, sample size, pre-registration, a second study> | not applicable | not applicable | <+ / – / more information needed> |
| Who is reached | <who took part, how recruited> | <who will be reached> | <yes / no> | <...> |
| What is delivered | <components, including extras> | <components kept, changed, dropped> | <...> | <...> |
| Who delivers and answers for it | <selection, training, supervision, pay, reporting line> | <the same, at scale> | <...> | <...> |
| How it reaches people | <channel, staff time, training> | <...> | <...> | <...> |
| Cost and funding | <cost per person> | <cost per person; whether the money exists> | <...> | <...> |
| Demand and commitment | <who wanted it> | <whether officials and frontline staff want it; whether the organization that would run it asked> | <...> | <...> |

## Verdict
<Recommended for scale-up / Promising: test first / Does not yet merit scale-up>, because <the rows that decided it>.

## The test I'd run first
<the row it tests; what is tested, by whom, where, against what comparison; how long; what result would change the verdict>

## What must be true for the effect to survive
1. <a statement that could prove false>: <how to check it>

## What to check before relying on this
- <the "more information needed" row that matters most>
- <the field in the pilot line most likely to be wrong>

## Where you could go from here
<One line saying the assessment is done.>
<Two or three next moves that fit this verdict, each with why it would help and when it fits. Candidates:
- `choose-trial-design`, when the first test needs its comparison worked out: which unit to randomize and against what
- `specify-intervention-adaptations`, when the scale version drops or changes parts of the pilot and the team needs to judge which changes the program can absorb
- `plan-scale-up-strategy`, when the verdict is recommended for scale-up, or the first test has come back and the decision to scale is made
- `estimate-cost-effectiveness`, when the cost row decided the verdict and the funder's question is cost per outcome
- the people who would deliver at scale (frontline staff, district planners) or the delivering system's own records, when a row is marked more information needed>
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

- **Carrying the pilot number.** The assessment says whether the effect is likely to survive, not how large it will be. Multiplying the pilot effect by the scale population skips the job.
- **Rows filled from the plan.** "Supervisors will visit monthly" is an intention. The pilot column records what happened; the scale column says who confirmed each line.
- **Cheap read as scalable.** A text message costs little to send to millions and still fails if what made the pilot work, a nurse who called back, does not go with it.

## When to bring in a specialist

Tell the user to consult an evaluator or implementation researcher with scale-up experience, and planners from the organization that would deliver it, when:
- Delivery moves from an NGO to government and the decision will not wait for a test under the new implementer
- The decision cannot be reversed: a national policy, a law, a procurement
- Treating whole areas could move prices, queues, or shared supplies, which a few pilot sites cannot show
- The program carries clinical or safety content

Bring them: the two lines, the marked table, and the pilot's evaluation design.
