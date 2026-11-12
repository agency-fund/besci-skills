# Changelog

## 0.3.0 - 2026-11-11
Follows the conversational-voice standard (ADR 0009). The output opens with a few plain sentences to the user and uses plain labels: "possible reason" for hypothesis, "still a barrier with full information, full access, and no social cost?" for the persistence test, "how the answer tells it apart" for "discriminates because", and each COM-B part glossed ("Capability: can they do it?"). "Check first" becomes "Where I'd start", still provisional. The output ends with next moves and their reasons, chosen from candidates listed in the closing, and the skill carries the shared voice block. The method is unchanged. Edited with Claude.

## 0.2.0 - 2026-11-11
Rewritten to the November 2026 standard, about 35% shorter. The method is unchanged in substance: six sub-components, the persistence test, a "discriminates because" line for every question, and a ranking that stays provisional; the optional bias-audit input is now any belief the team states, marked "team belief". The evidence was rechecked against the sources and a scan of use outside wealthy Western countries was added. Zezhen Wu added as co-author. Rewritten with Claude.

## 0.1.0 - 2026-10-08
Ported from Joe Speed's prototype (joe-speed/behavioural-skills, `comb-barrier-decomposer` v0.2.1, commit 68257d1) by Zezhen Wu on the authors' behalf. Restructured to this library's eight sections: added Before you start, How to do it, When to bring in a specialist, a replication note, and four evals; the worked example moved to `references/worked-example.md`; American spelling. Method content is the original authors'. Not yet reviewed.
