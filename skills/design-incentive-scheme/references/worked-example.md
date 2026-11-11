# Worked example: a transport payment for reporting an HIV self-test result in Lagos

A full run of the skill on a realistic case, showing the output it should produce. The case is illustrative, not a real program.

## The request

"We distribute HIV self-test kits through partner pharmacies in Alimosho, Lagos, to adults aged 18 to 35. Behavior: a person who collects a kit returns to the same pharmacy within 7 days and reports the result to the counselor. In exit interviews people say the return trip costs a fare (about NGN 600) and an hour, and they see no reason to come back if the result is negative. Counselors are at every partner pharmacy six days a week. The counselor records each return against the kit's serial number, which takes about 3 minutes. We have NGN 1,500 per return for 2,000 returns in a six-month pilot that ends on a fixed date. A typical day's income is around NGN 7,000. The people rewarded are kit users, not staff. Specify the incentive."

## The output

```markdown
# Incentive scheme specification

**Behavior:** Adults aged 18 to 35 who collect a self-test kit from a partner pharmacy in Alimosho return to that pharmacy within 7 days and report the result to the counselor.
**Confirmed barrier:** The return trip costs a fare of about NGN 600 and an hour, for no benefit the person can see after a negative result (exit interviews). Supply works: counselors are present six days a week at every partner pharmacy.
**Verification:** The counselor enters the return in the register against the kit's serial number, about 3 minutes per return. What is rewarded is the return and the report. The result is not checked and not rewarded, so nobody gains by misreporting it.

## The reward
- **Size:** NGN 1,500: 2.5 times the fare, and about a fifth of a day's income.
- **Form:** Cash, certain, described as transport money.
- **Timing:** Handed over at the counter when the register entry is made.
- **Recipient:** The kit user.

## The condition
- **Rule:** Return to the same pharmacy and report within 7 days. Enforced through the register.
- **Who it excludes:** People who have moved, lost the kit, or cannot travel. They can report by phone, unpaid, and are referred in the same way.

## The end
- **End date:** Six months after launch, funded by the pilot budget for 2,000 returns.
- **How people are told:** From month 5, counselors say at kit collection that transport money ends on the date, and a notice is posted at the counter.
- **Measured after the end:** The share of kits with a reported result within 7 days, from the register, for kits collected in the third month after the end.

## Motives that payment could displace
- **Who already acts unpaid, or works beside unrewarded colleagues:** People who returned before the pilot, whose number the register gives. Counselors receive nothing extra and handle the cash.
- **What is done about it:** Compare returns after the end with returns before the pilot. Tell counselors the payment is the user's fare, not a fee for testing.

## Monitoring
- **Claims without the behavior:** The register flags a serial number entered twice and a person who collects more than two kits in a month.
- **Review if:** Repeat collectors exceed 5% of returns in any month, or a pharmacy reports people asking for payment before testing; the program lead and a counselor representative review.

## Ethics check
- **Can a person refuse it:** Yes. The reward is about a fifth of a day's income, and a kit or a referral is never withheld from someone who does not return.
- **Who is left out:** People who report by phone, and users of pharmacies outside the pilot.
- **Specialist review:** A clinician, because the behavior is HIV testing: review the referral path and whether paying for returns leads to repeat testing.

## What the evidence supports
That a small, certain reward raises a one-off health action while it is paid, where the service is reliable. In rural Malawi a small payment doubled the share of people who came to learn their HIV result (Thornton, 2008), and in Rajasthan small gifts raised full immunization where camps were reliable (Banerjee et al., 2010). Several immunization studies found lower uptake once incentives were withdrawn (Saunders et al., 2025). No effect size is promised for Alimosho.

## What to check before relying on this
- Whether counselors record every return against a serial number and do not enter phone reports as returns.
- Whether NGN 600 and NGN 7,000 hold for women as well as men; both figures come from the field team.
```
