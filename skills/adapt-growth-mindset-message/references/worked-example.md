# Worked example: after-school math sessions in public secondary schools in Peru

A full run of the skill on a realistic case, showing the output it should produce. The case is illustrative, not a real program.

## The request

"Behavior: first-year students in 12 public secondary schools in Cusco attend the free after-school math sessions twice a week. Attendance falls from 70% to 30% after the first graded quiz in week 4. We interviewed 24 students who stopped coming: 15 said some version of 'I got a bad mark, so math is not for me', and four said they have to help at home on those afternoons. Cost, place, and transport are not the problem. Students can retake each quiz once, and tutors go over every wrong answer the next session; we have now announced the retake in every class. We have not asked what classroom teachers say when they hand quizzes back, or what friends say about going to the sessions. We want a growth-mindset lesson for the students who scored below 11 out of 20 on the quiz: one class period of 45 minutes in week 4, on paper, in Spanish, run by the session tutors. Some students read slowly. Six schools get it this term and six next term, so we can compare retake scores and attendance."

## The output

```markdown
The sessions give students a real way to improve, a retake and a tutor who goes over every wrong answer, so I've written the lesson. Two things are still unknown, what classroom teachers say when they hand a quiz back and what friends say about the sessions, so it isn't ready for students until the small test below has asked. Growth-mindset lessons have a small, mixed record, so I haven't promised an effect for Cusco.

# Growth-mindset lesson, adapted

**Behavior:** First-year students in 12 public secondary schools in Cusco attend the free after-school math sessions twice a week.
**The question students are asking:** "I got a bad mark, so math is not for me" (15 of 24 students who stopped attending; interviews after week 4)
**Who receives it:** First-year students who scored below 11 out of 20 on the week-4 quiz.

## Does the school give students a way to improve?
- **After a poor result:** One retake of each quiz, announced in every class; tutors go over every wrong answer the next session (program rules, as described by the team).
- **Teachers:** Not known. Nobody has asked what classroom teachers say when they hand quizzes back.
- **Peers:** Not known.
- **Verdict:** Delivers on feedback and a second attempt. Teachers and peers are not verified; the small test below asks both questions, and the lesson is not for delivery until it has.

## The lesson (working copy; a native speaker redrafts it)
1. **Ability grows with practice.** Nobody is born able to solve equations. A weaver's hands are slow in the first year at the loom and fast in the fifth, and the part of you that does math gets stronger the same way, by being used.
2. **Struggle is part of learning.** A wrong answer on the quiz says "this method is not mine yet". It does not say "math is not for me". The students who are good at math now got these same problems wrong first.
3. **A new strategy or help builds ability.** Doing the same problem the same way again rarely works. Solve it a second way, ask the tutor to show the one step where it went wrong, or explain the problem to a classmate. The retake is there so that you can use what you find.

## Advice task
"Next year a first-year student will get a low mark on this same quiz and think math is not for them. Write that student a letter. Tell them what a low mark means and does not mean, and two things you would do before the retake. We will give your letter, without your name, to a first-year student next year." Students who prefer to speak tell their letter to a tutor, who writes it down.

## Delivery
- **Sessions:** One class period of 45 minutes, on paper; the letter takes the last 15 minutes.
- **When:** Week 4, after the quiz is returned and before the retake.
- **Run by:** Session tutors, briefed for an hour to keep the three claims and the letter, and to leave out "you just need to try harder".

## How you will know
- **Outcome:** Retake score, and attendance over the six weeks after the quiz.
- **Judged on:** Students who scored below 11; the six schools that receive the lesson this term against the six that receive it next term.
- **Shows only that the lesson was received:** One item, "you can get better at math if you practice", asked before the retake.

## What trials have found
Across 63 studies, growth-mindset lessons raised achievement by d = 0.05, a twentieth of a standard deviation, and not significantly once publication bias was corrected for (Macnamara & Burgoyne, 2023). In a US national study, grades rose 0.10 points among lower-achieving students, more where peers favored challenge (Yeager et al., 2019). In urban public schools in Peru a 90-minute session gave a small improvement in math scores, larger outside the capital (Outes-León, Sánchez & Vakis, 2020); in 202 schools in Argentina a similar exercise had no effect (Ganimian, 2020). No effect size is promised for Cusco.

## A small test before use
Eight students who scored below 11, in two schools, read the Spanish draft and restate the three claims and the letter task in their own words. Three math teachers read it and say whether anything in it contradicts what happens in their class. Ask the students what their friends say about going to the sessions, and the teachers what they say when they hand a quiz back. Pass: all eight students can state that ability grows with practice, and no teacher names a contradiction.

## What to check before relying on this
- What classroom teachers say when they return a quiz. If they sort students into those who "have a head for numbers" and the rest, brief them before the lesson runs.
- The lesson does not touch the time barrier: the four students who help at home on those afternoons need a different day, not a message.

## Where you could go from here
That's the adapted lesson.
- Plan the small test with `plan-prototype-test`: the lesson can't be used until that test has asked about teachers and friends, and a plan would say which answers send it back for changes.
- Run it past `audit-intervention-ethics` before week 4: the students are children, and their letters go to next year's first-years, so how the letters are kept anonymous and who reads them is worth checking.
- Ask the schools whether the sessions could also run on another afternoon: the four students who help at home are the one barrier the lesson can't touch, and only the schools can change the timetable.
I'd lean toward planning the small test first, because what teachers say when they hand a quiz back could undo the lesson, and the test is where you find out.
Questions you could ask next: "What should the tutors' one-hour briefing cover?" · "How do we tell whether the lesson helped attendance, not just retake scores?"
```
