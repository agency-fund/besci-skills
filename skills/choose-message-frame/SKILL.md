---
name: choose-message-frame
description: >-
  Use when a team is choosing whether a message or offer should say what
  people gain by acting or what they lose by not acting, or assumes that
  "losses hit harder". Makes the gain version the default, writes both
  versions with only the frame changed, names who the loss version could
  frighten, and sets a pre-test. Do not use when no draft exists yet; use
  draft-lever-content. Not for the amount, condition, or timing of a payment;
  use design-incentive-scheme.
license: CC-BY-4.0
metadata:
  title: Choose gain or loss wording for a message
  type: atomic
  stage: design
  version: "0.3.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  tested_in: beyond-western-holds
  tags: "framing, message-design"
  consumes: "intervention-draft"
  produces: "intervention-draft"
---

## What it does

Decides whether one message or offer states what people gain by acting or what they lose by not acting.

**What this adds:** rejects "losses hit harder" as a reason; makes the gain version the default; writes both versions with only the frame changed; refuses a loss version that states more than the benefit forgone; names who it could frighten or shame; requires a pre-test before it is used; and promises no difference between the two.

A frame is the side of one fact a message states: "the vaccine protects your child" (gain) or "without it your child is at risk" (loss).

## When to use it

### Use it when
- A team says "loss aversion means we should tell them what they will lose"
- Someone asks whether a text should say "protect your baby" or "you are putting your baby at risk"
- A program wants to pay a bonus up front and take it back if a target is missed

### Do not use it when
- No draft exists; use `draft-lever-content`
- The question is how much to pay, to whom, or on what condition; use `design-incentive-scheme`
- The question is how to run a trial comparing versions; use `choose-trial-design`

## Before you start

Ask these before deciding on the wording. Do not ask anything the user has already answered.

1. **Required.** The draft message or offer in full, with the behavior it asks for (who, what, when), the channel, and the sender.
2. **Required.** Whether the behavior lowers a risk (a vaccine, saving) or reveals one (an HIV test, a screening).
3. **Required.** Whether a loss version would take back or withhold money people treat as theirs.
4. Optional. How this audience reacts to hearing a bad outcome named.
5. Optional. Whether the channel can send two versions at random.

If 1, 2, or 3 is missing, ask and stop. If 4 or 5 is missing, assume nothing is known and that it cannot.

## What it draws on

- Gallagher, K. M., & Updegraff, J. A. (2012). Health message framing effects on attitudes, intentions, and behavior: A meta-analytic review. *Annals of Behavioral Medicine*, 43(1), 101–116. https://doi.org/10.1007/s12160-011-9308-7 Supports: step 2. Gain wording did slightly better for prevention; frames made no difference for detection or for intentions.
- Akl, E. A., Oxman, A. D., Herrin, J., Vist, G. E., Terrenato, I., Sperati, F., et al. (2011). Framing of health information messages. *Cochrane Database of Systematic Reviews*, 2011(12), CD006777. https://doi.org/10.1002/14651858.CD006777.pub2 Supports: steps 3 and 9. The frames differed little or not at all in effect on behavior.
- Dorison, C. A., Lerner, J. S., Heller, B. H., Rothman, A. J., Kawachi, I. I., Wang, K., et al. (2022). In COVID-19 health messaging, loss framing increases anxiety with little-to-no concomitant benefits: Experimental evidence from 84 countries. *Affective Science*, 3(3), 577–602. https://doi.org/10.1007/s42761-022-00128-3 Supports: steps 5 and 6.

**Where the evidence comes from:** The reviews pool health studies; their abstracts name no countries. Gain and loss wording made no difference to savings reminders in Bolivia, Peru, and the Philippines, and no framed text changed COVID-19 behavior in Bihar, India; loss-framed pay raised output in Uganda and in a Chinese factory. Check locally whether a bad outcome for a child may be named aloud.

**Replication status:** Contested. Reviews agree the difference between frames is small and disagree on its direction for detection. Loss-framed pay showed a clear effect in laboratory studies and almost none in field studies.

## How to do it

