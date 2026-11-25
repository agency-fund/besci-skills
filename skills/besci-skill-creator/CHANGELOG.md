# Changelog

## 0.4.0 - 2026-11-25
Rewritten to follow Matt Pocock's grilling skill (https://github.com/mattpocock/skills, MIT license, copyright Matt Pocock) nearly word for word: the skill is mapped as a design tree rooted in the spec's four gates and grilled in rounds of numbered questions, each with a recommended answer. Facts such as the sources list and the catalog are looked up, not asked. Drafting waits until the author confirms a shared understanding; the drafting, revising, and supporting-skill steps move to the new `references/drafting.md`. The fourteen-phase interview, report template, and voice block are gone. Edited with Claude.

## 0.3.3 - 2026-11-24
Wording only: the interview guide and the bundled spec no longer point to decision records that have left the repository. Edited with Claude.

## 0.3.2 - 2026-11-24
Wording only: the metadata phase and the checklist say that the stage `other` is for meta-skills and for supporting skills, which are plain skills the interview and the checklist do not cover. Edited with Claude.

## 0.3.1 - 2026-11-13
Wording only: the pointer for writing a workflow no longer names the navigator's guide mode, which the navigator no longer has. Edited with Claude.

## 0.3.0 - 2026-11-11
Follows the conversational-voice standard when drafting a skill: a plain lead-in, plain labels, and a "Where you could go from here" closing in every output template; asks what people do next so the closing lists candidate next moves with their conditions; copies the shared voice-block markers. Its own report now opens with a few plain sentences, calls "Submit" "How to submit it", ends with next moves, and carries the shared voice block. Bundles the updated spec, template, and validator. Edited with Claude.

## 0.2.0 - 2026-11-10
Follows the November 2026 skill standard: asks for the "what this adds" line, runs the evidence scan and sets `tested_in`, checks every citation and leaves out what cannot be checked, drafts four named test cases with assertions, and writes `references/worked-example.md` and `references/evidence.md`. Edited with Claude.

## 0.1.1 - 2026-10-13
Trigger examples and one eval prompt use the repository's new name, `besci-skills`. No change to behavior.

## 0.1.0 - 2026-10-08
First version. Fourteen-phase interview against docs/skill-spec.md, bundled validator and packager, manual checklist for environments without code execution, one self-test pass. Five evals. Not yet reviewed.
