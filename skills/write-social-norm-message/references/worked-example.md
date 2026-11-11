# Worked example: a text message on fertilizer timing for maize farmers in Western Kenya

A full run of the skill on a realistic case, showing the output it should produce. The case is illustrative, not a real program.

## The request

"Behavior: maize farmers enrolled in our program in Kimilili sub-county apply top-dressing fertilizer between the third and fifth week after planting, each long-rains season. Field officers' plot records for last season show 64% of the 2,150 enrolled farmers in Kimilili did so. We surveyed 180 of them: the typical farmer thinks about 4 in 10 neighbors top-dress on time, and 82% say a farmer who does is 'doing what a good farmer should'. In interviews farmers said they wait to see what neighbors do. Fertilizer is stocked at the agrovets and enrolled farmers have credit for it. We send text messages in Kiswahili from each farmer's own field officer, and we hold every farmer's planting date and last season's record. Nothing about this is sensitive. Can we tell them most farmers already do it?"

## The output

```markdown
# Social norm message

**Behavior:** Maize farmers enrolled in the program in Kimilili sub-county apply top-dressing fertilizer between the third and fifth week after planting, each long-rains season.
**What the audience believes peers do and approve of:** The typical farmer believes about 4 in 10 neighbors top-dress on time; 82% say a farmer who does is doing what a good farmer should (survey of 180 enrolled farmers; interviews in which farmers said they wait to see what neighbors do).
**What peers really do:** 64% of the 2,150 enrolled farmers in Kimilili top-dressed within the window (field officers' plot records, last long-rains season).
**What peers really approve of:** 82% of 180 surveyed enrolled farmers approve of top-dressing on time (program survey, same season).
**Belief the message corrects:** Farmers believe about 4 in 10 do it; 6 in 10 did. Cost and access are ruled out: fertilizer is stocked and farmers have credit for it.

## Kind of message
- **Chosen:** Both: what most do, with what most approve of.
- **Rule applied:** At least half do it (64%), and approval was measured (82%).

## The message
Hello <name>. Last season 6 out of every 10 program farmers in Kimilili top-dressed their maize by week 5, and 8 out of 10 say that is what a good farmer does. Thank you if you were one of them. You planted on <date>: top-dress by <date plus 35 days>. Your agrovet has stock. <Field officer's name>

**Language:** Working copy in English. A native Kiswahili speaker redrafts it; "top-dress" and "week 5" use the words field officers use with farmers.

## Checks on the claim
- **Figure in the message against figure in the data:** "6 out of every 10" for 64%, and "8 out of 10" for 82%; both rounded down.
- **Group named against group the figure describes:** Same: program farmers in Kimilili.
- **Does the audience see this group as people like them:** Not known. Farmers said they watch neighbors, and some neighbors are not enrolled. Ask in the first check.
- **Lines saying how many do not do it:** None.

## For people who already do the behavior
- **Line of approval:** "Thank you if you were one of them."
- **How they are identified:** Last season's plot records show who top-dressed within the window.

## Sender and timing
- **Sender:** The farmer's own field officer, who sees the plots; farmers already expect a view on their farming from this person.
- **When:** Two weeks after the recorded planting date, once, so the window is open and the action is a few days away.

## Before wide use
- **Ask about ten recipients:** Read the message to ten farmers in two wards. Ask who they think "program farmers in Kimilili" are, whether they believe 6 in 10, and what they would do next.
- **Comparison:** One farmer in five, chosen at random within each ward, receives the same message without the two norm sentences and the thanks. Outcome: top-dressing within the window, from plot records, read at week 6.
- **Withdraw the message if:** Among farmers who top-dressed on time last season, the rate this season is lower with the norm lines than without them.

## What the evidence supports
That telling people a true majority figure for a group they belong to moves some of those who were not acting. Letters stating how many taxpayers had paid raised payment in Guatemala and in Peru. Nothing comparable was found for farming, and no effect size is promised for Kimilili.

## What to check before relying on this
- Whether farmers count enrolled farmers across the sub-county as their peers, or only the neighbors whose fields they can see. If it is neighbors, compute the share by ward and use it only where it is at least half.
- Whether the plot records are complete; a field officer who recorded only the farms visited would overstate the 64%.
```
