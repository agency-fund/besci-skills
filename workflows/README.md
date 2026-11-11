# Workflows

A **workflow** is a recommended set of skills for a task too big for one skill, with the relationships between the skills stated: which comes after which, which can run in parallel, which are independent, and where a human has to decide before the next step. Even "use these three, in any order, but A before B" is a workflow.

Workflows live here as single markdown files, one per workflow, following `WORKFLOW-TEMPLATE.md`. They are not skills and are never placed in `skills/`. The site draws each one as a graph at https://besci-skills.vercel.app/workflows/.

Each workflow is a recommended order, not a rule: you can start at any step with your own inputs, and every skill in a workflow also works on its own. They are listed from the shortest, a few steps in one or two stages, to the longest, ten steps across five stages.

| Workflow | File |
|---|---|
| Check the evidence | `check-the-evidence.md` |
| Define and measure agency | `define-and-measure-agency.md` |
| Design a wise intervention | `design-a-wise-intervention.md` |
| From a goal to a tested intervention | `from-a-goal-to-a-tested-intervention.md` |

To add one, copy `WORKFLOW-TEMPLATE.md` to `workflows/<name>.md` and open a pull request. `besci-navigator` drafts a workflow in guide mode whenever a user's goal spans several stages, and the site's [workflow builder](https://besci-skills.vercel.app/workflows/build/) turns a list of skills you pick into a proposal. From 2027, invited expert organizations are asked to contribute the workflows they actually use.
