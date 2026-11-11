# Worked example: a WhatsApp agronomy assistant asked for an RCT

A full run of the skill on a realistic case, showing the output it should produce. The case is illustrative, not a real program.

## The request

"MaizeMate is our WhatsApp AI assistant that answers agronomy questions for smallholder maize farmers in western Kenya. The goal is better yields through timely top-dressing. We've piloted with about 1,400 farmers through two cooperatives. Last quarter we benchmarked answers against an agronomist-written test set and 88% were rated acceptable. Usage is spiky: a lot of farmers ask one question and never come back. Our funder wants to discuss an RCT at the October board meeting and we need to decide what to propose. Which evaluation should we run next?"

## The output

```markdown
# What to evaluate next: MaizeMate

**Product:** A WhatsApp AI assistant that answers agronomy questions for smallholder maize farmers in western Kenya. In pilot with about 1,400 farmers through two cooperatives.
**Outcome it is meant to improve:** Maize yields, through top-dressing fertilizer applied on time.
**Decision this informs:** What to propose to the funder at the October board meeting: an RCT, or something else first.

## Recommendation
Run a stage 2 evaluation now: an A/B test of ways to bring farmers back after their first question, judged by the share who return within four weeks. Do not propose the RCT yet. Many farmers ask one question and never return, so a yield trial today would test a product that most of its users have barely used.

## The four stages
| Stage | Question, in the playbook's words | Evidence you have | Verdict |
|---|---|---|---|
| 1. Model | "Does the AI system perform as intended?" | 88% of answers rated acceptable against an agronomist-written test set last quarter. Nothing on unsafe or out-of-scope questions. | Keep monitoring: add test questions on pesticide misuse and on questions outside agronomy before any wider rollout |
| 2. Product | "Does the overall product engage and retain users?" | Your account: "a lot of farmers ask one question and never come back". No retention figure supplied. | Run now: this is the weakest stage, and the later ones depend on it |
| 3. User | "Does the product change users' thoughts, feelings, knowledge and behaviour towards the development outcome?" | None supplied. | Premature: a farmer who asks one question has had too little contact for a change in what they know or do to be detected |
| 4. Impact | "Do users with access to the product improve development outcomes?" | None supplied. | Premature: stages 2 and 3 have no strong evidence, and no partner is yet considering wider adoption |

## Why the later stages are premature
- **Stage 4 (the RCT):** Evidence at stages 2 and 3 is not strong, and no partner is yet considering wider adoption. If a yield trial run now found no effect, nobody could say whether advice by chat does not raise yields or whether farmers did not use it. The staged route answers the funder's question with less risk: fix return use, then show that farmers who use MaizeMate change when they top-dress, then test yields.
- **Stage 3:** Worth preparing, not yet worth running. Choose one or two measures now, such as whether a farmer can say when to top-dress, so they are ready once farmers come back.

## Build now so later evaluation is possible
- Tag every logged conversation with the model, prompt, and knowledge-base version that produced it.
- Bring new cooperatives on in a random order, so that those enrolled later can serve as a comparison group.
- When a new feature launches, keep a randomly chosen group of farmers on the current version.

## What would change this recommendation
- Stage 3 becomes "run now" when a steady share of farmers return within four weeks of their first question.
- Stage 4 becomes "run now" when stage 3 shows that users change when they top-dress, a government or funder is considering wider adoption, and the team has the capacity to work with independent researchers.
```
