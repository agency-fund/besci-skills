# Worked example: mobile immunization camps in rural Rajasthan

A full run of the skill on a realistic case, showing the output it should produce. The case is illustrative, not a real program.

## The request

"We need a theory of change for our immunization program. Outcome in the grant: children under two in two blocks of Udaipur district are fully immunized, with all scheduled doses, by 24 months. Our household listing put the share at about 22%, and the target is 40% by the end of 2027. What we do: a mobile camp with a nurse and a cold box visits each of 60 villages on a fixed day every month; a village mobilizer announces the camp two days before; each completed dose earns the caregiver one kilogram of lentils. The camps reach caregivers, mostly mothers; the outcome is for their children. Evidence: eight months of camp monitoring data, which show 92% of scheduled camps held with full stock, about 60% of eligible children getting a first dose at a camp, and a cold-box temperature problem reported in 3 of 24 camp-months. We have also talked informally with about a dozen mothers. Someone on the team remembers a trial of incentives in Rajasthan but we do not have the paper."

## The output

```markdown
The chain has four links, and only the first (camps held on the day with full stock) is backed by your own data on that link. The weakest is link 3, the lentils bringing caregivers back for later doses: it carries the whole drop from about 60% first doses to about 22% fully immunized, and nothing you supplied supports it. The trial your team remembers, once found and read, would be the first evidence for it.

# Theory of change: mobile immunization camps in two blocks of Udaipur district

**Outcome (as given):** Children under two in the two program blocks of Udaipur district are fully immunized by 24 months; from about 22% to 40% by the end of 2027.
**Population:** Activities reach caregivers of children under two in 60 villages, through the mobilizer and the camp nurse. The outcome is for those children.
**Activities (as delivered):** (a) monthly mobile camp on a fixed day in each village; (b) mobilizer's announcement two days before; (c) one kilogram of lentils per completed dose. All three are running.
**Evidence supplied:** Eight months of camp monitoring data; informal conversations with about twelve mothers. No study or review supplied.

## Causal chain

| # | Link (from, to) | Assumption (if ..., then ..., because ...) | Evidence | Strength |
|---|---|---|---|---|
| 1 | Monthly camp on a fixed day, a dose is available in the village on a known date | If the nurse arrives with stock on the fixed day, then a dose is available without travel, because the trip to a distant clinic is what caregivers cannot afford | Monitoring: 92% of scheduled camps held with full stock | tested here |
| 2 | Announcement and a known date, caregivers bring the child on camp day | If caregivers know the day and trust the camp will come, then they attend, because visits are missed for not knowing when, not from refusal | Monitoring: about 60% of eligible children get a first dose at a camp, which shows attendance but not what causes it. The reason rests on conversations with about twelve mothers, not systematic | assumption |
| 3 | Lentils per dose, caregivers return for each later dose | If each dose brings a small reward on the day, then fewer children drop out between doses, because the benefit of a later dose is distant while the cost of the trip is immediate | None supplied. The team recalls a trial but did not supply it | assumption |
| 4 | All doses received by 24 months, child fully immunized and protected | If the vaccine is kept cold and the schedule is completed, then the child is protected, because the vaccines work when stored and given as scheduled | Monitoring: a cold-box temperature problem in 3 of 24 camp-months. Nothing supplied on how well the vaccines protect | plausible mechanism |

## Behaviors the chain depends on
- The nurse brings a stocked, cold cold box to every camp (links 1 and 4); inferred; team to confirm
- The mobilizer announces the camp two days before, every month (link 2); inferred; team to confirm
- Caregivers bring the child to the camp on camp day (link 2); inferred; team to confirm
- Caregivers return for each later dose until the schedule is complete (link 3); confirmed by team

## Weakest links
- Link 3: it carries the whole gap between a first dose (about 60%) and full immunization (about 22%), and its evidence cell is empty. The trial the team recalls, once found and read, would raise it to "tested elsewhere". Completion rates from the program's own camps, compared between months with and without lentils, would raise it to "tested here".
- Link 2: the belief that caregivers miss camps because they do not know the date rests on a dozen conversations. If the real barrier is lost work on camp day or a husband's permission, the announcement does nothing. Twenty short interviews with caregivers who missed the last camp would raise it to "tested here".

## What to check before relying on this
- The reason given in link 2. It is the cheapest assumption to check.
- Three of the four behaviors are inferred. Confirm that the nurse's and the mobilizer's tasks are written into how the program is delivered.
- The cold-box problems in link 4 mean "fully immunized" on the register may overstate protection in some months.
- Outside the program: a government immunization drive or a new clinic in either block would raise coverage without the camps. Ask the district health office what else is planned through 2027.

## Where you could go from here
That's the theory of change.
- Search for evidence on link 3 with `assess-evidence-base`: a search on incentives for completing immunization schedules is the way to find the trial your team remembers, and anything that went against it.
- Interview twenty caregivers who missed the last camp: it is the cheapest check in the chain, and if they name lost work or a husband's permission rather than not knowing the date, link 2 needs a different activity.
- Decide how you will show the chain working with `plan-evaluation-design`, once it is agreed: the register may overstate protection in cold-box months, so the outcome you report needs thought.
I'd lean toward the search for link 3, because that link carries most of the gap to your 40% target and has nothing behind it yet; the interviews can run alongside.
Questions you could ask next: "How could we test link 3 with our own camp records?" · "What would we change if caregivers say they miss camps because of lost work, not the date?"
```
