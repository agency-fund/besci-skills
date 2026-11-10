# Worked example: a payday savings default for garment workers in Bangladesh

A full run of the skill on a realistic case, showing the output it should produce. The case is illustrative, not a real program.

## The request

"Behavior: workers at our three partner factories in Gazipur move part of their monthly wage into the savings pocket of their mobile-money wallet on payday. We surveyed 400 workers and interviewed 60: 71% say they want to put money aside each month, 3% have opened the pocket, and people describe meaning to do it and the money being gone by evening. The pocket is free, sits inside the wallet they already use, and withdrawals are instant. Today the whole wage lands in the spending balance; factory HR sets that in the payroll file. This would move wages. Many workers send money home on payday, and about 15% repay a cooperative loan each month. HR will accept any default a worker can switch off. Can we just auto-enroll everyone?"

## The output

```markdown
# Default option specification

**Behavior:** Workers at the three partner factories in Gazipur move part of their monthly wage into the wallet's savings pocket on payday.
**Confirmed barrier:** People want to save and do not act at payday: 71% of 400 surveyed workers say they want to put money aside, 3% have opened the pocket, and interviewees describe the money being gone by evening. Cost and access are ruled out; the pocket is free and inside the wallet they use.
**Decision point:** The payday wallet credit. Today 100% of the wage lands in the spending balance, and moving any of it takes a separate action. Factory HR controls this through the payroll file.

## The default
- **Proposed default:** 5% of the monthly wage is credited to the savings pocket and 95% to the spending balance.
- **Who receives it:** Workers at the three factories who have no cooperative loan repayment.
- **Who it is not for:** The roughly 15% of workers repaying a cooperative loan each month, for whom 5% less on payday could mean a missed repayment. They get an active choice at the next payday: a screen that asks "0%, 2%, or 5% to savings?" with nothing pre-selected.

## Mechanism
- **Relied on:** Ease. Workers intend to save and do not make the transfer; the default removes the step.
- **Why this setting supports it:** The intention is measured (71%) and the action is one transfer that people put off. Endorsement is not relied on, because whether workers trust HR with their wages is not known.

## Opt-out
- **How:** One tap in the wallet menu, "Stop saving from my wage", effective from the next payday. Money already in the pocket can be withdrawn at once, free.
- **Where it is shown:** In the payday message that announces the split, and on the pocket's balance screen.
- **Cost to the person:** None.

## Monitoring
- **Review if opt-outs exceed:** 30% within two paydays; the program lead and an HR representative review the rate and the reasons given.
- **Harm check:** Count same-day withdrawals of the full pocket balance and ask ten workers a month whether the split left them short. Track missed remittances reported to field staff.
- **When the default ends:** If the split is switched off, compare pocket deposits in the following two months with the months before it started.

## Ethics check
- **Serves the chooser because:** It does what most workers say they want, the money stays theirs, and it can be taken out at once.
- **Told before it applies:** A message one week before the first payday, and a notice read aloud at the line meeting, each stating the 5%, the opt-out, and that withdrawal is free.
- **Could it read as taking something:** Yes, if announced as an HR decision. The message comes from the wallet provider, shows the pocket balance in the worker's own name, and says "your money".
- **Specialist review:** A financial-services compliance lead, because the default moves wages. Review the opt-out and the disclosure before the pilot.

## What the evidence supports
That a savings default from pay raises participation and balances while it is in place. Field trials found this for employees of a firm in Afghanistan and for villagers paid weekly in India; in India the difference ended once everyone was paid in cash again. No effect size is promised for Gazipur.

## What to check before relying on this
- Whether workers who send their whole wage home on payday will read 5% in a pocket as a loss. Ask 15 of them before the pilot.
- Whether the 15% with loan repayments can be identified from payroll data without asking workers to disclose debts.
```
