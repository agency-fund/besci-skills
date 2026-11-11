---
name: draft-tdf-interview-guide
description: >-
  Use when one behavior is defined, the team has hypotheses about why it is
  not happening, and it needs the questions to ask people in interviews to
  find out which are real, or when someone says "let's do a few interviews"
  with no plan for what to ask. Writes a guide of open questions in which
  each one tests a hypothesis or opens an area the team has not considered.
  Do not use when no hypotheses exist yet; use decompose-comb-barriers. Not
  for checking whether survey questions are understood; use
  draft-cognitive-interview-script.
license: CC-BY-4.0
metadata:
  title: Write an interview guide that tests barrier hypotheses
  type: atomic
  stage: diagnose
  version: "0.2.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  tested_in: beyond-western-holds
  tags: "tdf, com-b, qualitative, diagnosis"
  consumes: "target-behavior-brief, comb-barrier-hypotheses"
  produces: "interview-guide"
---

## What it does

Writes an interview guide of open questions that tests a team's hypotheses about why one behavior is not happening.

**What this adds:** labels every question with the hypothesis it tests and its domain in the Theoretical Domains Framework; gives each domain with no hypothesis one open question, so the interviews can find what the team did not suspect; orders questions as a conversation, not by domain; rejects any question or probe that names the barrier it looks for; and ends with a map of questions to hypotheses.

The Theoretical Domains Framework (TDF) sorts the influences on behavior into 14 domains, such as Knowledge, Social influences, and Emotion.

## When to use it

### Use it when
- A behavior is defined, the team has hypotheses about why it is not happening, and the next step is to ask people
- Someone says "let's do a few interviews" or "what should we ask them?" with no plan for the conversation
- An existing guide asks only about knowledge and attitudes

### Do not use it when
- No hypotheses exist and the question is still "why aren't they doing it?"; use `decompose-comb-barriers`
- The interviews are to check whether draft survey questions are understood; use `draft-cognitive-interview-script`
- The interviews are done and the transcripts need analysis; use `synthesize-interview-findings`

## Before you start

Ask these before producing anything. Do not ask anything the user has already answered.

1. **Required.** The behavior: who does what, when, and where.
2. **Required.** The hypotheses to test: the reasons the team thinks the behavior is not happening, from a diagnosis or from its own guesses.
3. **Required.** Who will be interviewed, by whom, in what language, and for how long.
4. Optional. Local terms: what the behavior is called, and whose opinion matters to respondents.

If 1 or 2 is missing, ask and stop. If 3 is missing, assume 45 minutes with the people who should do the behavior, in their first language, and say so.

## What it draws on

- Atkins, L., Francis, J., Islam, R., et al. (2017). A guide to using the Theoretical Domains Framework of behaviour change to investigate implementation problems. *Implementation Science*, 12, 77. https://doi.org/10.1186/s13012-017-0605-9 Supports: the procedure: an open question with follow-up prompts for each domain, a flexible order, a pilot.
- Cane, J., O'Connor, D., & Michie, S. (2012). Validation of the theoretical domains framework for use in behaviour change and implementation research. *Implementation Science*, 7, 37. https://doi.org/10.1186/1748-5908-7-37 Supports: the 14 domains and their mapping to capability, opportunity, and motivation.
- McGowan, L. J., Powell, R., & French, D. P. (2020). How can use of the Theoretical Domains Framework be optimized in qualitative research? A rapid systematic review. *British Journal of Health Psychology*, 25(3), 677–694. https://doi.org/10.1111/bjhp.12437 Supports: step 6. Most of the reviewed studies with patients or the public reported nothing outside the framework.

**Where the evidence comes from:** The experts who validated the framework were mostly in the United Kingdom and the Netherlands. It has since guided interviews with health workers in Kenya, Nigeria, and South Africa and with parents in India, where answers fell in most domains; a study of knowledge brokers from 56 countries had to add codes for influences beyond the organization. Ask locally whose opinion matters to respondents.

**Replication status:** Single-study for the 14 domains, an expert sorting task. In a second study, judges could tell 11 of the 14 apart; Reinforcement, Goals, and Behavioral regulation blurred.

## How to do it

