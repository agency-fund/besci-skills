# Drafting

What to do once the author confirms a shared understanding.

## A new skill

1. **Check every source.** Resolve the DOI or open the page, and confirm author, year, and title. Never write a citation from memory; leave out what you cannot check and tell the author which ones. Run the evidence scan in section 7 of `skill-spec.md`; it sets `tested_in` and fills the evidence file.
2. **Draft the folder** from `../assets/skill-template/`: `SKILL.md` with the eight sections, four named test cases, the changelog, the worked example, and the evidence file. `interview-guide.md` maps what you heard to each section. Keep the author's wording where it is good. Set version `0.1.0` and status `draft`.
3. **Validate.** Run `python scripts/besci_validate.py <skill-folder>` from the skill-creator's folder and fix every error. With no filesystem, walk `checklist.md` and give the files as text blocks.
4. **Show one real output.** Run the "Full run" test case with only the drafted skill, show the author the output, and fix what an expert would object to.
5. **Hand over.** Run `python scripts/package_skill.py <skill-folder>`. Tell the author whether the validator passed, what is still open, and how to submit: the `.skill` file to a maintainer or https://besci-skills.vercel.app/upload/, or a pull request with the folder under `skills/`.

## Revising a skill

Read the skill's folder, changelog, and any open expert review before the first question, and grill on what should change. Change only what the answers call for. Bump the version and write the changelog entry in the same change. When it answers an expert review, the entry cites it ("Addresses expert review #42 (Jane Doe): ..."), a test case named "From an expert review #42" reproduces it, and the pull request says "Closes #42".

## A supporting skill

A skill that does a job many skills' outputs share, such as writing, and is not a method. Keep the author's text, add the frontmatter from section 13 of `skill-spec.md`, and draft its row for "Supporting skills" in `docs/canonical-sources.md`. A maintainer decides whether the library carries it.
