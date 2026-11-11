---
name: draft-theory-of-change
description: >-
  Use when a program needs its logic written down as a causal chain: "write
  our theory of change", "draft a logic model", or a proposal that says the
  activities produce the outcome without naming who must act differently in
  between. Writes each link from activity to behavior to outcome with its
  assumption, the evidence supplied, and a strength label. Do not use when the
  chain exists and the team must choose one behavior to work on; use
  define-key-behavior. Not for finding research on a link; use
  assess-evidence-base.
license: CC-BY-4.0
metadata:
  title: Write the causal chain from activities to outcome
  type: atomic
  stage: define
  version: "0.2.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  tested_in: not-applicable
  tags: "theory-of-change, logic-model, evaluation-framework"
  consumes: "program-goal"
  produces: "theory-of-change"
---

## What it does

Writes a program's theory of change, the claims it makes about why its activities lead to its outcome, as a chain of links.

**What this adds:** requires at least one link in which a named person does something differently; gives every link an assumption, an evidence cell filled only from what the user supplied, and one of four strength labels; refuses an output as the outcome; and names the weakest link nearest the outcome with the evidence that would raise its label.

## When to use it

### Use it when
- Someone asks "write our theory of change" or "draft a logic model"
- A proposal says the activities produce the outcome without naming who must act differently in between
- An evaluation is about to be planned on a chain nobody has written down

### Do not use it when
- The chain exists and the team must choose one behavior to work on; use `define-key-behavior`
- Nobody has checked what research exists on a link; use `assess-evidence-base`
- The chain exists and the question is how to test it; use `plan-evaluation-design`

## Before you start

Ask these before producing anything. Do not ask anything the user has already answered.

1. **Required.** The outcome: what changes in whose lives, by when.
2. **Required.** The activities as delivered: what is done, by whom, to whom, how often.
3. **Required.** Who the activities reach and who the outcome is for, where these differ.
4. Optional. Evidence for any link: monitoring data, a pilot, an evaluation, a review of studies.
5. Optional. The behaviors the team believes the chain runs through.

If 1, 2, or 3 is missing, ask and stop. If the "outcome" is a behavior or an output ("500 workers trained"), ask what change in people's lives it serves. If 4 is missing, write "none supplied" in every evidence cell. If 5 is missing, derive the behaviors and mark each "inferred; team to confirm".

## What it draws on

- Mayne, J. (2015). Useful theory of change models. *Canadian Journal of Program Evaluation*, 30(2), 119–142. https://doi.org/10.3138/cjpe.230 Supports: the stages of a chain (reach, capacity change, behavior change, direct benefit), and the rule that a chain becomes a theory of change only when each link states what must occur for it to work.
- Skivington, K., Matthews, L., Simpson, S. A., et al. (2021). A new framework for developing and evaluating complex interventions: update of Medical Research Council guidance. *BMJ*, 374, n2061. https://doi.org/10.1136/bmj.n2061 Supports: using the theory to find the key uncertainties before an evaluation is planned.
- Jang, C., Koki, E., Nyaga, R., Okafor, A., Singh, J., Vang, A., & Wendel, S. (2024). *The Busara toolkit: leveraging behavioral science for development*. Busara Groundwork No. 10. https://doi.org/10.62372/WQSB6195 Supports: revising the causal pathways as the project learns.

**Where the evidence comes from:** This is a drafting procedure and makes no claim about how people behave. Its sources come from Canada, the United Kingdom, and Kenya; in a review of 92 impact evaluations of immunization programs in low- and middle-income countries, only 19 stated any assumptions. What is local is the evidence in each cell.

**Replication status:** Not applicable. No source tests whether a chain written this way leads to a better program. The four strength labels are this skill's own.

## How to do it

1. **Carry the outcome over as given.** A behavior or an output offered as the outcome stays a row in the chain.
2. **List the activities as delivered.** Mark any that are planned and not running.
3. **Name the behavior each activity runs through:** who must do what, when. Include the people who deliver as well as the people the outcome is for. An activity that reaches the outcome with nobody acting differently is an output; say so in the row.
4. **Write each link** as from, to, and the assumption: "if X, then Y, because Z". Z names what must hold for the link to work, such as the person reached being the one who decides. Check for a skipped stage: reach, a change in what people can do, a change in what they do, a benefit.
5. **Fill the evidence cell only from what the user supplied.** Add no citation from memory, because an invented source stops the team looking for a real one.
6. **Label the strength** by where the data came from:
   - **tested here:** data on this link from this program's population
   - **tested elsewhere:** a study or evaluation from another population
   - **plausible mechanism:** a reasoned argument with no data
   - **assumption:** the team's belief
7. **List the behaviors the chain depends on**, each with its link number, marked confirmed or inferred.
8. **Name the weakest links**, starting with the lowest label nearest the outcome, with the evidence that would raise each label.
9. **Stop.** Do not choose a target behavior, search for studies, or design a test.

See `references/worked-example.md` for a complete run.

## Output template

```markdown
# Theory of change

**Outcome (as given):** <who, what change, by when>
**Population:** <who the activities reach; who the outcome is for, if different>
**Activities (as delivered):** <list; mark any that are planned, not running>
**Evidence supplied:** <monitoring data / pilot / past evaluation / review of studies / none>

## Causal chain

| # | Link (from, to) | Assumption (if ..., then ..., because ...) | Evidence | Strength |
|---|---|---|---|---|
| 1 | <activity>, <output or behavior> | <...> | <source as supplied, or "none supplied"> | <tested here / tested elsewhere / plausible mechanism / assumption> |
| 2 | <behavior>, <intermediate outcome> | <...> | <...> | <...> |
| 3 | <intermediate outcome>, <outcome> | <...> | <...> | <...> |

## Behaviors the chain depends on
- <who does what, when> (link <#>); <confirmed by team / inferred; team to confirm>

## Weakest links
- Link <#>: <why it is the weakest>; <the evidence that would raise its label>

## What to check before relying on this
- <the assumption most likely to be wrong>
- <any behavior marked inferred>
- <anything outside the program that could move the outcome>
```

## Where it goes wrong

- **One chain for several outcomes.** A program that claims three outcomes gets three chains. One chain with three endpoints hides which links are shared.
- **Label inflation.** A pilot that measured nothing is not "tested here", and neither is a study from a neighboring country. The label records where the data came from, not how confident the team feels.
- **The table read as proof.** A complete table lists what to test. It is not evidence that the program works; say so when the chain goes into a proposal.

## When to bring in a specialist

Tell the user to consult a specialist when:
- The chain will justify a funding, scale-up, or policy decision, and a link near the outcome is labeled "assumption" or "plausible mechanism": an evaluation specialist
- A link runs through medication, violence, or child protection: a clinician or safeguarding lead, to check the assumption
- The team disagrees about which behavior the chain runs through: a behavioral scientist

Bring them: the chain table, the evidence supplied for each link, and the weakest links.
