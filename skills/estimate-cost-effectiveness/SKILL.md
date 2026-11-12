---
name: estimate-cost-effectiveness
description: >-
  Use when a program has an effect estimate and someone asks what it cost
  per additional child immunized or student enrolled, or how it compares per
  dollar with another program, or when a team is about to divide its budget
  by its headline number. Prices every input the program used, paid or not,
  and reports cost per unit of effect with the choices behind it and how far
  the number moves. Do not use when the effect is not yet known; use
  estimate-expected-effect. Not for whether the cost will hold at scale; use
  assess-scalability.
license: CC-BY-4.0
metadata:
  title: Estimate the cost per unit of behavior change
  type: atomic
  stage: analyze
  version: "0.3.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  tested_in: not-applicable
  tags: "cost-effectiveness, quantitative, scaling"
  consumes: "effect-estimate"
  produces: "cost-effectiveness-estimate"
---

## What it does

Estimates what a program paid for each unit of behavior change it caused.

**What this adds:** prices every input at market value, including volunteer time and donated space, and keeps research costs out; states the perspective, currency year, exchange rate, and discount rate; shows the ratio with and without transfers (cash or goods handed to participants); gives no ratio for an effect not distinguishable from zero; reruns it at the effect's confidence bounds; and will not rank programs whose outcomes differ.

## When to use it

### Use it when
- An evaluation has an effect and a funder asks "what did it cost per additional child immunized?"
- Two programs with the same outcome must be compared per dollar
- A team is about to divide its budget by the number of people reached and call that the cost per outcome

### Do not use it when
- The effect is not known and the question is what size to plan for; use `estimate-expected-effect`
- The question is whether the cost will hold at scale; use `assess-scalability`
- The task is to set the size or form of a reward; use `design-incentive-scheme`

## Before you start

Ask these before producing the estimate; skip what the user has answered.

