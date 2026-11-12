---
name: draft-lever-content
description: >-
  Use when an intervention has been chosen and the team needs the words: a
  text message, a script, a poster, a sign, app wording. Also use to check
  existing copy against the technique it is meant to deliver. Drafts the
  content, ties every line to what the technique requires, and sets the
  comprehension test it must pass before launch. Do not use when the
  intervention is not yet chosen; use select-intervention-levers. Not for a
  technique with its own skill, such as write-social-norm-message.
license: CC-BY-4.0
metadata:
  title: Write an intervention's messages and scripts
  type: atomic
  stage: design
  version: "0.3.0"
  status: draft
  authors: "Joe Speed, Zezhen Wu"
  org: IL
  tested_in: beyond-western-differs
  tags: "behavior-change-techniques, east, message-design"
  consumes: "intervention-levers"
  produces: "intervention-draft"
---

## What it does

Drafts the words for an intervention that has already been chosen.

**What this adds:** states what the chosen technique must contain; ties every line of the draft to that requirement and cuts lines that deliver nothing; makes no claim about what other people do without a named data source; labels copy not in the audience's language as working copy for a native speaker to redraft; and sets a comprehension test with a sample size and a pass mark.

## When to use it

### Use it when
- An intervention is chosen and someone asks for "the message", "the script", "the sign", or "the app wording"
- A field team is about to write the copy on the spot
- Draft copy exists and the team wants to know whether it delivers the technique or only reads well

### Do not use it when
- The intervention is not chosen, or is named only as a category ("change the environment", "educate people"); use `select-intervention-levers`
- The technique has its own skill: `write-social-norm-message`, `choose-message-frame`, `design-reminder-schedule`, `draft-implementation-intention-prompt`, `draft-values-affirmation`, `draft-belonging-story`, or `adapt-growth-mindset-message`

## Before you start

Ask these before producing the draft. Do not ask anything the user has already answered.

1. **Required.** The chosen intervention: the technique, the barrier it answers, and the behavior (who does what, when).
2. **Required.** The channel (text message, spoken script, sign, screen) and how the team knows the audience uses it.
3. **Required.** The final copy's language, the audience's reading level, and who on the team speaks that language natively.
4. Optional. Data, with its source, on how many people already do the behavior.
5. Optional. Existing draft copy.

If 1 is missing or names only a category, ask and stop. If 2 is missing, ask once; then mark the channel "unconfirmed". If 3 is missing, write English working copy and say so. If 4 is missing, make no claim about what others do.

## What it draws on

- Kok, G., Gottlieb, N. H., Peters, G.-J. Y., et al. (2016). A taxonomy of behaviour change methods: An Intervention Mapping approach. *Health Psychology Review*, 10(3), 297–312. https://doi.org/10.1080/17437199.2015.1077155 Supports: the trace. A method works only if its practical form keeps the conditions that make it effective.
- Kettle, S., & Persian, R. (2022). *Target, Explore, Solution, Trial, Scale: An introduction to running simple behavioural insights projects*. The Behavioural Insights Team. https://www.bi.team/wp-content/uploads/2022/11/BIT-Handbook-How-to-run-simple-BI-projects.pdf Supports: the drafting rules, and testing a draft by asking people to use it.
- The Behavioural Insights Team (2024). *EAST: Four simple ways to apply behavioural insights* (revised and updated edition). https://bi.team/wp-content/uploads/2014/04/BIT-EAST.pdf Supports: the EAST check (easy, attractive, social, timely).

**Where the evidence comes from:** The drafting rules come from a UK team's trials of letters, emails, and texts, mostly in wealthy Western countries. Large trials of rewritten tax messages in Guatemala and Indonesia found that a message beat no message, and that which rewrite did best depended on what it added. Reading level, idiom, and channel are local, so test the draft on people from the audience.

**Replication status:** Mixed. Clearer messages have raised response in many trials, but not every rewrite works: in Guatemala two of four rewritten letters raised payment.

## How to do it

