---
name: specify-intervention-adaptations
description: >-
  Use when a tested intervention is being changed, on purpose or by the
  people delivering it, and someone asks "is this still the same program?",
  "the field team dropped the follow-up call, does that matter?", or "what
  may we change for the new district?". Records each change and checks it
  against the parts that make the intervention work. Do not use when there
  is no written description of the intervention as tested; use
  draft-intervention-description. Not for whether the effect will survive
  scale-up; use assess-scalability.
license: CC-BY-4.0
metadata:
  title: Track changes to a tested intervention
  type: atomic
  stage: implement
  version: "0.2.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  tested_in: not-applicable
  tags: "implementation-science, implementation, process-evaluation"
  consumes: "intervention-description"
  produces: "adaptation-record"
---

## What it does

Records each planned or unplanned change to a tested intervention against the parts that make it work.

**What this adds:** before logging any change, writes each core component's job, assumption, and allowed variation; logs every change, including those made unasked in the field, on a published framework's eight fields; marks each consistent, inconsistent, or unknown; and says when the result is a different intervention.

A core component does a job the effect depends on; anything else may change to fit a place.

## When to use it

### Use it when
- Someone asks "is this still the same program?" or "does it matter that the field team changed that?"
- A scale-up, a cost cut, or a new delivery partner is changing what was tested
- Monitoring shows delivery differing from the design
- The intervention is moving to a new population, setting, or language

### Do not use it when
- There is no written description of the intervention as tested; use `draft-intervention-description` first
- The question is whether the effect will survive scale-up; use `assess-scalability`
- The question is how to reach routine delivery; use `plan-scale-up-strategy`
- The question is which indicators would catch drift during delivery; use `design-fidelity-monitoring`

## Before you start

Ask these before producing anything. Do not ask anything the user has already answered.

1. **Required.** The intervention as tested: a description, protocol, or manual, and where and with whom it was tested.
2. **Required.** The changes, proposed or already seen, with who made each, when, and why, as far as known.
3. Optional. Why each part should work (a theory of change); any move to a new context; monitoring records or staff reports of what differs.

If 1 is missing, ask and stop: there is nothing to compare changes against. If 2 is missing, ask once, or open the record with an empty log. If 3 is missing, infer each job from the description and mark it "provisional".

## What it draws on

- Skivington, K., Matthews, L., Simpson, S. A., et al. (2021). A new framework for developing and evaluating complex interventions: update of Medical Research Council guidance. *BMJ*, 374, n2061. https://doi.org/10.1136/bmj.n2061 Supports: breaking the intervention into components with "agreement about permissible and prohibited variation" in their delivery.
- Wiltsey Stirman, S., Baumann, A. A., & Miller, C. J. (2019). The FRAME: An expanded framework for reporting adaptations and modifications to evidence-based interventions. *Implementation Science*, 14, 58. https://doi.org/10.1186/s13012-019-0898-y Supports: the eight fields of the log, and "unknown" where nothing shows whether a part is core.
- Moore, G., Campbell, M., Copeland, L., et al. (2021). Adapting interventions to new contexts—the ADAPT guidance. *BMJ*, 374, n1679. https://doi.org/10.1136/bmj.n1679 Supports: the steps for a move to a new context.
- Walton, G. M., & Wilson, T. D. (2018). Wise interventions: Psychological remedies for social and personal problems. *Psychological Review*, 125(5), 617–655. https://doi.org/10.1037/rev0000115 Supports: writing down the assumption behind each component.

**Where the evidence comes from:** This is a recording procedure and makes no claim about how people behave. Its frameworks come from health research in wealthy Western countries. What is local is which components are core: a part that does a job in one population may not be needed in another.

**Replication status:** Not applicable; no source tests whether recording changes this way improves outcomes.

## How to do it

1. **Write the baseline in one line**, with its source and date, and date the record itself as a version, so an evaluation can say which version its data describe.
2. **List the core components before reading the changes**, so the changes do not shape the list. For each, write its job, the assumption behind it, what may vary (language, timing, venue), and what may not. A component whose job nobody can state is "provisional".
3. **Log each change on the template's eight fields.** Unplanned changes made in the field go in the same log as decisions.
4. **Judge fidelity** against step 2. Consistent: within what may vary. Inconsistent: removes a component or crosses what may not vary. Unknown: nothing shows whether the change keeps the job, or whether the part is core; say what would settle it. Judge by the job, not the look: a shorter session that keeps the job is consistent; an intact-looking one that lost it is not.
5. **Judge the changes together**, and flag each change that is inconsistent or leaves a job in doubt. Several consistent changes can still leave a job undone. If they do, or if any change is inconsistent, write that this version is a different intervention, which the original evidence does not cover.
6. **For a move to a new context**, follow ADAPT: compare the contexts on what the jobs depend on, plan adaptations with the people who will deliver and receive it, pilot or evaluate as far as the uncertainty warrants, and name who keeps the record.

See `references/worked-example.md` for a complete run.

## Output template

```markdown
# Adaptation record: <intervention>, version <date>

**Baseline:** <the intervention as tested, in one line; source document and date>
**Move to a new context:** <none / from where to where, and what differs>

## Core components
| Component | Job it does for the effect | Assumption behind it | May vary | May not vary | Status |
|---|---|---|---|---|---|
| <...> | <...> | <...> | <...> | <...> | <confirmed / provisional> |

## Change log
| # | When | Planned? | Who decided | What changed | Level | Nature | Fidelity | Goal, and what prompted it |
|---|---|---|---|---|---|---|---|---|
| 1 | <before delivery / during delivery / at scale-up / routine running> | <planned / unplanned> | <role> | <content / delivery: how, where, by whom / training / evaluation: what> | <program / site / provider / group / person> | <added / removed / shortened / substituted / reordered / tailored> | <consistent / inconsistent / unknown: against which component, and why> | <...> |

## Taken together
<whether the changed version still does every component's job; if not: "This version is a different intervention from the one tested, and the original evidence does not cover it.">

## Flags
- **Change <n>:** <which component's job it removes or weakens>; decided by <role / no recorded decision>; reason: <...>

## Move to a new context (only when one is under way)
- **Fit:** <what the jobs depend on, and whether the new context has it>
- **Adaptations planned, and with whom:** <change numbers; who took part>
- **Piloting or evaluation warranted:** <what, where, what it must show>
- **Who keeps this record:** <role; how often it is updated>

## What to check before relying on this
- <the inconsistent or unknown change that matters most, and the monitoring or test that would show whether its job survives>
- <the provisional component most likely to be mislabeled>
```

## Where it goes wrong

- **Drift called adaptation.** A health worker who stopped calling because phone credit ran out did not adapt the program; log it as unplanned, with the real reason.
- **Everything marked core.** A list that includes the leaflet's font forbids every change and will be ignored.
- **Only the team's decisions logged.** Months of delivery with no unplanned entries means nobody asked frontline staff or read the monitoring.
- **Blessing a cost cut.** Teams often ask to hear that a cheaper version is fine. The verdict comes from the component table, not the budget.

## When to bring in a specialist

Tell the user to consult an implementation researcher, and where possible the original's designers and evaluators, when:
- A core component is being cut for cost or workload, and someone must judge whether a cheaper way to do its job exists
- A change touches clinical, safety, or legal content, such as dosing, test-result counseling, or referral; add a clinician or lawyer
- Delivery staff and designers disagree about what is core, which usually means the reason the intervention works was never written down

Bring them: the record and the description it started from.
