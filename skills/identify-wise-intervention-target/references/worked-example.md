# Worked example: first-year students in public secondary schools in Peru

A full run of the skill on a realistic case, showing the output it should produce. The case is illustrative, not a real program.

## The request

"Behavior: first-year students in 12 public secondary schools in Cusco attend the free after-school math sessions twice a week. Attendance falls from 70% to 30% after the first graded quiz in week 4. The sessions cost nothing, are held in the students' own school, and end before the last bus. We ran 24 interviews with students who stopped coming. Fifteen said some version of 'I got a bad mark, so math is not for me.' Nine said 'the ones who stay are the ones who were always good.' Four said they had to help at home on those afternoons. Students can retake each quiz once, and tutors go over every wrong answer the following session. The ministry wants a growth-mindset message. Is that the right call? This is for a 12-school pilot with a comparison group."

## The output

```markdown
Most students who stop are asking one question: does a bad mark mean I cannot do math? That fits the ministry's growth-mindset idea, but the four students who help at home have a time barrier that no message will fix. The setting can back a new answer, since every quiz can be retaken and tutors go over every wrong answer, provided students know the retake exists.

# The question first-year math students in Cusco are asking themselves

**Behavior:** First-year students in 12 public secondary schools in Cusco attend the free after-school math sessions twice a week.
**Evidence that a belief is the barrier:** Attendance falls from 70% to 30% after the first graded quiz, while cost, place, and transport stay the same.
**Audience's words used:** 24 interviews with students who stopped attending, after week 4.

## How the audience reads the situation

| Interpretation, in their words | Said by | Material barrier behind it | If that were fixed, would the behavior follow? | Material, meaning, or both |
|---|---|---|---|---|
| "I got a bad mark, so math is not for me" | 15 of 24 | None: the sessions are free, on site, and end before the last bus | Not applicable | Meaning |
| "The ones who stay are the ones who were always good" | 9 of 24 | None | Not applicable | Meaning |
| "I have to help at home on those afternoons" | 4 of 24 | Time | Yes: a different day or a shorter session would bring these students back | Material |

## The question
- **The need behind it:** To understand (can I get better at this?)
- **Question, in the audience's words:** "Does a bad mark mean I cannot do math?"
- **Why this one and not the others:** It is the most common reading, and it follows the event that precedes the drop. "The ones who stay were always good" is a belonging reading and comes second; it may be a consequence of the first, since those who stay are those who did not take the quiz as a verdict. The time barrier is real for four students and needs a schedule change, not a message.
- **When people start asking it:** The return of the first graded quiz, in week 4.

## What the setting offers
- **A new answer would promise:** A low first mark is where learning starts, and marks rise with practice.
- **The setting provides:** One retake of each quiz, and tutors who go over every wrong answer the next session (program rules, as described by the team).
- **Does the setting deliver?** Delivers, if the retake is offered to everyone and not on request. Not verified: whether students know the retake exists.

## What trials of this kind of intervention found
Beliefs about ability. Across 63 studies, growth-mindset interventions raised achievement by d = 0.05, an effect that disappeared after correcting for publication bias (Macnamara & Burgoyne, 2023). In urban public schools in Peru, a 90-minute session produced a small improvement in math scores, larger outside the capital (Outes-León, Sánchez & Vakis, 2020). In Argentina a similar exercise in 202 schools had no effect (Ganimian, 2020). No effect size is promised for Cusco.

## What to check before relying on this
- The belonging reading rests on nine students. Ask the next ten who stop attending which of the two readings is theirs.
- Whether students know they can retake the quiz. If they do not, announce the retake before any message about ability.

## Where you could go from here
That's the analysis.
- The tutors, on whether students know about the retake: if they do not, announcing it comes before any message about ability, and the setting check moves from "not verified" to "delivers".
- `adapt-growth-mindset-message`, once the retake is confirmed and offered to everyone: it would fit the lesson to these schools and time it for the return of the week-4 quiz.
- `select-intervention-levers`, for the four students who help at home: theirs is a time barrier, and a change to the schedule is the kind of fix it needs.
I'd lean toward checking the retake first, because it is cheap and a growth-mindset message only promises something true if students can use the retake.
Questions you could ask next: "How would the message reach students before the first quiz comes back?" · "What should the 12-school pilot measure besides attendance?"
```
