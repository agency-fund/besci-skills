# Changelog

## 0.3.0 - 2026-11-11
Follows the conversational-voice standard (ADR 0009). The output opens with a few plain sentences to the user (the effect to plan on, the correction that moved the numbers most, and how it compares with the published figure) and is titled "What effect to plan for" instead of "Effect-size benchmark". "Estimates read" is "The estimates, as read", the "Label" column is "Kind of estimate", and selective publication, take-up, and SD are glossed where they appear. The output ends with next moves and their reasons, chosen from candidates listed in the closing, and the skill carries the shared voice block. The method is unchanged. Edited with Claude.

## 0.2.0 - 2026-11-11
Rewritten to the November 2026 standard. The skill now reads the studies it is given under the shared citation rules, labels each estimate by how it was selected, and sets the low end from unselected results or at one sixth of the high end, the ratio in DellaVigna and Linos (2022); the bias-adjusted nudge figures were corrected against Maier et al. and Szaszi et al., and the laboratory-to-field gap is now attributed as Ferraro and Tracy do. `tested_in` comes from a new scan that found the same direction in low- and middle-income settings. Rewritten with Claude.

## 0.1.0 - 2026-10-12
First draft. Drafted with Claude from the verified evidence dossier (`docs/plan/2026-10-skill-expansion-dossier.md`) for Zezhen Wu's review; four evals; not yet reviewed.
