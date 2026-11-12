# Changelog

## 0.3.0 - 2026-11-11
Follows the conversational-voice standard (ADR 0009). The report opens with a few plain sentences (which planned subgroups held up, what the search suggests, and that the rest are hypotheses) under the title "Who benefited most from <the program>", and uses plainer labels: "Subgroups the plan named in advance (confirmatory)", "Other differences the data suggest (exploratory: hypotheses only)", "Did the model find real differences? (best linear predictor)", "Fit on one half, checked on the other", "What this trial was too small to tell (power)", and plain p-value columns. The output ends with next moves and their reasons, chosen from candidates listed in the closing, and the skill carries the shared voice block. The method is unchanged. Edited with Claude.

## 0.2.0 - 2026-11-11
Rewritten to the November 2026 standard and about 40% shorter; it now produces a heterogeneity report. The correction for testing several subgroups is done in the skill (Benjamini-Hochberg, or Bonferroni if the plan says so) instead of being handed elsewhere, and the sources now include the MRC framework and Test, Learn, Adapt on planning subgroups in advance. The citation of the generic machine-learning method gains its issue number, and its application is given as the immunization trial in India only. Rewritten with Claude.

## 0.1.0 - 2026-10-12
First draft. Drafted with Claude from the verified evidence dossier (`docs/plan/2026-10-skill-expansion-dossier.md`) for Zezhen Wu's review; four evals; not yet reviewed.
