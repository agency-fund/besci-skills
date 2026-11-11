# Evidence: Write an AI-use disclosure statement

## Sources

The library carries Busara's sIfA by choice, as the format it points to for disclosing how people and AI contributed to a piece of work.

- Saleh, E., & Schomerus, M. (2026). *The sIfA tool for a Statement of Intellectual Fellowship and Accountability: An invitation to reflect on how humans and AI interact in producing knowledge* (Groundwork No. 32). Busara. https://doi.org/10.62372/IUPB2137 Supports: the method. "For each role, the tool asks who the contributors are, and what their level of engagement in this role was (Lead, Equal, Support, or Sole). Each contributor is then asked about their use of AI in the different roles, their reasons for using AI, and what tool they used." The extent scale is "0: no interaction between humans and AI in this task", "1: some interaction", "2: extensive interaction". To judge the extent, the Groundwork points to three criteria for substantial use: "using AI to make decisions that directly affect research results", "using AI to generate content, data or images", and "using AI to analyze content, data or images"; it says the judgment "will always involve your own judgement and discretion". The audit trail means linking "to a documentation of the prompts used or a project summary". The accountability wording is adapted from Elsevier through Behavioural Research UK: "After using any tools or services, the author(s) reviewed and edited the content as needed and take(s) full responsibility for the content of the publication." The authors "recommend setting up a sIfA at the start of a project and filling it in as the project progresses, to make reflection as accurate as possible", and they say sIfA's purpose "is thus not precision and exact percentages". On whether tools count as contributors, one of the authors writes: "I use the contributor roles solely for the human contribution." Full text, except the figures.
- Schomerus, M. (2026). *sIfA Tool — Statement of Intellectual Fellowship and Accountability* (Version 1.4.1) [Computer software]. Busara. https://doi.org/10.5281/zenodo.20285993 Supports: the table and the rules on levels. For each contributor the tool asks "how was AI used?" ("Explain how AI was used and the reasons for doing so"), "Generative or non-generative?" ("whether AI was used to fully generate new content or to improve or shape existing content"), and "Is there an audit trail?" ("Include links to prompts, summaries, or projects where relevant"). Once a Sole contributor is named, no one else can be added to the role; once a Lead is named, others must be Support; once one contributor is Equal, "All contributors for this role must be Equal"; and an export is refused if every contributor is Support. The exported figure carries the accountability statement and "Contributor roles are based on the Contributor Role Taxonomy (CRediT)." The tool's text read, from the version released on 7 November 2026; landing page https://mareikeschomerus-ctrl.github.io/sIfA/. The DOI is a concept DOI: it always resolves to the latest version, so record the version number used.
- NISO (2022). *ANSI/NISO Z39.104-2022, CRediT, Contributor Roles Taxonomy*. https://www.niso.org/publications/z39104-2022-credit Supports: the fourteen roles: Conceptualization, Data curation, Formal analysis, Funding acquisition, Investigation, Methodology, Project administration, Resources, Software, Supervision, Validation, Visualization, Writing – original draft, and Writing – review & editing (https://credit.niso.org/). The standard's page and the role list read.
- Brand, A., Allen, L., Altman, M., Hlava, M., & Scott, J. (2015). Beyond authorship: attribution, contribution, collaboration, and credit. *Learned Publishing*, 28(2), 151–155. https://doi.org/10.1087/20150211 Supports: where CRediT comes from. "A multi-stakeholder group has produced a contributor role taxonomy for use in scientific publications", meant to lead "to appropriate credit, fewer author disputes". Abstract only.

Four rules are this skill's own and come from no source: a tool is never listed as a contributor (the sources describe humans in the roles, and one author's own practice is to do so); a tool that produced the first version of a person's work makes that person's rating a 2, however heavily it was edited; roles nobody performed are listed with the reason; and the statement says on its face that it is self-reported and not an audit.

## Where it has been tested

Searched November 2026. The skill is a disclosure procedure and makes no claim about how people behave, so this table records where its sources come from.

| Source | Type | Countries | Finding |
|---|---|---|---|
| [Saleh & Schomerus (2026)](https://doi.org/10.62372/IUPB2137) | Thought piece describing the method; full text | Published by Busara, Nairobi; written for research and other knowledge work anywhere | No test of the method is reported; the authors call the tool "at best, the beginning" of a conversation |
| [Schomerus (2026)](https://doi.org/10.5281/zenodo.20285993) | Open-source software, version 1.4.1 | Not applicable | Not applicable |
| [NISO (2022)](https://www.niso.org/publications/z39104-2022-credit) | Standard for scholarly publishing | Not applicable | No test reported |
| [Brand et al. (2015)](https://doi.org/10.1087/20150211) | Account of how the taxonomy was built; abstract only | Not stated in the abstract | No test reported |
| None found | | | No study of how completely or consistently teams fill in role-based AI-use statements. Searched: studies of the completeness of AI-use disclosure statements and CRediT contributor statements in research articles |

The procedure does not depend on the population. The role list does: CRediT's fourteen roles assume a research article, and program work has roles it does not name, such as community engagement, translation, or field supervision. sIfA lets a team set up its own role list.

## Replication

Not applicable; sIfA is a disclosure format and CRediT a taxonomy, so there is no effect to replicate. The sIfA authors note that the tool "does not in itself change the problem that researchers or other knowledge producers might be incentivized to not disclose their AI interactions".

## What to check locally

1. Whether the venue or funder requires its own AI-use format alongside the sIfA.
2. Whether the work has roles CRediT does not name, and whether to use a custom role list.
3. Whether prompts or chat logs were kept, and whether they can be linked without exposing participant data.
4. Whether any AI tool received confidential or participant data.
