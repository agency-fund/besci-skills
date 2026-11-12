# Worked example: HIV self-test kits through pharmacies in Lagos

A full run of the skill on a realistic case, showing the output it should produce. The case is illustrative, not a real program.

## The request

"We distribute HIV self-test kits through 120 community pharmacies, 12 in each of 10 local government areas (LGAs) in Lagos. We want to test two changes: a subsidy that cuts the kit price from 2,000 to 500 naira, and a peer-referral voucher that lets a buyer give a free kit to a partner. Outcome: the share of adult customers offered a kit who buy one, from the pharmacy sales log. The state program will decide whether to scale the subsidy, the voucher, or both to all 20 LGAs. Customers of the same pharmacy talk to each other, and partners may redeem vouchers at another pharmacy in the same LGA. The state program director says every pharmacy must have whatever works within 12 months; a pharmacy can wait, but none can be left out. Our team can launch in all 120 pharmacies in the same month. We set the price and hand out vouchers at the pharmacy; we cannot decide who buys. How should we randomize?"

## The output

```markdown
I'd randomize pharmacies, not customers, into four groups that cross the subsidy with the voucher, so the state program learns what each one adds. Two facts decided it: the pharmacy sets the price and hands out the vouchers, and the decision needs each change's separate value. One thing still unknown could weaken the comparison: how often vouchers are redeemed at a pharmacy other than the one that issued them.

# How to randomize the test: kit subsidy and partner voucher, Lagos pharmacies

**Change tested:** a price subsidy (2,000 to 500 naira) and a partner voucher, offered at community pharmacies
**Outcome:** share of adult customers offered a kit who buy one, from the pharmacy sales log
**Decision this informs:** scale the subsidy, the voucher, both, or neither to all 20 LGAs

## Constraints
| Constraint | Answer | Source |
|---|---|---|
| Spillovers: can it reach people not assigned it? | Within a pharmacy, through customers talking and a price posted at the counter; across pharmacies in an LGA, through vouchers redeemed elsewhere | Program staff |
| Delivered to | The pharmacy: it sets the price and hands out vouchers | Program design |
| Rollout | All 120 can launch in the same month | Program team |
| Can some wait or go without? | Any pharmacy can wait; all must have what works by month 12 | State program director |
| What the program controls | Assigns the subsidy and voucher to pharmacies; cannot assign who buys | Program design |
| Components or versions | 2; the decision needs each one's value: yes | State program |
| Units available | 120 pharmacies, 12 per LGA in 10 LGAs; 12 months | Program records |

## Designs ruled in or out
| Design | Verdict | Because | What it costs |
|---|---|---|---|
| Individual: randomize people | Out | The price is posted for everyone at the counter, and customers of one pharmacy talk | None |
| Cluster: randomize groups | In | The pharmacy delivers both changes, so the pharmacy is the unit | Fewer independent units than customers, so effects are estimated less precisely |
| Stepped-wedge: randomize the order of a phased rollout | Out for now; runner-up | Every pharmacy must be covered, but capacity does not force phases | Effects confounded with time unless time is modeled |
| Factorial: cross the components | In, chosen | Two separable components, and the decision needs each one's value | Each component is compared on 60 against 60 pharmacies; whether they work better together is beyond its reach |
| Multi-arm: several versions side by side | Not needed | The versions to compare are the four combinations, which the factorial already gives | None |
| Encouragement: randomize the offer | Out | The program controls the change at the pharmacy; buying is the outcome, not take-up of a treatment | None |

## Chosen design: pharmacy-level 2×2 factorial with a waitlist
- **Unit of randomization (what is assigned at random):** the pharmacy
- **Groups compared, and how many units in each:** four groups of 30 pharmacies: no change; subsidy only; voucher only; subsidy and voucher
- **Stratified by (drawn separately within each):** LGA, 3 pharmacies per group in each, because testing demand differs between LGAs and this keeps every group present wherever vouchers circulate
- **Timing:** months 1 to 6 are the test; from month 7, every pharmacy gets whichever combination the state program chooses, completed by month 12
- **How assignment is drawn:** in software from the list of 120 pharmacy IDs with the seed recorded, by the evaluation team, which has no stake in the result; the list and seed are filed with the state program before any pharmacy is told its group
- **Who agreed that some wait or go without:** the state program director, on the grounds that kits stay on sale at full price everywhere and the six-month wait ends for every pharmacy by month 12

## Runner-up: three-step stepped-wedge at the pharmacy level
It becomes the choice if launch capacity turns out to be limited, for instance to 40 pharmacies a quarter. Each step would then need to cross the two components for the decision to learn the voucher's separate value.

## Open questions
- How often vouchers are redeemed at a pharmacy other than the one that issued them. If often, redemptions in pharmacies without the voucher dilute the comparison.
- Whether the ethics board must approve the delay before the draw: ask the state program director.

## Where you could go from here
That's the design choice.
- Check the numbers with `estimate-sample-size`: each change is compared on 60 pharmacies against 60, and whether that can detect the change in purchases the state program cares about depends on figures not given here, such as customers offered a kit per pharmacy each month.
- Ask the state program director now whether the ethics board must approve the six-month wait: the draw cannot be filed until that is settled, and the answer may move the launch date.
- Fix the analysis with `write-pre-analysis-plan` before the draw: it is where to decide, in advance, how vouchers redeemed at another pharmacy will be counted.
I'd lean toward the sample-size check first, because if 60 pharmacies a side is too few, the design has to change before anything else is fixed.
Questions you could ask next: "What changes if we can only launch 40 pharmacies a quarter?" · "How do we explain the six-month wait to pharmacies drawn into the no-change group?"
```
