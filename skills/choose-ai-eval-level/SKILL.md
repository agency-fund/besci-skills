---
name: choose-ai-eval-level
description: >-
  Use when a team with an AI tool, product, or program for a social cause
  must decide what to evaluate next: "are we ready for an RCT?", "our funder
  wants proof of impact", "what evidence can we honestly show?". Gives one
  recommendation on which stage of evaluation to run now and which is
  premature, with the evidence behind each judgment and what to build now so
  later evaluation stays possible. Do not use when the evaluation is chosen
  and needs designing; use plan-evaluation-design. Not for programs with no
  AI model in them.
license: CC-BY-4.0
metadata:
  title: Choose which AI evaluations to run next
  type: atomic
  stage: test
  version: "0.3.0"
  status: draft
  authors: "Joe Speed, Zezhen Wu"
  org: IL
  tested_in: not-applicable
  tags: "ai-eval, evaluation-framework"
  consumes: "ai-product-account"
  produces: "ai-eval-level-recommendation"
---

## What it does

Recommends which stage of evaluation an AI tool, product, or program should run next.

**What this adds:** gives each of four stages a verdict tied to a named piece of evidence or to "none supplied"; makes one recommendation; says why each later stage is premature, in words a team can give a funder; refuses adjectives or a funder's request as evidence; and always lists what to build now so that an impact evaluation is possible later.

The idea is from The Agency Fund's AI evaluation playbook: evaluation is staged, from the model's answers to people's lives, and a result at a later stage means little until the earlier ones hold.

## When to use it

### Use it when
- A team asks "are we ready for an RCT?" (a randomized controlled trial) or "what should we evaluate next?"
- A funder or board asks for proof of impact from a product that is still changing
- Strong usage numbers lead someone to propose an impact evaluation

### Do not use it when
- The evaluation is chosen and the question is its outcome, comparison group, or sample; use `plan-evaluation-design`
- The program has no AI model in it; use `plan-evaluation-design`
- A trial has shown an effect and the question is whether it holds at scale; use `assess-scalability`

## Before you start

Ask only what the user has not answered.

1. **Required.** The product: what it does, for whom, the outcome in people's lives it is meant to improve, and how far along it is (prototype, pilot, deployed, scaling).
2. **Required.** The evidence so far: what has been tested or measured about the model's answers, use, users, and outcomes.
3. **Required.** The decision this informs: what the team will do differently depending on the answer.
4. Optional. Outside pressure: a funder's request, a deadline.

If 1, 2, or 3 is missing, ask and stop. No evidence at a stage is an answer, not a missing input: record "none supplied".

## What it draws on

- Wu, Z., On, R., Walsh, J., Korley, E., Madon, T., & Wong, L. (2025). *AI Evaluation in the Social Sector: A Living Playbook*. The Agency Fund. Current edition: *AI Evaluation Playbook* (2026), maintained by the Center for Global Development, IDinsight, and The Agency Fund. https://eval.playbook.org.ai/ Supports: the four stages and their questions, and steps 4 and 7.
- Chia, H. S., Carter, S., Abrol, F., Madon, T., On, R., Walsh, J., & Wu, Z. (2025, April 16). *An AI evaluation framework for the development sector*. Center for Global Development. https://www.cgdev.org/blog/ai-evaluation-framework-for-the-development-sector Supports: step 6. Funders should "match evaluation requirements to the product's development stage".

**Where the evidence comes from:** This is a procedure for ordering evaluations and makes no claim about how people behave. The playbook was written for generative AI products in low- and middle-income countries. What counts as a good answer, real use, and a better outcome must be set for each product and place.

**Replication status:** Not applicable. No study tests whether teams that order evaluation this way decide better, or whether two teams reach the same verdicts.

## How to do it

