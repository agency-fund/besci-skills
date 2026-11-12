# Changelog

## 0.3.0 - 2026-11-11
Follows the conversational-voice standard (ADR 0009). The output opens with a few plain sentences to the user (the prompt, what shows people already intend to act, and that it stays a draft until the pretest), is titled "A prompt to plan when and where" instead of "Implementation intention prompt", and uses plain labels: "If (the time, and where they will be just before)" for "If (time and cue)", "Added to" for "Rides on", and "How the person says it back" for "Said back". The output ends with next moves and their reasons, chosen from candidates listed in the closing, and the skill carries the shared voice block. The method is unchanged. Edited with Claude.

## 0.2.0 - 2026-11-11
Rewritten to the November 2026 standard, at well under half its earlier length. The evidence was rechecked against the sources: a 2025 meta-analysis of 642 tests replaces the 2006 one as the main source, the South African self-test trial is now reported with its result (no gain over a clear explanation), and field trials from South Africa, Uganda, and Kenya were added. The prompt is now written as an if-then plan with a time and a place and is said back once, following the meta-analysis; the skill no longer quotes a planning range for the effect or points to skills that have been removed. Rewritten with Claude.

## 0.1.0 - 2026-10-12
First draft. Drafted with Claude from the verified evidence dossier (`docs/plan/2026-10-skill-expansion-dossier.md`) for Zezhen Wu's review; four evals; not yet reviewed.
