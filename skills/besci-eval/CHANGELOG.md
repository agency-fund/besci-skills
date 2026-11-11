# Changelog

## 0.3.0 - 2026-11-11
Adds a ninth rubric criterion, Conversation (ADR 0009): answers what was asked before offering the run, marks the run, says where claims come from, and ends with next moves and their reasons. "Asked first" no longer penalizes a brief answer before the questions. Totals are out of 18; "ready" is a median of 16 or more. Bundles the updated validator and checklist. Edited with Claude.

## 0.2.0 - 2026-11-10
Grades each output against the test case's own assertions as well as the rubric, and adds `--no-skill-baseline`, which runs the same cases with no skill loaded to show what the skill adds. Expects the four named test cases of the November 2026 standard. Edited with Claude.

## 0.1.0 - 2026-10-08
First version. Structure, triggering, and output-quality checks; rubric derived from the eight sections; API runner for cross-model comparison with baseline support. Five evals. Not yet reviewed. The partnership plans to deepen this skill together once real skills exist to evaluate; expert ratings are a later-phase feature.
