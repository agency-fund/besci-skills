---
name: check-the-evidence
title: Check the evidence
description: >-
  For a program team that is about to choose a behavior or an intervention and
  wants to know what research already says: scan the published evidence, judge
  whether the most promising finding would hold in your setting, and, if a test
  is coming, set the effect size to plan it on. Ends with an evidence scan
  brief, a verdict on one finding with the assumptions to check locally, and
  optionally a planning range with one number to plan on. Does not choose the
  behavior, design the intervention, or compute a sample size.
license: CC-BY-4.0
metadata:
  version: "0.1.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  stages: "define, test"
  skills: "assess-evidence-base, assess-evidence-transferability, estimate-expected-effect"
  tags: "evidence-synthesis, quantitative"
---

## What it is for

A team has a goal and a favorite idea, and someone says "this worked in another country". This workflow puts a short, checked look at the research before the team commits: what has been tried, whether the best-looking result would carry over to this population and this way of delivering it, and what size of effect is realistic to plan on. It is the shortest workflow in the library: two steps in the define stage and one optional step in the test stage.

**Process it follows:** reviewing the existing evidence and judging whether it applies in a new setting, two steps Intervention Mapping names (Fernandez et al., 2019), then setting the effect size to plan on, a step in J-PAL's research resources.

## When to use it

- When a program goal is set and nobody has checked what has been tried for this behavior or population
- When a proposal or a funder quotes a study's effect as what your program will achieve
- When you already hold one study and only want to know whether it applies to you; start at step 2
- When you have several published estimates and need one number for a power calculation; start at step 3
- Not when the "evidence" is your own program's earlier attempt; use `review-prior-intervention` instead
- Not when a full systematic review is required for a publication or a policy decision; step 1 is a time-bounded scan, so bring in an evidence-synthesis specialist

## Skills in this workflow

| Step | Skill | Version | Relationship | What carries forward | Human decision point |
|---|---|---|---|---|---|
| 1 | `assess-evidence-base` | 0.2.0 | start | evidence scan brief: what has been tried, where and with whom, the findings that go against the goal, the gaps, and what the search covered | Pick the one finding worth checking against your setting, or decide the scan is too thin to act on |
| 2 | `assess-evidence-transferability` | 0.2.0 | after 1 | transferability assessment: a verdict on whether that finding is likely to hold here, and the assumptions to test locally | Decide whether to build on the finding, test its assumptions first, or go back to the brief for another one |
| 3 | `estimate-expected-effect` | 0.2.0 | after 2, optional | effect-size benchmark: a planning range and one effect to plan on, in the units of your test | Set the smallest effect worth acting on, and decide whether a test is worth running if the program is unlikely to reach it |

Relationship values: `start`, `after N`, `parallel with N`, `independent`, `optional`.

## How to run it

The order is a recommendation. Start at any step if you already have what it needs, and use any of these skills on its own.

1. Run `assess-evidence-base` on the program goal, with what you know about who the program reaches, where, and through what channel. Choose a search route: full-text search for health topics, general web search for economics, education, and program reports, or both. Read the brief's "Findings that do not support the goal" and "Search coverage" before its table of what worked. A search that found nothing is not evidence that nothing works.
2. Stop and choose one row of the brief. Take the finding closest to your population, channel, and deliverer, not the one with the largest effect.
3. Run `assess-evidence-transferability` with that study (the link from the brief), a description of your setting (who, where, what would be delivered, by whom, and which outcome matters), and the decision the verdict will inform.
4. Stop and read the verdict. "Likely to hold" is about direction, not size. "Cannot tell" or "Unlikely to hold" sends you back to the brief for another row, or to the local checks the assessment lists.
5. If a test or a proposal needs a number, run `estimate-expected-effect`. Give it the studies with their reported effects (from the brief and from the study you checked for transferability), your test's outcome, unit, and baseline from your own records, who will deliver it and to how many people, and the smallest effect worth acting on if someone has set it. It returns a range and one number to plan on; it does not compute a sample size.
6. Carry the results forward. The assumptions to test locally become questions for your diagnosis, for example in `decompose-comb-barriers` or `draft-tdf-interview-guide`. The effect to plan on goes to `estimate-sample-size` once `choose-trial-design` has set the comparison.

## Worked example

This example is illustrative; the program and its details are invented.

A network of savings groups in northern Ghana wants members to deposit every week and is drawn to SMS reminders. Step 1's brief lists reminder trials, most with bank customers outside Africa and one in West Africa; it puts any trial that found nothing in its own section and notes that it reached no program reports in local languages. The team picks the West African trial as the closest to its members. Step 2 compares the conditions: in the study every participant had a phone and an account, and researchers sent the messages; here many members share a phone, and the network's field officers would send the texts. The verdict is "likely to hold with changes", with two assumptions to test locally: members see texts sent to a shared phone, and they trust a message from a field officer. Step 3 takes the trial's effect, converts it to the network's weekly deposit rate using the network's own records, lowers it because field officers rather than researchers will deliver it, and returns a range with one number to plan on. The network's director then sets the smallest effect that would justify the cost of the texts. It sits above the middle of the range, so the team decides to check the shared-phone assumption with a few groups before paying for a trial.

## Where it goes wrong

- Searching only for the intervention the team already likes. Step 1 searches on the behavior and the population; a search for "does X work" returns the studies that say it does.
- Picking the finding with the biggest number at step 2. Pick the one whose population, channel, and deliverer are closest to yours.
- Reading "likely to hold" as "will produce the same effect". Step 3 exists because the published number has to be corrected for which studies get published and for who will deliver the program.
- Using a pilot's own estimate as the number to plan on. A pilot that persuaded the team to continue was selected for looking good.
- Running step 3 when step 2 said "cannot tell". A planning number built on a finding that may not apply is precise and wrong.

## When to bring in a specialist

- The decision is a multi-year program, a national policy, or a publication: a research librarian or evidence-synthesis specialist extends step 1. Bring the brief, the search terms, and the list of sources opened.
- The verdict at step 2 is "cannot tell" and the budget is large, or the doubtful condition is legal or institutional (who may deduct from pay, who can consent): a researcher who knows the local setting. Bring the assessment and its list of unknowns.
- The low end of the planning range is near zero and the test is expensive: an evaluation methodologist. Bring the estimates table, the corrections, and the decision the test serves.
