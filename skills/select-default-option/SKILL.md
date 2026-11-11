---
name: select-default-option
description: >-
  Use when people say they want something, it is available, and doing nothing
  leaves them without it: "nobody enrolls", "the form sits unsigned". Also use
  when a team wants to switch from opt-in to opt-out ("let's auto-enroll
  everyone"). Specifies the default, who it is for, how to opt out, and what
  to monitor. Do not use when the hassle is in the steps of a process; use
  audit-process-friction. Not for a restriction people choose for themselves;
  use design-commitment-device.
license: CC-BY-4.0
metadata:
  title: Choose what people get by default
  type: atomic
  stage: design
  version: "0.2.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  tested_in: beyond-western-holds
  tags: "choice-architecture, defaults"
  consumes: "barrier-diagnosis"
  produces: "intervention-draft"
---

## What it does

Specifies the option people receive when they take no action at one decision point.

**What this adds:** stops if the barrier is not inaction at a decision point; requires the default to serve the person who receives it and names who could be worse off; makes the designer say which mechanism the default relies on; fixes the opt-out as one free, visible step; and sets an opt-out rate at which the default is reviewed.

## When to use it

### Use it when
- A confirmed barrier is inaction at one decision point: people say they want the option, it is available, and doing nothing leaves them without it ("nobody enrolls", "the form sits unsigned")
- A team is about to switch a program from opt-in to opt-out
- A step already has a default, usually "nothing", and the team wants to check whether it serves the people who receive it

### Do not use it when
- The hassle is in the steps of a process (fields, documents, trips), which a default does not remove; use `audit-process-friction`
- People are to restrict their own future choices, such as a locked account they choose to open; use `design-commitment-device`

## Before you start

Ask these before producing anything. Do not ask anything the user has already answered.

1. **Required.** The behavior (who, what, when) and the confirmed barrier, with the evidence that people want the option and are stopped by not acting.
2. **Required.** The decision point: what happens today to a person who does nothing, and who controls that setting.
3. **Required.** Whether the default would move money, medical treatment, or legal status.
4. Optional. Who could be worse off under the proposed default.
5. Optional. Whether a party the audience trusts stands behind the default.

If 1 or 2 is missing, ask and stop. If 3 is unclear, treat the default as one that moves money. If 4 is missing, list "who could be worse off" as the first open question. If 5 is missing, assume no trusted party.

## What it draws on

- Jachimowicz, J. M., Duncan, S., Weber, E. U., & Johnson, E. J. (2019). When and why defaults influence decisions: a meta-analysis of default effects. *Behavioural Public Policy*, 3(2), 159–186. https://doi.org/10.1017/bpp.2018.43 Supports: the mechanism line. The authors name three channels: endorsement (the default is read as a recommendation), endowment (it is seen as the status quo), and ease (staying with it takes less effort than switching).
- Blumenstock, J., Callen, M., & Ghani, T. (2018). Why do defaults affect behavior? Experimental evidence from Afghanistan. *American Economic Review*, 108(10), 2868–2901. https://doi.org/10.1257/aer.20171676 Supports: checking that the barrier is a decision people put off.
- Somville, V., & Vandewalle, L. (2018). Saving by default: Evidence from a field experiment in rural India. *American Economic Journal: Applied Economics*, 10(3), 39–66. https://doi.org/10.1257/app.20160547 Supports: monitoring after the default ends.

**Where the evidence comes from:** The meta-analysis records only whether each of its 58 data sets was run in the United States, which made no difference. Field trials in Afghanistan, India, and Malawi, all on savings, each found that a default raised participation or balances; in India the gain ended when the default did. Check locally who may set the default, whether that party is trusted, and whether people need the money or service at once.

**Replication status:** Replicated in direction, with very uneven size: nearly all the variation across the 58 data sets is real difference between studies, and two found the opposite effect.

## How to do it

1. **Check that the barrier is inaction at one decision point.** If it is cost, access, distrust, or the steps after the decision, say a default is the wrong tool and stop.
2. **Name the current default:** what happens today to a person who does nothing, and who controls it.
3. **Choose the default that serves the person receiving it**, and say who could be worse off. For an identifiable group that would be worse off, specify an active choice (the person must pick; nothing is pre-set) or a different default.
4. **Name the mechanism relied on**, endorsement, endowment, or ease, and the local fact that supports it. Do not rely on endorsement when no trusted party stands behind the default.
5. **Design the opt-out:** one step, no cost, no waiting period, shown in the same place the default is announced.
6. **Set the monitoring:** the opt-out rate above which the default is reviewed, how the team will learn whether people who stayed in are worse off, and what is checked when the default ends.
7. **Run the ethics check:** does it serve the chooser, are people told before it applies, and could it be read as the organization taking something? If it moves money, treatment, or legal status, name the specialist who must review it.
8. **State what the evidence supports:** the direction. Do not promise an effect size.

See `references/worked-example.md` for a complete run.

## Output template

```markdown
# Default option specification

**Behavior:** <who, what, when>
**Confirmed barrier:** <the evidence that people want the option and are stopped by not acting>
**Decision point:** <what happens today to a person who does nothing; who controls it>

## The default
- **Proposed default:** <the option a person gets by doing nothing>
- **Who receives it:** <the population or segment>
- **Who it is not for:** <who could be worse off, and the active choice or other default they get; or "none identified, see open questions">

## Mechanism
- **Relied on:** <endorsement / endowment / ease>
- **Why this setting supports it:** <the local fact>

## Opt-out
- **How:** <the one step>
- **Where it is shown:** <the same place as the default is announced>
- **Cost to the person:** <none; or state it and justify it>

## Monitoring
- **Review if opt-outs exceed:** <rate, and who reviews>
- **Harm check:** <how the team learns whether those who stayed in are worse off>
- **When the default ends:** <what is checked>

## Ethics check
- **Serves the chooser because:** <...>
- **Told before it applies:** <how>
- **Could it read as taking something:** <how that is avoided>
- **Specialist review:** <not needed / <who>, because it moves money, treatment, or legal status>

## What the evidence supports
<the direction, and the nearest field evidence with where it was run; no effect size promised>

## What to check before relying on this
- <the assumption most likely to be wrong>
```

## Where it goes wrong

- **A default that serves the program.** Default enrollment in a fee-bearing product or a data-sharing consent uses people's inaction against them. If the honest answer to "who is this default for?" is the organization, refuse and say why.
- **Opt-out in name only.** An opt-out that needs a visit, a form, or a word with a supervisor keeps in people who would leave, and the participation figure then means nothing.
- **Quoting the pooled effect as a forecast.** The average hides studies with no effect and two with the opposite effect.

## When to bring in a specialist

Tell the user to consult the relevant specialist before any pilot when:
- The default moves money (a deduction, a contribution rate, a fee): a financial-services compliance lead checks the opt-out and the disclosure
- The default sets medical treatment or testing: a clinician confirms it is appropriate for everyone who receives it and that opting out is safe
- The default changes legal status or consent (data sharing, enrollment with obligations): a lawyer confirms that consent by inaction is valid in that jurisdiction

Bring them: the specification, the list of who could be worse off, and the opt-out design.
