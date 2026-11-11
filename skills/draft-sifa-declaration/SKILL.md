---
name: draft-sifa-declaration
description: >-
  Use when a report, paper, design, or other piece of work is being finished
  and the team must say how people and AI tools each contributed, or when a
  journal, funder, or policy asks for an AI-use disclosure and the current
  answer is "we used ChatGPT a bit". Writes a sIfA statement: for each
  contributor role, who did the work, which AI tool helped, how, and how
  much. Do not use to examine the team's beliefs about its audience; use
  audit-researcher-bias. Not for ruling on whether the AI use is allowed.
license: CC-BY-4.0
metadata:
  title: Write an AI-use disclosure statement
  type: atomic
  stage: implement
  version: "0.2.0"
  status: draft
  authors: "Joe Speed, Zezhen Wu"
  org: IL
  tested_in: not-applicable
  tags: "research-transparency, credit, ai-disclosure"
  consumes: "ai-use-account"
  produces: "sifa-declaration"
---

## What it does

Turns a team's account of how a piece of work was made into a sIfA, Busara's role-by-role statement of where AI tools took part.

**What this adds:** walks all fourteen CRediT roles, asking about uses teams drop; records each person's level and AI use per role on sIfA's 0 to 2 scale; rates a 2 whenever a tool produced the first version; never lists a tool as a contributor; and labels the account self-reported.

sIfA (Statement of Intellectual Fellowship and Accountability) is built on CRediT, the Contributor Roles Taxonomy: fourteen kinds of contribution to research.

## When to use it

### Use it when
- A report, paper, or design is being finished and the team must disclose where AI tools were involved
- A journal, funder, or policy asks for an AI-use disclosure and the current answer is one vague paragraph
- A project is starting and the team wants to record AI use as the work goes

### Do not use it when
- The team wants to examine its beliefs about its audience before research; use `audit-researcher-bias`
- The question is whether the AI use is allowed under a policy; the venue rules on that
- The subject is an AI product the team built; use `choose-ai-eval-level`

## Before you start

Ask these before producing anything. Do not ask anything the user has already answered.

1. **Required.** The work: its title, type, and the people accountable for it.
2. **Required.** Who did each part, at what level, and which AI tools (name, provider, version) were used where, for what, and why, with any chat logs kept. Ask about grammar passes, debugged code, chart drafts, literature searches, translation.
3. **Required.** Anything the team is unsure whether to disclose; it goes in the table.

If 1 or 2 is missing, ask and stop. If 3 is "nothing", ask once about review and editing, visualization, software, and data curation. Date it today and use CRediT unless told otherwise.

## What it draws on

- Saleh, E., & Schomerus, M. (2026). *The sIfA tool for a Statement of Intellectual Fellowship and Accountability: An invitation to reflect on how humans and AI interact in producing knowledge* (Groundwork No. 32). Busara. https://doi.org/10.62372/IUPB2137 Supports: the entries for each person in each role (level, tool, how and why, audit trail, extent from 0 to 2) and the statement of responsibility.
- Schomerus, M. (2026). *sIfA Tool — Statement of Intellectual Fellowship and Accountability* (Version 1.4.1) [Computer software]. Busara. https://doi.org/10.5281/zenodo.20285993 Supports: the table's columns, the generative or non-generative label, and the rules on levels.
- NISO (2022). *ANSI/NISO Z39.104-2022, CRediT, Contributor Roles Taxonomy*. https://www.niso.org/publications/z39104-2022-credit Supports: the fourteen roles.

The fixed rule for a 2, the roles-not-performed list, and the self-report line are this skill's own.

**Where the evidence comes from:** The method makes no claim about how people behave. sIfA comes from Busara, in Nairobi; CRediT comes from scholarly publishing and assumes a research article, so for other work sIfA allows a team's own role list.

**Replication status:** Not applicable. No study has tested whether teams fill in sIfA completely or alike; its authors note it "does not in itself change" the incentive not to disclose.

## How to do it

1. **Write the header:** the work, the people accountable, every AI tool used (name, provider, version) or "none", and the basis line: self-reported by the authors on the date, not an audit.
2. **Walk all fourteen roles.** A role with any AI use appears, however trivial the team thinks it; a grammar pass is AI use in Writing – review & editing. List roles nobody performed, with the reason, so an omission reads as a decision.
3. **Name the people in each role, each with a level** (Sole, Lead, Equal, Support): no one beside a Sole, only Support beside a Lead, at least one Lead, Equal, or Sole overall. A tool is never a contributor.
4. **Record each person's AI use in each role:** the tool; what it did, what the person did with its output, and why; generative (new content) or non-generative (improving existing content); and the audit trail, a link to prompts or chat logs, or "none kept".
5. **Rate each person's extent:** 0 none, 1 some, 2 extensive. sIfA leaves this to the authors and lists signs of substantial use: AI made decisions affecting results, or generated or analyzed content, data, or images. Fixed rule: a tool that produced the first version of the person's work makes it a 2, however heavily edited.
6. **Test each entry:** could a skeptical reader tell what the tool produced from what the people produced? "AI was used responsibly" fails.
7. **Close with sIfA's accountability statement, verbatim,** then the CRediT attribution and the sIfA citation; the sIfA tool can draw the figure from these entries.
8. **If asked to shape the statement to pass a policy,** record what happened anyway; the venue decides whether it passes.

See `references/worked-example.md` for a complete run.

## Output template

```markdown
# sIfA: <work title>

**People accountable for this work:** <names>
**AI tools used anywhere in the work:** <name, provider, version; one per line; or "none">
**Basis:** Self-reported by the authors on <date>. A disclosure, not an external audit.

## Role by role
| CRediT role | Performed by (level) | AI tool | How AI was used, and why | Generative or non-generative | Audit trail | Extent (0–2) |
|---|---|---|---|---|---|---|
| <role> | <name (Sole / Lead / Equal / Support)> | <tool and version, or "none"> | <what the tool did; what the person did with it; why> | <generative / non-generative / n/a> | <link, or "none kept"> | <0 / 1 / 2> |

<one row per person per role>

## Roles not performed
- <role>: <why it does not apply to this work>

## Accountability
After using any tools or services, the author(s) reviewed and edited the content as needed and take(s) full responsibility for the content of the publication.

Contributor roles are based on the Contributor Role Taxonomy (CRediT). More info at https://credit.niso.org. This statement follows the sIfA format: Schomerus, M. (2026). sIfA Tool — Statement of Intellectual Fellowship and Accountability (Version <version>) [Computer software]. Busara. https://doi.org/10.5281/zenodo.20285993
```

## Where it goes wrong

- **Rating by comfort.** Heavy first-drafting is rated 1 because 2 feels like an admission, or every role gets a 1 and the same reassuring note. Small honest ratings make the large ones credible.
- **Reconstructing at the end.** From memory, the statement misses the grammar pass, the debugged script, the translated quote; sIfA's authors recommend starting it with the project.
- **Mistaking self-report for verification.** A team that leaves out a tool gets a clean-looking statement that nothing here can catch, which is why the basis line stays.

## When to bring in a specialist

Tell the user to take the question to the venue's editor, the organization's research-integrity officer, or counsel when:
- The question is whether the AI use is acceptable under a policy; the statement is the input to that ruling
- Contributors disagree about who performed a role or who is an author; CRediT does not settle authorship
- AI tools processed confidential, participant, or third-party material; consent, data protection, and copyright go beyond disclosure, to counsel or a data-protection officer

Bring them: the statement, the team's raw account, and the policy text.
