# Changelog

## 0.3.0 - 2026-11-11
Follows the conversational-voice standard (ADR 0009). The assessment opens with a few plain sentences to the user (the verdict, the condition that decided it, and what it means for their number or plan), and its title asks in plain words whether the finding would hold in their setting, in place of "Transferability assessment"; the other labels were already plain. The output ends with next moves and their reasons, chosen from candidates listed in the closing, and the skill carries the shared voice block. The method and the five verdicts are unchanged. Edited with Claude.

## 0.2.0 - 2026-11-10
Rewritten to the November 2026 standard. Addresses expert review #14 (Kelly Zhang): the skill now reads the study and takes the estimate from its results, says when it read only the abstract, and answers "No evidence to assess" with the nearest related studies when no study tests the claim; a fifth test case reproduces the failure. The assessment follows Bates and Glennerster's four generalizability questions. The discounted effect range is gone; a planning number is the job of `estimate-expected-effect`. Rewritten with Claude.

## 0.1.0 - 2026-10-12
First draft. Drafted with Claude from the verified evidence dossier (`docs/plan/2026-10-skill-expansion-dossier.md`) for Zezhen Wu's review; four evals; not yet reviewed.
