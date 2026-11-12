# Changelog

## 0.3.0 - 2026-11-11
Follows the conversational-voice standard (ADR 0009). The output opens with a few plain sentences to the user (what the message says and the figure behind it, or why none should be sent; the belief it corrects; and that wide use waits on the checks), is titled "Telling <the audience> what most of their peers do or approve of" instead of "Social norm message", and "Rule applied" becomes "Rule for these figures". The output ends with next moves and their reasons, chosen from candidates listed in the closing, and the skill carries the shared voice block. The method is unchanged. Edited with Claude.

## 0.2.0 - 2026-11-11
Rewritten to the November 2026 standard, at a little over half its earlier length. The evidence was rechecked against the sources: the Peru property-tax trial is now cited from its working paper, the claim that a line of approval is what prevents backfire is narrowed to the one study that showed it, and the discounted planning number is gone. The skill now allows a message about what most people approve of when fewer than half do the behavior, and sends individual comparison reports to `design-feedback-report`. Rewritten with Claude.

## 0.1.0 - 2026-10-12
First draft. Drafted with Claude from the verified evidence dossier (`docs/plan/2026-10-skill-expansion-dossier.md`) for Zezhen Wu's review; four evals; not yet reviewed.
