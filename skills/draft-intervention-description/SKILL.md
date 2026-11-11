---
name: draft-intervention-description
description: >-
  Use when a team must write down exactly what an intervention was, item by
  item, so another team could deliver it again or a reader could tell what
  was delivered: for a funder, a new implementer, a scale-up partner, a
  registry, or a paper. Also use when the only record is a slide deck or a
  program name. Do not use when the messages or scripts still need writing;
  use draft-lever-content. Not for planning how delivery will be checked;
  use design-fidelity-monitoring.
license: CC-BY-4.0
metadata:
  title: Describe an intervention so others can replicate it
  type: atomic
  stage: implement
  version: "0.2.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  tested_in: not-applicable
  tags: "implementation-science, behavior-change-techniques, research-transparency, implementation"
  consumes: "intervention-draft"
  produces: "intervention-description"
---

## What it does

Writes down what an intervention is, item by item, in enough detail for a team elsewhere to deliver it again.

**What this adds:** fills TIDieR's twelve items (a reporting checklist), each tagged with its source so memory is labeled; names active parts by mechanism, never by a taxonomy code from memory; spells out the details a newcomer would drop; keeps planned variation apart from changes made during delivery; fills "how well: actual" only from monitoring data; and ends with a rebuild check.

## When to use it

### Use it when
- A pilot or program is ending or scaling, and the record of what was delivered is a slide deck or one person's memory
- A funder, scale-up partner, or new implementer asks "what exactly did you do?"
- A registry entry, pre-analysis plan, or paper needs its intervention section

### Do not use it when
- The messages, scripts, or materials still need writing; use `draft-lever-content`
- The question is how delivery will be checked during rollout; use `design-fidelity-monitoring`
- Changes made during delivery need judging against the program's essential parts; use `specify-intervention-adaptations`

## Before you start

Ask these before producing anything. Do not ask anything the user has already answered.

1. **Required.** The design documents: scripts, messages, materials, training notes, the reason for each part; or, if nothing is written, the team's own account.
2. **Required.** Whether and when it was delivered, where, and what records exist: monitoring data, logs, a record of changes.
3. Optional. Who will read it; where the materials are kept, in which languages; anything that cannot be shared.

If 1 is missing, ask and stop. If 2 stays unclear after one question, write it as planned and leave items 10 and 12 until delivery ends. If 3 is missing, assume a hand-off to an implementer.

## What it draws on

- Hoffmann, T. C., Glasziou, P. P., Boutron, I., et al. (2014). Better reporting of interventions: template for intervention description and replication (TIDieR) checklist and guide. *BMJ*, 348, g1687. https://doi.org/10.1136/bmj.g1687 Supports: the twelve items, including training materials and where to get them, tailoring kept apart from modifications, and how well, planned and actual.
- Michie, S., Richardson, M., Johnston, M., et al. (2013). The behavior change technique taxonomy (v1) of 93 hierarchically clustered techniques: Building an international consensus for the reporting of behavior change interventions. *Annals of Behavioral Medicine*, 46(1), 81–95. https://doi.org/10.1007/s12160-013-9486-6 Supports: specifying active content as named techniques, which researchers code against written definitions; the skill assigns no code from memory.
- OECD (2019). *Tools and Ethics for Applied Behavioural Insights: The BASIC Toolkit*. https://doi.org/10.1787/9ea76a8f-en Supports: instructions written for the people who will maintain the program, naming the features that look unimportant.

**Where the evidence comes from:** These are reporting standards and practice guidance; they make no claim about how people behave. TIDieR and the taxonomy come from health research. A reader elsewhere most often lacks what the team takes for granted: who delivered it, in which language, with what support.

**Replication status:** Not applicable; these are consensus standards. In six leading medical journals, 39% of 137 trial interventions were adequately described.

## How to do it