1. **Check that the frame is the open question.** A frame does not remove cost, distance, or distrust. If one of those is the barrier, say so and stop.
2. **Record the kind of behavior and whether it is words or money:** lowers a risk or reveals one; words only, or money.
3. **Make the gain version the default,** because the measured difference is small and the loss version has a known cost, anxiety. Keep a loss version as a candidate only when the behavior reveals a risk or the team has local evidence for it.
4. **Write both versions** with the same facts, action, sender, and length. The loss version states the benefit forgone and nothing more: no new harm, blame, or worst case.
5. **Name who the loss version could frighten or shame:** people who cannot act and so hear only the threat, people who already have the condition, people for whom naming the outcome is taboo.
6. **Set the pre-test.** Read both versions to five to ten people from the audience; ask what the message wants them to do and how each made them feel. Drop the loss version if it distresses anyone.
7. **Decide.** Where a loss version is still a candidate, the channel can randomize, and the audience is large, send both and measure the behavior, not intention, having written down that the gain version stays unless the loss version clearly does better. Otherwise use the gain version.
8. **If the loss version takes back or withholds money, do not design it;** name the specialist.
9. **State what the evidence supports.** Promise no difference between the versions.

See `references/worked-example.md` for a complete run.

## Output template

```markdown
<Two or three plain sentences to the user: which wording to use and the one fact that decided it, anything taken out of the loss version and why, and that no difference between the versions is promised.>

# Gain or loss wording for <the message, in a few words>

**Behavior:** <who, what, when>
**Draft received:** <the text or offer; channel; sender>
**Kind of behavior:** <lowers a risk / reveals a risk>, because <...>
**Words or money:** <words only / money: what a loss version would do to it>

## Decision
- **Frame to use:** <gain / both, sent at random / gain; loss version not designed, see specialist review>
- **Why:** <the default; or the stated reason a loss version is a candidate>
- **Reason set aside:** <"losses hit harder", if it was offered; or "none offered">

## The two versions
| | Gain | Loss |
|---|---|---|
| Text | "<...>" | "<...>" |
| Held constant | <facts, action, sender, length> | <same> |
| States more than the benefit forgone | not applicable | <no / removed: "..."> |

## Who the loss version could frighten or shame
- <group, and why; or "none identified">

## Pre-test
- **Who and how many:** <five to ten people from the audience; who reads it to them>
- **Asked:** <what the message wants them to do; how each version made them feel>
- **Loss version is dropped if:** <...>

## If both versions are sent
- **Assigned at random by:** <person, household, clinic; or "not possible: gain version used">
- **Outcome:** <the behavior, and the record it is read from>
- **Rule written down beforehand:** <gain version stays unless the loss version clearly does better>

## Specialist review
<not needed / <who>, because <the loss version takes back or withholds money / the behavior reveals a feared or stigmatized condition>>

## What the evidence supports
<the direction, and the nearest field evidence with where it was run; no difference promised>

## What to check before relying on this
- <the assumption most likely to be wrong>

## Where you could go from here
<One line saying the decision on wording is done.>
<Two or three next moves that fit what this run found, each with why it would help and when it fits. Candidates:
- `plan-prototype-test`, when the pre-test needs a full plan, or the same few people should also check that the message is understood in translation
- `choose-trial-design`, when both versions will be sent at random and the team has to settle what is randomized and what is compared
- `audit-intervention-ethics`, when a loss version is still a candidate, or the sender has power over the audience (an employer, a lender, a clinic)
- `design-incentive-scheme`, when the offer involves money and its amount, condition, or timing is still open
- a labor-law or ethics reviewer, when a loss version would take back or withhold money people treat as theirs
- a local health worker or community member, when nobody has asked whether the bad outcome may be named aloud there>
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

- **A fear appeal passed off as a loss frame.** "Your baby could die" is not the mirror of "keeps your baby healthy". Once the loss version carries a larger claim, any difference belongs to the claim.
- **Loss wording from a sender with power.** From an employer, a lender, or a clinic that controls a service, "you will lose" reads as a threat.
- **A small test read as a verdict.** A few hundred recipients cannot show a difference this small; "no difference" then says nothing about the frames.

## When to bring in a specialist

Tell the user to consult a specialist before any pilot when:
- A loss version would take back or withhold wages, stipends, or benefits: a labor-law or ethics reviewer
- The behavior reveals a feared or stigmatized condition (HIV, tuberculosis, cancer): a clinician or counselor and a local researcher review both versions before the pre-test

Bring them: both versions, the reason a loss version is wanted, and any pre-test results.
