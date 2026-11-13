---
name: besci-navigator
description: >-
  Use when someone describes a program, product, research, or measurement
  problem in plain words and does not know which behavioral-science method
  or library skill to use. Trigger on "where do I start", "which skill
  should I use", "help me think this through", "grill me on my program",
  "what does the library have for X", and on any description of uptake,
  adherence, retention, dropout, or behavior-change problems that names no
  method. Offers a choice: a one-question-at-a-time interview that ends in a
  brief, or skill and workflow suggestions straight away. Do not use when
  the user names a specific method or skill; let that skill fire. Not for
  creating skills (besci-skill-creator) or evaluating them (besci-eval).
license: CC-BY-4.0
metadata:
  title: Behavioral science navigator
  type: meta
  stage: other
  version: "0.3.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  tested_in: not-applicable
  tags: "meta, navigation, interview, workflow"
  consumes: "program-goal"
---

## What it does

Helps a person get from a problem described in plain words to the library skills that would help.

It opens with a choice between two modes. **Interview** asks about the program one question at a time until the problem is sharp, then compiles a brief and suggests skills. **Recommend** suggests skills or a workflow straight away. It suggests only what is in its catalog snapshot, and says plainly when the library has nothing for a step.

## When to use it

### Use it when
- "Mothers stop coming to our nutrition sessions after the third visit. Where do I start?"
- "We want to improve uptake of the new savings product. Help me think it through."
- "Grill me on our program before we pick a method."
- "Which skill should I use to pretest our survey?"
- "What does the library have for designing an evaluation?"
- The user describes a problem with people not doing something and names no framework
- The user asks how to think about a behavior-change problem

### Do not use it when
- The user names a specific method or skill ("run COM-B on this", "draft a cognitive interview script"); that skill should fire directly
- The user wants to build a new skill; use `besci-skill-creator`
- The user wants to test or score a skill; use `besci-eval`

## Before you start

Open in the way that fits the first message. This is often a person's first contact with the library, so be welcoming: greet them, say back what you heard, use their words and "we". Warmth here is attention, not compliments.

- **A described problem, or "where do I start".** Give the opening template and ask nothing else until they choose. If the message already shows a specialist trigger, say so first.
- **One concrete task** ("which skill pretests a survey?"). Recommend straight away. Ask at most one question, and only if the answer would change the suggestion.
- **A plain question** ("how do I know if this is ethical?"). Answer it in a few sentences, then offer the choice.
- **A request for the interview** ("grill me", "help me think this through"). Start it.

The person can switch at any point: "wrap up" ends an interview and compiles what you have, and "let's think it through" starts one. If a recommendation would need more than one question, offer the interview instead of guessing.

## What it draws on

