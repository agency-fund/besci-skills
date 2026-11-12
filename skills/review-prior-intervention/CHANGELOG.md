# Changelog

## 0.3.0 - 2026-11-11
Follows the conversational-voice standard (ADR 0009). The review opens with a few plain sentences (the classification, what decided it, and whether the team's explanation holds) under the title "Did <the program> fail because of the idea or the delivery?"; each delivery line asks its question ("Fidelity: delivered as designed?"), "Basis" becomes "How we know", "Causal claim check" becomes "Does the team's explanation hold up?", and the four classifications are glossed. "Next steps the evidence leaves open" becomes "Options the evidence leaves open", with the same content. The output ends with next moves and their reasons, chosen from candidates listed in the closing, and the skill carries the shared voice block. The method is unchanged. Edited with Claude.

## 0.2.0 - 2026-11-11
Rewritten to the November 2026 standard, keeping Joe Speed's method: what was planned against what was delivered, each finding labeled confirmed or inferred, the check of the team's own explanation, and a fixed classification. Added from the MRC process-evaluation guidance and BIT's project guide: a line on whether people responded as planned, a check on whether a null result was precise enough to rule out a useful effect, "both" as a fourth classification, whether an idea failure lies in the activity or the barrier it targeted, and the next steps the evidence leaves open; the evidence file is new. Zezhen Wu added as co-author. Rewritten with Claude.

## 0.1.0 - 2026-10-08
Ported from Joe Speed's prototype (joe-speed/behavioural-skills, `prior-intervention-post-mortem-reader` v0.2.1, commit 68257d1) by Zezhen Wu on Joe's behalf. Restructured to this library's eight sections: added Before you start, How to do it, When to bring in a specialist, a replication note, and four evals; the worked example moved to `references/worked-example.md`; American spelling. Method content is the original author's. Not yet reviewed.
