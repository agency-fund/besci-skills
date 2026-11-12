# Worked example: an AI mentor for student entrepreneurs

A full run of the skill on a realistic case, showing the output it should produce. The case is illustrative, not a real program.

## The request

"Pitch Partner is a WhatsApp AI mentor for Class 11 students in government schools in Delhi. They use it during a 12-week entrepreneurship course, in a mix of Hindi and English, mostly on a parent's phone in the evening. The course ends with a pitch scored by a panel. When we say agency we mean: students come up with a business idea that is really theirs, feel confident they can make it work, keep improving it when the mentor or the panel pushes back, and can tell when the mentor's suggestion is a bad one. Our worry is the mentor's default 'direct' mode, which suggests ideas straight away; we think students lean on it. So far we track messages per student and thumbs-up on replies, and both look good. Can you help us pin down what we are trying to measure?"

## The output

```markdown
What you mean by agency is a student's ability to form, defend, and revise a business idea of their own, and to judge when the mentor's input helps. Your four parts match four named ideas from research and fill three of the grid's four cells; the one left open is whether students feel free to question the mentor. The focus and the warning signs below are my proposal for you to confirm, and the whole definition is a hypothesis until students have been asked.

# What agency means for Pitch Partner's users

**Context:** Class 11 students in Delhi government schools use a WhatsApp AI mentor during a 12-week course to develop a business idea they will pitch to a panel. The mentor is meant to help them think, not to think for them.
**In your words:** "Students come up with a business idea that is really theirs, feel confident they can make it work, keep improving it when the mentor or the panel pushes back, and can tell when the mentor's suggestion is a bad one."
**Working definition:** A student's capability to form, defend, and revise a business idea of their own, and to judge when the mentor's input helps and when it does not.
**What your usage numbers measure instead:** Messages per student measure use. Thumbs-up measure satisfaction. Students can chat a lot and like the replies while the mentor does the thinking.

## Your definition, matched to theory
| # | What you said | Construct (a defined, measurable idea) | Theory |
|---|---|---|---|
| 1 | "a business idea that is really theirs" | Ownership of the goal: the idea comes from the student's own aims, not the mentor's | Goal setting (Donald et al.); relative autonomy (self-determination theory) |
| 2 | "feel confident they can make it work" | Entrepreneurial self-efficacy: belief in one's capability to develop and pitch a workable idea | Bandura, social cognitive theory |
| 3 | "keep improving it when the mentor or the panel pushes back" | Revising after feedback | Bandura: self-reactiveness |
| 4 | "can tell when the mentor's suggestion is a bad one" | Appropriate reliance: following the mentor when it is right and not when it is wrong | Lee & See, trust in automation |

## Where it sits in the 2x2 agency framework
| | With respect to the end goal: a workable business idea | With respect to the digital tool: the AI mentor |
|---|---|---|
| **Internally experienced** (thoughts and feelings) | Entrepreneurial self-efficacy (2); ownership of the goal (1) | Open: e.g., feeling free to question or reject the mentor's advice |
| **Externally expressed** (choices and actions) | Revising after feedback (3) | Appropriate reliance (4) |

**Focus:** Proposed; confirm. Both expressed cells, plus self-efficacy: your worry is about what students do with the mentor's suggestions, and the panel rewards confidence.
**Not covered by this focus:** Whether students feel able to question the mentor. A student who disagrees in silence and goes along with the suggestion would look, in the logs, like one who judged it sound.
**Signs the tool is wearing agency down:** Proposed; confirm. Asking the mentor to choose the idea; pasting the mentor's wording into the pitch; no revision after critique; being unable to explain the idea in class without the phone. Asking the mentor to check the arithmetic in a budget, by choice, is delegation and not one of these signs.

## What to check before relying on this
- "Really theirs" is the least settled part. Ask whether an idea a student took from a parent's business counts as their own.
- Ask five students what a classmate who is "in charge of" their own pitch does differently. If their answers do not match rows 1 to 4, revise the rows before measuring anything.

## Where you could go from here
That's the definition.
- Talk to five students before anything else: "really theirs" is the least settled part, and if students describe being in charge of a pitch differently from rows 1 to 4, the rows change and so does everything measured from them.
- Plan the measures with `plan-agency-measurement` once you have confirmed the focus: three of the four constructs sit in the cells you care about, and some of the warning signs (pasted wording, no revision after critique) may already be visible in the chat logs.
- Work out which evaluation of Pitch Partner comes next with `choose-ai-eval-level`, if your worry about the "direct" mode is heading toward a comparison of modes: agency would then be one outcome among several.
I'd lean toward the student conversations first, because they are cheap and they decide whether the rows are worth measuring at all.
Questions you could ask next: "Should an idea a student took from a parent's business count as their own?" · "How could we tell from the chat logs whether a student weighed the mentor's suggestion or just took it?"
```