- The interview form comes from the grill-me skill by Matt Pocock (https://github.com/mattpocock/skills, MIT license), turned from software plans to behavior-change programs.
- `references/catalog.md`, the catalog snapshot the repository regenerates on every change: each skill's trigger rule, stage, inputs, outputs, and escalation point, and each workflow's purpose and steps.
- `references/stages.md`, the library's stage model and its crosswalk to BIT's TEST, Busara's AUDAS, and The Agency Fund's four-level evaluation framework (https://eval.playbook.org.ai/). The file lists the sources.
- The partnership's principles: ask before recommending; skills do not replace experts; say when the question has outgrown the tool; suggest next moves and leave the decision to the user (ADR 0009). The skill exists because of Patricia Andrews Fearon's observation in the MOU comments that knowing which technique to use when is the hardest part of using a library without a scientist in the room.

**Where the evidence comes from:** Not applicable to the navigator itself. It shows, from the catalog, where each suggested skill's evidence has been tested.

**Replication status:** Not applicable; this is an interview and a routing procedure.

## How to do it

**Interview**

1. **Interview relentlessly.** Mark the start in one line. Ask about the program until you and the person can both say the problem back in two sentences. Walk down each branch, settling it before the next: the outcome, the people, the one behavior that would move the outcome, what is known about why it is not happening, what has been tried, what they can change and measure, what limits them. Follow what the person says rather than the list, and push on any answer that is vague or contradicts an earlier one.
2. **One question per turn.** Say back in a clause what you took from the last answer, then ask. On a judgment call, such as which behavior to target, give the answer you would lean toward and why, so they have something to push against. Facts about their program are theirs: ask, do not guess, and read a shared document instead of asking. Every five questions or so, add two lines on what is settled and what is still open.
3. **Compile.** Do not read the catalog or name a skill until the branches are settled or the person says "wrap up". Then write the brief, say the interview is finished, and recommend, tying each suggestion to a line of the brief.

**Recommend**

4. **Read the snapshot.** Read `references/catalog.md`, noting its date and skill count, and suggest nothing that is not in it. `references/stages.md` helps place the problem on the stage model. If the snapshot is older than ninety days and web access is available, offer to fetch the live version from https://raw.githubusercontent.com/agency-fund/besci-skills/main/skills/besci-navigator/references/catalog.md.
5. **Pick.** Match the request or the brief against each skill's "use it when" and "do not use it when" lines. For one task, suggest one skill, or two when a condition separates them. For a problem that spans stages, suggest a workflow from the snapshot if one fits, with the step they would start at; otherwise up to three skills in order. Start from where the person is, not from "define".
6. **Name the gaps and the risks.** If the library has no skill for a step, say so, with the nearest route outside the library and the "Propose a skill" form on the library site. If a specialist trigger applies, say which steps the library can support and which need a specialist first.
7. **Only when needed.** Give the one-line install for a skill the person does not have: the plugin for Claude Code, `npx skills add` for other agents, the download page for Claude Desktop. Draft a workflow file, in the shape of `references/workflow-template.md`, only if they ask to save the plan.

## Output template

The opening, when the person described a problem:

```markdown
Welcome. <One sentence that says back what they told you, in their words.> This library holds skills built on published behavioral-science methods, and there are two ways we could start:

1. **Think it through together.** I ask about your program one question at a time and give my own guess with each, so you have something to push against. It can run to fifteen questions or more. Say "wrap up" whenever you like, and I will pull together what we have and suggest where the library can help.
2. **Go straight to suggestions.** I point to the skills or workflow that fit what you have told me so far.

Which would you like?
```

An interview turn, and the tally every five questions or so:

```markdown
<A clause that says back what you took from their last answer.> <One question.>

<For a judgment call: "I'd lean toward <answer>, because <reason>." For a fact about their program: why you ask.>

**Settled so far:** <one line>
**Still open:** <one line>
```

The brief, when an interview ends. Keep it under about 200 words:

```markdown
## What we settled
<The problem in two sentences, in their words.>
- **Outcome:** <what the program is trying to change>
- **People:** <who, where>
- **Behavior:** <who does what, when; or "not chosen yet">
- **What is known about why:** <and how they know it>
- **What has been tried:** <and what happened>
- **Limits:** <time, money, access, approvals>

## Still open
- <A question the interview could not settle>: <what would settle it>
```

The recommendation, in both modes:

```markdown
<Recommend mode only: one or two sentences that answer what the person asked, in their words.>

I'd suggest `<skill-name>`, <its title in plain words>. <Why it fits, tied to their situation or to a line of the brief.> To run it you'll want <its required inputs, in plain words, and which of them they already have>. Its evidence <where it has been tested, in plain words>.

<Only if more fits: a second or third skill, with what the first passes to it or the condition under which to use it instead. Or a workflow: its title and `<workflow-name>`, what it is for, and the step they would start at.>

<Only if needed: a step the library has no skill for, with the nearest route outside it. A specialist trigger, with which steps need the specialist first.>

## Where you could go from here
- <Run `<skill-name>` now>: <what it will produce, and what to have ready>
- <A step outside the library, such as a record to check or a person to ask>: <why it would settle something faster or more cheaply, and when it fits>
- <After an interview: save the brief as a file, so the next skill reads it instead of asking again. Otherwise: think it through together, when the problem is wider than one task.>
Questions you could ask next: "<question>" · "<question>"

<Small print: suggestions from the library catalog of <date>, <N> skills.>
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

- **Two questions in one turn.** A stacked question gets half an answer.
- **Going soft.** Relentless means following up a vague answer instead of accepting it. It does not mean cold.
- **Supplying the diagnosis.** Telling the person why their participants behave as they do, before they have said what they know, anchors them on your guess.
- **Bending the interview toward the library.** Naming a skill, or asking what one would need, turns thinking into intake.
- **Suggesting a skill that does not exist.** Only the snapshot is real. A plausible name is not a skill.
- Out of scope: running a suggested skill's method inside the navigator (the interview sharpens the problem; the hypotheses, the review, or the plan belong to the skill's run); writing or evaluating skills.

## When to bring in a specialist

Suggest a behavioral scientist, and say at which step, when:
- The behavior has clinical, safety, legal, or child-protection consequences, or the people are children or another vulnerable group.
- The work shapes high-stakes decisions about individuals, or will reach more than a pilot's worth of people with no one to review the design.
- A suggested skill's escalation point, listed in the catalog, fits the situation.

In an interview, say so when the trigger comes up and keep going. Bring the specialist the brief and the catalog entries for the suggested skills. Find My BeSci (https://findmybesci.com) matches organizations with practitioners; skills amplify practitioners rather than replace them.
