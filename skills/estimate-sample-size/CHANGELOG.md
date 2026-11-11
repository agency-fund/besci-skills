# Changelog

## 0.2.0 - 2026-11-11
Rewritten to the November 2026 standard. The skill still runs `scripts/power_calc.py`, unchanged, for every number; it now passes `--true-effect` as a positive value and keeps the sensitivity grid between rates of 0 and 1, because the script misreports Type S and Type M for a negative effect and does not check the grid's bounds. Sources were re-verified and the uncheckable ones dropped; sub-Saharan African and South Asian ICC compilations now sit beside the US one. Rewritten with Claude.

## 0.1.0 - 2026-10-12
First draft. Drafted with Claude from the verified evidence dossier (`docs/plan/2026-10-skill-expansion-dossier.md`) for Zezhen Wu's review; four evals; not yet reviewed.
