# Worked example: a peer-distributed HIV self-testing program moving from Lagos to Ekiti State, Nigeria

A full run of the skill on a realistic case, showing the output it should produce. The case is illustrative, not a real program.

## The request

"We tested a peer-distributed HIV self-testing program in Lagos, Mo Wa Mo Ri. Our intervention description (July 2026) says: a trained peer from the same community hands a self-test kit to a man aged 20 to 35, shows a 3-minute demonstration video in Yoruba or Pidgin on a tablet, walks him through the result card, and phones him 14 days later to ask about the result and refer anyone positive to a named clinic. Our theory of change: men accept a kit from someone like them; the video and the card teach correct use and reading of the result; the call links anyone positive to care. We are now taking it to Ekiti State. The state AIDS control agency wants community pharmacies to hand out kits instead of peers, the video re-recorded in Ekiti dialect, the result card unchanged, and the 14-day call dropped because the state will not fund phone credit; the pharmacist would tell the client to come back if positive. Separately, our Lagos monitoring found that about a third of peers skipped the video when the tablet battery was low and explained verbally instead. Please record the adaptations and tell us which ones matter."

## The output

```markdown
# Adaptation record: Mo Wa Mo Ri HIV self-testing, version 2026-11-11

**Baseline:** a peer hands a self-test kit to a man aged 20 to 35, shows a 3-minute demonstration video, walks through the result card, and phones 14 days later to refer anyone positive to a named clinic, as delivered in Lagos (intervention description, July 2026)
**Move to a new context:** Lagos to Ekiti State; urban to mixed peri-urban and rural; peers to community pharmacies; Yoruba and Pidgin to Ekiti dialect

## Core components
| Component | Job it does for the effect | Assumption behind it | May vary | May not vary | Status |
|---|---|---|---|---|---|
| Hand-over by a peer from the same community | Men aged 20 to 35 accept the kit | These men trust someone like them more than a health worker | Venue, day, hour | A hand-over by someone the men do not see as one of them | confirmed: named in the theory of change |
| 3-minute demonstration video | Correct use of the kit | Men will watch a short video in their own language | Language, dialect, device | Replacing the demonstration with nothing, or with a summary that skips steps | confirmed |
| Result card walk-through | Reading the result correctly | The card's pictures are read the same way by the new audience | Language | Removing the walk-through | confirmed |
| Phone call at 14 days with referral | Anyone positive reaches care | Men who test positive will not go to a clinic unprompted | Day of the call; call or visit | No active follow-up of positives | confirmed |

## Change log
| # | When | Planned? | Who decided | What changed | Level | Nature | Fidelity | Goal, and what prompted it |
|---|---|---|---|---|---|---|---|---|
| 1 | at scale-up | planned | State AIDS control agency | delivery, by whom: community pharmacists hand out kits instead of peers | program | substituted | unknown: the theory of change says men accept the kit from someone like them; whether they see a pharmacist that way is not known | reach and cost; no peer stipends, existing pharmacy network |
| 2 | at scale-up | planned | NGO program team with the agency | content: video re-recorded in Ekiti dialect | program | tailored | consistent: language may vary | comprehension; the new audience's dialect |
| 3 | at scale-up | planned | State AIDS control agency | content: 14-day call removed; pharmacist tells the client to come back if positive | program | removed | inconsistent: removes the only active follow-up of positives, which may not vary | reduce cost; no phone credit in the state budget |
| 4 | during delivery, in Lagos | unplanned | Individual peers | content: video skipped and replaced by a verbal explanation | provider | substituted | unknown: whether a verbal explanation teaches correct use was never checked | keep distributing; tablet battery flat |

## Taken together
The Ekiti version does not do every component's job: change 3 removes the follow-up of positives, and change 1 may remove the trust the hand-over carried. This version is a different intervention from the one tested, and the original evidence does not cover it.

## Flags
- **Change 3:** removes the job of linking positives to care; decided by the State AIDS control agency; reason: cost
- **Change 1:** may weaken the job of getting men to accept the kit; decided by the State AIDS control agency; reason: reach and cost
- **Change 4:** may weaken correct use for about a third of Lagos participants; no recorded decision; reason: flat tablet batteries. The Lagos evaluation describes a mixed version.

## Move to a new context (only when one is under way)
- **Fit:** the jobs depend on men trusting the person who hands over the kit and on someone following up positives; Ekiti has no peer network and an existing pharmacy network the state funds
- **Adaptations planned, and with whom:** changes 1 to 3, proposed by the agency; to be discussed with six Ekiti pharmacists and eight men from the target group, including whether a text at day 14 or a paid return visit could do the follow-up job
- **Piloting or evaluation warranted:** 4 pharmacies for 8 weeks, against 2 pharmacies with a peer present on distribution days, counting kits handed out, videos shown, and positives who reach a clinic within 30 days
- **Who keeps this record:** the NGO monitoring officer, updated after every monitoring round

## What to check before relying on this
- Change 3 matters most: the pilot must count positives who reach a clinic within 30 days under the come-back instruction and under any cheaper follow-up; if neither links positives to care, the Ekiti program does not do what the Lagos program did.
- The peer hand-over rests on the Lagos theory of change; if Ekiti men say they would accept a kit from a pharmacist as readily, its "may not vary" line changes, and change 1 becomes consistent.
```
