# Worked example: a daily SMS medication reminder

A full run of the skill on a realistic case, showing the output it should produce. The case is illustrative, not a real program.

## The request

"We ran a 3-month SMS reminder program to improve adherence to a daily medication for our enrolled patients: one reminder text per day at 8am. Adherence, measured by pharmacy refill records, barely moved. Our take is that patients just don't care enough about their health to act on a reminder. We're deciding whether to drop reminders altogether. I pulled the SMS gateway's delivery logs for you: about 30% of messages failed silently on two carriers, with no resend. No other changes at the clinics during the period. Can you review it?"

## The output

```markdown
# Intervention post-mortem brief

**Prior intervention (as given):** A 3-month program sending one SMS reminder at 8am each day to enrolled patients to improve adherence to a daily medication, judged by pharmacy refill records. Adherence barely moved; the team's view is that patients do not care enough to act on a reminder.

## What was planned
Target behavior: enrolled patients take their daily medication. The 8am text was meant to prompt the dose that day, every day for 3 months, through the SMS gateway.

## What was actually delivered
- **Fidelity:** Not as designed. About 30% of messages failed silently on two carriers, with no fallback or resend. **Basis:** confirmed by the record (the gateway's delivery logs)
- **Dose:** For patients on the affected carriers, far fewer than the planned seven reminders a week arrived; how many fewer depends on how failures fell across days. **Basis:** confirmed that dose fell short; its size per patient is inferred
- **Reach:** Every enrolled patient was in scope, but reach to a working reminder was uneven and was not tracked by carrier at the time. **Basis:** confirmed that reach was uneven; which patients were affected is inferred, not logged
- **Context:** No change at the clinics during the 3 months. **Basis:** confirmed by the record (no change reported)
- **Response:** No data on whether patients who received the texts read them or took the dose after them. **Basis:** confirmed that no such data was collected

## Outcome as observed
Pharmacy refill records, a routinely tracked administrative measure, show adherence essentially flat. There was no comparison group, so the result is a description, not an estimate of the program's effect. It is also confounded by the delivery gap: the program delivered was weaker than the one designed.

## Causal claim check
- **Team's stated reason for the outcome:** Patients do not care enough about their health to act on a reminder.
- **Does the collected data support it?** No. Nothing was collected on patients' receipt of messages, their engagement, or their attitudes; the claim is inferred from the flat outcome alone.
- **Alternative explanation the data does not rule out:** Many patients never reliably received the reminder, given the carrier failures. Motivation was never tested against a fully delivered program.

## Implementation failure vs. idea failure
**Classification:** cannot yet tell
There is a confirmed implementation failure, large enough that the reminder idea has not been fairly tested. Without refill records split by carrier, or any data on response, the flat outcome cannot be attributed to the idea. The team's explanation about motivation is not supported by the data it collected.

## Factors to address before any retry
- Confirm delivery of each message, on every carrier, and resend failures.
- Record refill outcomes by whether messages arrived, so the next result can separate delivery from the idea.
- Ask a sample of patients what they did when a text arrived.

**Next steps the evidence leaves open:** run it again as designed, with delivery confirmed per message; dropping reminders is not supported by this record.
```