1. **Write the behavior at the top** as who does what, when, where, with or to whom; mark a missing part "[to confirm]".
2. **Assign each hypothesis to the domain that holds it**, using `references/tdf-domains.md`. Give a hypothesis that fits two domains both labels.
3. **Write the opening:** the purpose in plain words, a placeholder for the team's approved consent script, a warm-up question, then a question that reconstructs the last time the behavior was due. A specific day brings out the setting, other people, and habit; opinions do not.
4. **Write two or three questions for each hypothesis and one for each domain that has none.** Each is open, asks one thing, is about the behavior, and does not name the barrier it looks for. Label each with its domain and "tests H1" or "discovery".
5. **Add one or two probes to each question:** an example, what happened next, who else was involved. A probe never suggests a reason.
6. **Add one open question that belongs to no domain**; a guide built from a framework finds only what the framework names.
7. **Order the questions as a conversation:** broad before personal, sensitive ones in the middle, grouped by topic, not by domain.
8. **Bracket every local term the user has not supplied** and every word that may not translate ("goal", "plan", "confident").
9. **Fit the length** by cutting discovery questions first, starting with Reinforcement, Goals, and Behavioral regulation.
10. **Fill the map** and recommend a pilot with two respondents.

See `references/worked-example.md` for a complete run.

## Output template

```markdown
# Interview guide: <short name of the behavior>

**Behavior:** <who does what, when, where, with or to whom>
**Respondents:** <who> | **Interviewer:** <who> | **Length:** <minutes> | **Language:** <...>
**Hypotheses under test:** H1 <...> (<from a diagnosis / team guess>); H2 <...>

## Opening (about <n> minutes)
- **Purpose, in plain words:** "<...>"
- [CONSENT: insert the team's approved consent script here; do not start without it]
- **Warm-up:** "<an easy question about the respondent's day or work>"
- **Reconstruction:** "Think about the last time you <were due to do the behavior>. Tell me what happened that day."

## Questions, in running order
### <topic block>
1. "<open question>" [<domain>; tests <H#> / discovery]
   - Probe: "<...>"

### Anything we missed
<n>. "What else gets in the way, or helps, that we have not asked about?" [no domain; discovery]

## Closing (about <n> minutes)
- "If one thing changed to make this easier, what would it be?"
- Thanks; what happens next with what they said.

## Map of hypotheses to questions

| Domain | COM-B component | Tests | Questions |
|---|---|---|---|
| Knowledge | Capability, psychological | <H# / discovery> | <numbers> |
| Skills | Capability, psychological or physical | | |
| Memory, attention and decision processes | Capability, psychological | | |
| Behavioral regulation | Capability, psychological | | |
| Environmental context and resources | Opportunity, physical | | |
| Social influences | Opportunity, social | | |
| Social or professional role and identity | Motivation, reflective or automatic | | |
| Beliefs about capabilities | Motivation, reflective | | |
| Optimism | Motivation, reflective or automatic | | |
| Beliefs about consequences | Motivation, reflective | | |
| Intentions | Motivation, reflective | | |
| Goals | Motivation, reflective | | |
| Reinforcement | Motivation, automatic | | |
| Emotion | Motivation, automatic | | |

Outside the framework: question <n>.

## Local terms to fill in
- [<bracketed term>]: <who fills it>
- "<a word that may not translate>": <a plain substitute>

## What to check before relying on this
- Pilot with two respondents; drop any question that draws the same answer whichever hypothesis is true.
- <who should not interview whom>
- <the assumption most likely to be wrong>
```

## Where it goes wrong

- **The interviewer is part of the answer.** A supervisor, mentor, or program officer who asks "what makes this hard?" hears what is safe to say. Say who should not interview whom.
- **Imported wording.** Published TDF questions ask about "your manager", "the guideline", and "your professional role", which mean nothing to parents or farmers.
- **Silence read as a finding.** One question cannot show that a domain does not matter. A domain nobody mentions is "not raised", never "not a barrier".

## When to bring in a specialist

Tell the user to consult an experienced qualitative researcher who knows the setting, and the ethics review body, when:
- The topic is stigmatized or carries clinical, legal, or safety risk (sexual health, violence, substance use, household authority): questions and consent need review before anyone is interviewed
- Respondents are children, or the interviews are in a language or community nobody on the team knows
- Nobody can say how the transcripts will be analyzed

Bring them: the hypotheses, the draft guide, and the plan for who interviews whom.
