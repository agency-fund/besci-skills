# Changelog

## 0.3.0 - 2026-11-11
Follows the conversational-voice standard (ADR 0009). The summary opens with a few plain sentences to the user (what bears most on their goal, the strongest finding against it, and how far the search reached), and its title names the goal in plain words in place of "Evidence scan brief"; the other labels were already plain. The output ends with next moves and their reasons, chosen from candidates listed in the closing, and the skill carries the shared voice block. The method is unchanged. Edited with Claude.

## 0.2.0 - 2026-11-10
Rewritten to the November 2026 standard. Addresses expert review #13 (Kelly Zhang): the skill now opens every source before citing it, marks numbers read from an abstract, and never gives a link it did not open; a fifth test case reproduces the failure. Addresses expert review #16 (Zezhen (Michael) Wu): the skill is a third shorter, states what it adds, asks which search route to use (Paperclip or general web search), no longer rates a search method by where its evidence was tested, explains GRADE where it is cited, and the worked example drops the porting note. Zezhen Wu added as co-author. Rewritten with Claude.

## 0.1.0 - 2026-10-08
Ported from Joe Speed's prototype (joe-speed/behavioural-skills, `evidence-base-scoper` v0.1.1, commit 68257d1) by Zezhen Wu on Joe's behalf. Restructured to this library's eight sections: added Before you start, How to do it, When to bring in a specialist, a replication note, and four evals; the worked example moved to `references/worked-example.md`; American spelling. Method content is Joe's. Not yet reviewed.
