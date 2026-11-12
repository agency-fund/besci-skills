# Changelog

## 0.3.0 - 2026-11-11
Follows the conversational-voice standard (ADR 0009). The output opens with a few plain sentences to the user (the behavior chosen, the score that decided it, and which scores the audience could overturn), and its title names the behavior to target for the goal in place of "Target behavior brief". "Spillover" becomes "Spillover to other behaviors" and "APEASE concerns" becomes "Concerns about the chosen behavior (APEASE)". The output ends with next moves and their reasons, chosen from candidates listed in the closing, and the skill carries the shared voice block. The method is unchanged. Edited with Claude.

## 0.2.0 - 2026-11-10
Rewritten to the November 2026 standard, and now also does the job of `score-candidate-behaviors`, which is removed: candidates are scored on impact, likelihood of change, spillover, and measurability, each score labeled as data, audience input, or team guess, with APEASE kept as a screen on the selected behavior. Addresses expert review #12 (Temina Madon): the worked example no longer mentions who ported the skill, and code and prompt boxes on the site now wrap. Zezhen Wu added as co-author. Rewritten with Claude.

## 0.1.0 - 2026-10-08
Ported from Joe Speed's prototype (joe-speed/behavioural-skills, `key-behaviour-definer` v0.3.1, commit 68257d1) by Zezhen Wu on the authors' behalf. Restructured to this library's eight sections: added Before you start, How to do it, When to bring in a specialist, a replication note, and four evals; the worked example moved to `references/worked-example.md`; American spelling. Method content is the original authors'. Not yet reviewed.
