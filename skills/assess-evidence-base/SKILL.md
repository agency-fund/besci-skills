---
name: assess-evidence-base
description: >-
  Use when a program goal is set and nobody has checked what research already
  exists, or when someone asks "has this been done before?" or "what does the
  evidence say works here?". Searches the literature, checks every citation,
  and reports what worked, what did not, how large the effects were, and where
  each study was run. Do not use when the question is whether one known study
  applies to your setting; use assess-evidence-transferability. Not for
  reviewing your own past program; use review-prior-intervention.
license: CC-BY-4.0
metadata:
  title: Check what research already exists
  type: atomic
  stage: define
  version: "0.3.0"
  status: draft
  authors: "Joe Speed, Zezhen Wu"
  org: IL
  tested_in: not-applicable
  tags: "evidence-synthesis, rapid-evidence-assessment"
  consumes: "program-goal"
  produces: "evidence-scan-brief"
---

## What it does

Summarizes the existing research on the behavior, audience, or setting named in a program goal.

**What this adds:** runs a literature search and opens every source before citing it; always reports null and contradicting findings in their own section; states where each study was run next to your population; and says what the search covered, so a thin scan is not read as "nothing works".

## When to use it

### Use it when
- A program goal has been stated and no one has checked whether similar interventions have been tried for this behavior or population
- Someone asks "has this been done before?" or "what does the evidence actually say works here?"
- A team is about to choose a target behavior or an intervention from its own assumptions alone

### Do not use it when
- The question is whether one known study applies to the user's setting; use `assess-evidence-transferability`
- The "evidence" is the team's own earlier attempt at the program; use `review-prior-intervention`
- A full systematic review is required, for a publication or a policy decision; this is a time-bounded scan

## Before you start

Ask these before producing the summary. Do not ask anything the user has already answered.

1. **Required.** The program goal, and what is known about the population and setting: who, where, reached through what channel.
2. **Required, with a default.** Which search route to use:
   - **Paperclip** reads the full text of papers in PubMed Central, bioRxiv, medRxiv, and arXiv, so numbers come from the results section. It is strongest on health, needs the `paperclip` command-line tool installed and signed in, and misses most economics journals, working papers, and program reports.
   - **General web search** covers economics, education, working papers, and reports from J-PAL, IPA, 3ie, and the World Bank. It often reaches only the abstract.
   - **Both**, for a health topic where program reports also matter.
3. Optional. Studies, reports, or organizations the team already knows, and any intervention it is already considering.

If 1 is missing, ask and stop. If the user gives no route, use general web search, add Paperclip when it is installed and the topic is health, and say in one line which route you chose and what the other would add. If no search tool is available, say so in the first line and follow rule 6 in `references/citing-sources.md`.

## What it draws on

- Garritty, C., Gartlehner, G., Nussbaumer-Streit, B., et al. (2021). Cochrane Rapid Reviews Methods Group offers evidence-informed guidance to conduct rapid reviews. *Journal of Clinical Epidemiology*, 130, 13–22. https://doi.org/10.1016/j.jclinepi.2020.10.007 Supports: a time-bounded search that states its limits, in place of a full systematic review.
- Guyatt, G. H., Oxman, A. D., Vist, G. E., et al. (2008). GRADE: an emerging consensus on rating quality of evidence and strength of recommendations. *BMJ*, 336(7650), 924–926. https://doi.org/10.1136/bmj.39489.470347.AD Supports: reporting each finding with its study design. GRADE is a standard system for rating how certain a body of evidence is.
- Thalmayer, A. G., Toscanelli, C., & Arnett, J. J. (2021). The neglected 95% revisited: Is American psychology becoming less American? *American Psychologist*, 76(1), 116–129. https://doi.org/10.1037/amp0000622 Supports: stating where each study was run.

