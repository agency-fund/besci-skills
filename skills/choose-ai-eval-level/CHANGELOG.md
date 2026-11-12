# Changelog

## 0.3.0 - 2026-11-11
Follows the conversational-voice standard (ADR 0009). The recommendation now opens with a few plain sentences to the user: the evaluation to run now, the evidence or gap that decided it, and whether the trial someone asked for is premature. Its labels were already plain and are unchanged, and it had no directive closing line. The output ends with next moves and their reasons, chosen from candidates listed in the closing, and the skill carries the shared voice block. The method is unchanged. Edited with Claude.

## 0.2.0 - 2026-11-11
Rewritten to the November 2026 standard, at under half its earlier length. The skill now carries the playbook's main idea, that evaluation is staged, and gives one recommendation on what to evaluate now and what is premature; it no longer depends on the four other AI-evaluation skills, which were removed. The four questions are quoted from the playbook's current edition, the conditions for an impact evaluation follow that edition (strong evidence at the first three stages, a scale-up under consideration, and capacity to work with independent researchers), and the IDinsight interviews are now cited from their source. Zezhen Wu added as co-author. Rewritten with Claude.

## 0.1.0 - 2026-10-08
Ported from Joe Speed's prototype (joe-speed/behavioural-skills, `ai-eval-level-matcher` v0.1.1, commit 68257d1) by Zezhen Wu on Joe's behalf. Restructured to this library's eight sections: added Before you start, How to do it, When to bring in a specialist, a replication note, and four evals; the worked example moved to `references/worked-example.md`; American spelling. Method content is the original author's. Not yet reviewed.
