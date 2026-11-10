---
# Copy this folder to skills/<your-skill-name>/ and rename it. The folder name
# and the `name` field must match. Delete these comments when done.
# Run: uv run scripts/besci_validate.py skills/<your-skill-name>
name: your-skill-name
description: >-
  Use when <the situation or user intent that should fire this skill, in the
  words a user would use>. Do not use when <the nearest adjacent intent>; use
  <other skill>. Not for <a second thing people confuse this with>.
license: CC-BY-4.0
metadata:
  title: Human-readable title for the catalog
  type: atomic                 # atomic | meta
  stage: diagnose              # define | diagnose | design | measure | test | analyze | implement | other
  version: "0.1.0"
  status: draft
  authors: "Your Name"
  org: TAF                     # TAF | IL | community
  tested_in: mainly-western    # beyond-western-holds | beyond-western-differs | mainly-western | not-applicable
  tags: "framework-name, method-name"
  consumes: ""                 # io_types ids for the inputs the skill cannot run without
  produces: ""                 # exactly one io_types id: the thing the output template is
---

## What it does

One sentence, no "and".

**What this adds:** <what the skill makes the AI do that it would not do unprompted: a fixed output, a required check, a decision rule, verified sources, or a search or script call>

## When to use it

### Use it when
- A user says something like "..."
- A user has <input state> and asks for <operation>
- A team is about to <common mistake this skill prevents>

### Do not use it when
- The user wants <adjacent thing>; use <other skill or resource>
- The input is still <too vague / too far upstream>; use <other skill> first

## Before you start

Ask these before producing anything. Do not ask anything the user has already answered.

1. **Required.** <An input, named by what it is, not by which skill made it.>
2. **Required.** <A question that changes which branch of the method applies.>
3. Optional. <A question that improves the output if known.>

If 1 or 2 is missing, ask and stop. If 3 is missing, assume <default> and say so.

<!-- Or, if the skill does not need to ask:
Not applicable: <one real sentence saying why>.
-->

## What it draws on

- Author, A., & Author, B. (Year). Title. *Venue*. https://doi.org/... Supports: <what it supports in this skill>.
- Author, C. (Year). Title. *Venue*. https://... Supports: <...>.

**Where the evidence comes from:** <Which countries and populations were studied. What was found outside wealthy Western countries. What to check where the user works. Three sentences at most; the detail is in `references/evidence.md`.>

**Replication status:** <Replicated / mixed / contested / single study, in one sentence.>

## How to do it

1. <First step, imperative, with the reason it matters if not obvious.>
2. <Second step.>
3. <Produce the output using the template below. Fill every placeholder or say why it is blank.>

See `references/worked-example.md` for a complete run.

## Output template

```markdown
# <Title of the output>

**Context:** <who, what, when, carried over from the user's answers>

## <Section 1>
- <item>

## <Section 2>
- <item>

## What to check before relying on this
- <the assumption most likely to be wrong>
```

## Where it goes wrong

- <A failure mode the model is prone to with this method, and the instruction that prevents it. Not a repeat of a step above.>
- <An input that breaks the method.>
- <Something the skill must refuse to do.>

## When to bring in a specialist

Tell the user to consult a <kind of specialist> when:
- <concrete condition>
- <concrete condition>

Bring them: <what to prepare so the conversation is efficient>.

<!-- Or:
Not applicable: <one real sentence saying why this narrow technical skill has no judgement call a user could get wrong>.
-->
