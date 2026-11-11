# Worked example: HIV treatment text reminders moving from NGO clinics to county delivery in Kisumu, Kenya

A full run of the skill on a realistic case, showing the output it should produce. The case is illustrative, not a real program.

## The request

"We ran a cluster randomized trial of weekly text reminders for adults on HIV treatment at 8 NGO-supported clinics in Kisumu County: 1,640 patients over 12 months. Viral suppression at 12 months was 9 percentage points higher in the text arm than with standard care (95% CI 3 to 15), our pre-registered primary outcome. Our adherence counselors sent the messages from a dashboard and phoned anyone who replied 'need help' within 24 hours; each had about 120 patients. Monitoring logs show 94% of weekly messages went out. It cost about USD 4.10 per patient per year, counselor time included. The effect was concentrated in patients enrolled less than 12 months before; it was near zero in patients stable on treatment for more than 3 years, who we guess are about two-thirds of the county's patients. The county health department wants to roll it out to all 71 county clinics, about 48,000 patients, with messages sent automatically from the national electronic medical record and no one assigned to answer replies, because the budget allows USD 1.50 per patient. It would be a budget line next fiscal year, and the county says it can drop it after a year if it fails. Will this hold at scale?"

## The output

```markdown
# Scalability assessment: weekly treatment text reminders, Kisumu County

**Pilot:** viral suppression at 12 months 9 percentage points higher than standard care (95% CI 3 to 15) on the pre-registered primary outcome; cluster randomized trial, 8 clinics, 1,640 patients; among adults on HIV treatment at NGO-supported clinics in Kisumu County; delivered by NGO adherence counselors, with a phone call within 24 hours to anyone who replied "need help"; at about USD 4.10 per patient per year
**At scale:** 71 county clinics, about 48,000 patients; delivered by county staff, through automated sends from the national electronic medical record; changes: no one answers replies; budget: USD 1.50 per patient per year
**Decision this informs:** a county budget line for next fiscal year; reversible: yes, the county says it can drop it after one year

## Pilot against scale

| Row | In the pilot | At scale | Pilot tested the scale version? | Mark |
|---|---|---|---|---|
| Strength of the effect | Cluster randomized trial with a standard-care comparison; 8 clinics, 1,640 patients; pre-registered primary outcome; no second study | not applicable | not applicable | +: credible, though one study with eight clusters |
| Who is reached | All adults on treatment at 8 clinics; the effect sat in patients enrolled under 12 months | All patients at 71 clinics, most of them stable for years (the team estimates two-thirds) | No | –: most patients at scale are in the group where the pilot found near zero |
| What is delivered | Weekly text plus a counselor's call within 24 hours to "need help" replies | Weekly text only | No | –: the call-back is dropped, and nobody knows how much of the effect it carried |
| Who delivers and answers for it | NGO counselors with about 120 patients each, supervised by the NGO | County clinic staff with no assigned role; no one named as responsible | No | –: no person is accountable for the messages or the replies |
| How it reaches people | Counselors sent from a dashboard; 94% of weekly messages went out | Automated sends from the national record system, which holds phone numbers | No | more information needed: how reliably the system sends and whether numbers are current |
| Cost and funding | USD 4.10 per patient per year, counselor time included | USD 1.50 per patient per year in a county budget line | No | –: the money covers only the version without call-backs |
| Demand and commitment | The NGO ran it | The county health department asked for it; clinic staff have not been asked | No | more information needed: whether clinic staff will take on any part of it |

## Verdict
Promising: test first, because the effect is credible but the version the county can fund drops the call-back, gives no one responsibility for delivery, and reaches mostly the patients in whom the pilot found near zero. If the test shows the effect depended on the call-back, the USD 1.50 version does not yet merit scale-up.

## Test first
What is delivered: in 10 county clinics, assign 5 at random to automated texts only and 5 to automated texts with a county staff member who answers "need help" replies within 24 hours, and compare viral suppression among patients enrolled under 12 months against the 61 clinics not yet reached, using the medical record. Nine months. If automated texts alone show no gain over the comparison clinics, the county should fund the version with replies or none.

## What must be true for the effect to survive
1. Automated texts without call-backs still raise viral suppression among newly enrolled patients: the 10-clinic test.
2. County staff can answer replies within 24 hours alongside their other work: the reply log in the test clinics.
3. Weighted by the county's actual mix of new and long-term patients, the gain is still worth the cost: count patients enrolled under 12 months in the medical record, one week, no cost.
4. The record system sends texts reliably to current numbers: one month of send and delivery reports.

## What to check before relying on this
- Demand and commitment: the county department asked, but clinic staff, who would answer replies, have not been asked.
- The two-thirds share of long-term patients is the team's estimate; the record system can give the real figure in a week.
```
