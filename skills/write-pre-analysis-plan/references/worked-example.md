# Worked example: late-payment letters from a tax authority

A full run of the skill on a realistic case, showing the output it should produce. The case is illustrative, not a real program.

## The request

"A tax authority and our research team are about to send one of three letters to taxpayers who declared income but had not paid by the due date. Design: individual randomization of 24,000 late taxpayers, stratified by taxpayer type (individual or firm) and whether they paid last year; three arms of equal size: no letter, a standard reminder, and the reminder plus a sentence saying most taxpayers pay on time. Primary outcome: paid any of the declared amount within 60 days of the letter date, from the authority's payment ledger. Smallest change worth detecting: 3 percentage points, set by the authority as the gain that would justify a national mailing. Nobody has seen any payment data by arm. We also care about the share of the liability paid, paying in full, days to first payment, and filing on time next year. The authority wants the norm letter to work and would like to report revenue; our team has published on norm messages before. We'll register on the AEA RCT Registry before the letters go out. Please write the pre-analysis plan."

## The output

```markdown
The plan commits to one primary test, paying anything within 60 days, and fixes in advance what each result leads to: the norm letter goes national only if it beats the standard reminder by 3 points or more. It adds detail where the authority and your team have a stake, so a choice made after the data arrive cannot make the norm sentence look like it worked. It needs to be registered, with this plan attached, before the first letter is mailed.

# Pre-analysis plan: late-payment letters

**Date fixed:** 2026-11-11
**Outcome data by arm (each group compared) seen before this date:** none
**Registry:** AEA RCT Registry; id to be added on registration

## 1. Design (carried over)
Individual randomization of 24,000 late taxpayers; three arms of 8,000 (no letter; standard reminder; reminder plus norm sentence); stratified by taxpayer type and prior-year payment; payment read from the ledger 60 days after the mailing date.

## 2. Hypotheses
- **H1 (primary):** A reminder letter raises the share of late taxpayers who pay any of the declared amount within 60 days, compared with no letter; the norm sentence raises it further, compared with the standard reminder.
- **H2:** The letters raise the amount paid (family A).
- **H3:** The letters raise on-time filing in the next period (family B).

## 3. Primary outcome
Paid any amount against the declared liability within 60 days of the letter date: 1 if yes, 0 if no, from the payment ledger matched on taxpayer ID. No transformation. A taxpayer with no ledger match is coded as not paid, because the ledger records every payment. Smallest change worth detecting: 3 percentage points, set by the authority.

## 4. Secondary outcome families: outcomes tested as a group
| Family | Outcomes | How multiple tests are handled | Why grouped |
|---|---|---|---|
| A. Amount | Share of the liability paid within 60 days; paid in full within 60 days | False discovery rate correction (Benjamini–Hochberg) across the two | The authority's revenue question |
| B. Next period | Filed on time in the next period | One outcome; no correction | Whether the effect lasts |
| Descriptive | Days from letter to first payment, among payers | Reported without a test | Defined only for those who pay, so arms are not comparable |

## 5. How the effect is estimated (the estimator)
- **Effect estimated:** intention to treat, by assigned arm; a returned, undelivered letter stays in its arm
- **Model:** linear regression of the outcome on arm indicators, the four strata, and last year's amount paid
- **Standard errors (how uncertainty is computed):** heteroskedasticity-robust; individuals were randomized, so no clustering
- **Exclusions:** taxpayers deregistered before the mailing date, dropped from every arm by the same rule
- **Drop-out:** none expected, since the outcome comes from the ledger; the share deregistered is compared across arms

## 6. Subgroups
| Subgroup | Variable and cut | Why the effect should differ | Status |
|---|---|---|---|
| Paid last year or not | Prior-year payment, yes or no (a stratum) | For past payers the letter is a reminder; for others it is new information, so the norm sentence should matter more for them | Confirmatory |
| Firms or individuals | Taxpayer type (a stratum) | Firms' accountants act on reminders whatever the wording, so the norm sentence should matter less | Confirmatory |
| Size of liability | Above or below the median declared liability | No prediction | Exploratory |

## 7. Decision rules
| Primary result | What the team will do | Who decides |
|---|---|---|
| At or above 3 points for the norm letter over the standard reminder | Send the norm letter nationally to late payers | The authority's compliance director |
| Standard reminder 3 points or more above no letter; norm sentence adds less than 3 | Send the standard reminder; claim no norm effect | The authority's compliance director |
| Neither letter reaches 3 points | No national mailing; publish the result in full | The authority's compliance director |

**Would stop adoption whatever the primary shows:** formal complaints or disputes from letter recipients more than double the rate among taxpayers sent no letter.

## 8. Where this plan is detailed, where it is flexible
Detailed: the primary outcome, the two confirmatory subgroups, and the decision rules, because the authority wants the norm letter to work and the research team has published on norm messages. Flexible: further covariates added for precision, and any other subgroup, each to be reported as exploratory beside the pre-specified result. A populated plan reporting every test above and every deviation will be posted on the registry with the results.

## 9. Registration
AEA RCT Registry, as the research team's journals expect; no health outcome, so no clinical registry is needed. Registered before the first letter is mailed, with this plan attached and dated, hidden until the trial is complete. The research team holds the ledger extract until the registry confirms the entry; the authority's data team sends no tables by arm before day 60.

## Open questions
- Whether the ledger match on taxpayer ID is complete for firms with more than one registration: check at baseline.
- Whether returned letters are logged; if not, the effect of being sent a letter is diluted by an unknown non-delivery rate.

## Where you could go from here
That's the pre-analysis plan.
- Register on the AEA RCT Registry with this plan attached and hidden until completion, before the first letter is mailed: a plan dated after the first payments come in no longer shows what was decided in advance.
- Put the two open questions to the authority's data team: whether firms with more than one registration match in the ledger, and whether returned letters are logged, since both affect how cleanly payment can be read by arm.
- Check with `estimate-sample-size` that 8,000 per arm can detect 3 points between the two letters, if nobody has yet: the national decision turns on that comparison, not on letter against no letter.
I'd lean toward registering, because the first mailing is a hard deadline; but if nobody has checked the sample, that check belongs before the filing, since a shortfall would change the plan.
Questions you could ask next: "What do we report if the norm letter helps past non-payers but not past payers?" · "What do we say if the authority asks for an early look at payments by arm?"
```
