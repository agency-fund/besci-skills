---
name: write-social-norm-message
description: >-
  Use when a team wants to tell people what most of their peers do or approve
  of ("9 out of 10 parents here vaccinate"), or has a draft with such a line
  and wants it checked. Writes the message from a dated figure for a named
  group, adds a line for people who already do the behavior, and sets a check
  for backfire. Do not use when it is not yet known whether what others do
  matters for the behavior; use diagnose-social-norm. Not for a report that
  compares each person with their peers; use design-feedback-report.
license: CC-BY-4.0
metadata:
  title: Tell people what most of their peers already do
  type: atomic
  stage: design
  version: "0.3.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  tested_in: beyond-western-holds
  tags: "social-norms, message-design"
  consumes: "social-norm-diagnosis"
  produces: "intervention-draft"
---

## What it does

Writes one message that tells people what most of their peers do or approve of.

**What this adds:** refuses to write "most people" without a dated figure for a named group; stops when most of that group does the unwanted thing; never rounds a share up; adds a line of approval for people who already do the behavior; deletes any line that says how many do not; and sets a check on those people before wide use.

## When to use it

### Use it when
- A diagnosis or survey shows people underestimate how many peers do or approve of a behavior
- Someone asks "can we just say most people already do this?"
- A draft makes a claim about what others do and the team wants it checked

### Do not use it when
- Nobody has checked whether what others do or expect matters for this behavior; use `diagnose-social-norm`
- It is not known whose behavior and approval the audience tracks; use `map-reference-network`
- Each person is to be shown their own record against their peers'; use `design-feedback-report`

## Before you start

Ask these before producing the message. Do not ask anything the user has already answered.

1. **Required.** The behavior (who, what, when), and what the audience believes their peers do and approve of, from a norm diagnosis, a survey, or interviews.
2. **Required.** What those peers really do: the share, the group it describes, the source, and the date. Where measured, the share who approve.
3. **Required.** The channel and the sender.
4. Optional. Whether the behavior is illegal, stigmatized, or private.
5. Optional. Whether records show who already does the behavior.

If 1, 2, or 3 is missing, ask and stop. If 4 is missing, treat health status, sex, debt, and the law as sensitive. If 5 is missing, assume none.

## What it draws on

- The Behavioural Insights Team (2024). *EAST: Four simple ways to apply behavioural insights* (revised and updated edition). https://bi.team/wp-content/uploads/2014/04/BIT-EAST.pdf Supports: steps 2, 3, and 6, and stating what people do together with what they approve of.
- Schultz, P. W., Nolan, J. M., Cialdini, R. B., Goldstein, N. J., & Griskevicius, V. (2007). The constructive, destructive, and reconstructive power of social norms. *Psychological Science*, 18(5), 429–434. https://doi.org/10.1111/j.1467-9280.2007.01917.x Supports: steps 5 and 8. Told their neighborhood's average energy use, low users raised theirs; a message of approval removed the rise.
- Kettle, S., Hernandez, M., Ruda, S., & Sanders, M. (2016). *Behavioral interventions in tax compliance: Evidence from Guatemala*. World Bank Policy Research Working Paper 7690. https://doi.org/10.1596/1813-9450-7690 Supports: step 4. Its letter cited the 64.5% who had paid.

**Where the evidence comes from:** Letters stating how many taxpayers had paid raised payment in Guatemala and Peru; in Saudi Arabia, telling men how many peers approved of women working changed what they did. A review of 91 environmental field experiments found norms tended to be less influential in collectivistic countries. Check locally who the audience counts as "people like me" and whether they believe this sender.

**Replication status:** Replicated in direction, with small and uneven effects. The rise among people already doing well comes from one study; a program covering 600,000 United States households did not find it.

## How to do it

1. **Check that the message has a job.** It corrects a belief: people think fewer peers do or approve of the behavior than really do. If their belief is accurate, the barrier is cost or access, or people expect punishment for the behavior, say a norm message is the wrong tool and stop.
2. **Choose the kind of message from the figures.**
   - At least half do the behavior: state what most do, and what most approve of where measured.
   - Fewer than half do it and a measured majority approves: state only what most approve of.
   - Neither: stop. Saying that most people do not do it advertises the unwanted behavior.
