# Output-quality rubric

Nine criteria, each scored 0, 1, or 2. Every criterion is derived from a section or shared block every library skill has, so the rubric applies to any skill without customization. Quote the output in the justification.

| # | Criterion | Derived from | 0 | 1 | 2 |
|---|---|---|---|---|---|
| 1 | **Asked first** | Before you start | Produced the full output although required context was missing | Asked some required questions, or asked but produced anyway | Asked the required questions before producing the output when context was missing; did not re-ask what was given; produced when context was sufficient. A brief answer to a question the user asked, before the questions, is not penalized |
| 2 | **Template** | Output template | Shape bears no resemblance to the template | Most sections present, some missing or renamed | Every section of the template present in order; placeholders filled or explicitly left blank with a reason |
| 3 | **Evidence** | What it draws on | No reference to the method's evidence; or a citation not in the skill | Names the framework without saying what it implies | Names the framework and uses it; any citation matches the skill's evidence base |
| 4 | **Mechanism** | How to do it | Tactics only ("send a reminder") | Mechanism named in places | Each recommendation ties to the mechanism the method specifies |
| 5 | **Escalation** | When to bring in a specialist | Escalation condition present in the prompt but not flagged | Flagged vaguely ("consider an expert") | Flagged concretely: what kind of specialist, why, what to bring. Score 2 also when no condition was present and nothing was flagged |
| 6 | **Plain language** | Spec style rules | Jargon undefined; reads as a lecture | Mostly readable; some undefined terms | A program designer with no behavioral-science training could act on it; terms defined on first use |
| 7 | **No invention** | Spec style rules | Invented citations, statistics, or claims about the user's context | Overconfident claims without invention | Uncertainty stated; nothing invented; where the evidence has been tested is stated when the context calls for it |
| 8 | **Failure modes avoided** | Where it goes wrong | Commits a failure mode the skill itself lists | Brushes against one | Avoids every listed failure mode |
| 9 | **Conversation** | The shared voice block and the template's closing | Opens with the skill instead of the user's question, or ends with an instruction ("Next action: ...") | Some of: answers first, marks the run, says where claims come from, offers next moves with reasons | Answers what was asked before offering the run; marks when the run starts and finishes; uses the user's words; says which claims come from the skill and which are general knowledge; ends with two or three next moves, each with its reason, and questions the user could ask next |

Total out of 18. Interpretation for a single run:

- 16 to 18: ready, unless a blocking finding exists.
- 11 to 15: fix first; list the lowest-scoring criteria.
- Below 11: the skill is not doing its job on this case; send the author back to besci-skill-creator with the case and the scores.

**Blocking findings** override the total: any invented citation (criterion 7 at 0), any full output when the case expected questions (criterion 1 at 0 on a "missing context" case), or any missed escalation on a case designed to trigger it (criterion 5 at 0).

## Assertions

Each test case carries three to six assertions: short statements about the output that are true or false. The judge answers each one. Report the number passed per case next to the rubric total. The rubric says how good the output is; the assertions say whether it did the specific things this case is there to check.

## Trigger judgement

For each phrase, the judge sees the skill's `description` and the descriptions of every other skill in the catalog snapshot, then answers: "Would you load this skill for this request? yes or no, one reason." Precision = fired-and-should / fired. Recall = fired-and-should / should-fire. Report both; a skill that never fires has perfect precision and is useless.

## Comparing models, versions, or no skill

To show what a skill adds, run the same cases with no skill loaded and grade them the same way. The gap in assertions passed and in the rubric total is the skill's contribution on those cases. A skill whose outputs score no better than the model alone does not pass the library's "adds something" test.

Report the median total and the range across runs per model. A difference of less than two points on a three-run median is noise. Report blocking findings per model separately, because a model that scores well on average but invents a citation once is not safe.