1. **List the sources** at the top and tag each item with one, writing "recollection" where nothing was written.
2. **Fill items 1 to 8 as delivered:** name; why; materials, including training materials, by language, with where to get them; procedures in order, including enrollment and missed contacts; who provided; how; where; when and how much.
3. **Name each active part by its mechanism:** what it changes for the person and which barrier it addresses, in plain words. Add a technique label only if the design documents carry one or it is copied from the published taxonomy. A part that changes nothing for the person is scaffolding.
4. **Spell out what a newcomer would drop:** exact wording, sender, timing, paper color, order of steps, each marked essential.
5. **Keep tailoring (item 9) apart from modifications (item 10).** Tailoring is variation planned before delivery, with its rule; a modification is a change made during delivery, with what, why, when, and how.
6. **Write item 11 from the monitoring plan and item 12 only from monitoring data:** adherence, dose, and quality as measured, with sample, period, and range across sites. Without data, item 12 says "not measured" and what that means for any result.
7. **For a hand-off, add the delivery system:** staffing, supervision, logistics, information system, cost, and research-only inputs that will not come with the program.
8. **Run the rebuild check:** could a team elsewhere, with only this document and what it points to, deliver each item again? Mark complete, partial, or missing; "available on request" is missing.
9. **List the open questions:** each gap and who can close it, each remembered item, any limit on sharing.

See `references/worked-example.md` for a complete run.

## Output template

```markdown
# Intervention description: <brief name>

**Status:** <as planned / as delivered, <dates>, <where>> · **Written for:** <internal record / funder / implementer / registry / publication>
**Sources:** <documents used; "recollection" where nothing was written>

## 1. Brief name
<the name used in the field, and any other names it went by>

## 2. Why
**Target behavior:** <who does what, when> · **Barrier:** <what stands in the way, with its source>

| Part | What it changes for the person | Barrier it addresses | Essential? | Source |
|---|---|---|---|---|
| <part; technique label only if documented> | <mechanism in plain words> | <barrier> | <essential / adaptable / scaffolding> | <document / recollection> |

## 3. What: materials
| Material | Language(s) | Where to get it | Source |
|---|---|---|---|
| <each material, including training materials> | <languages> | <link, folder, appendix; "available on request" counts as missing> | <document / recollection> |

## 4. What: procedures
<each activity in order, including enrollment, missed contacts, and support between contacts; the details a newcomer would drop, marked essential>

## 5. Who provided
<role, background, number, training, supervision>

## 6. How
<mode; individual or group>

## 7. Where
<type of place, infrastructure, and the features that mattered>

## 8. When and how much
<number of contacts, schedule, duration, intensity, period>

## 9. Tailoring
<variation planned before delivery: what, for whom, by what rule; or "none">

## 10. Modifications
| What changed | When | Who | Why | Part touched | Source |
|---|---|---|---|---|---|
| <change; or "none recorded", saying whether a record was kept> | <date> | <role> | <reason> | <part; essential or not> | <record / recollection> |

## 11. How well: planned
<what was checked, how, by whom, with what thresholds; what kept delivery on track; or "no monitoring planned">

## 12. How well: actual
<adherence, dose, quality as measured, with sample, period, and range across sites; or "not measured", and what that means for any result>

## Delivery system
<for a hand-off: staffing and skills, supervision, logistics, information system, cost to deliver; research-only inputs marked; or "not needed for this reader">

## Rebuild check
| Item | Complete / partial / missing | What a team elsewhere would still need |
|---|---|---|
| <1 to 12, one row each or grouped> | <status> | <blank only if complete> |

## Open questions
- <each partial, missing, or remembered item, and who can close it>
- <any limit on sharing>
```

## Where it goes wrong

- **Adjectives in place of ingredients.** "An engaging, community-led, culturally sensitive approach" names nothing a team could rebuild. If a part's effect cannot be written, the ingredient is unknown; the rebuild check says so.
- **Silence about the comparison.** In a trial, "usual care" goes undescribed, so a reader cannot tell what the effect is measured against. TIDieR covers comparison conditions too.
- **Identifying people.** Quotes, photos, and village names from a small program can identify participants or deliverers; remove them before the description leaves the team.

## When to bring in a specialist

Tell the user to consult a specialist when:
- It goes into a registry, a pre-analysis plan, or a publication: a methodologist, against the venue's reporting guideline, such as CONSORT-SPI 2018 for social and psychological intervention trials
- It includes a clinical part (a medicine, a dose, a referral rule): a clinician checks items 4 and 8
- Materials are confidential or could identify people: counsel or a data-protection officer, before anything is shared
- Monitoring data and the team's account disagree on an essential part: an evaluator, before item 12 is written

Bring them: the draft with its rebuild check, the monitoring data, and the materials.
