---
name: analyze-qualitative-themes
description: >-
  Use when someone has interviews, focus groups, or open-ended survey answers
  and asks "what are the themes?" or wants a thematic analysis with no
  hypotheses fixed in advance. Runs Braun and Clarke's six phases with AI
  agents, on its own or with the researcher deciding at three checkpoints,
  and writes a report with a thematic map. Caveat: the method's authors
  reject generative AI for this analysis, so the output is a first reading
  for a person to check. Do not use when the team has barrier hypotheses to
  test against the interviews; use synthesize-interview-findings.
license: CC-BY-4.0
metadata:
  title: Run a thematic analysis of interviews or open-ended responses
  type: atomic
  stage: analyze
  version: "0.1.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  tested_in: not-applicable
  tags: "qualitative, thematic-analysis, ai-agents, llm-assisted-analysis"
  consumes: "qualitative-data"
  produces: "thematic-analysis-report"
---

## What it does

Builds themes from a qualitative data set by the six phases of thematic analysis.

**Caveat, to read and to say first:** the method's authors reject this use. In a statement signed by 419 qualitative researchers, Braun and Clarke hold that reflexive thematic analysis is a human practice requiring a positioned, reflexive researcher, and that generative AI is not congruent with it (Jowsey et al., 2026). An AI run of the six phases is not their method as they intend it. What this skill produces is a first reading for a person to check. Never call it reflexive thematic analysis.

**What this adds:** opens with the caveat; offers two ways to run (the researcher decides at three checkpoints, or AI agents stand in); states every analytic choice before coding; gives each data item its own reader; checks every extract against the data by script; draws the map and builds the Word report by script; and reports who made each interpretive call.

## When to use it

### Use it when
- Someone has transcripts, notes, or open-ended survey answers and asks "what are the themes?"
- Someone asks for a thematic analysis, qualitative coding, or a findings section from interviews, with no hypotheses yet
- A team is about to report its interview questions as "themes"

### Do not use it when
- The team has hypotheses about why a behavior is not happening and wants a verdict on each; use `synthesize-interview-findings`
- The request is to revise existing prose; use `write-in-academic-voice`

## Before you start

Open with the caveat before any question. Then offer the two ways to run: on its own, with AI agents standing in for the researcher; or, better, with the user making the calls at three checkpoints. Then ask what is not yet answered.

1. **Required.** The data set: the items, who they are from, the language, and whether they are transcripts, notes, or translations.
2. **Required.** What they want to understand. For "explore", draft a broad question and revisit it after coding.
3. **Required.** Which way to run: with them, or on its own. "Just run it" means on its own.
4. Optional. Their view on the choices in `references/analysis-choices.md`, in plain words.
5. Optional. Sources to cite, and what they noticed while collecting the data.

If 1, 2, or 3 is missing, ask and stop. If 4 is missing, use that file's defaults and state them as choices. If 5 is missing, cite only the method papers.

## What it draws on

- Braun, V., & Clarke, V. (2006). Using thematic analysis in psychology. *Qualitative Research in Psychology*, 3(2), 77–101. https://doi.org/10.1191/1478088706qp063oa Supports: the six phases, the choices before coding, the two-level review, the map, the fifteen criteria, and the pitfalls.
- Clarke, V., & Braun, V. (2017). Thematic analysis. *The Journal of Positive Psychology*, 12(3), 297–298. https://doi.org/10.1080/17439760.2016.1262613 Supports: the definitions of code and theme, and the difference from versions built on agreement between coders.
- Jowsey, T., Braun, V., Clarke, V., Lupton, D., & Fine, M. (2026). We reject the use of generative artificial intelligence for reflexive qualitative research. *Qualitative Inquiry*, 32(10), 931–935. https://doi.org/10.1177/10778004251401851 Supports: the caveat.

**Where the evidence comes from:** The procedure makes no claim about how people behave. Evidence on AI running it is recent and mostly from wealthy Western countries; a review reports fabricated quotes, and a study in Bangladesh found coding errors that differ by who is speaking.

**Replication status:** Not applicable: its authors expect two analysts to build different themes from the same data.

## How to do it

Read `references/phases.md` first: roles, the brief for sub-agents, the working folder, and what to do without sub-agents or files.

