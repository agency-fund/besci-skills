---
name: plan-scale-up-strategy
description: >-
  Use when a tested program must move into a system that will run it
  routinely and someone asks "how do we scale this?", "how do we hand this to
  the ministry?", or "who runs this when our grant ends?". Walks nine
  planning steps, from the program's parts to the organization that will
  own it, and ends in prioritized actions, each with an owner and a date. Do
  not use when nobody has judged whether the effect will survive scale; use
  assess-scalability. Not for deciding which changes to the program are
  allowed; use specify-intervention-adaptations.
license: CC-BY-4.0
metadata:
  title: Plan how a tested program reaches routine delivery
  type: atomic
  stage: implement
  version: "0.2.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  tested_in: not-applicable
  tags: "scaling, implementation-science, implementation"
  consumes: "scalability-assessment"
  produces: "scale-up-strategy"
---

## What it does

Plans how a tested program moves into a system that will deliver it routinely.

**What this adds:** walks the WHO and ExpandNet guide's nine steps in order; marks every part of the program, training and supervision included, essential or not; marks each system change needed to make it routine yes, no, or unknown; gates each wave of expansion on an open test; and drops any action without an owner and a date.

Vertical scaling makes a program routine through policy and budget changes; horizontal scaling takes it to more sites.

## When to use it

### Use it when
- Someone asks "how do we scale this?", "how do we hand this to the ministry?", or "what happens when our grant ends?"
- A government or large partner has agreed in principle, and nobody has written down the sequence, owners, or financing
- A funder asks for a sustainability or exit plan for a program run by project staff

### Do not use it when
- Nobody has judged whether the effect will survive scale; use `assess-scalability` first
- The question is which parts of the program may change for new sites; use `specify-intervention-adaptations`
- The question is which indicators will show whether delivery drifts; use `design-fidelity-monitoring`

## Before you start

Ask these before producing anything. Do not ask anything the user has already answered.

1. **Required.** A judgment that the effect is likely to survive scale, with any tests still open. If there is none, stop: that judgment comes first.
2. **Required.** The program as tested, every part, including materials, training, and supervision.
3. **Required.** Who would run it routinely (the user organization, such as a ministry or district) and whether it has asked; who supports the move now (the resource team), and until when.
4. **Required.** The governing policy, the budget cycle, supporters and opponents, elections ahead.
5. Optional. Financing options; uninvited copies; plans to add components.

If any of 1 to 4 is missing, ask and stop. If 5 is missing, write "none known".

## What it draws on

- World Health Organization & ExpandNet (2010). *Nine steps for developing a scaling-up strategy*. https://www.who.int/publications/i/item/9789241500319 Supports: the nine steps, the elements they assess, the table of system changes, and the prioritized recommendations.
- Fernandez, M. E., Ruiter, R. A. C., Markham, C. M., & Kok, G. (2019). Intervention Mapping: Theory- and evidence-based health promotion program planning: Perspective and examples. *Frontiers in Public Health*, 7, 209. https://doi.org/10.3389/fpubh.2019.00209 Supports: separating who decides to adopt a program from who delivers it, and planning "who has to do what" at each stage.

**Where the evidence comes from:** This is a planning procedure and makes no claim about how people behave. The guide grew out of health programs, and its authors helped teams in Africa, Asia, and Latin America use it. What is local is every answer: who owns the program, the budget cycle, the law.

**Replication status:** Not applicable; no source tests whether programs scaled with these steps last longer than programs scaled without them.

## How to do it

