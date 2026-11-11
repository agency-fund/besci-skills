# Worked example: weekly SMS for ART adherence at two clinics in Kisumu

A full run of the skill on a realistic case, showing the output it should produce. The case is illustrative, not a real program.

## The request

"We ran a weekly SMS program for adults on antiretroviral therapy (ART) at two public clinics in Kisumu County, Kenya, from March 2025 to February 2026. The county health office wants to run it at four more clinics and has asked us for a write-up it can work from. We have the design brief (the target behavior was taking the daily dose at the chosen time; the barriers were forgetting at the moment of the dose and feeling alone with the regimen between visits), the 12-message bank in Swahili, Dholuo, and English, the enrollment form, the nurse callback script, the two-hour nurse training deck, the SMS gateway configuration, our monitoring plan and its data (gateway logs, monthly back-check calls, observed enrollments), and our log of changes. Everything is on the county shared drive. Four nurses, two per clinic, enrolled patients; our program officer ran the gateway."

## The output

```markdown
# Intervention description: Tuko Pamoja weekly SMS

**Status:** As delivered, March 2025 to February 2026, two public ART clinics in Kisumu County · **Written for:** hand-off to the county health office
**Sources:** design brief; message bank; enrollment form; callback script; training deck; gateway configuration; monitoring plan and data; change log. Nothing from recollection.

## 1. Brief name
"Tuko Pamoja" (Swahili, "we are together"); called "the Monday message" by patients and nurses.

## 2. Why
**Target behavior:** Adults on ART at the two clinics take their daily dose at the time they chose, every day. · **Barrier:** Forgetting at the moment of the dose, and feeling alone with the regimen between clinic visits (design brief).

| Part | What it changes for the person | Barrier it addresses | Essential? | Source |
|---|---|---|---|---|
| Weekly text at the time the patient chose | Puts the dose back in mind at a fixed moment each week | Forgetting | Essential | Design brief |
| Offer of a nurse call on reply "1" | Gives a person to reach between visits | Feeling alone with the regimen | Essential | Design brief |
| Wording that never names HIV or ART | Keeps the message safe if someone else reads the phone | Fear of disclosure, which would stop patients enrolling | Essential | Design brief; change log |
| Greeting line and clinic name | None: tells the patient who the sender is | n/a | Scaffolding | Message bank |

## 3. What: materials
| Material | Language(s) | Where to get it | Source |
|---|---|---|---|
| Message bank, 12 messages, one a week, rotating four times | Swahili, Dholuo, English | County shared drive, "Tuko Pamoja/messages" | Message bank |
| Enrollment form with consent, language, and time of day | Swahili, English | Same drive, "Tuko Pamoja/forms" | Enrollment form |
| Nurse callback script | English | Same drive, "Tuko Pamoja/forms" | Callback script |
| Nurse training deck, 2 hours | English | Same drive, "Tuko Pamoja/training" | Training deck |
| Gateway configuration: schedule, reply keyword, stop keyword | n/a | Same drive, "Tuko Pamoja/gateway", as an export | Gateway configuration |

## 4. What: procedures
At a routine ART visit the nurse explains the program, takes consent, and records the phone number, language, and preferred time on the form, then enters them in the gateway the same day. The first message goes the next Monday at the chosen time, and one goes every Monday after. A patient who replies "1" is called by a clinic nurse within 72 hours, and the nurse logs the call. A patient who replies "STOP" is removed the same day. A patient who misses a clinic visit stays enrolled, and no message mentions the missed visit. A patient who changes number is re-enrolled at the next visit. Essential details a newcomer might drop: the message goes at the patient's own chosen time, not a batch time; no message names HIV or ART; the sender shows the clinic name, not a personal number.

## 5. Who provided
Four ART nurses, two per clinic, each trained for two hours on enrollment and the callback script, supervised by the clinic in-charge. One program officer ran the gateway and reviewed the callback log weekly.

## 6. How
Individual text messages; an individual phone call from a nurse when the patient replied.

## 7. Where
Enrollment in the ART clinics during routine visits, weekdays 8am to 4pm, in a private counseling room at both clinics. Messages were received wherever the patient was. Both clinics had reliable mobile coverage; the gateway was hosted off-site, so one clinic's power cuts did not affect it.

## 8. When and how much
One enrollment contact of about ten minutes; one message a week for 48 weeks; nurse calls when patients replied, a median of one per patient over the period.

## 9. Tailoring
Planned before delivery: language (three options) and time of day, both chosen by the patient at enrollment.

## 10. Modifications
| What changed | When | Who | Why | Part touched | Source |
|---|---|---|---|---|---|
| Two Dholuo messages re-translated | Week 6 | Program officer with a Dholuo-speaking nurse | A back-translation showed they implied a diagnosis to anyone reading the phone | Wording that never names HIV or ART; essential | Change log |
| Callback window widened from 48 to 72 hours | Week 14 | Clinic in-charge | One nurse on leave; 48 hours could not be met | Nurse call; essential | Change log |

## 11. How well: planned
Gateway delivery logs for every message (dose); each month, back-check calls to 20 patients per clinic drawn at random, asking whether a message arrived in the last two weeks (dose); the callback log checked weekly against the reply log, with a 48-hour, later 72-hour, threshold (adherence); two enrollments per nurse per month observed by the program officer against the consent points on the form (quality). Delivery below 85% in a month triggered a gateway check; callbacks within the window below 80% triggered a staffing review with the in-charge.

## 12. How well: actual
From the monitoring data, March 2025 to February 2026: 92% of scheduled messages delivered (gateway logs; 93% at one clinic, 91% at the other); 84% of 480 back-checked patients said a message had arrived in the previous two weeks; 71% of replies called back within 48 hours before week 14, and 88% within 72 hours after; 7 of 8 observed enrollments covered every consent point. Not measured: whether messages were read at the chosen time.

## Delivery system
Staffing: two nurses per clinic for enrollment and callbacks, about two hours a week each, after a two-hour training; one officer for the gateway, about one day a week. Supervision: the clinic in-charge for the nurses. Logistics: an off-site SMS gateway with a monthly fee; airtime for nurse calls. Information system: the gateway's own records; enrollment forms filed at the clinic. Cost to deliver: not yet totaled. Research-only inputs that will not come with the program unless the county keeps them: the monthly back-check calls and the observed enrollments.

## Rebuild check
| Item | Complete / partial / missing | What a team elsewhere would still need |
|---|---|---|
| 1, 2, 4 to 12 | Complete | |
| 3 | Partial | The drive holds both old and re-translated Dholuo messages; the current versions are not marked |
| Delivery system | Partial | The cost to deliver per patient per year |

## Open questions
- Item 3: the program officer can mark the current Dholuo versions this month.
- Delivery system: the program's finance officer can total the gateway fee, airtime, and staff time.
- Whether the county will keep the back-check calls; without them, item 12 cannot be repeated at the new clinics.
- No limit on sharing: the materials contain no patient details.
```