1. **Required.** The effect: outcome and units, estimate and confidence interval, the people it applies to, the period, and its source (this program's evaluation, or a planning estimate).
2. **Required.** The costs: an ingredients list with prices, or the budget plus inputs used but not paid for (volunteers, donated space, government staff), and which costs were research.
3. Optional. The comparator program.
4. Optional. Whose costs count (the implementer's, the government's, or society's, which adds participants' time), and the funder's conventions.

If 1 is missing, ask and stop. If 2 is missing, ask once; with only a budget, list every unpriced input as a gap. If 3 is missing, report this program alone. If 4 is missing, use the implementer's perspective at market exchange rates, discount later costs 10% a year, and add a second ratio with participants' time the program requires, which J-PAL counts.

## What it draws on

- Dhaliwal, I., Duflo, E., Glennerster, R., & Tulloch, C. (2013). Comparative cost-effectiveness analysis to inform policy in developing countries. In *Education Policy in Developing Countries* (pp. 285–338). University of Chicago Press. https://doi.org/10.7208/chicago/9780226078854.003.0008 Supports: listing every ingredient, pricing donated inputs at market cost, treating transfers both ways, and reporting "no significant impact" instead of a ratio.
- Bhula, R., Mahoney, M., & Murphy, K. (2020). *Conducting cost-effectiveness analysis (CEA)*. J-PAL Research Resources. https://www.povertyactionlab.org/resource/conducting-cost-effectiveness-analysis-cea Supports: the default conventions, counting only the costs a program adds, and results per $100 spent.
- Banerjee, A. V., Duflo, E., Glennerster, R., & Kothari, D. (2010). Improving immunisation coverage in rural India: clustered randomised controlled evaluation of immunisation campaigns with and without incentives. *BMJ*, 340, c2220. https://doi.org/10.1136/bmj.c2220 Supports: the fixed-cost check. Small incentives at immunization camps cut the cost per fully immunized child from $55.83 to $27.94, because the daily fixed cost, mainly the nurse's and assistant's pay, was spread over more children.

**Where the evidence comes from:** The procedure makes no claim about how people behave. It was built to compare development programs; its sources' examples are education programs in six countries and immunization in rural India. What is local is prices: wages for volunteer and participant time, the exchange rate, and whether donated inputs stay free at scale.

**Replication status:** Not applicable: this is a costing method. Its sources differ on whether transfers are a cost, so the output shows both.

## How to do it

1. **Fix the effect first.** If its interval includes zero, give no ratio: write "no significant impact" if the estimate is precise, or "too imprecise to cost" if the interval is wide. If it is a planning estimate, label every ratio "projected".
2. **State the perspective** and why it fits the decision.
3. **List the ingredients:** staff time (hours times a local wage, volunteers and government staff included), materials, transport, equipment (spread over its useful life), space, training, monitoring, and, for society, participants' time. Price each at market value, paid or not, and mark it paid, donated, or borrowed. Count only costs the program added. Keep transfers on their own line and research costs out of the delivery total.
4. **Fix the conventions:** currency year, exchange rate, and discount rate for costs after the first year. Convert everything.
5. **Divide cost by effect:** delivery cost per person reached, cost per additional unit of outcome, and additional units per $100.
6. **Rerun the ratio** at the effect's confidence bounds, with and without transfers, with donated and borrowed inputs at zero, with a higher wage for volunteer time, and under the society perspective.
7. **State what limits comparison:** how the comparator priced inputs and treated transfers, the share of fixed costs (training, equipment, set-up), and how each measured the outcome.
8. **Stop at one outcome.** A cost-effectiveness ratio cannot rank programs with different outcomes; say so.

See `references/worked-example.md` for a complete run.

## Output template

```markdown
<Two or three plain sentences to the user: the cost per additional <outcome unit>, how far it moves across the rows below, and the one thing that most limits comparing it with another program.>

# What <the program, in a few words> cost per additional <outcome unit>

**Program:** <name; what was delivered, to whom, over what period>
**Effect:** <outcome in units; estimate (95% CI); people it applies to; source: this program's evaluation / planning estimate (every ratio projected)>
**Whose costs count (perspective):** <implementer / government / society>, because <reason tied to the decision>
**Currency and year:** <currency, year; exchange rate used>; **discount rate:** <rate, or none and why>
**Compared with:** <program and the common outcome unit, or none>

## Ingredients: everything the program used, paid or not

| Category | Item | Quantity | Unit price | Cost | Paid / donated / borrowed |
|---|---|---|---|---|---|
| <staff time, materials, transport, equipment, space, training, monitoring> | <item> | <...> | <...> | <...> | <...> |
| Participants' time (society perspective only) | <...> | <...> | <...> | <...> | Not in the delivery total |
| **Delivery total** | | | | <...> | |
| Transfers to participants (cash or goods) | <item, or none> | | | <...> | |
| Research costs (excluded) | <item> | | | <...> | |

## Cost per result
- Delivery cost per person reached: <...>
- Cost per additional <outcome unit>: <delivery total> / <additional units> = <...>
- Additional <outcome units> per $100: <...>
<or: "No significant impact: <precise / wide> estimate; no ratio reported.">

## How far the number moves (sensitivity)

| Scenario | Cost used | Effect used | Cost per additional <unit> | Per $100 |
|---|---|---|---|---|
| Headline | <...> | <point estimate> | <...> | <...> |
| Effect at lower confidence bound | <...> | <...> | <...> | <...> |
| Effect at upper confidence bound | <...> | <...> | <...> | <...> |
| <With / without> transfers | <...> | <...> | <...> | <...> |
| Donated and borrowed inputs at zero | <...> | <...> | <...> | <...> |
| Volunteer time at <higher wage> | <...> | <...> | <...> | <...> |
| Society perspective | <...> | <...> | <...> | <...> |

## What limits comparing it with other programs
- <transfers: how this program and the comparator treat them>
- <fixed-cost share, and what falls per person as the program grows>
- <wages and prices assumed>
- <differences in how the outcome was measured>

## What to check before relying on this
- <the input most likely to be mispriced>
- <whether the comparator costed its inputs the same way>

## Where you could go from here
<One line saying the estimate is done.>
<Two or three next moves that fit what this run found, each with why it would help and when it fits. Candidates:
- `assess-scalability`, when the decision is whether to fund a larger rollout or a new implementer, since set-up costs fall per person and free inputs may stop being free
- `estimate-sample-size`, when the effect was too imprecise to cost and a larger trial is being considered
- `review-prior-intervention`, when there was no significant impact and the team must decide whether to retry, change, or drop the program
- the comparator program's team or its published costing, when the two ratios will sit in one table and the comparator's ingredients are not known
- timesheets and finance records, when the largest line rests on planned rather than actual hours or prices
- a health or development economist, when the decision moves money between programs with different outcomes>
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

- **People reached counted as people changed.** Only additional outcomes, from a comparison, go under the line.
- **Pilot costs presented as scale costs.** Training and set-up fall per person as a program grows, while free inputs may stop being free.
- **A projected ratio quoted as a result.** A ratio built on a planning estimate reaches a proposal as if measured.
- **Two ratios that only look comparable.** If one program priced volunteer time and the other did not, the cheaper-looking one may simply have counted less.

## When to bring in a specialist

Tell the user to consult a health or development economist with costing experience when:
- The decision will move money between programs with different outcomes, which needs a cost-benefit analysis or the decision-maker's explicit weights
- The outcome is to be expressed in life-years or disability-adjusted life-years
- Costs run over several years with uncertain prices, or the funder's conventions conflict with the defaults here
- The ratio will be published beside others whose costing cannot be checked

Bring them: this estimate, with its ingredients table and sensitivity rows.