1. **State the product, the outcome, and the decision.**
2. **Sort the team's evidence under the four questions.** For each, name the item (a test-set pass rate, a retention figure, a survey result) or write "none supplied". "Engagement is strong" and a funder's request are not evidence.
3. **Give each stage a verdict:** run now, keep monitoring, or premature. A stage is premature when a weakness at an earlier one would make its result unreadable: people stop using a product whose answers are poor, and one-time use cannot change what they do. The first three stages can run side by side.
4. **Recommend an impact evaluation only when the playbook's three conditions hold:** evidence at the first three stages is strong; funders or policymakers are considering wider adoption; the team has capacity to work with independent researchers. Where use is too inconsistent to expect an effect, recommend stage 3.
5. **Make one recommendation:** the evaluation to run now and what it will show. Name the kind of study, not its design. Some stage always has a question worth answering, so never recommend nothing.
6. **Explain each premature stage:** what a result there would and would not mean today.
7. **List what to build now**, whatever the verdicts: a holdout group (users kept on the old version), a staged rollout or built-in random assignment, and a version tag on every release. These decide whether an impact evaluation is possible later without rebuilding the product.
8. **Say what would change the recommendation.**

See `references/worked-example.md` for a complete run.

## Output template

```markdown
<Two or three plain sentences to the user: the evaluation you would run now, the evidence (or the gap) that decided it, and whether the trial or impact evaluation someone has asked for is premature.>

# What to evaluate next: <product>

**Product:** <what it does, for whom, and how far along it is>
**Outcome it is meant to improve:** <the change in people's lives>
**Decision this informs:** <what the team will do differently depending on the answer>

## Recommendation
<one to three sentences: the evaluation to run now, what it will show, and why not a later stage>

## The four stages
| Stage | Question, in the playbook's words | Evidence you have | Verdict |
|---|---|---|---|
| 1. Model | "Does the AI system perform as intended?" | <named evidence, or "none supplied"> | <run now / keep monitoring / premature: one line why> |
| 2. Product | "Does the overall product engage and retain users?" | <...> | <...> |
| 3. User | "Does the product change users' thoughts, feelings, knowledge and behaviour towards the development outcome?" | <...> | <...> |
| 4. Impact | "Do users with access to the product improve development outcomes?" | <...> | <...> |

## Why the later stages are premature
- **<stage>:** <what a result would and would not mean today, in words the team can give a funder; or "No stage is premature.">

## Build now so later evaluation is possible
- <a holdout group, a staged rollout or random assignment, version tags: the specific step for this product>

## What would change this recommendation
- <the evidence that would move each premature stage to "run now">

## Where you could go from here
<One line saying the recommendation is done.>
<Two or three next moves that fit what this run found, each with why it would help and when it fits. Candidates:
- `plan-evaluation-design`, when the evaluation to run now needs one outcome and its data source fixed, such as the change in what users know or do at the user stage
- `choose-trial-design`, when the evaluation to run now compares versions or groups (an A/B test of the product, or an impact evaluation once its conditions hold) and the team must decide what to randomize
- `define-agency-construct`, when the outcome the product is meant to improve is users' agency or confidence and nobody has defined it well enough to measure
- the product's own logs, when a stage reads "none supplied" but usage, retention, or test-set records already exist and could fill it before anything new is run
- the funder or board, with the table of stages, when they have asked for a trial the table finds premature
- an independent evaluator (a university partner or an evaluation firm), when the recommendation is an impact evaluation>
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

- **Answering the pressure.** The funder wants a trial, so stage 4 is found ready. A stage 4 row that cites the funder's interest and no earlier evidence has answered the politics.
- **A ladder climbed once.** "Stage 1: done" misreads the idea. A new model, prompt, or knowledge base reopens stage 1; a redesign reopens stage 2.
- **The order read as a rule about where to start.** Teams begin with their biggest risk: safety for a health tool, whether anyone will use a new service. The stages say what a result can mean, not which question to ask first.
- **Usage read as stage 3.** Return visits show that people come back, not that they know or do anything differently.

## When to bring in a specialist

Tell the user to bring in:
- When the recommendation is an impact evaluation: an independent evaluator (a university partner or an evaluation firm), so that people with no stake in the result design it
- When the product gives health, legal, financial, or child-protection advice: a domain expert, to define a correct and safe answer before any stage 1 result is read
- When the funder and the team still disagree after seeing the table: an evaluation methodologist neither side employs

Bring them: the product description, the table of stages, and the list of what is built for later evaluation.
