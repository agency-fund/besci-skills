# Worked example: a two-author field study report

A full run of the skill on a realistic case, showing the output it should produce. The case is illustrative, not a real program.

## The request

"Please write the AI-use statement for our final report, 'Market-vendor mobile savings study'. The authors are J. Okello and A. Diallo, and we're both accountable for it. We designed the study together. I used Claude Sonnet 4.5 (Anthropic) to search and summarize the literature on deposit behavior, and from that summary it drafted the report's background section, which Amara rewrote substantially; I checked every paper it cited against the original. Amara ran and transcribed the diagnostic interviews herself. We did the analysis together in R, and I had Claude debug two of my scripts. Claude also made the first versions of Figures 2 and 3 from our cleaned data, and I fixed the axes and labels. At the end I ran the whole report through Claude for grammar, and Amara and I went through every change together. The chat logs are in our project folder. It was an unfunded two-person pilot. Date it 7 August 2026."

## The output

```markdown
Three roles are rated 2, extensive AI use: the literature search, the first versions of Figures 2 and 3, and the background section, which stays a 2 although Amara rewrote it, because the tool wrote its first version. The statement is self-reported, so it shows what you described, not what anyone has checked. It runs from the title to the sIfA citation, ready to paste into the report.

# AI-use statement (sIfA): Market-vendor mobile savings study, final report

**People accountable for this work:** J. Okello, A. Diallo
**AI tools used anywhere in the work:** Claude Sonnet 4.5 (Anthropic)
**Basis:** Self-reported by the authors on 7 August 2026. A disclosure, not an external audit.

## Role by role
| CRediT role | Performed by (level) | AI tool | How AI was used, and why | Generative or non-generative | Audit trail | Extent (0–2) |
|---|---|---|---|---|---|---|
| Conceptualization | J. Okello (Equal) | none | Study question set by the authors | n/a | n/a | 0 |
| Conceptualization | A. Diallo (Equal) | none | As above | n/a | n/a | 0 |
| Methodology | J. Okello (Equal) | none | Study design set by the authors | n/a | n/a | 0 |
| Methodology | A. Diallo (Equal) | none | As above | n/a | n/a | 0 |
| Investigation | A. Diallo (Lead) | none | Ran the diagnostic interviews in person | n/a | n/a | 0 |
| Investigation | J. Okello (Support) | Claude Sonnet 4.5 | Searched and summarized the literature on deposit behavior, to save time on the background; Okello checked every cited paper against the original | Generative | Chat logs in the project folder | 2 |
| Data curation | A. Diallo (Sole) | none | Transcribed the interviews herself | n/a | n/a | 0 |
| Formal analysis | J. Okello (Equal) | Claude Sonnet 4.5 | Debugged two of Okello's R scripts; the analysis choices were the authors' | Non-generative | Chat logs in the project folder | 1 |
| Formal analysis | A. Diallo (Equal) | none | Ran the analysis with Okello | n/a | n/a | 0 |
| Visualization | J. Okello (Sole) | Claude Sonnet 4.5 | Produced the first versions of Figures 2 and 3 from the cleaned data; Okello corrected the axes and labels | Generative | Chat logs in the project folder | 2 |
| Writing – original draft | J. Okello (Equal) | Claude Sonnet 4.5 | Drafted the background section from the literature summary, at Okello's request | Generative | Chat logs in the project folder | 2 |
| Writing – original draft | A. Diallo (Equal) | Claude Sonnet 4.5, through Okello's draft | Rewrote the tool-drafted background section substantially; the other sections were drafted by the authors without AI | Generative | Chat logs in the project folder | 2 |
| Writing – review & editing | J. Okello (Equal) | Claude Sonnet 4.5 | Grammar and consistency pass over the whole report; both authors reviewed every change | Non-generative | Chat logs in the project folder | 1 |
| Writing – review & editing | A. Diallo (Equal) | Claude Sonnet 4.5, through the grammar pass | Reviewed every suggested change with Okello | Non-generative | Chat logs in the project folder | 1 |

## Roles not performed
- Funding acquisition: unfunded pilot.
- Project administration: no separate administration in a two-person pilot.
- Resources: no materials, instruments, or participants were provided by others.
- Software: no software was produced; the analysis scripts are covered under Formal analysis.
- Supervision: neither author supervised the other.
- Validation: no separate check of reproducibility was run.

## Accountability
After using any tools or services, the author(s) reviewed and edited the content as needed and take(s) full responsibility for the content of the publication.

Contributor roles are based on the Contributor Role Taxonomy (CRediT). More info at https://credit.niso.org. This statement follows the sIfA format: Schomerus, M. (2026). sIfA Tool — Statement of Intellectual Fellowship and Accountability (Version 1.4.1) [Computer software]. Busara. https://doi.org/10.5281/zenodo.20285993

## Where you could go from here
That's the statement.
- Have Amara read her own rows: the account came from you, and two of her entries describe her work through your draft and your grammar pass, so she should agree with how they read.
- If the report goes to a funder or journal with an AI-use policy, take the statement and the policy text to its editor or your research-integrity officer: three roles are rated 2, and whether that is acceptable is their call, not the statement's.
- Start the next project's table on its first day: the debugged scripts and the grammar pass are the uses most easily forgotten, and they are easiest to log the day they happen.
I'd lean toward Amara's read first, because a co-author should agree with her entries before anyone else sees them.
Questions you could ask next: "Why is the rewritten background still a 2?" · "Does the literature search belong under Investigation?"
```
