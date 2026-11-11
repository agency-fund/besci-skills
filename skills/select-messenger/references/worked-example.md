# Worked example: who tells pregnant women in Malawi that the tablets are safe

A full run of the skill on a realistic case, showing the output it should produce. The case is illustrative, not a real program.

## The request

"Behavior: pregnant women enrolled at our 12 health centers in Mchinji district take one iron-folate tablet daily from the first antenatal visit until delivery. We interviewed 48 women. They stop in the first weeks because they and their husbands read the nausea as a sign that the 'hospital medicine' is harming the pregnancy, and nobody they trust has told them otherwise. Tablets are free and in stock. Women come to antenatal visits; most belong to a church women's guild that meets weekly; Health Surveillance Assistants (HSAs) visit each village about monthly and reach perhaps a third of households. In the interviews we asked whose advice about pregnancy they act on: 31 named the guild leader, 12 the antenatal nurse, 5 the HSA. We did not ask whom to tell so that news spreads. We could field the HSA (who delivers the message now), the antenatal nurse, the group village headman, the guild leader, or a mother who finished the course last year. The headman allocates land and farm-input coupons. We can split the 12 catchments. Who should deliver the message?"

## The output

```markdown
# Messenger choice

**Behavior:** Pregnant women enrolled at the 12 health centers in Mchinji district take one iron-folate tablet daily from the first antenatal visit until delivery.
**Barrier the message addresses:** Women and their husbands read nausea as a sign that the tablets harm the pregnancy, and nobody they trust has said otherwise (interviews with 48 women). Cost and supply are ruled out: tablets are free and in stock.
**Kind of barrier:** Distrust of the source.
**Audience, and who talks to them about this now:** Pregnant women in the 12 catchments. The HSA raises the tablets on a monthly village visit that reaches about a third of households; the nurse does so at antenatal visits.

## Candidates
| Candidate | Reach | Likeness | Expertise or office | Trust on this topic | Cost per contact | Basis |
|---|---|---|---|---|---|---|
| HSA (current sender) | Low: monthly visit, a third of households | Medium: lives nearby, employed by the health service | Medium: trained health worker | Low: named by 5 of 48 | Low: already paid | Reach from program records; trust from audience answers |
| Women's guild leader | High: most women attend the weekly guild | High: a mother from the same villages | Low: no health training | High: named by 31 of 48 | Low: a short briefing each month | Trust from audience answers; reach and likeness assumed |
| Antenatal nurse | Medium: every enrolled woman, only on visit days | Low | High | Medium: named by 12 of 48 | None extra | Trust from audience answers; reach from clinic records |
| Mother who finished the course | Low: her own neighbors | High | Low | Not known: nobody was asked about her | Low | Assumed |
| Group village headman | High: village meetings, which few women attend | Low | High office | Not known: nobody named him | Low | Assumed |

## What the audience was asked
- **Reach question:** "If we wanted every pregnant woman here to hear something about the tablets, whom should we tell?" Not yet asked.
- **Trust question:** "Whose advice about pregnancy do you act on?" Asked.
- **Who was asked:** 48 enrolled women, in interviews at the health centers. Women who had stopped attending were not reached.
- **Who they named:** Guild leader 31; antenatal nurse 12; HSA 5.

## Choice
- **Messenger:** The women's guild leader in each catchment.
- **Rule applied:** Distrust: trust first. She is the person most women say they act on, and she is like them.
- **Runner-up:** The antenatal nurse: the expertise the guild leader lacks, and trusted by a quarter of the women, but she sees them only on visit days and husbands never hear her.
- **Power over the audience:** None for the guild leader. The headman controls land and input coupons, so he is not used.

## Messenger's brief
- **Says:** What the antenatal nurse has confirmed in writing about nausea and the tablets, and, where it is true, that she took them herself. She gives no other medical advice and sends questions to the nurse.
- **To whom, how often, until when:** Women at the weekly guild meeting, once a month, for the six months of the pilot.
- **Receives:** A half-day briefing from the nurse and airtime each month. She is asked to carry no other program's message during the pilot.
- **Does the behavior themselves:** Not known. Ask each leader whether she took the tablets in her own pregnancies.

## Comparison
- **Chosen messenger in:** Six catchments, drawn at random.
- **Current sender in:** The other six, where the HSA continues as now.
- **Outcome, and who records it:** Women who collect their second month of tablets, from the antenatal register kept by the nurse.
- **If no comparison is possible:** Not applicable.

## Specialist review
A person with standing in the local church advises, before any leader is briefed, on what the guild's involvement commits the program to. No safeguarding review is needed: the chosen messenger controls nothing the women need.

## What the evidence supports
That people act more readily on a message from someone like themselves whom they trust on the topic. Farmers in Malawi were most convinced by communicators who shared their group identity or farming conditions. No trial of messengers for antenatal supplements was found, and no effect size is promised for Mchinji.

## What to check before relying on this
- The guild leader's reach is assumed. Ask the reach question of ten women per catchment, including women who are not in the guild.
- The 48 women were interviewed at health centers, so those who trust the clinic least are missing. Ask ten women who have stopped attending whom they act on.
- Husbands share the belief and do not attend the guild. Ask who would need to tell a husband.
```
