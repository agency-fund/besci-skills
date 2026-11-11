# Worked example: when to offer a savings wallet to casual workers in Kampala

A full run of the skill on a realistic case, showing the output it should produce. The case is illustrative, not a real program.

## The request

"We run a savings product for casual workers around Kampala: porters, construction laborers, boda riders. The ask is chosen: an agent offers, in person at the work site, to open a named savings wallet and take a first deposit of at least 2,000 shillings. Opening is free and takes ten minutes, any day an agent is there. In interviews with 40 workers nearly all said they want to save for school fees and that they mean to start 'next week'; when our agents visit, mostly on Tuesdays, people say they have nothing on them. Porters and laborers are paid in cash on Friday afternoons; boda riders earn daily. Rent is due at the start of the month. School fees fall in early February, late May, and early September. Christmas is the big spending season. A colleague wants to launch in the first week of January as a 'new year, new start' campaign. When should the agent make the offer?"

## The output

```markdown
# Delivery moment specification

**The ask:** Casual workers at Kampala work sites open a named savings wallet with the agent and make a first deposit of at least 2,000 shillings. Cost at that moment: cash in hand, and ten minutes.
**Confirmed barrier:** Workers want to save and are asked when they hold no cash. In 40 interviews nearly all said they want to save for school fees; on the agents' Tuesday visits they say they have nothing on them. They also put it off: "next week".
**When the action can be done:** Any day an agent is at the site.

## Money calendar
| Period | Money in | Money out | Position | Source |
|---|---|---|---|---|
| Friday afternoon, every week | Cash wages for porters and laborers | None reported | Flush | User report |
| Monday to Thursday | None for weekly-paid workers | Daily living costs | Short | User report (nothing on them on Tuesdays); costs assumed |
| Every evening | Boda riders' daily takings | Fuel and bike hire | Neutral | User report; costs assumed |
| First week of each month | Wages as usual | Rent | Short | User report |
| Early February, late May, early September | Wages as usual | School fees | Short | User report |
| December | Wages as usual | Christmas spending | Short | User report |

## Candidate moments
| Moment | Money in hand? | Attention free? | Action possible then? | Verdict |
|---|---|---|---|---|
| Tuesday site visit (the current moment) | No | Yes | Yes | Rejected: no cash in hand |
| Friday afternoon, just after wages are paid | Yes | Yes, the work week is ending | Yes, if the agent is at the pay point | Chosen, outside rent and fee weeks |
| Friday in the first week of the month | Partly; rent is due | No | Yes | Rejected: the wage is already spoken for |
| First week of January, "new year, new start" | No: it follows Christmas spending, rent is due, and February fees are ahead | No | Yes | Rejected: a landmark that falls on a short week; untested here |
| The weeks school fees fall due | No | No | Yes | Rejected |

## Chosen moment
- **When:** Friday afternoon at the pay point, within an hour of wages being paid, on the second, third, and fourth Fridays of the month, skipping the weeks school fees fall due.
- **Relies on:** Money in hand.
- **Why this setting supports it:** Wages are paid in cash at the site on Fridays, and by Tuesday workers report having nothing left.

## Deadline
A light one, because workers themselves say they put saving off until "next week". The agent takes first deposits only on that Friday afternoon and says so. Nothing is lost by waiting: the same offer returns the following Friday at the same price.

## Who this moment leaves out
- **Who:** Boda riders, who have no Friday wage, and workers who are absent or paid by another contractor that week.
- **Second moment for them:** For riders, the end of the riding day at the stage, on a weekday evening outside the first week of the month. For absent workers, the next Friday.

## What the evidence supports
That an offer made while people hold cash is taken up more than the same offer made later. Farmers in western Kenya bought fertilizer in response to a small, time-limited offer made just after harvest, and later offers did less. That evidence comes from farmers paid once a season; it has not been tested with weekly wage workers. "New year" as a fresh start is untested here. No effect size is promised.

## What to check before relying on this
- Whether wages at every site are paid in cash on Friday afternoon, or some by mobile money. If by mobile money, the moment is when the transfer lands.
- Whether workers will hand cash to an agent in front of workmates. Ask ten before the pilot.
- The boda riders' row: their daily costs are assumed.
```
