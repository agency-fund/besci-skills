# Worked example: revising a paragraph on AI-assisted writing

A full run of the skill on a realistic case, showing the output it should produce. The case is illustrative, not a real program.

## The request

"Can you revise this paragraph from my introduction? It reads like a chatbot wrote it. It's for a psychology journal.

'Importantly, the rapid proliferation of large language models has fundamentally transformed the landscape of scientific writing. Kobak et al. (2025) delve into more than 15 million PubMed abstracts and showcase that at least 13.5% of 2024 abstracts were processed with LLMs, a pivotal finding that underscores the profound impact of these tools. Not only does this trend extend to peer review, but Liang et al. (2024) also found that between 6.5% and 16.9% of review text at AI conferences could have been substantially modified by LLMs. Taken together, these studies provide compelling evidence that AI is revolutionizing how researchers write, and it remains to be seen how the field will navigate these complexities.'"

## The output

```markdown
I revised the paragraph and kept both citations and all four numbers where they were. The change that matters most is the last sentence: the two studies estimate how much text was processed with a language model, and neither shows a change in how researchers write, so I cut that claim back to what they report and listed it below.

# Introduction, paragraph on AI-assisted writing

**Task:** revised
**Written for:** a psychology journal; APA 7th edition and American spelling assumed

## The text
Large language models are now used in a measurable share of scientific writing. Kobak et al. (2025) analyzed more than 15 million PubMed abstracts and estimated that at least 13.5% of those from 2024 had been processed with a large language model. Peer review shows a similar pattern. Liang et al. (2024) estimated that between 6.5% and 16.9% of the text of reviews submitted to AI conferences could have been substantially modified by one. Neither study establishes what this use has changed about how researchers write.

## What changed
- Inflated vocabulary replaced with plain verbs: "delve into ... and showcase that" became "analyzed ... and estimated that"
- Openers and closers that made no claim were cut: "Importantly," "Taken together," and "it remains to be seen how the field will navigate these complexities"
- A "not only ... but also" pivot became two direct sentences: "Peer review shows a similar pattern. Liang et al. (2024) estimated ..."
- Emphasis the evidence does not carry was removed: "a pivotal finding that underscores the profound impact of these tools"
- One claim was cut back: "has fundamentally transformed the landscape of scientific writing" became "are now used in a measurable share of scientific writing"

## Claims that still need a source
- "AI is revolutionizing how researchers write": neither cited study measures a change in writing practice. A study of how authors use these tools, or of how texts changed beyond word choice, would support a version of it. The revision says only that the two studies do not establish it.

## What to check before relying on this
- "Estimated" replaces "showcase that" and "found that". Both papers report estimates from word frequencies, but compare the verbs with how each paper states its result.
- "AI conferences" is kept from your draft. Name the conferences if the journal's readers will not know which are meant.

## Where you could go from here
The paragraph is done.
- I would lean toward comparing the two verbs with the papers themselves, because "estimated" is a claim about their method and it takes five minutes.
- `assess-evidence-base` would fit if you want to keep a claim about changed writing practice and need to know whether any study supports it.
- `draft-sifa-declaration` would fit before submission, since the journal may ask how AI was used in preparing the manuscript.
Questions you could ask next: "Which of my other paragraphs make claims the citations do not carry?" · "Can you match the voice of my methods section?"
```
