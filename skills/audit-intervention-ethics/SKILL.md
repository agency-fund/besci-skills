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
  version: "0.3.0"
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

Ask these before producing the review. Do not ask anything the user has already answered.

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
4. **Rate the six checks in the template** pass, concern, fail, or cannot assess, each with a reason. For transparency, write the plain disclosure the audience could be given. For whose interest, public approval does not settle it.
5. **Give the verdict.** Go: every check passes, or each concern has a named mitigation. Revise: a fail, or an unmet condition of the rule, that a named change fixes. Stop: a fail no change fixes.
6. **List the changes required.** Do not rewrite the draft.
7. **List the questions for an ethics board**, and say whether it must see the draft before launch.

See `references/worked-example.md` for a complete run.

## Output template

```markdown
<Two or three plain sentences to the user: the verdict, the one thing that decided it, and that the decision to launch stays with them.>

# Ethics review: <the intervention, in a few words>

**The intervention:** <one paragraph: what is delivered, by whom, to whom, and how it is meant to work>
**The deliverer's hold over the audience:** <the relationship; children or dependents: none / who>

## What kind of influence this is
- **Can people tell they are being influenced, by whom, and why?** <yes / no, and why>
- **Can the least powerful person in the audience decline it?** <yes / no: whether it works through a choice they could turn down>
- **What the OECD toolkit asks of this kind of influence:** <the rule from step 3>
- **Whether the draft meets that:** <each condition: met / not met, with the reason>

## Six checks

| Check | Rating | Reason |
|---|---|---|
| Transparency: would it still work if people were told? | <pass / concern / fail / cannot assess> | <the plain disclosure; whether the intervention survives it> |
| Way out: how easy is it to say no? | <...> | <how a person declines; steps; cost; who sees it> |
| Whose interest it serves | <...> | <who benefits, by whose judgment> |
| Who bears the cost | <...> | <who is left out, exposed, or worse off> |
| Pressure: shame, fear, or deception | <...> | <what it relies on; or none> |
| Responsibility and data | <...> | <consequences people did not knowingly choose; what is collected; who sees it> |

## Verdict: <GO / REVISE / STOP>
<two to four sentences pointing at the rule and the rows that decided it>

## What would need to change before launch
1. <a specific change; or "Nothing.">

## Questions for an ethics board
- <a research-ethics question; or "None identified.">

**Board review before launch:** <required / advisable / not needed>, because <the organization's rules, the audience, or the risk of harm or distress>

## What this review could not assess
- <the missing fact, and who can supply it>

## Where you could go from here
<One line saying the review is done.>
<Two or three next moves that fit this verdict, each with why it would help and when it fits. Candidates:
- `draft-lever-content`, when the verdict is revise and the wording has to change
- `plan-prototype-test`, when a few people from the audience should see the revised draft before launch, to check they understand what they are agreeing to
- `select-intervention-levers`, when the verdict is stop and the team needs another way to address the barrier
- the ethics board, a safeguarding lead, or people from the audience, for what this review could not assess>
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
