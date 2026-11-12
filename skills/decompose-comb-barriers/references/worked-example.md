# Worked example: savings deposits by Nairobi market vendors

A full run of the skill on a realistic case, showing the output it should produce. The case is illustrative, not a real program.

## The request

"Target behavior: enrolled produce vendors in Gikomba and Toi markets move part of the day's takings into the savings feature of their mobile-money wallet before leaving the market, each trading day. What we know: the decision happens at the end-of-day cash count at the stall, with cash in hand. Neighboring stallholders can see the count, and requests to borrow are common. A spouse often waits at home for the day's takings. There is a mobile-money agent kiosk inside each market that vendors already use daily. Most vendors belong to a weekly savings group. Monitoring data say 15% used the savings feature last month. I think it mostly comes down to discipline. We can do one round of vendor interviews. Why aren't they depositing?"

## The output

```markdown
I found eight possible reasons vendors aren't depositing. What your team has already seen points most to one: setting cash aside where neighbors can see invites requests to borrow. None of these is confirmed until vendors are asked, and your one interview round can test most of them at once.

# Possible reasons vendors aren't saving their takings before they leave the market

**The behavior:** Enrolled produce vendors in Gikomba and Toi markets move part of the day's takings into the savings feature of their mobile-money wallet before leaving the market, each trading day.
**What we know so far:** The team's field observations (the cash count is visible to neighbors; borrowing requests are common; a spouse waits for the takings; vendors use the agent kiosk daily; most are in a savings group) and program monitoring data (15% used the feature last month).

## Capability: can they do it?
### Physical capability: the bodily skill
- **Possible reason:** Vendors cannot complete the savings-feature menu steps unaided, although they send and receive money daily.
  **Still a barrier with full information, full access, and no social cost?** Yes. With a working phone, an agent nearby, and nobody watching, a vendor who has never used the menu would still fail.
  **What to ask or watch:** Ask the vendor to show a savings deposit of 10 shillings on her own phone, unaided.
  **How the answer tells it apart:** If this is the reason, she cannot finish. If any opportunity or motivation reason is, she finishes easily when asked.
### Psychological capability: knowledge, understanding, memory, planning
- **Possible reason:** Vendors cannot tell how much of the day's cash is surplus, because stock money and takings sit in one pocket.
  **Still a barrier with full information, full access, and no social cost?** Yes. Privacy and a nearby agent would not tell her what she can spare.
  **What to ask or watch:** "After yesterday's count, how much of the cash was yours to keep once tomorrow's stock was paid for? How did you work it out?"
  **How the answer tells it apart:** If this is the reason, she gives no figure, or a guess she cannot explain. If the savings-group preference is the reason, she gives a clear figure that she chose to keep in cash.

## Opportunity: does their situation let them?
### Physical opportunity: time, money, distance, materials
- **Possible reason:** The agent queue at closing time costs more stall-minding time than vendors will give.
  **What to ask or watch:** Time the queue at the market kiosk at closing and at midday on three days.
  **How the answer tells it apart:** If this is the reason, the closing-time queue is long and the few savers deposit at quieter hours. A short queue rules it out whatever vendors say about time.
### Social opportunity: what the people around them do, expect, and allow
- **Possible reason:** Setting cash aside in view of neighbors invites requests to borrow, so vendors avoid being seen to have spare money.
  **What to ask or watch:** "The last time you had a good day, what did you do with the cash before you left? Who could see?"
  **How the answer tells it apart:** If this is the reason, vendors hide the count or move the money elsewhere. The queue reason predicts no hiding.

## Motivation: do they want to, at the moment it counts?
### Reflective motivation: their judgments and plans
- **Possible reason:** Vendors judge the savings group a safer and more useful place for spare money than the wallet.
  **What to ask or watch:** "If you had 200 shillings spare today, where would you put it? What happened the last time you put money there?"
  **How the answer tells it apart:** If this is the reason, she names the savings group and gives a reason. If a capability or opportunity reason is, she names the wallet and then says what stopped her.
### Automatic motivation: habits, emotions, and impulses
- **Possible reason:** Handing the day's takings to a spouse at home is a routine with no decision point, so a deposit beforehand never comes up.
  **What to ask or watch:** "Tell me what happened with yesterday's takings from the moment you closed the stall."
  **How the answer tells it apart:** If this is the reason, her account has no moment of choice. If the savings-group preference is, she describes a choice.
- **Possible reason (team belief):** Vendors spend spare cash on impulse before the day ends.
  **What to ask or watch:** "On your last good day, what was the cash spent on between the count and reaching home?"
  **How the answer tells it apart:** If this is the reason, she lists purchases she did not plan. If the hand-over is, the cash reaches home intact.

## Which to check first (a provisional order)

| Possible reason | Evidence so far | Cost of checking |
|---|---|---|
| Social opportunity: spare cash in view invites borrowing | High: borrowing requests and the visible count are both in the team's field observations | Low: the interview round |
| Automatic motivation: routine hand-over to a spouse | Medium: the team reports a spouse waiting; nobody has asked vendors | Low: the interview round |
| Reflective motivation: the savings group is preferred | Medium: most vendors belong to one (team's observation) | Low: the interview round |
| Psychological capability: cannot tell surplus from stock money | Low: no observation yet | Low: the interview round |
| Physical capability: cannot work the savings menu | Low: vendors use mobile money daily, which counts against it | Medium: a demonstration with each vendor |
| Physical opportunity: queue at closing | None | Medium: three days of timing |
| Automatic motivation: impulse spending | None: team belief | Low: the interview round |

**Where I'd start:** the borrowing reason, then the hand-over to a spouse. Both have support in what the team has seen, and one interview round can test them together. This order is a best guess until the questions above are answered in the field.

## What to check before relying on this
- "It comes down to discipline" entered as a team belief with no evidence. The question about the last good day tests it; it is better not to design for it before then.
- Every rating above rests on staff observation. No vendor has been asked yet.

## Where you could go from here
That's the list of possible reasons.
- Build the interview guide with `draft-tdf-interview-guide`: you already have one interview round planned, and a guide built on these questions would test the top three reasons in the same conversations.
- Check the team's own belief first with `audit-researcher-bias`: worth it if "discipline" keeps coming up in planning, since it is the one reason resting on nothing but the team's view.
- Pull the deposit records by time of day before the interviews: if the few savers all deposit at midday, the queue reason gains weight and you can drop the timing exercise.
I'd lean toward the interview guide, because the interviews are already planned and most of these reasons are cheapest to check there.
Questions you could ask next: "How should we word the borrowing question so vendors don't feel accused?" · "What would we do differently if the savings group turns out to be the reason?"
```
