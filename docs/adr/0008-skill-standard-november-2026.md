---
status: proposed
date: 2026-11-10
---
# Raise the skill standard before launch: an inclusion test, a "what this adds" line, and plain evidence wording

Four expert reviews (#12, #13, #14, #16) and a read of all 71 atomic skills found the same problems across the library: skills that restate what a model does unprompted, wrong or unchecked citations in first-pass output, drafting notes left in the text, evidence notes written from one planning file, and a map whose links nobody chose. The skills were bulk-drafted as placeholders for expert-review practice, and the site has not launched. We change the standard now, before anything can be cited.

**A skill earns its place by three tests.** Its task is a named step or tool in two or more sources in `docs/canonical-sources.md`; one line can state what it makes the AI do that it would not do unprompted; and no other skill produces the same output template. The library also carries a few frameworks by choice (wise interventions, The Agency Fund's agency framework and AI evaluation playbook, Busara's SIFA); skills built on them skip the first test only.

**Every atomic skill shows its value and its evidence the same way.**
- "What it does" carries a `**What this adds:**` line.
- "What it draws on" carries `**Where the evidence comes from:**` and `**Replication status:**`. The field `metadata.weird` becomes `metadata.tested_in`, with four plain values set by a fixed evidence scan. The acronym WEIRD stays in the glossary and on the About page only.
- Every source is checked by DOI or by opening the page. What cannot be checked is left out, not flagged.
- `references/worked-example.md` and `references/evidence.md` are required, with fixed headings.
- `evals/evals.json` holds four named cases, each with three to six assertions. A review that reports a failure adds a fifth.
- `SKILL.md` aims for about 1,000 words and the description for about 500 characters.

**Links between skills are suggestions.** `consumes` lists only required inputs and `produces` exactly one output. A skill describes an input by what it is, and names another skill only under "Do not use it when".

**Consequences.** The validator carried the new rules as warnings (W040 to W049) behind one switch, `STRICT_V2`, while the drafts were revised; with every skill rewritten, the switch is on and they are errors. `metadata.weird` is still read, and mapped to the new values, until then. Drafts that fail the tests are removed outright, and `GOVERNANCE.md` now says deprecation applies from the v1 launch. `besci-eval` grades against assertions and can run a case with no skill loaded, which tests the "what this adds" line. This changes the spec and the validator, so it needs agreement from maintainers of both organizations before it is accepted.
