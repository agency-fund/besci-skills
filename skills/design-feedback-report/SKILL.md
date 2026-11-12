---
name: design-feedback-report
description: >-
  Use when a program wants to tell people regularly how they are doing: health
  workers' visit counts, teachers' session records, households' water or
  energy use. Also use when a report is already sent and some people did worse
  after seeing it. Specifies the metric, the comparison, what people at the
  top and bottom see, who else sees it, and what to monitor. Do not use when
  the message only says what most others do; use write-social-norm-message.
  Not for data the program keeps to check delivery; use
  design-fidelity-monitoring.
license: CC-BY-4.0
metadata:
  title: Design a performance feedback report
  type: atomic
  stage: design
  version: "0.3.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  tested_in: beyond-western-differs
  tags: "feedback, social-comparison, audit-and-feedback"
  consumes: "barrier-diagnosis"
  produces: "intervention-draft"
---

## What it does

Specifies what a repeated report tells one person about their own performance on a task.

**What this adds:** stops if the barrier is not that people misjudge how they are doing; fixes one metric the person can move; picks the comparison by a rule and never shows a rank; specifies what people at each end see; fixes who else sees the report; and requires results to be read separately for both ends.

## When to use it

### Use it when
- "We want to text each community health worker every month with how many home visits they completed"
- "Teachers will get their class's results each term; how should we present them?"
- A report is already sent and moves nobody, or some people did worse after getting it

### Do not use it when
- The message only tells people what most others do, with no figure about the person; use `write-social-norm-message`
- The data are kept by the program to check delivery and are not returned to the person; use `design-fidelity-monitoring`
- A payment or prize is to be tied to the number; use `design-incentive-scheme`

## Before you start

Ask these before producing the report design. Do not ask anything the user has already answered.

1. **Required.** The behavior (who, what, when) and the confirmed barrier, with the evidence that people misjudge how they are doing and could change it themselves.
2. **Required.** What data exist for each person, how often they are collected, and whether people will believe them.
3. **Required.** Who besides the person would see the report, and whether it could be used in appraisal, pay, or discipline.

If 1 or 2 is missing, ask and stop. If 3 is unknown, specify that only the person sees it.

## What it draws on

- Kluger, A. N., & DeNisi, A. (1996). The effects of feedback interventions on performance: A historical review, a meta-analysis, and a preliminary feedback intervention theory. *Psychological Bulletin*, 119(2), 254–284. https://doi.org/10.1037/0033-2909.119.2.254 Supports: step 5. Over a third of 607 feedback effects were negative, and feedback worked less well as it drew attention from the task toward the self.
- Ivers, N., Yogasingam, S., Lacroix, M., et al. (2025). Audit and feedback: effects on professional practice. *Cochrane Database of Systematic Reviews*, 2025(3), CD000259. https://doi.org/10.1002/14651858.CD000259.pub4 Supports: steps 2 and 3. Across 292 trials with health professionals, feedback worked better with each person's own data, a comparison with top peers or a benchmark, and a plan for action; comparison with the average of all peers showed no effect.
- Ashraf, N., Bandiera, O., & Lee, S. S. (2014). Awards unbundled: Evidence from a natural field experiment. *Journal of Economic Behavior & Organization*, 100, 44–63. https://doi.org/10.1016/j.jebo.2014.01.001 Supports: step 4. In health worker training in Zambia, comparison with other trainees reduced performance, most among the weakest.

**Where the evidence comes from:** The reviews draw mostly on wealthy Western countries; 26 of the 292 health trials were run in low- or middle-income countries. Comparison reports cut household water use in Costa Rica and Colombia and electricity use in India; diagnostic feedback to teachers in India did not raise learning. Check locally whether people believe the number and whether "the average" can be read as named colleagues.

**Replication status:** Replicated on average, with wide variation. A sign of approval kept low-use households from using more energy in one study and made no detectable difference in a much larger US program.

## How to do it

1. **Check that the barrier is not knowing.** If supplies, pay, or skill stop people, say feedback is the wrong tool and stop.
2. **Choose one metric:** counted for each person, the same way every period, and movable by that person's own action within one period. An outcome that depends on others is never the headline.
3. **Choose the comparison by this rule.** Use a standard, or what the top quarter of peers achieve, where one is within reach. Use the person's own past where people work under different conditions. Show the average of peers only to people below it. Never show a rank.
4. **Specify both ends.** People at or above the comparison see their own past and a sign of approval, with no lower figure to drift toward. People far below see the gap to the next step, not to the top.
5. **Keep the content on the task:** the number, the comparison, the gap, and one action to take before the next report. No label, praise, or blame of the person.
6. **Fix who sees it.** If anyone besides the person does, write what they may and may not do with it.
7. **Set the frequency and the end:** no more often than the data are refreshed, and what is expected when reports stop.
8. **Set the monitoring:** results read separately for people who started above the comparison and far below it, and the change at which the report is reviewed.
9. **State what the evidence supports:** the direction. Promise no effect size.

