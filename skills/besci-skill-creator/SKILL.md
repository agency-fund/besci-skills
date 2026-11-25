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
  version: "0.5.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  tested_in: not-applicable
  tags: "meta, authoring, interview"
  produces: "skill-draft"
---

Grills an author about a behavioral-science method, then drafts a skill folder that meets the library's standard.

Interview the author relentlessly about every aspect of their method until you reach a shared understanding. Walk down each branch of the design tree, resolving dependencies between decisions one by one. The root is the four gates in section 1 of `references/skill-spec.md`: the skill does **one thing**, the task is **common**, it **adds something**, and it is **distinct** from every skill in the catalog.

Ask the questions one at a time, waiting for the author's answer to each before asking the next. Asking multiple questions at once is bewildering. A reply holds one question and nothing after it.

Format a question like so:

```
❓ **<question title>**: <question body, including the choices when there are some>

➡️ <your recommended answer>
```

For each question that is a decision, give your recommended answer. A question about the author's own experience of the method (where it goes wrong, what a good result looks like) has no recommended answer: ask it plainly, leave the ➡️ line out, and do not guess. Ask about the method in the author's terms, not about the spec's sections; `references/interview-guide.md` has questions that work.

If a _fact_ can be found in the environment (the sources list, the catalog, a citation, a file they shared, etc.), look it up rather than asking the author, and say what you found. The _decisions_ are the author's: put each one to them and wait for the answer.

Do not draft until the author confirms you have reached a shared understanding. Then follow `references/drafting.md`.
