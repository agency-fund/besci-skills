---
name: synthesize-interview-findings
description: >-
  Use when interviews or field notes are in and the team needs to know which
  of its barrier hypotheses they support, or when someone asks "we have 15
  transcripts, what did we learn?" or wants interviews coded against COM-B
  or the TDF. Charts every interview against every hypothesis and gives each
  a verdict, with quotes and the interviews that go against it. Do not use
  before the interviews, to decide what to ask; use
  draft-tdf-interview-guide. Not for choosing what to do about a confirmed
  barrier; use select-intervention-levers.
license: CC-BY-4.0
metadata:
  title: Turn interview transcripts into a barrier diagnosis
  type: atomic
  stage: analyze
  version: "0.2.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  tested_in: not-applicable
  tags: "qualitative, tdf, com-b, diagnosis"
  consumes: "qualitative-data, comb-barrier-hypotheses"
  produces: "barrier-diagnosis"
---

## What it does

Gives each barrier hypothesis a verdict from a set of interviews.

**What this adds:** charts every interview against every hypothesis, each cell a summary in the respondent's words with a quote reference; separates "not asked" from "asked, said nothing"; keeps a column for what no hypothesis predicted; judges each hypothesis on frequency, conflicting accounts, and strength of belief; names every interview against a verdict; and never turns counts into shares of a population.

A barrier hypothesis is a guess about why people are not doing a behavior, often labeled with a part of COM-B (capability, opportunity, motivation) or a domain of the Theoretical Domains Framework (TDF).

## When to use it

### Use it when
- Interviews, focus groups, or field notes are done and the team asks "what did we learn?" or "do the interviews back our hypotheses?"
- Someone asks to code transcripts against COM-B or the TDF domains
- A team is about to quote the two most vivid interviews as "what people told us" without reading the rest

### Do not use it when
- The interviews have not happened and the question is what to ask; use `draft-tdf-interview-guide`
- There are no hypotheses yet; to list them, use `decompose-comb-barriers`
- The barrier is confirmed and the question is what to do about it; use `select-intervention-levers`

## Before you start

Ask these before producing anything. Do not ask anything the user has already answered.

1. **Required.** The interviews (transcripts, notes, or recordings), with who was interviewed, by whom, in what language, and who translated.
2. **Required.** The hypotheses the interviews were meant to test, with their COM-B component or TDF domain if labeled.
3. Optional. The interview guide.
4. Optional. Groups to compare (people who do the behavior and people who do not, site, sex), and other evidence: records, a survey, observation.

If 1 or 2 is missing, ask and stop. If 3 is missing, take what was asked from the transcripts; where notes do not show the question, mark "not asked". If 4 is missing, compare no groups and say so.

## What it draws on

- Gale, N. K., Heath, G., Cameron, E., Rashid, S., & Redwood, S. (2013). Using the framework method for the analysis of qualitative data in multi-disciplinary health research. *BMC Medical Research Methodology*, 13, 117. https://doi.org/10.1186/1471-2288-13-117 Supports: the matrix of interviews by codes with quote references, open coding of the first transcripts, and the warning that counts from a chosen sample describe no population.
- Atkins, L., Francis, J., Islam, R., et al. (2017). A guide to using the Theoretical Domains Framework of behaviour change to investigate implementation problems. *Implementation Science*, 12, 77. https://doi.org/10.1186/s13012-017-0605-9 Supports: coding to TDF domains, the three tests of whether a domain matters, and keeping what fits no domain.
- UNICEF (2022). *Social & Behaviour Change at UNICEF: Programme Guidance*. https://www.sbcguidance.org/ Supports: a second reader, attention to outliers, and checking findings against other evidence.

**Where the evidence comes from:** The procedure makes no claim about how people behave. The method papers come from health research in the United Kingdom, Canada, and Australia; the UNICEF guidance was written for low- and middle-income countries. What is local is the reading: someone who does not know the language or the place misses idiom and what was left unsaid.

**Replication status:** Not applicable: no source tests whether two analysts reach the same verdicts from the same interviews.

## How to do it

