---
name: audit-researcher-bias
description: >-
  Use when a team is about to start research and has not written down what it
  already believes about why its audience behaves as it does, or when someone
  says "we already know why they don't do it". Checks each stated belief: can
  it be tested as worded, does it assume the audience is like or unlike the
  team without evidence, and what would change the team's mind. Do not use
  when the question is what published research says; use
  assess-evidence-base. Not for listing the possible barriers to a behavior;
  use decompose-comb-barriers.
license: CC-BY-4.0
metadata:
  title: Check your team's assumptions about the audience
  type: atomic
  stage: diagnose
  version: "0.2.0"
  status: draft
  authors: "Joe Speed, Zezhen Wu"
  org: IL
  tested_in: not-applicable
  tags: "confirmation-bias, researcher-calibration, assumptions"
  consumes: "researcher-assumptions"
  produces: "bias-audit-report"
---

## What it does

Flags the weak points in what a team has written about why its audience behaves as it does.

**What this adds:** works only on beliefs the team has written in answer to three fixed prompts; checks every belief four ways (testable as worded, an assumed likeness or difference between team and audience, a named observation that would change the team's mind, experience carried over from another population); gives every flag a rewrite or a question; and sets when the audit is repeated.

## When to use it

### Use it when
- A project is starting, or entering a new phase, and the team has not written down why it thinks the audience behaves as it does
- Someone says "we already know why they don't do it"
- A team is about to list barrier hypotheses or write an interview guide and wants its own beliefs on record first

### Do not use it when
- The question is what published research says about the audience; use `assess-evidence-base`
- The team wants the possible reasons a defined behavior is not happening; use `decompose-comb-barriers`
- The team wants to know why an earlier attempt failed; use `review-prior-intervention`
- The unknowns are facts about the setting (who decides, which channels reach people); use `map-audience-context`

## Before you start

Ask these before producing anything. Do not ask anything the user has already answered.

1. **Required.** The team's written answers to three prompts, given before it looks at data on the audience:
   a. What do you believe causes the gap between what people do and what the program wants?
   b. Which population have you worked with most, and how similar is it to this one?
   c. What observation would change your mind?
2. Optional. Who wrote the answers, who will read the flags, and where the project stands.
3. Optional. A written review of any earlier attempt.

If 1 is missing, give the three prompts and stop. If an answer is only general humility ("I could be wrong about anything"), ask for a specific belief. If 2 is missing, assume one author who is also the only reader, at kickoff, and say so.

## What it draws on

- World Bank (2015). *World Development Report 2015: Mind, Society, and Behavior*, chapter 10. https://doi.org/10.1596/978-1-4648-0342-0 Supports: the premise and step 3. Of World Bank staff surveyed, 42% predicted that most poor people in Nairobi would agree that vaccines can cause sterilization; 11% of poor respondents there agreed.
- Gyani, A., Tindall, K., & Gallagher, R. (2022). *Explore Field Guide*. The Behavioural Insights Team. https://www.bi.team/wp-content/uploads/2022/11/BIT-Explore-Field-Guide.pdf Supports: writing the team's preconceptions down before research, to evaluate them later.
- Jang, C., Koki, E., Nyaga, R., Okafor, A., Singh, J., Vang, A., & Wendel, S. (2024). *The Busara toolkit: leveraging behavioral science for development*. Busara Groundwork No. 10. https://doi.org/10.62372/WQSB6195 Supports: prompt b and step 5. Its step "Catalog your perspective" asks what knowledge, preconceived notions, and biases the team brings.

**Where the evidence comes from:** This is a procedure and makes no claim about how the audience behaves. Its premise, that professionals misjudge the people they serve, comes from a survey of 1,850 World Bank staff set against poor respondents in Jakarta, Nairobi, and Lima. Every "check locally" line needs an answer from people in or close to the audience.

**Replication status:** Not applicable. No source tests whether writing beliefs down changes what a team later concludes.

## How to do it

1. **Copy the answers** verbatim, then split them into separate beliefs.
2. **Ask whether each belief can be tested.** If any result could be redescribed to fit it ("it is a discipline problem"), flag it and rewrite it so that one obtainable observation could contradict it.
3. **Look for assumed likeness and assumed difference.** Likeness: the belief takes the team's own circumstances as normal (a salary, a bank account, one person deciding alone). Difference: it gives the audience a mindset nobody has asked them about (fatalism, ignorance, not valuing the future). Name the local fact that would settle it and who can supply it.
4. **Check the answer to "what would change your mind?"** Quote it, or write "none given". Flag one that is vague or needs proof of something unobservable, such as intent; such a belief survives any data. Write an observable version.
5. **Check the carry-over.** Record the population the team knows best, the similarity it claims, and what differs enough that experience may not transfer: how income arrives, who decides, which services exist.
6. **Cross-check any earlier review.** Flag a cause that earlier data did not support when it returns as a fresh belief.
7. **If nothing is flagged**, say so in one line and ask whether the answers were specific enough to audit.
8. **Set the next audit** at a project event: before diagnosis, before design, or after the first field findings. If the author is the only reader, name a second.

See `references/worked-example.md` for a complete run.

## Output template

```markdown
# Bias audit report

**Answers as given:**
a. <what the team believes is causing the gap, verbatim>
b. <the population the team knows best, and the similarity it claims, verbatim>
c. <what would change the team's mind, verbatim; or "none given">
**Written by:** <who> | **Flags read by:** <who; or "the same person"> | **Project stage:** <...>

## Beliefs that cannot be tested as worded
- "<belief>" **Why:** <how any observation could be redescribed to fit it>. **Rewrite:** <a version that one obtainable observation could contradict>

## Assumed likeness or difference
- "<belief>" **Assumes:** <the norm taken from the team's own circumstances, or the mindset given to the audience without asking>. **Check locally:** <the fact that would settle it, and who can supply it>

## What would change the team's mind
- "<belief>" **Answer given:** <verbatim; or "none given">. **Problem:** <vague / needs something unobservable / none>. **Observable version:** <what the team could see or count>

## Carry-over from another population
- **Population the team knows:** <as stated>. **Similarity claimed:** <as stated>. **What differs:** <...>. **Question to ask:** <...>

## Seen before
<a belief that an earlier review already found unsupported; or "No earlier review supplied.">

## Next audit
<the project event that triggers it, and who reads the flags>
```

## Where it goes wrong

- **The audit taken as the fix.** A flag changes nothing until someone checks it in the field, yet "we audited our assumptions" reaches design as if it had.
- **Softened flags.** The author is usually the reader, so the pull is to praise the team's self-awareness and bury the flag. State each flag plainly, first.
- **Answering for the audience.** The audit slides from "the team assumes vendors lack discipline" into arguing whether they do. It says what to check and who can answer; it never supplies the answer.

## When to bring in a specialist

Tell the user to consult a local researcher, or a behavioral scientist outside the team, when:
- Nobody on the team is from or close to the audience, so nobody inside can answer the "check locally" questions
- The beliefs concern stigmatized, clinical, or legal matters (mental health, violence, sexuality, substance use) that the team cannot ethically investigate alone
- The author is the only reader on a project with a large budget or a rollout decision

Bring them: the answers as written and the flags with their rewrites.
