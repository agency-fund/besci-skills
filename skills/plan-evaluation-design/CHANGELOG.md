# Changelog

## 0.3.0 - 2026-11-11
Follows the conversational-voice standard (ADR 0009). The plan opens with a few plain sentences to the user (the primary outcome and its source, whose threshold it is, and the open question most likely to undo the plan), is titled "How you will know if <the behavior> changed" instead of "Measurement plan", and glosses "primary outcome" and "proxy" where they appear. The output ends with next moves and their reasons, chosen from candidates listed in the closing, and the skill carries the shared voice block. The method is unchanged. Edited with Claude.

## 0.2.0 - 2026-11-11
Rewritten to the November 2026 standard, with one job: the primary outcome, where its data come from, when it is measured, and the smallest change worth detecting. The comparison condition moved to choose-trial-design and the dated pre-registration of the analysis to write-pre-analysis-plan; data sources are now chosen down the Behavioural Insights Team's order of preference, every feasibility answer names who confirmed it, and each barrier supplied still gets its own intermediate measure. Citations were re-verified, and Olken (2015) moved to write-pre-analysis-plan. Zezhen Wu added as co-author. Rewritten with Claude.

## 0.1.0 - 2026-10-08
Ported from Joe Speed's prototype (joe-speed/behavioural-skills, `evaluation-design-scoper` v0.2.1, commit 68257d1) by Zezhen Wu on Joe's behalf. Restructured to this library's eight sections: added Before you start, How to do it, When to bring in a specialist, a replication note, and four evals; the worked example moved to `references/worked-example.md`; American spelling. Method content is the original author's. Not yet reviewed.
