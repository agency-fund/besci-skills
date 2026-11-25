---
name: besci-skill-creator
description: >-
  Use when someone wants to create a new skill for the Behavioral Science
  Skills Library, turn a method, framework, paper, playbook, or checklist
  into a skill, revise an existing library skill, or check a draft skill
  against the library's spec. Trigger on "create a besci skill", "turn this
  method into a skill", "write a SKILL.md for the behavioral science
  library", "contribute a skill", "is my skill atomic", "check my skill
  draft", "revise this skill". Grills the author about the method, then
  drafts the skill folder to the library's standard. Do not use for skills
  outside this library (Anthropic's skill-creator handles general skills).
  Not for evaluating a finished skill (besci-eval) or for finding which
  skill to use (besci-navigator).
license: CC-BY-4.0
metadata:
  title: Behavioral science skill creator
  type: meta
  stage: other
  version: "0.4.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  tested_in: not-applicable
  tags: "meta, authoring, interview"
  produces: "skill-draft"
---

Grills an author about a behavioral-science method, then drafts a skill folder that meets the library's standard.

Interview the author relentlessly about their method until you reach a shared understanding. Map this as a **design tree**: every decision branches into the decisions that hang off it. The root is the four gates in section 1 of `references/skill-spec.md`: the skill does **one thing**, the task is **common**, it **adds something**, and it is **distinct** from every skill in the catalog.

Work the tree in **rounds**. The **frontier** is every decision whose prerequisites are already settled: the questions you can ask _now_ without guessing at answers you haven't heard yet. Ask the whole frontier in one round: number each question and give your recommended answer. Then wait for the user's answers before the next round.

Format a round like so:

```
❓ **Q1** - **<question title>**: <question body, might be multiple paragraphs, including multiple choices>

➡️ <your recommended answer>

---

❓ **Q2** - **<question title>**: <question body, might be multiple paragraphs, including multiple choices>

➡️ <your recommended answer>
```

Word each question so "yes" accepts your recommended answer. Ask about the method in the author's terms, not about the spec's sections; `references/interview-guide.md` has questions that work.

Each round the user answers reshapes the tree: settled decisions push the frontier outward and unblock questions that depended on them. Recompute the frontier and ask the next round. A question whose answer depends on another question still open in this round belongs to a _later_ round, not this one.

Finding _facts_ is your job, never the user's. When a frontier question needs a fact from the environment (the sources list, the catalog, a citation, a file they shared, etc.), dispatch a sub-agent with a fresh context window to find it; don't ask the user for anything you could look up yourself. Don't block on it: a running exploration is an unsettled prerequisite, so only the questions downstream of it wait for the sub-agent to report; ask the rest of the frontier now. The _decisions_ are the user's: put each to them and wait.

The session is done when the frontier is empty: every branch of the design tree visited, nothing left silently assumed. Do not act on it until the user confirms you have reached a shared understanding. Then follow `references/drafting.md`.
