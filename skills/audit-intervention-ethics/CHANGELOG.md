# Changelog

## 0.3.0 - 2026-11-11
Follows the conversational-voice standard (ADR 0009). A question such as "how do I know if this is ethical?" is answered before the review is offered. The review opens with a few plain sentences (the verdict, what decided it, and that the decision stays with the team), asks its two classifying questions in plain words ("Can people tell they are being influenced?", "Can the least powerful person decline it?"), and names each check by what it asks. It ends with next moves and their reasons, drawn from a new last step, and carries the shared voice block. The method and the verdict rules are unchanged. Edited with Claude.

## 0.2.0 - 2026-11-11
Rewritten to the November 2026 standard, at a little over half its earlier length. The review now starts from the OECD toolkit's two questions (can people tell they are being influenced, and can they avoid it) and its rule for each of the four types, read from the toolkit itself; the six checks and the verdict follow. Sources that were cited without having been read were rechecked: the dark-pattern studies and the notes on shrinking effect sizes are gone, and the rest are marked with how much of each was read. The output is a new type, `ethics-review`. Rewritten with Claude.

## 0.1.0 - 2026-10-12
First draft. Drafted with Claude from the verified evidence dossier (`docs/plan/2026-10-skill-expansion-dossier.md`) for Zezhen Wu's review; four evals; not yet reviewed.
