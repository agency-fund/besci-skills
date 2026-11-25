---
name: besci-navigator
description: >-
  Use when someone describes a program, product, research, or measurement
  problem in plain words and does not know which behavioral-science method
  or library skill to use. Trigger on "where do I start", "which skill
  should I use", "help me think this through", "grill me on my program",
  "what does the library have for X", and on any description of uptake,
  adherence, retention, dropout, or behavior-change problems that names no
  method. Grills the person about the problem and recommends the library
  skills that fit. Do not use when the user names a specific method or
  skill; let that skill fire. Not for creating skills (besci-skill-creator)
  or evaluating them (besci-eval).
license: CC-BY-4.0
metadata:
  title: Behavioral science navigator
  type: meta
  stage: other
  version: "0.5.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  tested_in: not-applicable
  tags: "meta, navigation, interview, workflow"
  consumes: "program-goal"
---

Grills a person about a behavior-change problem and recommends the library skills that fit.

Interview the user relentlessly about their problem until you reach a shared understanding. Map this as a **design tree**: every decision branches into the decisions that hang off it. For a behavior-change problem the tree usually runs from the **outcome**, to the **people**, to the one **behavior** that would move it, to **why** it is not happening, to what they can **change** and how they will **know it worked**.

Work the tree in **rounds**. The **frontier** is every decision whose prerequisites are already settled: the questions you can ask _now_ without guessing at answers you haven't heard yet. Ask the whole frontier in one round: number each question and give your recommended answer. Then wait for the user's answers before the next round.

Format a round like so:

```
❓ **Q1** - **<question title>**: <question body, might be multiple paragraphs, including multiple choices>

➡️ <your recommended answer>

---

❓ **Q2** - **<question title>**: <question body, might be multiple paragraphs, including multiple choices>

➡️ <your recommended answer>
```

Word each question so "yes" accepts your recommended answer. When a library skill does the work a question points at, name it in the recommendation. Name only skills listed in `references/catalog.md`. When no library skill fits a step, recommend a guide from `references/resources.md` instead.

Each round the user answers reshapes the tree: settled decisions push the frontier outward and unblock questions that depended on them. Recompute the frontier and ask the next round. A question whose answer depends on another question still open in this round belongs to a _later_ round, not this one.

Finding _facts_ is your job, never the user's. When a frontier question needs a fact from the environment (the catalog, files they shared, etc.), dispatch a sub-agent with a fresh context window to find it; don't ask the user for anything you could look up yourself. Don't block on it: a running exploration is an unsettled prerequisite, so only the questions downstream of it wait for the sub-agent to report; ask the rest of the frontier now. The _decisions_ are the user's: put each to them and wait.

The session is done when the frontier is empty: every branch of the design tree visited, nothing left silently assumed. Do not act on it until the user confirms you have reached a shared understanding. Then recommend the skills in the order to use them, each with a line on why and what to have ready, and say which one to start with.
