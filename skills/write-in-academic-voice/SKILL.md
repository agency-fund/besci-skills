---
name: write-in-academic-voice
description: >-
  Use when someone asks to draft or revise research prose, says "make this
  sound less like AI" or "tighten my discussion section", or wants a report
  from another skill written up for a journal or a funder. Applies a fixed set
  of voice rules, keeps every citation, number, and hedge in place, and lists
  what changed and which claims still lack a source. Do not use when the
  claims themselves need sources found or checked; use assess-evidence-base.
  Not for messages to program participants; use draft-lever-content.
license: CC-BY-4.0
metadata:
  title: Write or revise research prose in a natural academic voice
  type: atomic
  stage: other
  version: "0.1.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  tested_in: not-applicable
  tags: "academic-writing"
  produces: "academic-prose"
---

## What it does

Drafts or revises research prose so it reads as a researcher's own argument.

**What this adds:** applies one fixed rule set in a fixed order of priority (correctness, precision, clarity, voice, style); takes an inventory of every citation, number, quotation, and hedge before writing and checks each is still in place after; never adds a citation or strengthens a claim; and returns the changes by kind and the claims that still lack a source.

This is a supporting skill, not a behavioral-science method. Library skills that end in a written report follow the same rules.

## When to use it

### Use it when
- "Revise this section so it doesn't read like AI wrote it"
- "Tighten my discussion" or "this draft is too wordy and inflated"
- Someone has findings, notes, or an outline and asks for a manuscript or report section drafted from them
- A report from another skill is headed for a journal or a funder and its prose needs another pass

### Do not use it when
- The claims need sources found or checked; use `assess-evidence-base`
- The text is a message, script, or exercise for program participants; use `draft-lever-content`
- The task is to describe an intervention so another team can repeat it; use `draft-intervention-description`

## Before you start

Ask these before writing. Do not ask anything the user has already answered.

1. **Required.** The text to revise, or the material to draft from: findings, notes, an outline, the sources.
2. Optional. Where it will be read: the journal or audience, and any style guide.
3. Optional. How much may change: sentences only, or the order of the argument too.
4. Optional. A sample of the author's own writing, to match.

If 1 is missing, ask and stop. If 2 is missing, assume researchers in the field, APA 7th edition, and American spelling, and say so. If 3 is missing, revise sentences and keep the order of the argument. If 4 is missing, keep whatever voice the text already has.

## What it draws on

- The rules in `references/academic-voice.md` are Zezhen Wu's own revision practice for research manuscripts, adapted for this library. The rules on structure rest on that practice and have not been tested.
- Kobak, D., González-Márquez, R., Horvát, E.-Á., & Lause, J. (2025). Delving into LLM-assisted writing in biomedical publications through excess vocabulary. *Science Advances*, 11(27), eadt3813. https://doi.org/10.1126/sciadv.adt3813 Supports: most of the avoid-list; words such as "delve", "underscore", and "pivotal" rose abruptly in abstracts after language models appeared.
- Liang, W., Izzo, Z., Zhang, Y., Lepp, H., Cao, H., Zhao, X., Chen, L., Ye, H., Liu, S., Huang, Z., McFarland, D. A., & Zou, J. Y. (2024). Monitoring AI-modified content at scale: A case study on the impact of ChatGPT on AI conference peer reviews. *Proceedings of Machine Learning Research*, 235, 29575–29620. https://proceedings.mlr.press/v235/liang24b.html Supports: the rule against inflated adjectives, including "profound" and "pivotal".
- Oppenheimer, D. M. (2006). Consequences of erudite vernacular utilized irrespective of necessity: Problems with using long words needlessly. *Applied Cognitive Psychology*, 20(2), 139–156. https://doi.org/10.1002/acp.1178 Supports: the plain word when it is as precise; readers judged authors of needlessly complex text as less intelligent.

**Where the evidence comes from:** The skill is a procedure for writing. The vocabulary studies cover English-language biomedical abstracts and peer reviews at AI conferences, and they show which words mark machine-processed text, not that readers judge such text worse. Conventions differ by field and by language, so check the target journal's own style.

**Replication status:** Not applicable: the rules are a practitioner's method, and the cited studies each support one part of the word list.

## How to do it

1. **Read `references/academic-voice.md` in full** before writing anything.
2. **Take the inventory.** List every citation with the claim it supports, every number, every quotation, every defined term, and every hedge ("may", "in this sample", "suggests"). When drafting from material, list instead what each planned paragraph rests on.
3. **Write.** Apply the rules in their order of priority. When a rule and precision conflict, precision wins: a technical term stays even if it is on the avoid-list.
4. **Run the last pass** at the end of the rules file.
5. **Check against the inventory.** Each citation is still attached to the same claim, each number is unchanged, each quotation is untouched, and each hedge is still there. Restore what was lost.
6. **Do not add.** No new citation, finding, mechanism, or example. Where the text makes a claim with no source, keep it only as strong as the text supports and list it.
7. **Keep the frame of another skill's report.** Its headings, labels, tables, and quoted extracts stay as they are. Revise only the prose between them.
8. **Report** the changes by kind, one before-and-after example each.

See `references/worked-example.md` for a complete run.

## Output template

```markdown
<Two or three plain sentences to the user: what was drafted or revised, the kind of change that mattered most, and whether any claim was cut back or still needs a source.>

# <Title of the section or document>

**Task:** <revised / drafted from <the material>>
**Written for:** <journal or audience; the style assumed>

## The text
<The prose.>

## What changed
- <kind of change>: "<before>" became "<after>"
- <when drafting: what each paragraph rests on>

## Claims that still need a source
- "<claim>": <what kind of source would support it>
- <or "None">

## What to check before relying on this
- <a sentence whose meaning may have shifted, for the author to compare with the original>
- <a word kept or changed on a guess about whether it is a technical term>

## Where you could go from here
<One line saying the text is done.>
<Two or three next moves that fit what this run found, each with why it would help and when it fits. Candidates:
- a co-author or a colleague in the field reads the new text against the original, when a technical passage was changed
- `assess-evidence-base`, when claims are listed as needing a source
- `draft-sifa-declaration`, when the text will be submitted and the use of AI in writing it has to be stated
- `draft-intervention-description`, when the text describes a program and a reader must be able to repeat it
- the target journal's author guidelines, when house style or a reporting checklist governs the section>
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

- **Hedges removed.** Cutting "may" and "in this sample" makes prose crisp and wrong.
- **Synonyms for a construct.** Rotating "self-efficacy", "confidence", and "belief in one's ability" to avoid repetition turns one construct into three.
- **Over-correction.** Stripping listed words that are technical in the field, or adding flaws to seem human.
- **One finish everywhere.** Revising each sentence to the same polish replaces the author's voice with a generic one.
- **Quotations edited.** Participants' words and quoted sources are data. The rules stop at the quotation mark.
- Out of scope: translating, checking that claims are true, and formatting reference lists.

## When to bring in a specialist

Tell the user to go to a co-author, a subject expert, or the journal's editor when:
- A good revision would need to change what a claim says or how strong it is; that is the authors' call
- The section falls under a reporting guideline or a journal's house style that fixes its wording or order
- The text gives clinical, legal, or safety guidance, where a change of wording changes what people do
- The text is not in English, or belongs to a tradition (legal writing, some humanities) these rules were not written for

Bring them: the original, the revision, and the lists of changes and unsourced claims.