3. **Name the group the figure describes, and no other.** Prefer the closest group the audience identifies with; people follow those they see as like themselves.
4. **State the figure plainly,** in counts people use ("6 out of 10") and with its period. Round down, never up.
5. **Add one line of approval for people who already do the behavior** ("Thank you if you were one of them"), so being ahead does not read as permission to ease off.
6. **Delete every line that says or implies how many do not do it.**
7. **Ask for one action,** with where and by when.
8. **Set two checks before wide use.** Ask about ten recipients who they think the group is and whether they believe the figure. Hold back a comparison group, follow people who already did the behavior separately, and withdraw the message if their rate falls.
9. **State the direction the evidence supports.** Promise no effect size.

See `references/worked-example.md` for a complete run.

## Output template

```markdown
<Two or three plain sentences to the user: what the message tells people and the figure it rests on, or why no norm message should be sent; the belief it corrects; and that it goes out widely only after the checks below.>

# Telling <the audience, in a few words> what most of their peers do or approve of

**Behavior:** <who, what, when>
**What the audience believes peers do and approve of:** <the belief, and how it was learned>
**What peers really do:** <share; the group it describes; source; date>
**What peers really approve of:** <share; group; source; date; or "not measured">
**Belief the message corrects:** <believed share against true share; or "none: a norm message is the wrong tool">

## Kind of message
- **Chosen:** <what most do / what most approve of / both / none>
- **Rule for these figures:** <at least half do it / fewer than half do it and a measured majority approves / neither: stopped>

## The message
<the text: the group named, the figure, the line of approval, one action with where and by when>

**Language:** <final / working copy for a native speaker to redraft>

## Checks on the claim
- **Figure in the message against figure in the data:** <both; rounded down, or exact>
- **Group named against group the figure describes:** <same / wider, and why>
- **Does the audience see this group as people like them:** <the evidence; or "not known: ask in the first check">
- **Lines saying how many do not do it:** <none / removed: "...">

## For people who already do the behavior
- **Line of approval:** <the sentence>
- **How they are identified:** <records / self-report / cannot be identified>

## Sender and timing
- **Sender:** <who, and why their approval counts with this audience>
- **When:** <how long before the moment of action; how many times>

## Before wide use
- **Ask about ten recipients:** <who they think the group is; whether they believe the figure>
- **Comparison:** <who does not receive the norm line; the outcome; when it is read>
- **Withdraw the message if:** <the result among people who already did the behavior>

## What the evidence supports
<the direction, and the nearest field evidence with where it was run; no effect size promised>

## What to check before relying on this
- <the assumption most likely to be wrong>

## Where you could go from here
<One line saying the message is done, or that the figures stopped it.>
<Two or three next moves that fit what this run found, each with why it would help and when it fits. Candidates:
- `map-reference-network`, when it is not known whether the audience sees the named group as people like them
- `audit-intervention-ethics`, before the message is sent, when the figure describes a small group, the behavior is private, or the sender has a hold over the audience
- `plan-prototype-test`, when the team wants to see what a few recipients do with the message, not only whether they believe the figure
- `choose-trial-design`, when the comparison should be set up as a randomized test
- `select-intervention-levers`, when a norm message turned out to be the wrong tool and the confirmed barrier needs another kind of intervention
- the records behind the figure, when they may be incomplete or cover only people the program registered>
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

- **A figure made to fit.** Widening the group until the share passes half produces a claim recipients can test against what they see, and a figure they disbelieve costs the sender trust.
- **Program records taken for the norm.** A share computed from enrolled clients describes enrolled clients; the audience's peers include people the program never registered.
- **Shared-resource behaviors.** Told that most people already give blood, a person may leave it to them; so too for other voluntary contributions to a common good.

## When to bring in a specialist

Tell the user to consult a specialist before anything is sent when:
- Most of the group does the unwanted thing and the team wants to cite a rising trend: a behavioral scientist, because trials of trend messages disagree
- The behavior is illegal, stigmatized, or private (HIV testing, contraception, debt): a local qualitative researcher and a safeguarding lead, because a figure about a small group can expose its members
- The practice is enforced by punishment (child marriage, cutting): a specialist in community norm change, because a message can single out the first people to act

Bring them: the figures with source and date, what the audience believes, and the draft.
