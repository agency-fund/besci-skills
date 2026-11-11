---
name: design-pilot-feasibility-study
description: >-
  Use when a team plans a small first run of a program before a larger trial
  or a scale-up ("let's pilot it with 50 people first") and must decide what
  the pilot has to show: whether people can be recruited and kept, the
  program delivered, and the data collected. Sets go, amend, and stop
  thresholds before fieldwork. Do not use when a few people from the
  audience should first react to a draft; use plan-prototype-test. Not for
  whether the program works; use plan-evaluation-design.
license: CC-BY-4.0
metadata:
  title: Design a pilot that tests feasibility, not effect
  type: atomic
  stage: test
  version: "0.2.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  tested_in: not-applicable
  tags: "experimental-design, process-evaluation, implementation-science"
  consumes: "intervention-draft"
  produces: "pilot-plan"
---

## What it does

Designs a pilot that tests whether a planned trial or scale-up can run, not whether the program works.

**What this adds:** each feasibility question becomes a rate with go, amend, and stop lines fixed before fieldwork from the main study's needs; the pilot is sized by the computed margin on those rates, not by power; each band names its change to the main study; interviews with dropouts and deliverers; no sizing from the pilot's effect.

## When to use it

### Use it when
- Someone says "let's pilot it with 50 people first" without saying what the pilot must show
- A funder or ethics board asks for a feasibility study or progression criteria
- A team is about to size a main trial from a pilot's effect

### Do not use it when
- The team wants a few people from the audience to react to or try a draft before any pilot; use `plan-prototype-test`
- The question is whether the program works and how the outcome is measured; use `plan-evaluation-design`

## Before you start

Ask these before producing anything. Do not ask anything the user has already answered.

1. **Required.** The intervention: what is delivered, by whom, to whom, how often, through what channel.
2. **Required.** What the pilot leads to: a trial (unit of randomization, outcome and how it is collected, planned size, assumed attrition) or a scale-up (where, delivered by whom), or "not designed yet".
3. **Required.** The pilot's resources: people or sites, duration, staff, and who can run short interviews.
4. Optional. The team's biggest worry: recruitment, dropout, delivery, acceptance, or data.

If 1, 2, or 3 is missing, ask and stop. If nothing is designed yet, mark every line provisional. If 4 is missing, weight headings equally.

## What it draws on

- Skivington, K., Matthews, L., Simpson, S. A., et al. (2021). A new framework for developing and evaluating complex interventions: update of Medical Research Council guidance. *BMJ*, 374, n2061. https://doi.org/10.1136/bmj.n2061 Supports: a feasibility study "designed to assess predefined progression criteria" on the evaluation (recruitment, data collection, retention, outcomes) and the intervention (delivery, acceptability, adherence, capacity of providers).
- Eldridge, S. M., Chan, C. L., Campbell, M. J., et al. (2016). CONSORT 2010 statement: extension to randomised pilot and feasibility trials. *BMJ*, 355, i5239. https://doi.org/10.1136/bmj.i5239 Supports: criteria to proceed, proceed with amendments, or not proceed; a size "based on the feasibility objectives"; no test of effectiveness, and no reliance on the pilot's effect estimate, which is imprecise.
- World Health Organization & ExpandNet (2011). *Beginning with the end in mind*. https://www.who.int/publications/i/item/9789241502320 Supports: piloting in the settings and institutions that would scale the program, keeping "externally provided nonreplicable inputs to a minimum".

**Where the evidence comes from:** The method makes no claim about how people behave. The trial guidance comes from clinical and public-health research; the guidance on piloting for scale-up from WHO and ExpandNet, whose tools have been used in Africa, Asia, and Latin America. What varies by setting is the rates, which move with season, site, and who must agree before anyone is approached.

**Replication status:** Not applicable; this is method guidance. OECD lists "indicators of what effect size of the intervention to expect" among a pilot's purposes; the trial guidance warns against this, and the skill follows it.

## How to do it

