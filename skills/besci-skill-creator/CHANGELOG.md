# Changelog

## 0.3.0 - 2026-11-11
Follows the conversational-voice standard (ADR 0009) when drafting a skill: a plain lead-in, plain labels, and a "Where you could go from here" closing in every output template; asks what people do next so the last step of "How to do it" lists next moves with their conditions; copies the shared voice-block markers. Bundles the updated spec, template, and validator. Edited with Claude.

## 0.2.0 - 2026-11-10
Follows the November 2026 skill standard: asks for the "what this adds" line, runs the evidence scan and sets `tested_in`, checks every citation and leaves out what cannot be checked, drafts four named test cases with assertions, and writes `references/worked-example.md` and `references/evidence.md`. Edited with Claude.

## 0.1.1 - 2026-10-13
Trigger examples and one eval prompt use the repository's new name, `besci-skills`. No change to behavior.

## 0.1.0 - 2026-10-08
First version. Fourteen-phase interview against docs/skill-spec.md, bundled validator and packager, manual checklist for environments without code execution, one self-test pass. Five evals. Not yet reviewed.
