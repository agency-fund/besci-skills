# Worked example: savings deposits by Nairobi market vendors

A full run of the skill on a realistic case, showing the output it should produce. The case is illustrative, not a real program.

## The request

"Target behavior: enrolled produce vendors in Gikomba and Toi markets move part of the day's takings into the savings feature of their mobile-money wallet before leaving the market, each trading day. What we know: the decision happens at the end-of-day cash count at the stall, with cash in hand. Neighboring stallholders can see the count, and requests to borrow are common. A spouse often waits at home for the day's takings. There is a mobile-money agent kiosk inside each market that vendors already use daily. Most vendors belong to a weekly savings group. Monitoring data say 15% used the savings feature last month. I think it mostly comes down to discipline. We can do one round of vendor interviews. Why aren't they depositing?"

## The output

```markdown
# COM-B barrier hypotheses

**Behavior:** Enrolled produce vendors in Gikomba and Toi markets move part of the day's takings into the savings feature of their mobile-money wallet before leaving the market, each trading day.
**Evidence used:** The team's field observations (the cash count is visible to neighbors; borrowing requests are common; a spouse waits for the takings; vendors use the agent kiosk daily; most are in a savings group) and program monitoring data (15% used the feature last month).

## Capability
### Physical
- **Hypothesis:** Vendors cannot complete the savings-feature menu steps unaided, although they send and receive money daily.
  **Persistence test:** Yes. With a working phone, an agent nearby, and nobody watching, a vendor who has never used the menu would still fail.
  **Question:** Ask the vendor to show a savings deposit of 10 shillings on her own phone, unaided.
  **Discriminates because:** This predicts she cannot finish. Every opportunity or motivation hypothesis predicts she finishes easily when asked.
### Psychological
- **Hypothesis:** Vendors cannot tell how much of the day's cash is surplus, because stock money and takings sit in one pocket.
  **Persistence test:** Yes. Privacy and a nearby agent would not tell her what she can spare.
  **Question:** "After yesterday's count, how much of the cash was yours to keep once tomorrow's stock was paid for? How did you work it out?"
  **Discriminates because:** This predicts no figure, or a guess she cannot explain. The reflective-motivation hypothesis predicts a clear figure that she chose to keep in cash.

## Opportunity
### Physical
- **Hypothesis:** The agent queue at closing time costs more stall-minding time than vendors will give.
  **Question:** Time the queue at the market kiosk at closing and at midday on three days.
  **Discriminates because:** This predicts a long closing-time queue and deposits by the few savers at quieter hours. A short queue rules it out whatever vendors say about time.
### Social
- **Hypothesis:** Setting cash aside in view of neighbors invites requests to borrow, so vendors avoid being seen to have spare money.
  **Question:** "The last time you had a good day, what did you do with the cash before you left? Who could see?"
  **Discriminates because:** This predicts vendors hiding the count or moving the money elsewhere. The queue hypothesis does not predict concealment.

## Motivation
### Reflective
- **Hypothesis:** Vendors judge the savings group a safer and more useful place for spare money than the wallet.
  **Question:** "If you had 200 shillings spare today, where would you put it? What happened the last time you put money there?"
  **Discriminates because:** This predicts she names the savings group and gives a reason. A capability or opportunity hypothesis predicts she names the wallet and then says what stopped her.
### Automatic
- **Hypothesis:** Handing the day's takings to a spouse at home is a routine with no decision point, so a deposit beforehand never comes up.
  **Question:** "Tell me what happened with yesterday's takings from the moment you closed the stall."
  **Discriminates because:** This predicts an account with no moment of choice. The reflective hypothesis predicts a choice she can describe.
- **Hypothesis (team belief):** Vendors spend spare cash on impulse before the day ends.
  **Question:** "On your last good day, what was the cash spent on between the count and reaching home?"
  **Discriminates because:** This predicts purchases she did not plan. The hand-over hypothesis predicts the cash reaches home intact.

## Ranking, pending field answers

| Hypothesis | Evidence so far | Cost of checking |
|---|---|---|
| Opportunity, social: spare cash in view invites borrowing | High: borrowing requests and the visible count are both in the team's field observations | Low: the interview round |
| Motivation, automatic: routine hand-over to a spouse | Medium: the team reports a spouse waiting; nobody has asked vendors | Low: the interview round |
| Motivation, reflective: the savings group is preferred | Medium: most vendors belong to one (team's observation) | Low: the interview round |
| Capability, psychological: cannot tell surplus from stock money | Low: no observation yet | Low: the interview round |
| Capability, physical: cannot work the savings menu | Low: vendors use mobile money daily, which counts against it | Medium: a demonstration with each vendor |
| Opportunity, physical: queue at closing | None | Medium: three days of timing |
| Motivation, automatic: impulse spending | None: team belief | Low: the interview round |

**Check first:** The social-opportunity hypothesis, then the routine hand-over. Both have support in what the team has seen, and one interview round can test them together. Provisional until the questions above are answered in the field.

## What to check before relying on this
- "It comes down to discipline" entered as a team belief with no evidence. The question about the last good day tests it; do not design for it before then.
- Every rating above rests on staff observation. No vendor has yet been asked.
```
