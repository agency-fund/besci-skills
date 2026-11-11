---
name: audit-intervention-ethics
description: >-
  Use when a behavioral intervention has been drafted (a default, a pledge,
  an incentive, a message, a reminder) and someone asks "is this ok to do?",
  "is this manipulative?", or "do we need to tell them?", or a funder wants
  an ethics check before launch. Classifies the draft by whether people can
  see it and avoid it, rates six checks, and returns go, revise, or stop. Do
  not use when no draft exists yet; use select-intervention-levers. Not for
  the research ethics of a study, which belong to an ethics board.
license: CC-BY-4.0
metadata:
  title: Check an intervention is ethical before launch
  type: atomic
  stage: design
  version: "0.2.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  tested_in: not-applicable
  tags: "ethics, choice-architecture"
  consumes: "intervention-draft"
  produces: "ethics-review"
---

## What it does

Reviews one drafted intervention against published ethics guidance before launch.

**What this adds:** classifies the draft by two questions from the OECD's toolkit, whether people can tell they are being influenced and whether they can avoid it, then applies the toolkit's rule for that type; rates six checks as the least powerful person in the audience would meet them; never returns "go" above a failed check; and lists separately the questions for an ethics board.

## When to use it

### Use it when
- A draft intervention exists and a team, funder, or partner asks whether it is acceptable to run
- Someone asks "is this manipulative?", "will people feel shamed?", "do we have to tell them?", or "is it ok to pay poor people for this?"
- The draft shows who did and who did not do the behavior, or reaches children or people who depend on the deliverer

### Do not use it when
- No draft exists yet; use `select-intervention-levers`
- The question is the ethics of a study (consent to research, random assignment); take it to the organization's ethics board

## Before you start

Ask these before producing anything. Do not ask anything the user has already answered.

1. **Required.** The draft: what is delivered, to whom, and how it is meant to work (a default, a public pledge, a payment).
2. **Required.** Who delivers it, what hold they have over the audience (employer, lender, teacher, official), and whether the audience includes children or people in crisis.
3. **Required.** What the audience will and will not be told, including whether this is part of a trial.
4. Optional. What data it collects, and who sees it.

If 1 is missing, or nobody can say how the draft is meant to work, ask and stop. If 2 or 3 is missing, ask once; then rate the affected checks "cannot assess" and give no verdict above "revise". If 4 is missing, assume delivery records only.

## What it draws on

- OECD (2019). *Tools and Ethics for Applied Behavioural Insights: The BASIC Toolkit*. https://doi.org/10.1787/9ea76a8f-en Supports: the two classifying questions, the rule for each of the four types, and the checks on transparency, a way out, whose interest, and responsibility.
- Kettle, S., & Persian, R. (2022). *Target, Explore, Solution, Trial, Scale: An introduction to running simple behavioural insights projects*. The Behavioural Insights Team. https://www.bi.team/wp-content/uploads/2022/11/BIT-Handbook-How-to-run-simple-BI-projects.pdf Supports: checking side-effects and equity, and what decides whether an ethics board must review the draft.
- Feeney, L., Kopper, S., & Sautmann, A. (2022). *Ethical conduct of randomized evaluations*. J-PAL Research Resources. https://www.povertyactionlab.org/resource/ethical-conduct-randomized-evaluations Supports: the line between this review and research ethics.

**Where the evidence comes from:** This is a review procedure and makes no claim about how people behave. Its sources are guidance the OECD wrote for governments, a UK team's project guide, and a research network's guide to field trials. What differs by place is who can consent for whom, whether being seen reads as praise or as shame, and what power the deliverer holds.

**Replication status:** Not applicable. The sources state principles; none tests whether reviewers agree.

## How to do it

1. **Describe the intervention in one paragraph:** what is delivered, by whom, to whom, and how it is meant to work.
2. **Classify it.** Transparent: can people tell who is influencing them, how, and why? Avoidable: does it work through a conscious choice that people can decide against? One that works automatically, such as a default, is unavoidable. Judge both in practice, for the least powerful person in the audience.
3. **Apply the rule for the type.**
   - Transparent, avoidable: acceptable if it serves people's interests.
   - Transparent, unavoidable: also needs an easy route to object.
   - Not transparent, unavoidable: also needs its existence and purpose clearly communicated, and nobody held accountable for the result.
   - Not transparent, avoidable: not acceptable unless it prevents harm to others.
4. **Rate six checks** pass, concern, fail, or cannot assess, each with a reason.
   - **Transparency.** Write the plain disclosure the audience could be given. Would the intervention still work if they read it?
   - **Way out.** How does a person decline: how many steps, at what cost, seen by whom?
   - **Whose interest.** Who benefits, and by whose judgment? Public approval does not settle it.
   - **Who bears the cost.** Who is left out, exposed, or made worse off while the average improves?
   - **Pressure.** Does it rely on shame, fear, or deception?
   - **Responsibility and data.** Are people held to consequences they did not knowingly choose? What is collected about them, and who sees it?
5. **Give the verdict.** Go: every check passes, or each concern has a named mitigation. Revise: a fail, or an unmet condition of the rule, that a named change fixes. Stop: a fail no change fixes.
6. **List the changes required.** Do not rewrite the draft.
7. **List the questions for an ethics board**, and say whether it must see the draft before launch.

See `references/worked-example.md` for a complete run.

## Output template

```markdown
# Ethics review

**Intervention:** <one paragraph: what is delivered, by whom, to whom, and how it is meant to work>
**Deliverer's hold over the audience:** <the relationship; children or dependents: none / who>

## Type
- **Transparent:** <yes / no: whether people can tell who is influencing them, how, and why>
- **Avoidable:** <yes / no: whether it works through a conscious choice the least powerful person could decline>
- **Rule for this type:** <the rule from step 3>
- **Conditions:** <each condition of the rule: met / not met, with the reason>

## Checks

| Check | Rating | Reason |
|---|---|---|
| Transparency | <pass / concern / fail / cannot assess> | <the plain disclosure; whether the intervention survives it> |
| Way out | <...> | <how a person declines; steps; cost; who sees it> |
| Whose interest | <...> | <who benefits, by whose judgment> |
| Who bears the cost | <...> | <who is left out, exposed, or worse off> |
| Pressure | <...> | <the shame, fear, or deception relied on; or none> |
| Responsibility and data | <...> | <consequences people did not knowingly choose; what is collected; who sees it> |

## Verdict: <GO / REVISE / STOP>
<two to four sentences pointing at the rule and the rows that decided it>

## Changes required before launch
1. <a specific change; or "None.">

## Questions for an ethics board
- <a research-ethics question; or "None identified.">

**Board review before launch:** <required / advisable / not needed>, because <the organization's rules, the audience, or the risk of harm or distress>

## What this review could not assess
- <the missing fact, and who can supply it>
```

## Where it goes wrong

- **Reviewing the wording.** A friendly sentence announcing a default passes on transparency, while the default acts on everyone who never reads it.
- **"It works" as the answer to whose interest.** That shows the program got what it wanted, not that the person did.
- **Rating for the people who comply.** A public list honors those on it and exposes those who are not. Rate pressure and cost for the people left off.

## When to bring in a specialist

Tell the user to take the draft to the organization's ethics board, with the specialist noted, when:
- A check fails and the team wants to proceed, or disputes a "stop"
- The audience includes children, people in crisis, or people who depend on the deliverer: a safeguarding lead reviews before launch
- It could reveal a person's health, debt, or legal status: a data-protection officer checks what may be collected and shown
- People seen not to comply could face violence or lose income: a local qualitative researcher checks what being seen costs here

Bring them: the draft and the full review.