1. **Write the plan:** question, data set, each analytic choice with its reason. Checkpoint 1: the researcher confirms it, or a stand-in analyst sets it and records why.
2. **Get to know the data (phase 1).** One reader per item reads it in full, twice.
3. **Code (phase 2).** Each reader codes its whole item, copying extracts word for word. Merge labels that mean the same; report no agreement between readers. Run `scripts/check_extracts.py` and fix every mismatch from the data.
4. **Build candidate themes (phase 3).** Group codes by the idea that holds them together, discard nothing, and draw the candidate map with `scripts/draw_map.py`. Checkpoint 2.
5. **Review (phase 4)** against the extracts under each theme, then the whole data set, with a challenger looking for what does not fit. Stop when a round only fine-tunes.
6. **Define, then name (phase 5).** Give each theme its central idea and its scope in two or three sentences; if that cannot be written, return to step 5. Checkpoint 3.
7. **Write the report (phase 6)** as in `references/report-guide.md`, in the voice of `write-in-academic-voice` if installed, after answering `references/quality-check.md`.
8. **Build the map and the Word file** with `scripts/draw_map.py` and `scripts/build_report.py`, or give the report in the conversation with a Mermaid map where no code runs.

`references/worked-example.md` shows a complete run.

## Output template

```markdown
<Two or three plain sentences to the user: the themes in a line, which way the analysis was run, and the one thing to check before relying on it. On its own, repeat the caveat here. Then where the files are.>

# <What was studied, and with whom>

**Question:** <the question the analysis answers, as it stood at the end>
**Data set:** <n items of what kind, from whom; collected by whom; language; transcripts, notes, or translations>
**How it was run:** <with <who> deciding at three checkpoints / by AI agents, with no person making the interpretive calls>

## Introduction
<The question and why it matters here. Literature only from sources the user supplied.>

## Method
### Data
<The data set and how it was chosen from everything collected.>
### Analytic approach
<Thematic analysis following Braun and Clarke (2006). Each choice with its reason: whole data set or one aspect; data-driven or theory-driven; surface or underlying meaning; how participants' words are treated; the unit for prevalence.>
### Procedure
<What was done in each of the six phases. Who did the analysis: the statement for this mode from the report guide, with the AI model named and the authors' position on AI cited.>
### Quality checks
<Extracts checked against the data: n checked, n corrected. Any of the fifteen criteria not met.>

## Findings
<One paragraph: the themes, and the story they tell together about the question.>

![Figure 1. Thematic map of <topic>](thematic-map.png)

*Note.* <What the solid and dashed lines show, and what was set aside.>

| Theme | Central idea | Sub-themes | Appears in |
|---|---|---|---|
| <name> | <one sentence> | <names, or none> | <n> of <N> <items> |

### <Theme name>
<Definition: what the theme covers and what it does not.>

<The analytic point, in the analyst's words.>

> <extract, word for word> (<participant label>)

<What the extract shows beyond what it says: what it assumes, implies, or leaves out. Then what goes against the theme.>

## Discussion
<The overall story and what it means for the question. How it sits with the supplied literature. What the analysis cannot claim.>

## What to check before relying on this
- <the theme that rests most on interpretation, and the items to read against it>
- <what rests on notes or translation; who was not interviewed>
- <on its own only: that no person has read the data against these themes>

## References
<APA 7th edition: the method papers, then each supplied source that was confirmed.>

## Where you could go from here
<One line saying the analysis is done.>
<Two or three next moves that fit what this run found, each with why it would help and when it fits. Candidates:
- someone who collected the data or knows the setting reads two or three items against the themes, when the run was on its own or a theme rests on few speakers
- `write-in-academic-voice`, when the report is headed for a journal or a funder and the prose needs another pass
- `draft-sifa-declaration`, when the report will be shared and readers should know what people and AI each did
- `decompose-comb-barriers`, when a theme points to reasons a behavior is not happening and the team wants to turn it into hypotheses to test
- `assess-evidence-base`, when the user wants to know what published research says about a theme
- `draft-tdf-interview-guide`, when a theme is thin and a second round of interviews could fill it>
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

- **A quote nobody said.** Models tidy, merge, and invent quotes. Never fix a failed extract by rewording it; go back to the item or drop it.
- **Topics passed off as themes.** "Challenges with the app" is a heading; a theme name reads as a claim.
- **Too tidy.** Four equal themes with three sub-themes each is a model's habit.
- **Agreement read as quality.** Agents that code alike share a model.
- **A pretend researcher.** On its own, never write "I" or "we" as if a person decided.

## When to bring in a specialist

Tell the user to consult an experienced qualitative researcher, or the safeguarding or data-protection lead, when:
- The run was on its own and the report will be published or drive a costly decision
- The analysis is of underlying meaning and nobody on the team knows the participants' world or language
- An item discloses harm (violence, abuse, a child at risk): the safeguarding response comes first
- Participants did not agree to their words being processed by an AI service, or the data cannot be de-identified

Bring them: the plan, the code list, and the theme definitions.
