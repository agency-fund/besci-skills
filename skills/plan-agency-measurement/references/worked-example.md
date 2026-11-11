# Worked example: an AI mentor for student entrepreneurs

A full run of the skill on a realistic case, showing the output it should produce. The case is illustrative, not a real program.

## The request

"Here is the agency definition for Pitch Partner, our WhatsApp AI mentor for Class 11 students in Delhi government schools during a 12-week entrepreneurship course. Working definition: a student's capability to form, defend, and revise a business idea of their own, and to judge when the mentor's input helps. Constructs: (1) ownership of the goal and (2) entrepreneurial self-efficacy, both internally experienced, with respect to the end goal; (3) revising after feedback, externally expressed, end goal; (4) appropriate reliance on the mentor, externally expressed, digital tool. We are focusing on 2, 3, and 4. We need to decide whether to switch the mentor from its 'direct' mode, which suggests ideas straight away, to a mode that asks students questions first; a funder report may follow. Students consented to their chats being analyzed for program improvement. We track messages per student and thumbs-up on replies. Teachers observe one class session a week, and the course ends with a pitch scored by a panel on a rubric. We can afford a 20-minute in-person survey in week 1 and week 12. We won't compare schools or languages. For items, give us drafted examples now and search queries for published scales."

## The output

```markdown
# Agency measurement plan: Pitch Partner (AI mentor for student entrepreneurs)

**Definition:** A student's capability to form, defend, and revise a business idea of their own, and to judge when the mentor's input helps. Focus: entrepreneurial self-efficacy (2), revising after feedback (3), appropriate reliance on the mentor (4).
**Decision this plan supports:** Keep the direct mode or switch to the questions-first mode; a funder report may follow.
**Assumed:** The students' consent covers analysis of a de-identified copy of their chats by a language model. Confirm with the ethics reviewer before any coding.
**Do not go ahead as proposed:** Do not compare the two modes on the model-coded measure (#3) until it has been checked against human coders in both modes. Until then, compare modes on #4, #5, and #6.

## Measures on the 2x2 agency framework
| | With respect to the end goal: a workable business idea | With respect to the digital tool: the AI mentor |
|---|---|---|
| **Internally experienced** (thoughts and feelings) | **On-platform:** one-item confidence check in the chat right after the student revises the idea, weeks 3, 6, and 9 (#1)<br>**Off-platform:** entrepreneurial self-efficacy scale in the week 1 and week 12 survey (#2) | Not in focus |
| **Externally expressed** (choices and actions) | **On-platform:** model coding of chats for setting and revising the idea, weekly; experimental (#3)<br>**Off-platform:** panel's pitch rubric, week 12 (have) (#4) | **On-platform:** share of turns that hand a decision to the mentor against turns that push back on or edit its suggestion, weekly (#5)<br>**Off-platform:** teacher observation of whether a student can explain the idea without the phone, weekly (have; needs a checklist) (#6) |

Data the team already collects is marked "(have)".
**In no cell:** Messages per student measure use. Thumbs-up on replies measure satisfaction. Students can chat a lot and like the replies while the mentor does the thinking.

## Measure details
| # | Instrument | Items | Source | Evidence, and what to check here | Use, adapt, or build |
|---|---|---|---|---|---|
| 1 | Single in-chat item, three labeled options | Drafted example, not from the literature: "How sure are you that you can make your idea work? Not sure / A little sure / Very sure" | Self-efficacy (Bandura, social cognitive theory) | Single items track multi-item measures only in part; check against #2. Ask about the idea, not about the mentor | Build |
| 2 | Entrepreneurial self-efficacy scale for Class 11, in Hindi and English | Not accessed: no published scale opened in this session; see the first query below | Self-efficacy (Bandura, social cognitive theory); the published scale, once found | Unknown until a scale is found: check who it was validated with, then test wording and response format with Class 11 students in Hindi | Adapt, once found |
| 3 | Coding instruction with low, medium, and high anchors for setting, testing, and revising the idea | Drafted example anchor, not from the literature: "High: the student changes the idea in response to a critique and says why" | Forethought, self-reactiveness, and self-reflectiveness (Bandura, 2001, https://doi.org/10.1146/annurev.psych.52.1.1) | Untested until compared with trained human coders on these chats, in mixed Hindi and English; a chat shows what students write, not what they do outside it | Build; experimental |
| 4 | The course's pitch rubric | The course's own criteria | The course | Agreement between panelists unknown; a strong pitch can come from the mentor's wording, so read it with #5 and #6 | Use; double-score a sample |
| 5 | Log coding rule for handing over versus pushing back | Drafted example rule, not from the literature: count turns like "just pick one for me" or "write my pitch" as handing over, and turns that reject or rewrite a suggestion as pushing back | Appropriate reliance (Lee & See, 2004, https://doi.org/10.1518/hfes.46.1.50_30392); answer-seeking (Bastani et al., 2025, https://doi.org/10.1073/pnas.2422633122) | Copying text outside WhatsApp is invisible. Asking the mentor to check the arithmetic in a budget, by choice, is delegation, not handing over | Build |
| 6 | Observation checklist for teachers | Drafted example, not from the literature: "Explains the idea in their own words without looking at the phone: yes / partly / no" | Unassisted capability (Bastani et al., 2025) | Teachers see one session a week; being watched can change what students do | Build on the existing observation |

## Testing, sized to the claim
| # | Check | Keep if | Revise or drop if |
|---|---|---|---|
| 1, 2 | Cognitive interviews with 8 students on #1 and #2, in Hindi; then correlate #1 with #2 in one pilot class | Students read the items as intended, and #1 moves with #2 | Items misread: reword them. #1 does not track #2: keep it as a separate signal and do not report it as self-efficacy |
| 3 | Two trained coders code 150 weekly chat segments, stratified by mode, school, and language mix, and agree first; then compare the model with their consensus | The model's agreement with the coders is close to theirs with each other, and above 0.8; errors do not cluster by mode or language mix | Below, or clustered: do not use #3 to compare modes; keep human coding on a sample |
| 4 | Two panelists double-score 20 pitches | The two scores agree | Low agreement: revise the rubric's anchors before comparing modes |
| 5 | Read 50 turns flagged by #5 by hand | Flagged turns mean what the rule says | Many wrong flags: revise the rule |
| 5, 6 | Compare #5 with #6 by mode | Both point the same way | #5 rises in the direct mode while #6 shows students cannot explain their ideas: treat it as erosion, whatever #1 says |

**Specialist to bring in:** None for the mode decision. Before a funder report, a psychometrician for #2 and a researcher who has checked model coding against human coders for #3.

## What to find out next
- A published entrepreneurial self-efficacy scale for secondary-school students: "Validated scales of entrepreneurial self-efficacy for secondary-school students in India or other low- and middle-income countries: items, response format, validation sample, and known limits in Hindi. Cite sources."
- Whether handing decisions to the mentor relates to what students can do unaided: "Studies linking AI chat behavior (answer-seeking, delegation) to unassisted performance among adolescents. Which behaviors were measured, and how were they validated? Cite sources."
```
