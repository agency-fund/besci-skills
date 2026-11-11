# Changelog

## 0.2.0 - 2026-11-10
Rewritten to the November 2026 standard. Addresses expert review #14 (Kelly Zhang): the skill now reads the study and takes the estimate from its results, says when it read only the abstract, and answers "No evidence to assess" with the nearest related studies when no study tests the claim; a fifth test case reproduces the failure. The assessment follows Bates and Glennerster's four generalizability questions. The discounted effect range is gone; a planning number is the job of `estimate-expected-effect`. Rewritten with Claude.

## 0.1.0 - 2026-10-12
First draft. Drafted with Claude from the verified evidence dossier (`docs/plan/2026-10-skill-expansion-dossier.md`) for Zezhen Wu's review; four evals; not yet reviewed.