1. **State what the technique must contain:** the ingredient without which it would be a different technique. Copy it from the published definition if you have it open; otherwise mark your wording "paraphrase".
2. **Fix the channel and the moment:** when and where the person decides.
3. **Write the language note.** A native speaker writes the final version afresh from the working copy, because a translation carries the wrong register and idiom. If the team has no native speaker, say a local writer is needed.
4. **Draft the content.** Put the key message first, ask for one action, say how to do it, and cut what is not needed to act. A ten-year-old should understand it.
5. **Trace every line.** Beside each element, write the part of step 1's requirement it delivers. Cut an element that delivers nothing, or label it scaffolding (a greeting). Then cover the technique's name: if the copy could now belong to any campaign, redo the trace.
6. **Write the delivery notes:** who the content appears to come from and why this audience trusts them; when it arrives; how many times before it is ignored or resented.
7. **Run the EAST check.** Under "social", make a claim about what others do only with a named data source; otherwise write "none made" and why.
8. **Set the test before launch.** At least five people from the audience see the final-language version cold, then say or show what it asks of them. State the pass mark. "Do you understand?" does not count; people say yes to please.
9. **Say what the content cannot do:** what must exist for it to work, and which claims still need checking.

See `references/worked-example.md` for a complete run.

## Output template

```markdown
<Two or three plain sentences to the user: what the copy asks people to do, the one thing it must contain to deliver the technique, and that it is not ready until people from the audience pass the test in the final language.>

# Draft wording: <the intervention, in a few words>

**Behavior:** <who does what, when>
**Barrier it answers:** <the confirmed barrier>
**Technique:** <name; taxonomy label if known>
**What it must contain:** <the ingredient without which this is a different technique; "(paraphrase)" unless copied from the published definition>
**Channel and moment:** <channel and format; when and where it reaches the person; "unconfirmed" if nobody has checked that the audience uses it>
**Language note:** <language of the final copy; who drafts it; whether the copy below is working copy>

## Draft content
<the literal copy: message text, script lines, sign wording, screen text>

## What each part of the draft delivers

| Part | What it delivers |
|---|---|
| "<quoted element>" | <the part of "what it must contain" it delivers; or "scaffolding: <why it stays>"> |

## Delivery notes
- **Sender:** <who it appears to come from; why this audience trusts them>
- **Timing:** <when, relative to the moment of decision>
- **How often is too often:** <how many times before it is ignored or resented>

## EAST check: is it easy, attractive, social, and timely?
- **Easy:** <the one action; the reading-level check>
- **Attractive:** <what draws attention at the moment of delivery>
- **Social:** <the claim about what others do, with its data source; or "none made: <why>">
- **Timely:** <how delivery meets the moment>

## Test before launch
<who, how many, what they are asked to say or do, the pass mark; run on the final-language version>

## What this content does not do
- <what must exist for the content to work; which claims still need checking>

## Where you could go from here
<One line saying the draft is done.>
<Two or three next moves that fit what this run found, each with why it would help and when it fits. Candidates:
- `plan-prototype-test`, when the team wants to see what a few people from the audience do with the draft, not only whether they understand it
- `audit-intervention-ethics`, before the draft reaches people, and especially when it sets a default, makes a claim about others, or comes from someone with a hold over the audience
- `select-messenger`, when nobody has checked that the audience trusts the sender
- `choose-message-frame`, when the copy states a consequence and the team is unsure whether to put it as a gain or a loss
- a native speaker from the audience, when the copy above is working copy in another language>
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

- **A second technique slipped in.** "While we're at it, add a pledge." One draft delivers the one technique that was chosen; an added one is an intervention nobody diagnosed.
- **A text message by habit.** Most published examples are texts, so drafts default to them. When the barrier sits at a place (a kiosk, a clinic desk), the content belongs there.
- **A passed test read as proof.** The test shows that people understand the request, not that they will act on it.

## When to bring in a specialist

Tell the user to consult the relevant specialist when:
- The copy states a health, financial, or legal fact: a clinician, compliance lead, or lawyer checks it first, because a comprehension test does not check truth
- The audience includes children, people in crisis, or a stigmatized group: a safeguarding or community review comes before the test
- The test fails twice: a qualitative researcher judges whether the technique, the channel, or the wording is at fault

Bring them: what the technique must contain, the draft with its trace, and the test results so far.
