# Worked example: collecting an HIV self-test kit in Lagos

A full run of the skill on a realistic case, showing the output it should produce. The case is illustrative, not a real program.

## The request

"Behavior: men aged 18 to 30 in Lagos who receive our SMS collect a free HIV self-test kit from a partner pharmacy within two weeks and report the result by USSD. Last quarter: about 3,000 SMS a month, roughly 400 kits logged as collected, about 90 results reported. The process as staff describe it: an SMS with a code and a second SMS listing 25 pharmacies; the man picks one and travels there; shows the code and a photo ID; fills a one-page form (phone number, age, address); the pharmacist explains the kit; he takes it home and uses it; then dials a USSD code, enters the result and the 12-digit kit serial number. Nobody on the team has gone through it as a user; a field officer can do that at three pharmacies next week. The program runs the SMS, the form, and the USSD line; the pharmacies run their counters. Where are we losing people?"

## The output

```markdown
Getting from the SMS to a reported result takes a man one round trip, a photo ID, four decisions, and about 40 minutes of handling, plus travel, queues, and waiting that nobody has measured. Most men are lost before they reach a pharmacy, and most who collect a kit never report a result. The changes at the top of the list are the program's own: drop the address field, pre-fill phone and age, and stop asking men to type the 12-digit serial number. Every time below is a staff estimate until the field officer's visits next week.

# What it takes to collect a self-test kit and report the result, step by step

**Behavior:** Men aged 18 to 30 in Lagos who receive the program's SMS collect a free HIV self-test kit from a partner pharmacy within two weeks and report the result by USSD.
**Process audited:** From the first SMS (the collection code) to a result recorded on the USSD line.
**How the steps were learned:** Described by staff. Nobody has gone through it as a user, so every time below is an estimate until the field officer's visits next week.

## Step log

| # | Step, from the user's side | Time, with waiting | Money | Documents | Decision or fact demanded | Controlled by | Keep, remove, move, or check | Why | People in → out |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Read the SMS with the code, then a second SMS listing 25 pharmacies | 2 min (estimate) | None | None | Which pharmacy is nearest and open; the SMS gives no hours | Program | move | The program can name the nearest pharmacy from the area he registered in | 3,000 in; no data out |
| 2 | Travel to the pharmacy and back | Not known | Transport fare and lost earnings; amounts not known | None | When to go, around working hours | Program, through its choice of partners | move | A distributor nearer to where he lives or works would shorten it; needs new partners | No data |
| 3 | Wait at the counter | Not known | None | None | None | Pharmacy | move | A set collection hour would remove the wait | No data |
| 4 | Show the code and a photo ID | 2 min (estimate) | None | Photo ID | None | Program, with the pharmacies | check | Staff say the ID prevents double collection, which the code already does. Nobody could say whether a rule requires it; ask the program's compliance lead | No data |
| 5 | Fill the form: phone number, age, address | 5 min (estimate) | None | None | Give a home address | Program | remove (address); move (phone, age) | Nothing uses the address. Phone and age are already held from registration and can be pre-filled | No data in; about 400 out |
| 6 | Hear the pharmacist explain the kit | 5 min (estimate) | None | None | None | Pharmacy | keep | Safety: how to use the kit and what to do after a positive result | No data |
| 7 | Take the kit home, find a private moment, use it | 20 min for the test (estimate); the wait for privacy is not known | None | The kit leaflet | When and where he can be alone | The user | keep | It is the behavior | No data |
| 8 | Dial the USSD code, enter the result, enter the 12-digit serial number | 5 min (estimate); longer if the session times out | None | The kit box, for the serial number | Find and type 12 digits | Program | remove (serial number); keep (result) | The pharmacist can record the serial number against the code at collection | No data in; about 90 out |

**Total for one person:** 1 round trip, 1 document, 4 decisions; about 40 minutes of handling plus travel, queue, and the wait for privacy, none of them measured; money not known.
**Who is lost, where known:** Not known. Men without a photo ID cannot pass step 4.

## Changes, in order
1. Step 5, the address field: delete; controlled by the program; aimed at the loss between the SMS and collection.
2. Step 5, phone and age: pre-fill from registration; controlled by the program; same loss.
3. Step 8, the serial number: delete from the USSD entry, and the pharmacist records it at collection; controlled by the program, with the pharmacies' agreement; aimed at the loss between collection and reporting (about 400 to about 90).
4. Step 1, the choice among 25 pharmacies: name the nearest pharmacy and its hours in the SMS; controlled by the program; aimed at the loss between the SMS and collection.
5. Step 4, the photo ID: delete if the compliance lead confirms no rule requires it; controlled by the program with the pharmacies.
6. Step 3, the queue: a set collection hour; controlled by the pharmacies.
7. Step 2, the trip: distributors nearer to where men live or work; needs new partners.
8. A clearer SMS: information; last, and not expected to change either loss by itself.

## Steps kept
- Step 6, the pharmacist's explanation: safety. Not yet confirmed whether the kit's distribution rules require it; the program's clinical lead can say.
- Step 7, the test: it is the behavior.
- Step 8, entering the result: it is the completion point.

## Diagnosis
Two losses are measured: about 3,000 to about 400 between the SMS and collection, and about 400 to about 90 between collection and the reported result. The first spans five steps, and no count says which one loses people. The second spans the test at home and a USSD entry that asks for a 12-digit number. This rests on staff description and three counts; nothing has been observed.

## What the evidence supports
That removing steps, or doing them for people, raises completion more than explaining the process does. In the United States, help filling in a student-aid form raised college attendance where information alone did not (Bettinger et al., 2012). In Morocco, households that were told about a water connection on credit and had the paperwork handled at home signed up far more often than households left to apply by themselves (Devoto et al., 2012). No completion rate is promised for Lagos.

## What to check before relying on this
- Every time is an estimate. Have the field officer time each step at the three pharmacies, and count how many men arrive, are turned away at the ID check, and leave with a kit.
- Whether the loss after collection is the USSD entry or the test itself. Ask 15 men who collected a kit and did not report.
- The pharmacies must agree to record serial numbers and to drop the ID check.

## Where you could go from here
That's the audit.
- The field officer's visits to the three pharmacies next week: timing each step and counting who is turned away at the ID check would replace the estimates above and show which of the five steps before collection loses the most men.
- The program's compliance lead, on the photo ID: if no rule requires it, the fifth change can go ahead with the first four.
- `select-intervention-levers`, once the visits have shown where men are lost: worth it if the loss sits somewhere the program cannot delete or pre-fill, such as the trip.
I'd lean toward the field visits, because they are already planned and the order above rests on staff description alone.
Questions you could ask next: "What should the field officer record at each pharmacy so the three visits can be compared?" · "What would we ask the 15 men who collected a kit and never reported?"
```
