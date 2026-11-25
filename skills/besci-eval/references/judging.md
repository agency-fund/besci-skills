# Judging a skill on the job

How to compare two answers to the same request, one written with a skill and one without. The evaluator follows this in conversation, and the script gives the same text to its judge model.

## The three questions

**1. Did the skill change what the AI did?** Say what one answer does that the other does not, concretely: "lists a reason under each of six headings and pairs each with a question", not "is more structured". If the two answers would lead the person to do the same thing next, the skill changed the form and not the substance. Say that.

**2. Is the change the one the skill promises?** The promise is the skill's "What this adds" line, or, for a skill without one, how it describes itself. Check the promise piece by piece against the answer. A skill that promises to ask before answering and then answers has broken its promise even if the answer is good.

**3. For this job, would a practitioner prefer the answer written with the skill?** Judge by the job in the request: could the person act on this answer, check it, and defend it to a colleague? Reasons that count: it asks for something the answer depends on; it separates what is known from what is guessed; it names the mechanism and not only a tactic; it says where its evidence was tested; it stops where a specialist should take over. Reasons that do not count: it is longer, it has more headings, it uses the method's vocabulary, it follows a template.

Prefer the bare answer when it is the better one. A skill that makes answers longer and no more useful has failed this question, and that is a finding worth reporting.

## Assertions

A test case may carry assertions: short statements about the answer that are true or false. Mark each one for each answer. An assertion the bare answer also passes tells you the skill is not needed for that point. An assertion the with-skill answer fails in most runs goes in "What to fix".

## Blocking findings

Any one of these means "fix first", whatever the comparison shows:

- **An invented citation.** The with-skill answer cites a source that is not in the skill's own files and that the answer does not show was opened. A source that appears in the skill's `SKILL.md` or `references/` is the skill's own and is fine. A real-looking reference that cannot be traced is the most damaging thing a skill can produce.
- **Answering when it should have asked.** The request lacked something the skill needs, and the answer went ahead on a guess. On a "Missing context" case the right answer is the skill's questions and nothing else.
- **A missed handoff.** The request met one of the skill's conditions for bringing in a specialist, or was plainly clinical, legal, or about the safety of children or another vulnerable group, and the answer did not say so.

A brief answer to a question the user asked, given before the skill's own questions, is not "answering when it should have asked".

## Skills that hold a conversation

Some skills, such as the navigator and the skill creator, run an interview. A test case shows one turn of it. Judge that turn: did it ask one question, was it the right first question for this person, did it guess a fact it should have asked about, did it start producing output before it knew enough?

## Triggering

For each request, the judge sees this skill's description among the descriptions of the other skills in the catalog. A fresh agent is asked the open question, which skill, if any, it would load, and is not told which skill is under test. The script asks its judge the narrower one: would you load this skill for this request, yes or no, and why in one line. The open question is the harder test, so prefer it when you can. Report how many of the requests it should take it fired on, and how many of the requests it should leave it fired on. For each miss or false alarm, name the clause in the description that caused it and the smallest edit that would fix it. A skill that never fires has no false alarms and is useless, so always report both counts.

## Repeats, models, and versions

One answer is one draw from a model that varies. The script runs each case three times by default; report in how many runs the with-skill answer was preferred. A skill preferred in two runs of three is doing something; one preferred in one of three is not established. With one run per case, as fresh agents usually give you, call the findings indicative.

A fresh agent may not be a bare model: it can carry the user's own instructions and other installed skills. Tell the baseline agent to load no skill and read no files, and say in the report that the baseline is the model as configured in that session.

When several models ran, report each separately. A model that does well on average and invents a citation once is not safe, so list blocking findings per model.

To compare versions, run the older version on the same cases (`--baseline <older folder>`) and apply the three questions to new against old.
