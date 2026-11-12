# Worked example: wallet savings among Nairobi market vendors

A full run of the skill on a realistic case, showing the output it should produce. The case is illustrative, not a real program.

## The request

"Target behavior: enrolled produce vendors in Gikomba and Toi markets move part of the day's takings into the wallet's savings feature before leaving the market each trading day. We reach about 2,000 women through weekly field-officer visits. Last month 15% of them used the savings feature. The mobile-money provider says it can share daily transaction records for vendors who consent; their partnerships manager confirmed that. Field officers also keep a paper log of visits. Our sponsor says a rise of 10 percentage points in the share of trading days with a deposit would justify taking this to other markets. We think the main barriers are that vendors trust their savings group more than the wallet, and that saving in view of neighbors invites requests to borrow. The scaling decision is due in nine months. How will we know if this worked?"

## The output

```markdown
The primary outcome is the share of trading days on which a vendor makes a deposit into the savings feature, taken from the provider's transaction records for every consenting vendor. The 10-point threshold is your sponsor's, and the plan keeps it as set. What could still undo the plan is consent: nobody yet knows how many vendors have no wallet or will refuse, and they drop out of the measure.

# How you will know if vendors' daily wallet saving changed

**Target behavior:** Enrolled produce vendors in Gikomba and Toi markets move part of the day's takings into the wallet's savings feature before leaving the market each trading day.

## Primary outcome: the one measure that decides whether it worked
- **Measure:** Share of trading days with a deposit into the savings feature
- **Defined as:** For each vendor enrolled at baseline who consented to share records, the number of trading days (Monday to Saturday, market holidays excluded) with at least one deposit into the savings feature, divided by the number of trading days in the window. Every such vendor counts, including those who never open the feature.
- **Observes the behavior directly:** Yes, for the deposit. It does not show whether the money came from that day's takings or was moved before leaving the market; the wallet records the time of each deposit, which narrows the second gap.
- **Could be distorted by:** a field officer making deposits on a vendor's behalf if officers are ever rewarded on deposits; splitting one deposit into several does not change the measure, which counts days, not deposits.

## Data source

| Option | Available here? | Verdict |
|---|---|---|
| Records already collected | The provider's transaction records, daily, per vendor | Chosen: records every deposit for every consenting vendor, whether or not a field officer visited |
| Records with a field added | The paper visit log could record deposits | Rejected: exists only for vendors an officer visited, and relies on what vendors say |
| Observation or survey | A survey of saving | Rejected: vendors would overstate saving to the officers who encourage it |
| Proxy: a stand-in that should move with the behavior | Wallet balance at month end | Rejected: a balance can rise from one large deposit, and the behavior is recorded directly |

**Chosen source:** The mobile-money provider's daily transaction records, shared for consenting vendors.

## Feasibility

| Check | Answer | Confirmed by |
|---|---|---|
| Who holds the data and grants access | The provider; access needs a data-sharing agreement | Provider's partnerships manager |
| Individuals or totals | Individual transactions, with time stamps | Provider's partnerships manager |
| How often recorded, against when needed | Daily; needed monthly for monitoring and at month 8 for the decision | Provider's partnerships manager |
| Format | Not confirmed | Not confirmed |
| Consent and approvals | Written consent from each vendor; whether it can be collected during trading hours is not known | Not confirmed |
| Recorded the same way for everyone compared | Yes for vendors with the wallet; vendors without one do not appear | Not confirmed |

## When it is measured
Baseline: the two months before launch, from the same records. Outcome window: months 3 to 8 after launch, so the first weeks of novelty are not counted. The decision is due in month 9.

## Smallest change worth detecting
10 percentage points in the share of trading days with a deposit, set by the sponsor as the rise that would justify taking the program to other markets.

## Other measures

| Measure | Role | Source |
|---|---|---|
| Vendors' trust in the wallet compared with their savings group, one survey item at baseline and month 6 | Intermediate: trust barrier | Short survey by an enumerator who is not the vendor's field officer |
| Number of requests to borrow received at the stall in the past week | Intermediate: visibility barrier | Same survey |
| Contributions to the vendor's savings group | Must not get worse | Same survey |

## Outcome statement
As of 2026-11-11, the primary outcome is the share of trading days with at least one deposit into the wallet's savings feature, among all vendors enrolled and consenting at baseline, from the provider's transaction records, measured in months 3 to 8 after launch; the smallest change worth detecting is 10 percentage points.

## Open questions
- The file format of the provider's records: ask the partnerships manager.
- Whether written consent can be collected during trading hours, and by whom: ask the provider and the field team lead.
- How many enrolled vendors have no wallet or refuse consent, and so drop out of the measure: ask the field team lead before baseline.

## Where you could go from here
That's the measurement plan.
- Settle the three open questions with the provider's partnerships manager and the field team lead before baseline: the share of vendors with no wallet or no consent decides whom the outcome covers, and nothing else in this plan can tell you.
- Write the three survey items with `draft-survey-items`: the trust, borrowing-request, and savings-group measures all come from one short survey that does not exist yet.
- Choose the comparison with `choose-trial-design`: this plan leaves out what deposits will be compared against, and the decision is due in nine months.
I'd lean toward the open questions first: two people can answer them, and the survey and the comparison both depend on knowing which vendors the outcome covers.
Questions you could ask next: "What would we measure if the provider withdrew access after launch?" · "Should the share of vendors who refuse consent be reported beside the outcome?"
```