See `references/worked-example.md` for a complete run.

## Output template

```markdown
<Two or three plain sentences to the user: the number each person will see and what it is compared with, how people at the top and the bottom are treated differently, who else sees it, and that no effect is promised.>

# A feedback report for <who receives it, in a few words>

**Behavior:** <who, what, when>
**Confirmed barrier:** <the evidence that people do not know or misjudge how they are doing, and can change it>
**Data:** <where each person's number comes from, how often, and known problems>

## Metric
- **Headline:** <one count the person can move by their own action in one period>
- **Not shown:** <outcomes that depend on others, and why>

## Comparison
- **Compared with:** <a standard / top peers / own past / peer average for those below it>, because <reason>
- **Which standard or group:** <the standard or the group, and why the person will recognize it>

## What each group sees
- **At or above the comparison:** <own past and the sign of approval; no lower figure>
- **Below it:** <the comparison and the gap>
- **Far below:** <the gap to the next step, and one small action>

## What the report says
<the skeleton for one period: the number, the comparison, the gap, one next action; no rank, label, praise, or blame>

## Who sees it
- **The person:** <channel; a short text message if none was given>
- **Anyone else:** <who, and what they may and may not do with it; or "no one">

## How often, and when it stops
- **Sent:** <how often, matched to the data cycle>
- **When reports stop:** <what is expected, and what is checked>

## Monitoring
- **Results read separately for:** <people who started at or above the comparison; people who started far below>
- **Review if:** <the change in either group, and who reviews>

## Specialist review
<not needed / <who>, because <reason>>

## What the evidence supports
<the direction, and the nearest field evidence with where it was run; no effect size promised>

## What to check before relying on this
- <the assumption most likely to be wrong>

## Where you could go from here
<One line saying the report design is done, or, if not knowing is not the barrier, why no report was designed.>
<Two or three next moves that fit what this run found, each with why it would help and when it fits. Candidates:
- `plan-prototype-test`, when nobody has checked that people believe their number or read the wording as intended
- `audit-intervention-ethics`, when anyone besides the person sees the report, or it could reach appraisal, pay, or discipline
- `design-fidelity-monitoring`, when the program also needs to check that the reports go out on time and as designed
- `design-incentive-scheme`, when the team wants a payment or prize tied to the number, which this report does not cover
- a monitoring and evaluation specialist, when each person's data are thin or disputed
- a human-resources or labor specialist with program management, when supervisors want the figures for appraisal, pay, or discipline>
Questions you could ask next: "<question>" · "<question>"
```

<!-- shared: template/shared/voice.md. Edit it there, then run scripts/check_sync.py --fix. -->
**How to talk with the user**

- If the user asked a question rather than asked for this skill's output, answer the question first, in a few plain sentences. Then offer the run and say what it would add.
- Mark the run. When it starts, say so in one line: the skill, and what it will produce. When the output is done, say the run is finished. The user should always know when the library's method is in force.
- Talk with the person, not at them. Use their words for their program and the people in it, say why you ask each question, and say what you are unsure of. No praise, no filler.
- Say where each claim comes from: this skill's sources, your general knowledge, or nothing in the library. A number the sources do not give, such as how many interviews to run, is your judgment; say so, and why you chose it.
- End with the template's closing: two or three next moves that fit what this run found, each with its reason and when it fits, and one or two questions the user could ask next. Say which move you would lean toward and why; the user decides.
<!-- /shared -->

## Where it goes wrong

- **Trusting the sign of approval.** A smiley or "on track" may not hold people at the top; keep the separate read in step 8.
- **A peer average in a small group.** In a team of twelve, "the average worker in your area" is a list of names, and private feedback becomes a public ranking.
- **A number that exists only when someone watches.** Teachers in India worked harder while observed and their students learned no more. Prefer a count from routine records.

## When to bring in a specialist

Tell the user to consult the relevant specialist before any pilot when:
- Supervisors could use the report in appraisal, pay, or discipline: a human-resources or labor specialist and program management agree written rules of use
- The metric is a clinical quality measure: a clinician confirms it is safe to pursue on its own
- Each person's data are thin or disputed: a monitoring and evaluation specialist fixes the measurement first

Bring them: the specification, the notes on data quality, and the list of who sees the report.
