# Worked example: who pregnant women in rural Malawi follow on iron-folate tablets

A full run of the skill on a realistic case, showing the output it should produce. The case is illustrative, not a real program.

## The request

"Practice: pregnant women enrolled at four rural health centers in Mchinji district, Malawi, take one iron-folate tablet every day from the first antenatal visit to delivery. Earlier interviews suggested women stop because husbands and mothers-in-law expect them to avoid 'hospital medicine' in pregnancy, and a woman is blamed if anything goes wrong. We reach women through clinic nurses and through Health Surveillance Assistants (HSAs) at home. The four catchments hold about 4,000 households. We then interviewed 28 pregnant women alone (7 per center, every fourth name on the antenatal register, half in a first pregnancy). We asked whose opinion matters when they decide whether to take the tablets, who would notice, whose approval they would want, who they would ask, and for each person named whether they would take the tablets if that person told them to. Tallies: husband named by 22 (20 would follow him; 9 say he is against; he controls transport money); mother-in-law 19 (16 would follow; 15 say she is against; she lives in the compound and sees the tablets); own mother 11 (8 would follow, mostly first pregnancies; usually lives elsewhere); older neighbors and co-wives 9 (5 would follow); traditional birth attendant 7 (4 would follow; 5 say she is against); church women's guild leader 6 (5 would follow; 5 say she approves); HSA 4 (1 would follow); nurse 3 (1 would follow). We showed the tally to six women at one center: they said a woman's own mother matters most in a first pregnancy, and the birth attendant matters more at the two centers far from the road. Who do we need to be talking to?"

## The output

```markdown
The people pregnant women say they would follow on the tablets are their husbands and mothers-in-law, and both can also block it: husbands hold the transport money, and mothers-in-law see the tablets every day. The program reaches neither; it talks to women through nurses and HSAs, whom women named least and would rarely follow. What husbands and mothers-in-law actually think is so far known only from their wives.

# Whose opinion matters when pregnant women in Mchinji decide whether to take iron-folate tablets

**Practice:** Pregnant women enrolled at four rural health centers in Mchinji district take one iron-folate tablet every day from the first antenatal visit to delivery.
**Why others are thought to matter:** Earlier interviews: women stop because husbands and mothers-in-law expect them to avoid "hospital medicine" in pregnancy, and a woman is blamed if anything goes wrong.
**Who the program reaches now:** Pregnant women, through clinic nurses at antenatal visits and Health Surveillance Assistants (HSAs) at home.

## How the names were collected
- **Approach:** Egocentric (women's own contacts only), as collected.
- **Why, and what it cannot show:** The four catchments hold about 4,000 households with no boundary to census, and 28 interviews were done. Women described their own contacts and nobody they named was interviewed. So every view attributed to a husband or a mother-in-law is the woman's report, and the map cannot show how the people named are tied to each other.
- **Who answered:** 28 pregnant women, 7 per health center, every fourth name on the antenatal register, half in a first pregnancy; each interviewed alone.

## Questions asked
1. "When you decide whether to take the tablets each day, whose opinion matters to you?"
2. "Who would notice if you took them, or stopped?"
3. "Whose approval would you want before taking the tablets?"
4. "Who would you ask if you were unsure about the tablets?"
**Asked about each role named:** "If they told you to take the tablets every day, would you?" Whether they approve and whether they can block or permit were noted where women said so, not asked of every role.

## Who they named, by role

| Role, no names | Named by | Influence: would act differently if they did | Gatekeeping: can permit or block | Does it themselves | Approves of it |
|---|---|---|---|---|---|
| Husband | 22 of 28 | Yes: 20 of 22 | Yes: controls the transport money for clinic visits | Not applicable | Mixed, as reported: 9 of 22 say he is against |
| Mother-in-law | 19 of 28 | Yes: 16 of 19 | Yes: lives in the compound and sees the tablets | Not asked | No, as reported: 15 of 19 say she is against |
| Own mother | 11 of 28 | Partly: 8 of 11, mostly in first pregnancies | No: usually lives elsewhere | Not asked | Not asked |
| Older neighbors and co-wives | 9 of 28 | Partly: 5 of 9 | No | Not asked | Not asked |
| Traditional birth attendant | 7 of 28 | Partly: 4 of 7 | No | Not applicable | No, as reported: 5 of 7 say she is against |
| Church women's guild leader | 6 of 28 | Yes: 5 of 6 | No | Not asked | Yes, as reported: 5 of 6 |
| HSA | 4 of 28 | No: 1 of 4 | No | Not applicable | Not asked |
| Clinic nurse | 3 of 28 | No: 1 of 3 | No | Not applicable | Not asked |

## Who sways the decision, and who can block it
- **Influential:** Husband; mother-in-law; church women's guild leader, named by few, though five of the six women who named her would follow her.
- **Gatekeepers:** Husband, through the transport money. Mother-in-law, who is in the compound every day and sees the tablets.
- **Named often but not influential:** None.

## Who the program reaches, and who it misses
The program speaks to pregnant women through nurses and HSAs. Women named nurses and HSAs least, and almost none would take the tablets on their word. Husbands and mothers-in-law, whom most women would follow and who can block the behavior, are not reached at all. The guild leader is outside the program.

## Checked with respondents
Six women at one center saw the tally. They said a woman's own mother matters most in a first pregnancy, and the birth attendant matters more at the two centers far from the road.

## Who must be reached
- Husbands: to permit, by releasing transport money, and to approve.
- Mothers-in-law: to approve, and to stop discouraging the tablets at home.
- Own mothers, for women in a first pregnancy.
- The guild leader is a possible route to older women. Whether she should speak for the program is a separate decision.

## What to check before relying on this
- What husbands and mothers-in-law think is known only from wives. Interview about ten of each, alone, before designing around their opposition.
- Seven women per center: the birth attendant's weight at the two remote centers rests on a handful of answers.
- No role looks named out of politeness. The nurse and the HSA, the likeliest polite answers, were named least.

## Where you could go from here
That's the map.
- Interviews with about ten husbands and ten mothers-in-law, each alone: the opposition the program would design around is known only from their wives, and people are often wrong about what others think.
- `map-audience-context`, for husbands and mothers-in-law: the program has no channel to either, and where and when they could be reached comes before what to say to them.
- `select-messenger`, once the program knows how to reach them: whether the guild leader, a woman's own mother, or someone else should speak for the program is the decision this map leaves open.
I'd lean toward the interviews, because the case for reaching husbands and mothers-in-law rests on what their wives believe they think.
Questions you could ask next: "How would we find husbands to interview when they don't come to the clinic?" · "How do we ask mothers-in-law about 'hospital medicine' without putting them on the defensive?"
```
