---
status: proposed
date: 2026-11-24
---
# The `other` stage holds supporting skills

Several skills end in a written report, and each was left to choose its own prose register. The first skill that needed a shared answer was `analyze-qualitative-themes`, whose report is meant to be read as research writing. A writing skill is not a behavioral-science method. It is a named step in none of the canonical sources, so it fails the first inclusion test, and it belongs to no stage of a project. Until now the `other` stage was a place to park a skill that fit nowhere: the validator warned on it, and the site filed anything in it under "Meta-skills".

**`other` is the stage for supporting skills.** A supporting skill is not a behavioral-science method. It does a job that the outputs of many skills share, such as writing. The first is `write-in-academic-voice`, which skills that produce a report can name. Meta-skills also declare `other`, as before; they are told apart by `type: meta`.

**A supporting skill skips the "common" test only.** It still states what it adds, and it is distinct: no other skill produces the same output template. It follows the eight sections and the four test cases, and it carries both reference files. `tested_in` is `not-applicable` unless the skill makes a claim about how people behave, in which case the evidence scan applies. "What it draws on" says whose practice the skill encodes.

**Each supporting skill is listed in `docs/canonical-sources.md`**, under "Supporting skills", with the reason the library carries it. The list is what keeps the stage from becoming a place for anything that fails the first test. Adding a row is a change to that page, so it needs agreement from maintainers of both organizations, like any other change to it.

**The validator checks the list.** W013 used to fire on every atomic skill in `other`. It now fires only when the skill is not named under "Supporting skills". A bundled copy of the validator, which cannot see the page, stays silent.

**The site shows them as their own group.** The catalog, the map, and the workflow builder show "Other" as a group after the seven stages, separate from "Meta-skills". The home page's stage chart keeps the seven stages, because a supporting skill is not a point in a project.

**Consequences.** `taxonomy.yaml` describes `other` as the stage for supporting skills. The spec (section 1 and the `metadata.stage` row), `docs/taxonomy.md`, `CONTEXT.md`, the skill-creator's checklist, and the navigator's stage file say the same. A supporting skill can be named in another skill's closing, or in its procedure, like any library skill; the rule that a named skill must exist (E056) covers it. This widens what the library carries beyond behavioral-science methods, so it needs agreement from maintainers of both organizations before it is accepted.
