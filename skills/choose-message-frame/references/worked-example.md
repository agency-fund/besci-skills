# Worked example: an iron tablet reminder for pregnant women in Malawi

A full run of the skill on a realistic case, showing the output it should produce. The case is illustrative, not a real program.

## The request

"We send a weekly SMS in Chichewa, from the clinic's number, to pregnant women enrolled in antenatal care at four rural clinics in Dedza district, reminding them to take their daily iron-folate tablet. Interviews found the barrier is forgetting on busy days; the tablets are free and women have them at home. The current draft, in English before translation: 'Taking your iron tablet every day keeps your blood strong for you and your baby. Take today's tablet after your evening meal.' Our program manager wants it to hit harder as a loss: 'If you skip your tablets your baby could be born too small or die.' No money is involved. About 1,200 women enroll each quarter and messages go per phone number, so we could randomize. We have not asked women how they react to wording like that."

## The output

```markdown
# Message frame decision

**Behavior:** Pregnant women enrolled at the four Dedza clinics take one iron-folate tablet every day from their first antenatal visit until delivery.
**Draft received:** "Taking your iron tablet every day keeps your blood strong for you and your baby. Take today's tablet after your evening meal." Weekly SMS from the clinic's number; English working copy, to be sent in Chichewa.
**Kind of behavior:** Lowers a risk, because the tablet reduces the chance of anemia; it does not show whether a woman has it.
**Vehicle:** Words only.

## Decision
- **Frame to use:** Gain.
- **Why:** The default. The behavior lowers a risk, and nothing is known locally that favors loss wording, so the loss version is not a candidate for sending.
- **Reason set aside:** "It would hit harder as a loss."

## The two versions
| | Gain | Loss |
|---|---|---|
| Text | "Taking your iron tablet every day keeps your blood strong for you and your baby. Take today's tablet after your evening meal." | "Missing your iron tablet leaves your blood weaker for you and your baby. Take today's tablet after your evening meal." |
| Held constant | The fact (iron and strong blood), the action (take today's tablet), the cue (after the evening meal), the sender, 23 words | Same, 21 words |
| States more than the benefit forgone | not applicable | Removed: "your baby could be born too small or die". The gain version makes no claim about birth weight or death, so this is a new and larger claim, not the other side of the same fact |

## Who the loss version could frighten or shame
- Women who have already missed tablets, who would read it as blame for a harm they cannot undo.
- Women who have lost a pregnancy or a child.
- Women whose tablets ran out between visits, who would hear the threat with no way to act on it.

## Pre-test
- **Who and how many:** Eight enrolled women, two from each clinic, with the message read aloud in Chichewa by a nurse aide they do not know.
- **Asked:** "What is this message asking you to do?" and "How did it make you feel?", for the gain version first.
- **Loss version is dropped if:** It is not being sent. If the team later wants it tested, it is read to the same eight women and dropped if any of them is distressed or says the clinic should not speak that way.

## If both versions are sent
- **Assigned at random by:** Not applicable: only the gain version is sent.
- **Outcome:** Not applicable.
- **Rule written down beforehand:** Not applicable.

## Specialist review
Not needed for the gain version. If the team returns to a loss version that names harm to the baby, a midwife and a local researcher review it before any woman hears it.

## What the evidence supports
That the choice between gain and loss wording makes little or no difference to behavior, with a slight edge for gain wording where the behavior prevents illness. Gain and loss wording made no difference to savings reminders sent by banks in Bolivia, Peru, and the Philippines. No trial of framed reminders for antenatal supplements was found, and no difference between the versions is promised for Dedza.

## What to check before relying on this
- Whether "keeps your blood strong" carries the intended meaning in Chichewa. Ask the eight women what they think the tablet does.
- Whether forgetting is still the barrier once the reminder arrives; if women report nausea, wording will not help.
```