**Where the evidence comes from:** The search method makes no claim about how people behave, so the question applies to what it finds. In six leading psychology journals from 2014 to 2018, a little over 60% of samples and authors were American, and the countries where 89% of people live supplied 4 to 5% (Thalmayer et al., 2021). "No evidence found" therefore means none was published where the scan looked.

**Replication status:** Not applicable; a rapid review is a method. Two scans of one question can turn up different studies, so the brief states what it searched.

## How to do it

1. **Restate the goal and name the search route.**
2. **Search on the behavior and the population**, not only on an intervention the team already favors. Run at least one search for reviews and meta-analyses and one for studies in the user's country or region. A search for "does X work" returns the studies that say it does.
3. **Open each source before using it**, following `references/citing-sources.md`: confirm authors, year, and title; take effect sizes from the results; write "abstract only" where that is all you read; drop any source whose link does not resolve.
4. **Write one row per finding:** the intervention, where and with whom it was tested, the result with its size, unit, and study design, and how that population compares with the user's. Several papers on one trial are one row.
5. **Fill "Findings that do not support the goal":** null results, contradicting results, and backfires, each with what it means for this program. If there are none, write "None found in this search."
6. **State the gaps:** what the goal asks that no located study addresses.
7. **Write "Search coverage":** what was searched, with which terms, how many sources were opened, and what was not reached.
8. **Stop at the summary.** Do not choose a behavior or recommend a design.

See `references/worked-example.md` for a complete run.

## Output template

```markdown
<Two or three plain sentences to the user: what the research found that bears most on their goal, the strongest finding against it, and how far the search reached, so a thin search is not read as "nothing works".>

# What research already exists on <the goal, in a few words>

**Program goal (as given):** <the goal, verbatim or lightly cleaned>
**Search route:** <Paperclip / general web search / both / no search tool available>

## What has been tried

| Intervention | Tested where and with whom | Result | Compared with your population | Source |
|---|---|---|---|---|
| <...> | <country, population, setting> | <size, unit, and direction; study design; "abstract only" if the full text was not read> | <same country and group / different in <what>> | <authors, year, link> |

## Findings that do not support the goal
- <null result, contradicting result, or backfire>: <where and with whom>; <what it means for this program>; <source>

## Gaps
<what the goal asks that no located study addresses>

## Search coverage
- **Searched:** <tools or databases, and the search terms>
- **Opened:** <n sources: n in full text, n abstract only>
- **Not reached:** <languages, program reports, databases>
- **A fuller review would add:** <...>

## Where you could go from here
<One line saying the evidence summary is done.>
<Two or three next moves that fit what this search found, each with why it would help and when it fits. Candidates:
- `assess-evidence-transferability`, when one study looks like the model for the program and the question is whether its result would hold for this population
- `estimate-expected-effect`, when the team will test a program and needs an effect size to plan on from the estimates found
- `define-key-behavior`, when the goal is still broad and the team is ready to pick the one behavior to work on
- `review-prior-intervention`, when the team or a partner has already run something similar and its records exist
- a research librarian, an evidence-synthesis specialist, or the databases this search could not reach (3ie, J-PAL, program reports, other languages), when the decision is hard to reverse or the gaps sit where the search did not look>
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

- **Citing from memory.** A recalled citation can carry the wrong authors, year, or link, and the reader cannot tell. Every row's source was opened in this run, or the row says "from memory, not checked".
- **Stretching a loosely related study.** US students' saving is not evidence about rural farmers. If it is the nearest evidence, say so in the comparison column and under Gaps.
- **Reading "no evidence found" as "does not work".** Absence from a time-bounded search is not a null result.

## When to bring in a specialist

Tell the user to consult a research librarian, an evidence-synthesis specialist, or a behavioral scientist in the field when:
- The decision is high-stakes or hard to reverse: a multi-year program, a national policy recommendation, a publication
- The located studies contradict each other and the team must decide which to weight
- The relevant evidence probably sits in program reports or non-English sources the scan could not reach

Bring them: the brief, the search terms, and the list of sources opened.