1. **Carry over the scalability judgment.** Each open test gates a wave of expansion and becomes a dated action.
2. **The innovation (step 1).** List every part, "hardware" (products, materials) and "software" (training, supervision, management), asking what it took to put each in place: pilots carry inputs nobody wrote down. Mark each essential or not, and whether that was tested. Ask the guide's question "Is it still appropriate to proceed with plans for scaling up?", and stop if the package is too complex or costly for routine delivery.
3. **The user organization (step 2):** its need and champion, capacity gaps, and timing. Name who decides to adopt separately from who delivers.
4. **The environment (step 3):** fill the table; put elections and the budget cycle in the timetable.
5. **The resource team (step 4):** the skills it lacks (advocacy and management matter more at scale) and when its role ends. The user organization owns the program.
6. **Vertical scaling (step 5):** mark each change yes, no, or unknown, and start the yeses first; they take longest.
7. **Horizontal scaling (step 6):** waves of sites, each gated on an open test, starting where capacity and champions are strongest. Monitor outcomes, not only activity: quality tends to fall as expansion speeds up.
8. **Diversification and spontaneous scaling (steps 7 and 8):** adding a component waits until the original runs soundly; check whether uninvited copies keep the essential parts.
9. **The strategy (step 9):** drop actions nobody can act on, prioritize the rest, and give each an owner (a role in a named organization), a date, and its dependency. "The team" and "partners" are not owners. Set a review date; the strategy will change once delivery starts.

See `references/worked-example.md` for a complete run.

## Output template

```markdown
# Scale-up strategy: <program>

**Scalability judgment carried over:** <verdict>; open tests: <each, with its due date>
**Type of scaling:** <vertical / horizontal / both, in what order>, because <reason>

## 1. The innovation
| Part | Hardware or software | Essential? | Judgment tested? |
|---|---|---|---|
| <...> | <...> | <essential / could be simplified / not essential> | <yes: how / no> |

**Still appropriate to proceed?** <yes / no: why>

## 2. The user organization
- **Who adopts, who delivers:** <decision maker; delivering unit and cadre>
- **Perceived need and champion:** <has it asked, by whom, in writing / no>
- **Capacity gaps:** <what, and how each is built>
- **Timing:** <changes ahead inside the organization>

## 3. The environment
| Factor | Helps or hinders | Action | Owner |
|---|---|---|---|
| <policy and politics / bureaucracy / other sectors / social and economic context / people's needs and rights> | <...> | <...> | <...> |

## 4. The resource team
- **Members:** <...>, including from the user organization: <who / none>
- **Skills to add:** <...>
- **Role ends:** <date or milestone>

## 5. Vertical scaling: changes needed
| Change | Needed? | Action | Lead |
|---|---|---|---|
| <policy / political commitment / law / regulations and guidelines / budget / logistics / information systems / supervision / staff appraisal and incentives / training curricula / workforce / information materials> | <yes / no / unknown> | <...> | <...> |

## 6. Horizontal scaling
- **Waves:** <sites, in order, each with the open test it waits for>
- **Site differences and adaptations:** <...>
- **Cost per wave and who pays:** <...; what replaces project funds, and when>
- **Monitoring outcomes:** <what is tracked, from what data>

## 7. Diversification
<none until the original is routine / what, when>

## 8. Spontaneous scaling
<not known to occur / where, and whether the essential parts are kept; support, redirect, or leave>

## 9. Recommended actions
| Category | Recommendation | Priority |
|---|---|---|
| <...> | <...> | <high / medium / low> |

## Operational plan
| Action | Owner (role, organization) | By when | Depends on |
|---|---|---|---|
| <...> | <...> | <...> | <open test or none> |

**Review date:** <...>

## What to check before relying on this
- <the assumption about the user organization most likely to be wrong>
- <the open test that could stop the plan>
```

## Where it goes wrong

- **Scaling the NGO instead of the program.** More sites run by the pilot organization on donor money means no user organization, and a resource team that never leaves.
- **More sites mistaken for a routine program.** Forty districts with no budget line or job description are a bigger pilot.
- **A user organization that has not asked.** Where the government was not part of the pilot, the guide says vertical scaling "must begin with advocacy for adopting the innovation", not with training.
- **Changing the program inside the plan.** "Shorten the counseling to fit the health worker's day" changes the intervention; check it against the essential parts first.

## When to bring in a specialist

Tell the user to consult a health-systems or public-policy specialist with scale-up experience, with the government's planning and legal staff, when:
- The scale-up needs a change in law or regulation, such as who may dispense a product, so the timeline is not the team's to set
- The organization expected to run the program has not asked for it
- Financing after the project depends on a public budget line; add a public-finance specialist
- Uninvited copies drop essential parts, with safety consequences

Bring them: the scalability judgment, the parts table, the system-changes table, and the operational plan.