1. **State what the pilot serves:** the intervention and the trial or scale-up, so each line traces to it.
2. **Write the feasibility questions as rates or counts** under five headings: recruitment (share of eligible people who enroll; enrollments per week), retention (share still in at endline), delivery (share of planned contacts delivered as designed), acceptability (share who keep using it), and outcome data (share with a usable outcome). Name each denominator: a rate over the wrong group flatters.
3. **Set go, amend, and stop lines (progression criteria) before fieldwork,** from what the main study needs: retention from the attrition the main sample assumes, recruitment from the enrollment its timeline needs. Each amend band names the change it triggers.
4. **Size the pilot by its margin of error.** For the rate that matters most, the 95% margin is about 1.96 × √(p(1 − p)/n): with 60 people and a rate near 80%, ±10 points. Choose n so the margin is narrower than the gap between go and stop, and report each site's rate where sites may differ.
5. **List the main trial's inputs the pilot will measure,** such as take-up, attrition, and the outcome's baseline, and write: "This pilot's effect estimate will not be used to size the main trial."
6. **Plan short interviews** with refusers, dropouts, and deliverers, each with its one question, interviewer, and timing. A rate never says why.
7. **Choose typical sites and routine conditions:** the staff, resources, and season of the main study. Say what the chosen sites leave unknown.
8. **Tabulate what changes in the main study** under each result, and write the report skeleton.

See `references/worked-example.md` for a complete run.

## Output template

```markdown
# Pilot plan: <program>

**Intervention piloted:** <what, by whom, to whom, how often, channel>
**What it serves:** <the trial: unit, outcome, planned size, assumed attrition; or the scale-up; or "not designed yet: thresholds provisional">
**What this pilot is not for:** estimating the program's effect. Its effect estimate will not be used to size the main trial.
**Main-trial inputs it will measure:** <take-up, attrition, baseline, ...>; not measured: <...>

## Feasibility questions and progression criteria
| Heading | Question (rate or count, with its denominator) | Go | Amend | Stop | Why this line |
|---|---|---|---|---|---|
| Recruitment | <...> | <...> | <...> | <...> | <derived from the main study's ...> |
| Retention | <...> | | | | |
| Delivery | <...> | | | | |
| Acceptability | <...> | | | | |
| Outcome data | <...> | | | | |

## Pilot size
<the rate that matters most; n; its 95% margin, with the arithmetic; how that compares with the gap between go and stop; duration>

## Sites and conditions
<which sites and why they are typical; who delivers it, with what resources; season; what these sites leave unknown>

## Interviews
| Who | The one question | Asked by | When |
|---|---|---|---|
| <refusers / dropouts / deliverers> | <...> | <...> | <...> |

## What changes in the main study
| Question | If go | If amend | If stop |
|---|---|---|---|
| <...> | <no change> | <named change> | <named stop or redesign> |

## Report skeleton
1. Participant flow: approached, eligible, enrolled, retained, with usable outcome data
2. Each question: line, observed rate with its margin, decision
3. Interview reasons
4. Changes to the main study
5. Any difference in outcomes, labeled "not a basis for sizing the main trial"

## What to check before relying on this
- <the assumption most likely to be wrong>
```

## Where it goes wrong

- **A good-looking effect becomes the case for the trial.** "The pilot showed a 15-point gain" reaches the funder without its interval, though a pilot's comparison is too noisy to carry it.
- **A pilot run with help the main study will not have.** Research staff deliver it, a project vehicle carries supplies, the best clinic hosts it; the rates then describe a program that will not exist.
- **No stop line.** Teams avoid writing one because stopping feels like failure; a pilot that cannot stop the trial is not testing it.

## When to bring in a specialist

Tell the user to consult a specialist when:
- The team wants to size the main trial from the pilot's effect, or persuade a funder with it: an evaluation methodologist
- The pilot involves medication, clinical care, children, or people who depend on the organization: an ethics reviewer, before the pilot, with a stopping rule for harm
- Refusals or dropout point to stigma, coercion, or community objection rather than logistics: a local qualitative researcher, before any amend decision

Bring them: the progression criteria, the sizing arithmetic, the main study's design, and interview notes.
