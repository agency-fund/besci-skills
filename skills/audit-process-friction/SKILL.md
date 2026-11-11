---
name: audit-process-friction
description: >-
  Use when people say they want to enroll, apply, register, or collect
  something and few finish, and the suspect is the process itself: forms,
  documents, trips, queues, fees, decisions. Also use when the proposed fix is
  "explain it more clearly". Logs every step from the user's side with its
  time, money, documents, and decisions, then ranks what the program can
  remove. Do not use when people do nothing at a single decision point; use
  select-default-option. Not for a behavior that is still vague; use
  define-key-behavior.
license: CC-BY-4.0
metadata:
  title: Count the hassle between intention and completion
  type: atomic
  stage: diagnose
  version: "0.2.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  tested_in: beyond-western-holds
  tags: "sludge, choice-architecture"
  consumes: "target-behavior-brief"
  produces: "barrier-diagnosis"
---

## What it does

Counts what each step of a process costs a person, from the first chance to act through completion.

**What this adds:** logs every step from the user's side with its time, money, documents, and decisions; requires a written reason for each step that stays; writes "no data" where no count exists; ranks better information last among the changes; and never marks a step that protects the person as removable.

This is often called a sludge audit; sludge is friction that costs people time or money without good reason.

## When to use it

### Use it when
- People say they want to enroll, apply, or collect something, few finish, and nobody has gone through the process as a user would
- A team's proposed fix is clearer information or more awareness
- A service involves forms, documents, trips, queues, or fees, and someone asks "where are we losing people?"

### Do not use it when
- People want the option and do nothing at one decision point, with no steps in the way; use `select-default-option`
- The behavior is not yet stated as who does what, when; use `define-key-behavior`
- The friction is confirmed and the question is what to do; use `select-intervention-levers`

## Before you start

Ask these before producing anything. Do not ask anything the user has already answered.

1. **Required.** The behavior (who, what, when) and what counts as done.
2. **Required.** The process as the team believes it runs, from the moment a person first could act to completion.
3. **Required.** How the steps were learned: someone went through them as a user, users were asked, or staff described them.
4. Optional. Counts: how many start, how many finish.
5. Optional. Who controls each step.

If 1 or 2 is missing, ask and stop. If 3 is missing, assume staff described the process. If 5 is missing, assume the program controls only the steps it runs.

## What it draws on

- Sunstein, C. R. (2022). Sludge audits. *Behavioural Public Policy*, 6(4), 654–673. https://doi.org/10.1017/bpp.2019.32 Supports: the audit itself: institutions should catalogue what their frictions cost and decide which to reduce.
- The Behavioural Insights Team (2024). *EAST: Four simple ways to apply behavioural insights* (revised and updated edition). https://bi.team/wp-content/uploads/2014/04/BIT-EAST.pdf Supports: steps 2 and 3. Every extra step may lose people, and some friction, such as a cooling-off period, serves the person.
- Bettinger, E. P., Long, B. T., Oreopoulos, P., & Sanbonmatsu, L. (2012). The role of application assistance and information in college decisions: Results from the H&R Block FAFSA experiment. *The Quarterly Journal of Economics*, 127(3), 1205–1242. https://doi.org/10.1093/qje/qjs017 Supports: ranking information last. Help with a student-aid form raised college attendance; information without help did not.

**Where the evidence comes from:** Of 119 studies of administrative burden in one review, 82% were run in the United States, Europe, or Australia. In Morocco, households helped with the paperwork for a water connection took it up far more often, though help came with information; in Kenya, farmers bought fertilizer when it was delivered free just after harvest; in Indonesia a requirement to apply kept out the better-off more than the poor. Check locally which steps the law requires and whom each step turns away.

**Replication status:** Replicated in direction: across 51 field experiments on benefit take-up, help with the steps raised take-up more than information did. The audit as a method is untested.

## How to do it

1. **Fix the start and the end.** Start when the person first could act, not at the office door: the trip there is a step.
2. **Log every step from the user's side:** what the person does, the time with waiting, the money (fees, transport, lost earnings), the documents, the decision or fact demanded, and who controls it. Count trips, queues, and return visits; official flow charts leave them out. Mark each time "observed" or "estimate"; times from staff are estimates.
3. **Tag each step and write the reason.**
   - Keep: the law, safety, consent, or eligibility requires it, or it protects the person.
   - Remove: it duplicates another step or serves only the institution's convenience.
   - Move: staff could do it, or it could be pre-filled, joined to another step, or done where the person already is.
   - Check: nobody can give the reason. Name who can.
4. **Record how many people enter and leave a step only where counts exist.** Elsewhere write "no data"; an invented drop-off will be read as a measurement.
5. **Record who is lost,** where anyone knows: for example, people with no ID or no money for the fare.
6. **Order the changes.** Steps the program controls come before steps another institution controls; deleting and pre-filling before personal help; help before better information.
7. **Write the diagnosis:** where the friction sits, and whether that rests on observation, users' reports, or estimates.
8. **State the direction the evidence supports.** Promise no completion rate.
9. **Stop.** Do not redesign the service.

See `references/worked-example.md` for a complete run.

## Output template

```markdown
# Process friction audit

**Behavior:** <who, what, when>
**Process audited:** <from the first moment the person could act to the completion point>
**How the steps were learned:** <walked as a user by <who> / users asked / described by staff>

## Step log

| # | Step, from the user's side | Time, with waiting | Money | Documents | Decision or fact demanded | Controlled by | Tag | Reason for the tag | In → out |
|---|---|---|---|---|---|---|---|---|---|
| 1 | <...> | <observed / estimate> | <...> | <...> | <...> | <program / partner / government> | <keep / remove / move / check> | <...> | <counts, or "no data"> |

**Total for one person:** <trips>, <hours>, <money>, <documents>, <decisions>
**Who is lost, where known:** <which people fail at which step; or "not known">

## Changes, in order
1. <step>: <delete / pre-fill / join to another step / move to staff / personal help / information>; controlled by <who>; aimed at <which loss>

## Steps kept
- <step>: <the law, safety, consent, or eligibility reason; who confirmed it>

## Diagnosis
<where the friction sits; resting on observation, users' reports, or estimates>

## What the evidence supports
<the direction, and the nearest study with where it was run; no completion rate promised>

## What to check before relying on this
- <the cell most likely to be wrong>
- <who must agree before a step changes>
```

## Where it goes wrong

- **Auditing the designed process.** Staff describe the process as designed, without the second trip, the photocopy shop, or the missing ID. Such an audit undercounts; say so in the diagnosis.
- **Friction that does a job.** In Indonesia a requirement to apply kept better-off households out of a cash transfer. Before a step goes, ask whom it turns away today.
- **Hours taken for the cause.** A long process does not show that length is why people stop. If people are lost before the first step, the barrier lies elsewhere.

## When to bring in a specialist

Tell the user to consult a specialist before proposing a change when:
- A step tagged "remove" or "move" belongs to a government or regulated process (identity, eligibility, bank customer checks): a legal or compliance officer confirms it can change
- The step is consent to treatment, data use, or a financial product: a safeguarding or ethics lead reviews it, and the audit keeps it until then
- The team wants a completion figure for a funder: an evaluator measures it

Bring them: the step log, the ordered changes, and any counts.
