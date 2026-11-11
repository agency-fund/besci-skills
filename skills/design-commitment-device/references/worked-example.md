# Worked example: a locked restocking fund for market vendors in Nairobi

A full run of the skill on a realistic case, showing the output it should produce. The case is illustrative, not a real program.

## The request

"Behavior: women stall vendors in Nairobi's Gikomba market set aside KES 500 from the week's surplus into a restocking fund every Saturday. We interviewed 40 vendors: 34 say they intend to, 31 have a surplus most weeks (KES 300 to 1,200), and most describe spending it the same evening or lending it to neighbors who ask. Our mobile-money partner can open a locked savings pocket with an unlock date the vendor chooses and can show the balance on request; it is licensed by the central bank and vendors already use it for daily payments. Income dips in the two weeks before school terms start. About a third already give cash to a chama treasurer to hold. Design the device."

## The output

```markdown
# Commitment device specification

**Behavior:** Women stall vendors in Gikomba market set aside KES 500 from the week's surplus into a restocking fund every Saturday.
**Confirmed barrier:** Giving way at the moment the cash is in hand. Of 40 vendors interviewed, 34 intend to set money aside and 31 have a surplus most weeks; most describe spending it the same evening or lending it to neighbors who ask. Cost and access are ruled out for most; nine vendors have no regular surplus and the device is not for them.
**What people already do to bind themselves:** About a third give cash to a chama treasurer to hold.

## The device
- **Type:** Hard, as a lock with nothing forfeited, because the balance can be checked and a lock answers both the evening purchase and the neighbor's request ("it is locked, I cannot send it"), while a forfeit would take money from vendors whose surplus is small.
- **Goal:** An unlock date the vendor picks, suggested as the week she restocks, and a weekly amount she picks.
- **Checked by:** The provider's pocket balance, shown to the vendor on request at no cost.
- **What the person puts up:** Access to her own deposits until the unlock date. Weekly deposit of KES 100 to 1,000, chosen by the vendor and changeable each month.
- **Cap:** No money can be lost. No unlock date may fall later than the start of the two-week dip before a school term, so that nothing is locked when income is lowest.
- **Where forfeited money goes:** Nothing is forfeited.
- **Emergency release:** One request per term, paid out after 48 hours, free. The delay holds against an evening impulse and not against an illness.

## The offer
- **Who is offered it, and how:** Vendors with a surplus most weeks, by the provider's agent at the Saturday float top-up, with a one-page sheet in Swahili.
- **How a person says no:** The agent records "declined" and does not offer again that term.
- **Kept separate from:** Float loans, stall fees, and chama membership.

## People who commit and fail
- **What they lose:** No money. A vendor who stops depositing keeps her balance locked to her date, then receives it.
- **How they are told, and whether they can try again:** A balance message each month. After four missed weeks the agent offers a smaller weekly amount for the next term.
- **Who is most likely to fail:** Vendors whose surplus is under KES 500 in most weeks, and those with children starting a school term.

## Monitoring
- **Take-up:** Vendors who open a pocket as a share of those offered, split by weekly surplus. Expect many to decline.
- **Review if the share of committers who fail or lose their stake exceeds:** 40% stopping deposits or using the emergency release within a term; the program lead and the provider review the weekly amounts and the unlock dates.
- **After the device ends:** Whether vendors restocked from the fund, and whether those who used the pocket still set money aside a term later.

## Specialist review
A financial consumer-protection specialist, because the device locks money. Review the 48-hour release, the disclosure sheet, and who can see a vendor's balance.

## What the evidence supports
That offering a locked savings account raises balances at the provider among those offered, and that many decline: in the Philippines 28.4 percent of bank clients offered a locked account opened one, and after twelve months the balances of all those offered had grown more than the control group's (Ashraf, Karlan & Yin, 2006). Where savers set their own penalty for missed deposits, 55% defaulted and lost money (John, 2020), which is why this design forfeits nothing. No effect size is promised for Gikomba.

## What to check before relying on this
- Whether the interviews, held in one month, missed weeks with no surplus. Ask ten vendors to recall the last eight Saturdays.
- Whether a locked balance is visible to a husband or relative who shares the phone.
```
