# Taxonomy

The controlled vocabularies live in `taxonomy.yaml` at the repository root. This page explains them. Change the YAML file in the same pull request as the first skill that needs the change.

## Stage

Where in a project a skill is normally used. Every skill declares one. The seven project stages are strong recommendations rather than rules. `other` is the stage for supporting skills (`type: supporting`): plain skills that are not behavioral-science methods but do a job the outputs of many skills share, such as writing. Each one is listed under "Supporting skills" in `docs/canonical-sources.md`. Meta-skills also declare `other`; an atomic skill never does.

| Stage | Covers | BIT TEST | Busara AUDAS | TAF four-level evaluation |
|---|---|---|---|---|
| define | Turn a goal, population, or outcome into something specific enough to work on | Target | Align | Level 0, theory of change |
| diagnose | Explain why the current behavior pattern exists | Explore | Understand | Level 1, formative research |
| design | Produce intervention content, levers, messages, strategy | Solution | Design | Level 1, prototype |
| measure | Choose, adapt, or build instruments | Trial (measurement) | Assess | Level 2, outcome measures |
| test | Plan a pilot, experiment, or evaluation | Trial | Assess | Level 3, experimental evaluation |
| analyze | Analyze data from a test and interpret it | Trial (analysis) | Assess | Levels 3 and 4, analysis |
| implement | Roll out, adapt, scale, and report | Scale | Share | Level 4, scale and welfare |
| other | Supporting skills that many outputs use, such as writing; also the meta-skills | | | |

The crosswalk is a navigation aid. It does not claim the frameworks are equivalent, and a skill is not required to map to any of them. Sources: Behavioural Insights Team, *Test, Learn, Adapt* (2012) and *EAST* (2014); Busara, *The Busara toolkit* (Groundwork No. 10, 2024, https://doi.org/10.62372/WQSB6195), whose stages are Align, Understand, Design, Assess, Share; The Agency Fund, four-level evaluation framework (https://eval.playbook.org.ai/).

Why one axis rather than two: the stage is what a program designer thinks in ("I'm at the point where I need to measure this"), and it is the axis the navigator walks. A second controlled axis for "what kind of operation" mostly restates the first and doubles maintenance. Finer cuts are tags.

## Type

`atomic` for a skill that does one behavioral-science operation; `meta` for a skill that operates on the library itself (the creator, the navigator, the evaluator), written in its own shape (`docs/skill-spec.md`, section 14); `supporting` for a plain skill in the stage `other` (`docs/skill-spec.md`, section 13).

## Status

`draft` while in review or when merged without review; `published` once a maintainer has approved it; `deprecated` when retired. Deprecated skills leave the catalog and plugin but stay in history.

## Tested in

Where the evidence behind a skill has been tested. Required for atomic skills, and set from the evidence scan described in `docs/skill-spec.md`, section 7.

| Value | Label | What earns it |
|---|---|---|
| `beyond-western-holds` | Tested beyond wealthy Western countries; results hold | A systematic review, or at least two field studies outside wealthy Western countries, point the same way as the original evidence |
| `beyond-western-differs` | Tested beyond wealthy Western countries; results differ | Studies outside wealthy Western countries exist, and their results differ from the original evidence or from each other |
| `mainly-western` | Tested mainly in wealthy Western countries | The scan found fewer than two field studies outside wealthy Western countries |
| `not-applicable` | Not applicable | The skill is a procedure that makes no claim about how people behave |

Researchers call samples from wealthy Western countries WEIRD (Western, Educated, Industrialized, Rich, Democratic). Skills and the site use the plain wording.

## Verbs

The list of verbs a skill name may start with. Verb-first names are the atomicity rule applied to the folder name: if the skill cannot be named with one verb, it is more than one skill. Add a verb to the list in the same pull request as the first skill that needs it.

## Input and output types

The vocabulary for `metadata.consumes` and `metadata.produces`. `consumes` lists the inputs a skill cannot run without, matching the required questions in its "Before you start"; `produces` names the one thing its output template is. Where one skill produces what another consumes, the site's map draws an arrow and the navigator can suggest an order.

An arrow is a suggestion that two skills fit together, there to help people assemble a workflow. It is not a rule about where an input must come from: a person can bring any input from their own work, and any skill can be used on its own. Unknown ids are a warning: add the type to the YAML in the same pull request.

## Tags

Free-form, comma-separated. `suggested_tags` in the YAML keeps spelling consistent for common frameworks and methods; any tag is allowed.
