# Changelog

## 0.3.0 - 2026-11-11
Follows the conversational-voice standard (ADR 0009). The output opens with a few plain sentences to the user (the kind and technique chosen, what decided it, and what must be confirmed before design), is titled "Choosing an intervention for <the barrier>" instead of "Intervention lever brief", and uses plain labels: "the Behaviour Change Wheel's table" for "the table", "How feasible each one is here (APEASE)" for "Feasibility (APEASE)", "The kind I'd choose, and the technique" for "Selected lever", "Label in the behavior change technique taxonomy" for "Taxonomy label", and "What to confirm before design starts" for "To confirm before design". The output ends with next moves and their reasons, chosen from candidates listed in the closing; drafting content is offered only once what is listed to confirm is in hand. The skill carries the shared voice block. The method is unchanged. Edited with Claude.

## 0.2.0 - 2026-11-11
Rewritten to the November 2026 standard, at about two-thirds of its earlier length. The table linking kinds of barrier to kinds of intervention is now bundled in `references/function-matrix.md`, copied from the 2011 paper, so the skill reads it and no longer rates its own recall of it; the worked example's row for a social-opportunity barrier is corrected to match. A kind with a negative score is not selected unless the change that removes the negative is stated. Zezhen Wu added as co-author. Rewritten with Claude.

## 0.1.0 - 2026-10-08
Ported from Joe Speed's prototype (joe-speed/behavioural-skills, `intervention-lever-selector` v0.2.1, commit 68257d1) by Zezhen Wu on Joe's behalf. Restructured to this library's eight sections: added Before you start, How to do it, When to bring in a specialist, a replication note, and four evals; the worked example moved to `references/worked-example.md`; American spelling. Method content is the original author's. Not yet reviewed.
