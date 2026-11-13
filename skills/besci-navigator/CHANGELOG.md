# Changelog

## 0.3.0 - 2026-11-13
Rebuilt around two modes (ADR 0010). The navigator now opens with a choice: an interview that asks about the program one question at a time, adapted from Matt Pocock's grill-me skill, or suggestions straight away. An interview ends with a short brief ("What we settled", "Still open") and then the recommendation. Conversation is no longer a mode; a plain question is answered first, then the choice is offered. One recommendation template replaces the route and guide templates. Existing workflows are recommended from the catalog snapshot, which now lists them; a workflow file is drafted only on request. The skill text outside the templates is about 30% shorter. Edited with Claude.

## 0.2.0 - 2026-11-11
Conversation is now the default mode (ADR 0009): the navigator answers what was asked as a thought partner, says which parts come from the library and which are general knowledge, and offers a skill only when the person wants to do something. Route and guide replies are written as sentences rather than labeled fields, and end with next moves and their reasons instead of "Next action". Workflow runs say which step the person is on. Carries the shared voice block. Edited with Claude.

## 0.1.2 - 2026-11-10
Wording only: says where a skill's evidence has been tested in plain words, following the renamed `tested_in` field. Edited with Claude.

## 0.1.1 - 2026-10-13
Points the live-catalog fallback at the renamed repository, `agency-fund/besci-skills`. No change to behavior.

## 0.1.0 - 2026-10-08
First version. Route and guide modes, catalog snapshot in references, stage crosswalk, specialist check, workflow-draft output. Five evals. Not yet reviewed. An agency-centered variant is planned for a later version.
