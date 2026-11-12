# Changelog

## 0.3.0 - 2026-11-11
Follows the conversational-voice standard (ADR 0009). The calculation opens with a few plain sentences to the user (whether the feasible sample can detect the planned effect, the input it moves on most, and what would change the verdict) and is titled "How big the sample must be" instead of "Power calculation". Alpha, power, ICC, attrition, covariate R², and the design effect are glossed in the output; "Individual-level sample per arm" is "Sample per arm before adjustments"; the minimum detectable effect, sensitivity, and Type S and Type M headings say in plain words what they show. The script and every number in the worked example are unchanged. The output ends with next moves and their reasons, chosen from candidates listed in the closing, and the skill carries the shared voice block. The method is unchanged. Edited with Claude.

## 0.2.0 - 2026-11-11
Rewritten to the November 2026 standard. The skill still runs `scripts/power_calc.py`, unchanged, for every number; it now passes `--true-effect` as a positive value and keeps the sensitivity grid between rates of 0 and 1, because the script misreports Type S and Type M for a negative effect and does not check the grid's bounds. Sources were re-verified and the uncheckable ones dropped; sub-Saharan African and South Asian ICC compilations now sit beside the US one. Rewritten with Claude.

## 0.1.0 - 2026-10-12
First draft. Drafted with Claude from the verified evidence dossier (`docs/plan/2026-10-skill-expansion-dossier.md`) for Zezhen Wu's review; four evals; not yet reviewed.
