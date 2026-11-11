---
name: select-messenger
description: >-
  Use when the question is who should deliver a message: "should the nurse
  say this or the village elder?", "would a peer land better than our staff?".
  Also use when a program has made its own staff the sender without checking,
  or wants to pick community ambassadors. Rates candidates on what the
  audience has said, checks whether the leading one has power over the
  audience, and writes the messenger's brief. Do not use when the question is
  whose opinion the audience weighs for a practice; use map-reference-network.
  Not for the words; use draft-lever-content.
license: CC-BY-4.0
metadata:
  title: Choose who delivers the message
  type: atomic
  stage: design
  version: "0.2.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  tested_in: beyond-western-holds
  tags: "message-design, network"
  consumes: "barrier-diagnosis"
  produces: "messenger-choice"
---

## What it does

Chooses who delivers one message to one audience.

**What this adds:** stops when the barrier is one no messenger can fix; rates the program's current sender against a person the audience names; rates reach, likeness, expertise, and trust separately and marks unconfirmed ratings "assumed"; matches the messenger to the barrier by a stated rule; checks whether the leading candidate has power over the audience; and writes what the messenger carries and receives.

## When to use it

### Use it when
- Someone asks "who should say this?" or "would a peer be more convincing than our staff?"
- A program has made its own staff the sender without checking whether the audience trusts them
- A program wants community "ambassadors" and needs a way to pick them

### Do not use it when
- The question is whose behavior or approval the audience tracks for a practice; use `map-reference-network`
- The team needs the words; use `draft-lever-content`

## Before you start

Ask these before producing anything. Do not ask anything the user has already answered.

1. **Required.** The behavior (who, what, when) and the confirmed barrier the message addresses, with its evidence.
2. **Required.** The audience, and who talks to them about this topic now.
3. **Required.** The messengers the program could field, and whether any controls something the audience needs: wages, credit, land, grades, a service.
4. Optional. Whom the audience says they hear news from, and whose advice on this topic they act on.
5. Optional. Whether the program covers enough groups to try two messengers side by side.

If 1, 2, or 3 is missing, ask and stop. If 4 is missing, write the questions to ask and mark every rating "assumed". If 5 is missing, assume it does not.

## What it draws on

- Dolan, P., Hallsworth, M., Halpern, D., King, D., & Vlaev, I. (2010). *MINDSPACE: Influencing behaviour through public policy*. Institute for Government and Cabinet Office. https://www.instituteforgovernment.org.uk/sites/default/files/publications/MINDSPACE.pdf Supports: step 4. People weigh information by the messenger's perceived authority, likeness to themselves, and how they feel about them.
- BenYishay, A., & Mobarak, A. M. (2019). Social learning and incentives for experimentation and communication. *The Review of Economic Studies*, 86(3), 976–1009. https://doi.org/10.1093/restud/rdy039 Supports: steps 5 and 7. Farmers in Malawi were most convinced by communicators who shared their group identity or farming conditions; communicators' effort depended on incentives.
- Banerjee, A., Chandrasekhar, A. G., Duflo, E., & Jackson, M. O. (2019). Using gossips to spread information: Theory and evidence from two randomized controlled trials. *The Review of Economic Studies*, 86(6), 2453–2490. https://doi.org/10.1093/restud/rdz008 Supports: step 3. In India, information seeded with people villagers named as good at spreading it traveled further than with people chosen at random.

**Where the evidence comes from:** MINDSPACE was written for the United Kingdom government. Field trials in Malawi, India, Indonesia, and Honduras each found that who carries a message changes how far it spreads or whether people act on it. Check locally whether people named as good at spreading news are also trusted on this topic, and are willing.

**Replication status:** Mixed. No review was found that compares kinds of messenger by their effect on behavior. The rule in step 5 is this skill's own reading of a few field trials, in which the kind of messenger that did best differed.

## How to do it

