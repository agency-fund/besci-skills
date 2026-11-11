---
name: diagnose-social-norm
description: >-
  Use when a team suspects people keep a practice (open defecation, early
  marriage, skipping a clinic visit) because of what others do or expect, or
  says "everyone here does it", and wants to check before building on it.
  Classifies the practice from respondents' answers as a social norm,
  descriptive norm, custom, or moral rule, and reports the gap between private
  belief and perceived expectation. Do not use when the question is whose
  approval people track; use map-reference-network. Not for writing a norm
  message; use write-social-norm-message.
license: CC-BY-4.0
metadata:
  title: Find out whether a practice is a social norm
  type: atomic
  stage: diagnose
  version: "0.2.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  tested_in: beyond-western-differs
  tags: "social-norms, qualitative"
  consumes: "target-behavior-brief, qualitative-data"
  produces: "social-norm-diagnosis"
---

## What it does

Decides whether people follow one practice because of what they expect of each other.

**What this adds:** classifies only from the answers of the people whose behavior is in question, under four fixed questions; uses a decision tree that allows "cannot tell"; never reads a prevalence figure as a norm; reports the gap between private belief and perceived expectation; and marks the call provisional.

The method is Bicchieri's. A social norm is a practice people follow because they believe others follow it (an empirical expectation) and expect it of them (a normative expectation), and would drop if those beliefs changed.

## When to use it

### Use it when
- A team says "everyone here does it" or "the community would never accept that" without having asked the people concerned
- Someone asks "is this a norm or just a habit?"
- A program plans a norm message or a public declaration with no evidence that expectations drive the practice

### Do not use it when
- A norm is established and the question is whose approval people track; use `map-reference-network`
- The team wants a survey story that varies what others do and think; use `draft-norms-vignette`
- The diagnosis exists and the team wants the message; use `write-social-norm-message`

## Before you start

Ask these before producing anything. Do not ask anything the user has already answered.

1. **Required.** One practice (who does what, when) and the direction the program wants. "Hygiene" is too wide.
2. **Required.** What the people whose behavior is in question have said (transcripts, notes, survey answers), from how many, chosen how. Or that nothing has been collected.
3. **Required.** Whether the practice is illegal, harmful, or stigmatized.

If 1 or 2 is missing, ask and stop. If nothing has been collected, give the four questions in local wording, mark the call "pending field answers", and stop. If 3 is missing, treat the practice as sensitive.

## What it draws on

- Bicchieri, C. (2017). *Norms in the Wild: How to Diagnose, Measure, and Change Social Norms*. Oxford University Press. https://doi.org/10.1093/acprof:oso/9780190622046.001.0001 Supports: the definitions; agreement about what is appropriate shows no norm until conditional preferences are assessed.
- Bicchieri, C., & Penn Social Norms Training and Consulting Group (2016). *Why Do People Do What They Do? A Social Norms Manual for Viet Nam, Indonesia and the Philippines*. UNICEF Office of Research – Innocenti. https://repository.upenn.edu/pennsong/12 Supports: the four questions, the flow chart in step 2, and the warning in step 6 about "what if" questions.
- Cislaghi, B., & Heise, L. (2018). Theory and practice of social norms interventions: eight common pitfalls. *Globalization and Health*, 14, 83. https://doi.org/10.1186/s12992-018-0398-x Supports: steps 3 and 5.

**Where the evidence comes from:** The framework is theory, taught through UNICEF courses in Southeast Asia. Field studies differ by practice: in Saudi Arabia men underestimated other men's support for women working and acted once told, while in Sudan cutting rates across 45 communities did not fit a practice held by shared expectations. Check locally whether people will state expectations honestly to an outsider.

**Replication status:** Contested for particular practices. The questions have no published reliability test; across 17 studies of contraception norms, no measure was used twice.

## How to do it

1. **Sort what respondents said under four questions,** in their words, with counts:
   - Personal belief: do they think a person like them should do it?
   - Empirical expectation: how many of ten people like them do they think do it?
   - Normative expectation: do people who matter to them think they should? Who?
   - Consequences: what happens to someone who does not; would they still do it if most others stopped?

   Use only answers from the people whose behavior is in question, or from people they name; staff and leaders describe the official position. Write "not asked" where no respondent answered a question.
2. **Classify by the tree, showing each branch.** Would people keep the practice whatever others did? Yes: a custom (it meets their own need) or a moral rule (they hold it right). No: a descriptive norm when what others do is enough to move them; a social norm when what others expect, usually backed by sanctions, also matters. Write "cannot tell" where the answers stop short of a branch, and report groups on different branches separately.
3. **Report the gap** between personal belief and normative expectation. People who misjudge each other can be shown the truth; where most really do favor a harmful practice, publicizing that can make things worse.
4. **List who respondents named and the sanctions:** roles, not names; what happens to those who deviate.
5. **List what else respondents said holds the practice in place:** cost, access, law, beliefs about facts.
6. **Mark the call provisional,** because people struggle to answer "what if everyone stopped?" about their own community. Name what would confirm it: a vignette or experiment that varies what others do and think.
7. **Stop.** Do not draft a message.

See `references/worked-example.md` for a complete run.

## Output template

```markdown
# Social norm diagnosis

**Practice:** <who does what, when; the direction the program wants>
**Answers used:** <how many respondents; who; how chosen; where and when; or "none yet: questions only">
**Sensitivity:** <none stated / sensitive: how the questions were adapted, or which were not asked>

## What respondents said

| Question | Answers, with counts or quotes | What it indicates |
|---|---|---|
| 1. Personal belief | <...> | <for / against / split> |
| 2. Empirical expectation | <...> | <how common they believe it is> |
| 3. Normative expectation | <...> | <who they believe approves or disapproves> |
| 4. Consequences | <...> | <the sanction; would stop if others did: yes / no / split> |

## Classification

**Call (provisional):** <social norm / descriptive norm / custom / moral rule / cannot tell>

- Would people keep the practice whatever others did? <yes / no / split, with the evidence>
- Is what others do enough to move them? <yes / no / cannot tell, with the evidence>
- Does what others expect also matter, with sanctions? <yes / no / cannot tell, with the evidence>

**Gap between private belief and perceived expectation:** <people misjudge each other / a real majority holds the view / cannot tell>

## Who respondents named
<roles named under question 3, and how often>

## Sanctions
<what happens, who does it, who is exempt>

## What else holds the practice in place
<cost, access, law, or factual beliefs respondents raised; or "none raised">

## What would confirm the call
<the vignette or experiment that varies what others do and think; the respondents still missing>

## What to check before relying on this
- <the group most likely to have given the official answer>
- <the branch the answers reached least>
```

## Where it goes wrong

- **Prevalence read as strength.** "70% do it" counts behavior. A practice nearly everyone follows can be a custom; a rare one can carry heavy sanctions.
- **The approved answer.** Where a practice is illegal or campaigned against, people say what the organization wants to hear, or what their community demands. Say which way the pressure runs.
- **Asking "why".** "Why do you do it?" returns reasons that are acceptable to give. Adapt the wording of the four questions, never their structure.

## When to bring in a specialist

Tell the user to consult a local qualitative researcher who knows the practice, with an ethics reviewer, before anyone is asked, when the practice is:
- Harmful or illegal (female genital cutting, child marriage, partner violence): asking who punishes whom can endanger respondents and interviewers
- Stigmatized (HIV status, sexual behavior): asking in a group how many people do it can expose individuals

When answers split cleanly between two groups, a survey researcher designs a sample for each.

Bring them: the practice, the questions in local wording, the sampling plan, and any answers.