1. **Set the columns before reading:** one per hypothesis, with its COM-B or TDF label, and one "not predicted". Use five statuses: supports, contradicts, mixed, asked but said nothing, not asked.
2. **Read every interview once before charting**, and code the first two or three openly; fixed columns find only what the team expected.
3. **Chart each interview into its row:** one to three sentences in the respondent's terms, a quote reference (respondent, page or minute), and a status. Mark cells that rest on notes or translation. Leave no cell empty; an empty cell looks like an unread one. A second reader, if available, charts the first few too; settle differences before going on.
4. **Read down each column.** Count interviews by status, find conflicting accounts and strongly held beliefs, and compare groups. A real barrier usually shows as people who do not do the behavior reporting it, while those who do it did not face it or got round it.
5. **Give each hypothesis a verdict:** supported, not supported, mixed, or not tested (most interviews did not ask). Weigh all three tests (frequency, conflict, strength; frequency does not apply to focus groups), not the count alone, and name every interview that goes against it.
6. **List what no hypothesis predicted**, and the outliers, such as someone who does the behavior despite the barrier.
7. **Set each verdict beside the other evidence** the user has, and say whether it agrees.
8. **Name the confirmed barriers** and the open hypotheses, with what would settle each. Propose no interventions.

See `references/worked-example.md` for a complete run.

## Output template

```markdown
# Interview synthesis: <short name of the behavior>

**Behavior:** <who does what, when, as given>
**Interviews:** <n> with <respondents>; interviewed by <who>; in <language>; <n> transcripts, <n> notes, <n> recordings; translated by <who, or not translated>
**Read by:** <who; whether a second reader charted any rows; whether a reader knows the interview language>
**Hypotheses:** H1 <hypothesis> [<COM-B component / TDF domain>]; H2 <...>

## Matrix

| Respondent | Group | H1 <label> | H2 <label> | Not predicted |
|---|---|---|---|---|
| R01 | <group> | <summary in their terms> (R01, <ref>) [<supports / contradicts / mixed / asked, said nothing / not asked>] | <...> | <...> |

† = the cell rests on notes or translation, not a transcript.

## Verdicts

### H1 <hypothesis>: <supported / not supported / mixed / not tested>
- **Interviews:** <n> support, <n> contradict, <n> mixed, <n> asked and said nothing, <n> not asked (of <N>)
- **By group:** <how the pattern differs between groups, or "no difference seen">
- **Conflicting accounts:** <who said what, or "none">
- **Held strongly:** <who, and the words that show it, or "none">
- **Quotes:** "<quote>" (R0x); "<quote>" (R0y)
- **Goes against it:** <every such respondent and what they said, or "none">

## Not predicted, and outliers
- <topic or person>: <how many interviews; quote reference>

## Against other evidence
- <H# or topic>: <the other source>; <agrees / disagrees / none available>

## Confirmed barriers
- <barrier> [<COM-B component / TDF domain>]: <the evidence in one sentence>
- **Open:** <hypothesis>: <what would settle it>

## What to check before relying on this
- <the verdict the decision depends on most, and how thin its evidence is>
- <the cells most likely to have lost meaning in notes or translation>
```

## Where it goes wrong

- **Counts read as prevalence.** "Nine of twelve farmers" describes the people the team chose to interview. Never turn a count into a percentage; a difference between groups is a lead, not a rate.
- **The vivid interview.** One dramatic story outweighs the rest of the column. The column decides; the quote illustrates.
- **Notes read as words.** An interviewer's English summary of a Chichewa answer is already an interpretation; a quote from it is a paraphrase.

## When to bring in a specialist

Tell the user to consult an experienced qualitative researcher who reads the interview language, and where relevant the organization's safeguarding lead, when:
- Nobody on the team reads the interview language, so no cell can be checked against the words
- An interview disclosed harm (violence, abuse, a child at risk, a crime): the safeguarding response comes before analysis
- The verdict the decision rests on is mixed or rests on a few interviews, and the decision is costly to reverse

Bring them: the hypotheses, the guide, and the matrix with its quote references.