1. **Check that a messenger can address the barrier:** people have not heard something, doubt that people like them do it, or distrust the source. If it is cost, supply, or distance, say so and stop.
2. **List at least three candidates:** the current sender, a person the audience would name, and others the program can field.
3. **Get the audience to name people.** Write two questions: "If we wanted everyone here to hear about X, whom should we tell?" (reach) and "Whose advice about X would you act on?" (trust). Ask about ten people per group.
4. **Rate each candidate separately** on reach (how many of the audience they talk to), likeness (same group and conditions as the audience), expertise or office, trust on this topic, and cost per contact. Keep expertise and trust apart: an audience can obey an official it does not believe.
5. **Choose by the barrier.** Not heard: reach first. Doubt that people like them do it: likeness first. Distrust of the source: trust on this topic first. Name the runner-up.
6. **Check for power.** If the leading candidate controls something the audience needs, people may agree without believing or feel unable to refuse. Choose the runner-up, or name the specialist.
7. **Write the messenger's brief:** what they say, to whom, how often, until when, what they receive, and whether they do the behavior themselves.
8. **Set the comparison.** Where there are enough groups, give some the chosen messenger and others the current sender, and name the outcome. Otherwise say who will be asked whether they heard the message, and from whom.
9. **State what the evidence supports.** Promise no effect size.

See `references/worked-example.md` for a complete run.

## Output template

```markdown
# Messenger choice

**Behavior:** <who, what, when>
**Barrier the message addresses:** <the barrier and its evidence>
**Kind of barrier:** <not heard / doubt that people like them do it / distrust of the source>
**Audience, and who talks to them about this now:** <...>

## Candidates
| Candidate | Reach | Likeness | Expertise or office | Trust on this topic | Cost per contact | Basis |
|---|---|---|---|---|---|---|
| <current sender> | <high / medium / low: why> | <...> | <...> | <...> | <...> | <audience answers / records / assumed> |
| <person the audience names> | <...> | <...> | <...> | <...> | <...> | <...> |
| <other candidate> | <...> | <...> | <...> | <...> | <...> | <...> |

## What the audience was asked
- **Reach question:** <"If we wanted everyone here to hear about X, whom should we tell?", in local wording>
- **Trust question:** <"Whose advice about X would you act on?", in local wording>
- **Who was asked:** <how many, chosen how; or "not yet run: ratings above are assumed">
- **Who they named:** <roles with counts; or "pending">

## Choice
- **Messenger:** <role>
- **Rule applied:** <not heard: reach first / doubt: likeness first / distrust: trust first>
- **Runner-up:** <role, and why second>
- **Power over the audience:** <none / yes: what they control, and what was done about it>

## Messenger's brief
- **Says:** <the point, not the wording>
- **To whom, how often, until when:** <...>
- **Receives:** <payment, airtime, recognition, or nothing; and the limit on what else they are asked to carry>
- **Does the behavior themselves:** <yes / no / not known>

## Comparison
- **Chosen messenger in:** <which groups>
- **Current sender in:** <which groups>
- **Outcome, and who records it:** <...>
- **If no comparison is possible:** <who is asked whether they heard the message, and from whom>

## Specialist review
<not needed / <who>, because <the reason>>

## What the evidence supports
<the direction, and the nearest field evidence with where it was run; no effect size promised>

## What to check before relying on this
- <the rating marked "assumed" that the choice depends on>
```

## Where it goes wrong

- **Reach read off the staff list.** The program names its own health worker because it employs her; the village would have named a shopkeeper.
- **The expert by default.** In a United States vaccine trial, lay people like the audience moved the most reluctant more than experts did.
- **A rise credited to the messenger.** More visits bring more uptake whoever makes them; without the comparison, messenger and attention cannot be told apart.

## When to bring in a specialist

Tell the user to consult a specialist before anything is delivered when:
- The only workable messenger has power over the audience (employer, lender, official, teacher): a safeguarding lead reviews whether people can decline
- The topic is stigmatized (HIV, contraception, debt) or the audience includes children: a local qualitative researcher checks whether being approached by this person exposes anyone
- A religious or traditional leader leads in a setting the team does not know: someone with local standing advises on what the endorsement commits the program to

Bring them: the candidate table, the questions and answers, and the brief.
