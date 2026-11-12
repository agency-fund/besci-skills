# Worked example: a daily SMS medication reminder

A full run of the skill on a realistic case, showing the output it should produce. The case is illustrative, not a real program.

## The request

"We ran a 3-month SMS reminder program to improve adherence to a daily medication for our enrolled patients: one reminder text per day at 8am. Adherence, measured by pharmacy refill records, barely moved. Our take is that patients just don't care enough about their health to act on a reminder. We're deciding whether to drop reminders altogether. I pulled the SMS gateway's delivery logs for you: about 30% of messages failed silently on two carriers, with no resend. No other changes at the clinics during the period. Can you review it?"

## The output

```markdown
The record can't yet tell you whether reminders work: about 30% of the texts never arrived, so the idea was never fairly tested. Your team's explanation, that patients don't care enough, has no data behind it, and failed delivery explains the flat refill records just as well. Dropping reminders is not supported by this record.

# Did the daily SMS medication reminder fail because of the idea or the delivery?

**The program, as you described it:** A 3-month program sending one SMS reminder at 8am each day to enrolled patients to improve adherence to a daily medication, judged by pharmacy refill records. Adherence barely moved; the team's view is that patients do not care enough to act on a reminder.

## What was planned
Target behavior: enrolled patients take their daily medication. The 8am text was meant to prompt the dose that day, every day for 3 months, through the SMS gateway.

## What was actually delivered
- **Fidelity: delivered as designed?** No. About 30% of messages failed silently on two carriers, with no fallback or resend. **How we know:** confirmed by the record (the gateway's delivery logs)
- **Dose: how much, against the plan?** For patients on the affected carriers, far fewer than the planned seven reminders a week arrived; how many fewer depends on how failures fell across days. **How we know:** confirmed that dose fell short; its size per patient is inferred
- **Reach: what share of the intended people did it get to?** Every enrolled patient was in scope, but reach to a working reminder was uneven and was not tracked by carrier at the time. **How we know:** confirmed that reach was uneven; which patients were affected is inferred, not logged
- **Context: what changed around the program?** Nothing at the clinics during the 3 months. **How we know:** confirmed by the record (no change reported)
- **Response: did the people reached open, understand, or use it?** No data on whether patients who received the texts read them or took the dose after them. **How we know:** confirmed that no such data was collected

## What the outcome data show
Pharmacy refill records, a routinely tracked administrative measure, show adherence essentially flat. There was no comparison group, so the result is a description, not an estimate of the program's effect. It is also confounded by the delivery gap: the program delivered was weaker than the one designed.

## Does the team's explanation hold up?
- **The team's explanation for the outcome:** Patients do not care enough about their health to act on a reminder.
- **Does the collected data support it?** No. Nothing was collected on patients' receipt of messages, their engagement, or their attitudes; the claim is inferred from the flat outcome alone.
- **Another explanation the data does not rule out:** Many patients never reliably received the reminder, given the carrier failures. Motivation was never tested against a fully delivered program.

## The idea or the delivery?
**Classification:** cannot yet tell
There is a confirmed implementation failure, large enough that the reminder idea has not been fairly tested. Without refill records split by carrier, or any data on response, the flat outcome cannot be attributed to the idea. The team's explanation about motivation is not supported by the data it collected.

## What would need fixing before any retry
- Confirm delivery of each message, on every carrier, and resend failures.
- Record refill outcomes by whether messages arrived, so the next result can separate delivery from the idea.
- Ask a sample of patients what they did when a text arrived.

**Options the evidence leaves open:** run it again as designed, with delivery confirmed per message; dropping reminders is not supported by this record.

## Where you could go from here
That's the review.
- Split the refill records you already hold by carrier: if patients on the two failing carriers refilled less often than the rest, that is a first sign the reminder did something where it arrived. It is not a fair test, since carriers were not assigned at random, but it costs only a records pull.
- Ask a few patients what they did when a text arrived: the record has nothing on response, and asking them is the most direct test of the team's view that patients don't care enough.
- Plan how delivery will be tracked in a retry with `design-fidelity-monitoring`: the gap here came to light only because someone pulled the gateway logs afterward.
I'd lean toward splitting the refill records first, because it uses data you already have and gives a first read on whether reminders did anything before you plan a retry.
Questions you could ask next: "What would a fair retry need to log?" · "How do we explain this to the clinic managers who already think reminders don't work?"
```
