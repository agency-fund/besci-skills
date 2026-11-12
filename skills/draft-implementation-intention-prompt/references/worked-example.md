# Worked example: a plan prompt for redeeming input vouchers in Chipata, Zambia

A full run of the skill on a realistic case, showing the output it should produce. The case is illustrative, not a real program.

## The request

"We work with 2,400 smallholder farmers in Chipata district, Zambia. Each registered farmer gets a seed-and-fertilizer voucher card, fully paid, to redeem at any of three agro-dealers between 1 and 21 November. After last season's registration we surveyed 300 farmers: 88% said they would redeem, and dealer records show 54% did. We interviewed 30 who did not. Most said they meant to go on a market day and the window closed; nobody mentioned cost or distrust of the dealers, and stock records show no shortages. The dealers are in Chipata town, on the Katete road, and at Chiparamba, all places farmers already go to market. They open Monday to Saturday, 8am to 5pm. The farmer must bring the voucher card and a national registration card. Camp extension officers hand out the cards at village meetings in the last week of October and spend a few minutes with each farmer. Meetings are held in Chinyanja. Draft the plan prompt."

## The output

```markdown
Here is the prompt: as each farmer receives the voucher card, the officer asks which day, hour, and dealer they will go to, and the farmer says the plan back once. It rests on the gap you found, 88% who said they would redeem against 54% who did, with cost, access, and trust ruled out. It stays a draft until eight farmers have answered it cold, before the October meetings.

# A prompt to plan when and where: redeeming the input voucher

**Behavior:** Registered farmers in Chipata district redeem their seed-and-fertilizer voucher at an agro-dealer between 1 and 21 November.
**Confirmed barrier:** An intention not acted on. 88% of 300 surveyed farmers said they would redeem; 54% did. In 30 interviews, farmers who did not redeem said they meant to go on a market day and the window closed. Cost, access, and trust are ruled out: the voucher is fully paid, the dealers are where farmers already go to market, stock records show no shortages, and nobody mentioned distrust.
**Action:** One dated occasion.
**Real options:** Any day from 1 to 21 November except Sundays, 8am to 5pm, at the agro-dealer in Chipata town, on the Katete road, or at Chiparamba. Bring the voucher card and the national registration card.

## The prompt
Asked aloud in Chinyanja by the extension officer as the card is handed over. Working copy in English:

"Which day between 1 and 21 November will you collect your inputs, and at what time? Where will you be just before you go? Which dealer will you go to?

Now say it in your own words: 'If it is ______ (day) at ______ (time) and I am ______ (where I will be just before), then I will take my voucher card and my registration card to ______ (dealer) and collect my inputs.'"

## Why each part is there
- **If (the time, and where they will be just before):** A day and an hour inside the window, tied to somewhere the farmer will already be, such as leaving the market. Farmers who missed the window had left the trip to "a market day" and never fixed which one.
- **Then (action and place):** One named dealer and the two cards, so the action is complete when the cue arrives.
- **Anything added:** Nothing. No obstacle is planned for, because the interviews point to none beyond not fixing a day.

## Delivery
- **Added to:** The village meeting where voucher cards are handed out, in the last week of October.
- **Asked by:** The camp extension officer, one farmer at a time.
- **When:** As the farmer first holds the card, one to three weeks before the chosen day, while every day in the window is still open.
- **How the person says it back:** The farmer says the whole sentence aloud once. The officer checks only that the day, hour, and dealer are real options and does not choose for the farmer.
- **What the person keeps:** Nothing is required. A farmer who wants to can mark the day on the back of their own voucher card.

## Who else sees or hears the plan
Neighbors at the meeting hear it. Collecting farm inputs is not sensitive, so no specialist review is needed. Nobody records or collects the plans.

## Pretest
Eight farmers from two villages, half of them women, answer the prompt cold in Chinyanja. It passes if all eight name a day from 1 to 21 November that is not a Sunday, an hour between 8am and 5pm, and one of the three dealers, and can say the sentence without help.

## What the evidence supports
That asking people to name a time and a place raises follow-through on a one-off, dated action they already intend to take. The clearest field trial is from the United States, where a prompt for the date and time of a flu vaccination raised the rate among a firm's employees. Elsewhere results differ: a job-search plan helped unemployed youth in South Africa, and plan prompts made little or no difference to HIV testing in Uganda or to reporting HIV self-test results in South Africa. Nothing found tests the prompt with farmers. No effect size is promised.

## What to check before relying on this
- Whether "I will redeem" holds when the question names a day. Ask 20 farmers "which day?" before the meetings.
- Whether women farmers choose the day and the dealer themselves, or the trip depends on a husband's agreement or on transport money.
- Whether officers have time to do this one farmer at a time. If they fill in the day for people, the prompt has not been delivered.

## Where you could go from here
That's the prompt.
- Ask 20 farmers "which day?" before the meetings: the 88% came from a survey yes, and the prompt only helps if that intention holds once a day is named.
- Plan a short test at one real meeting with `plan-prototype-test`: worth it if you are unsure officers can take a few minutes per farmer without choosing the day for them, which is the likeliest way the prompt fails.
- Write it up for every camp with `draft-intervention-description`: fits once the pretest passes, since officers across the district must ask it the same way.
I'd lean toward asking the 20 farmers first, because it is cheap and tests the one thing the whole prompt rests on.
Questions you could ask next: "What should the officer say if a farmer can't name a day?" · "Should we ask women farmers separately, in case the trip isn't their decision?"
```
