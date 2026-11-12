# Worked example: savings among Nairobi market vendors

A full run of the skill on a realistic case, showing the output it should produce. The case is illustrative, not a real program.

## The request

"Our goal is to increase long-term savings among informal-sector market vendors in Nairobi, so they have a buffer against income shocks. Most are women running produce stalls. They earn daily in cash and through mobile money, and most already belong to a savings group. Before we pick a behavior to target: has this been done before, and what does the evidence say? Use general web search."

## The output

```markdown
The closest results come from rural Kenya and from programs where a payer or employer chose how people were paid; none tested self-employed urban vendors who earn daily. The strongest finding against the idea is that a savings default in India faded as soon as the payment channel went back to cash. I opened three sources and could read only their abstracts, so treat this as a first look, not a review.

# What research already exists on savings among Nairobi market vendors

**Program goal (as given):** Increase long-term savings among informal-sector market vendors in Nairobi, so they have a buffer against income shocks.
**Search route:** General web search, as asked. Paperclip would add full-text reading for health papers; this topic sits mostly in economics journals, which it does not cover.

## What has been tried

| Intervention | Tested where and with whom | Result | Compared with your population | Source |
|---|---|---|---|---|
| A safe place to keep money at home (a lockable box) | Rural western Kenya; members of savings groups | Health savings rose 66%; randomized field experiment; abstract only | Same country. Rural, and saving for health costs, not a general buffer | Dupas & Robinson (2013), https://doi.org/10.1257/aer.103.4.1138 |
| Paying a weekly payment into a bank account by default instead of in cash | Rural India; villagers who had or opened an account | Account savings rose 131% within three months; randomized field experiment; abstract only | Different country. The payer chose the channel; vendors have no payer | Somville & Vandewalle (2018), https://doi.org/10.1257/app.20160547 |
| Enrolling employees by default in a savings account fed from salary | Afghanistan; employees of one firm, paid by mobile money | Participation rose 40 percentage points, the same as a 50% match; randomized field experiment; abstract only | Different country. Salaried staff with an employer who can deduct; vendors are self-employed | Blumenstock, Callen & Ghani (2018), https://doi.org/10.1257/aer.20171676 |

## Findings that do not support the goal
- The default did not outlast the payment channel: in the India study, once everyone was paid in cash again, savings patterns no longer differed. A program that changes how vendors are paid for a few months should not expect a lasting habit. Somville & Vandewalle (2018), abstract only.
- Earmarking savings for one purpose helped only for emergencies, or for people often asked for money by friends and relatives. A label on a savings pot is not a general remedy. Dupas & Robinson (2013), abstract only.

## Gaps
No located study tests a savings intervention with self-employed urban vendors who earn daily and have no employer or program paying them. All three positive results depend on either a safe physical place for cash or a payer who sets the channel. Whether a mobile-money wallet can play either role for vendors is untested in what this scan found.

## Search coverage
- **Searched:** general web search, with the terms "default savings field experiment", "savings market vendors Kenya randomized", "commitment savings low-income countries review"
- **Opened:** 3 sources, all abstract only
- **Not reached:** full texts; mobile-money operators' own evaluations; reports in Swahili; the 3ie and J-PAL evaluation databases
- **A fuller review would add:** a search of those two databases, the full text of each study for sample sizes and take-up, and any systematic review of savings promotion in sub-Saharan Africa

## Where you could go from here
That's the evidence summary.
- Search the 3ie and J-PAL databases and open the full text of the three studies: every number above comes from an abstract, and the behavior you pick should not rest on figures nobody has read in full.
- Check whether the lockbox result would hold for your vendors with `assess-evidence-transferability`: Dupas & Robinson (2013) is the only study from Kenya and its participants were in savings groups, as most of your vendors are, but they were rural and saving for health costs.
- Pick the behavior with `define-key-behavior` once you have read enough: the gap above says no tested approach yet fits vendors with no payer, so the behavior you choose will be a bet the research does not settle.
I'd lean toward the fuller search first, because it is cheap next to choosing a behavior on three abstracts.
Questions you could ask next: "Which of these studies is closest to our vendors, and would its result hold in Nairobi?" · "Can a mobile-money wallet play the role of the lockbox?"
```
