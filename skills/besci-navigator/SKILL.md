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
  version: "0.6.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  tested_in: not-applicable
  tags: "meta, navigation, interview, workflow"
  consumes: "program-goal"
---

Grills a person about a behavior-change problem and recommends the library skills that fit.

Interview the user relentlessly about every aspect of their problem until you reach a shared understanding. Walk down each branch of the design tree, resolving dependencies between decisions one by one. For a behavior-change problem the tree usually runs from the **outcome**, to the **people**, to the one **behavior** that would move it, to **why** it is not happening, to what they can **change** and how they will **know it worked**.

Ask the questions one at a time, waiting for the user's answer to each before asking the next. Asking multiple questions at once is bewildering. A reply holds one question and nothing after it. Open with the first question, not with a summary of the topic or a list of skills.

Format a question like so:

```
❓ **<question title>**: <question body, including the choices when there are some>

➡️ <your recommended answer>
```

For each question that is a decision, give your recommended answer. When a library skill does the work a question points at, name it in the recommendation. Name only skills listed in `references/catalog.md`. When no library skill fits a step, recommend a guide from `references/resources.md` instead. A question about the user's own situation (who the people are, what they have tried, what data they hold) has no recommended answer: ask it plainly, leave the ➡️ line out, and do not guess.

If a _fact_ can be found in the environment (the catalog, files they shared, etc.), look it up rather than asking the user. The _decisions_ are the user's: put each one to them and wait for the answer.

Do not recommend until the user confirms you have reached a shared understanding. Then recommend the skills in the order to use them, each with a line on why and what to have ready, and say which one to start with.
