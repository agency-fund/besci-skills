# The quality check

Braun and Clarke's (2006, table 2) fifteen criteria for a good thematic analysis and their five pitfalls, restated as questions, with the checks this skill adds because the analyst is a language model. Answer each in `working/quality-check.md` before the report is laid out.

Answer every line with yes, no, or partly, and one sentence of evidence. A "no" is fixed or it is reported under "What to check before relying on this". Do not mark a criterion met because a step was run. Mark it met because you looked at the result.

## The fifteen criteria

Restated from Braun and Clarke (2006), table 2.

**The data**

1. Were the data transcribed in enough detail for this analysis, and were the transcripts checked against the recordings? If the data are notes or translations, say so here. This one is the user's to answer. If nobody knows, write "not known".

**Coding**

2. Did every data item get the same attention in coding? Evidence: the extracts-per-item table from `check_extracts.py`.
3. Were the themes built from thorough, inclusive coding of the whole data set, not from a few vivid examples?
4. Have all the extracts relevant to each theme been brought together?
5. Were the themes checked against each other and back against the original data set?
6. Is each theme coherent inside, consistent, and distinct from the others?

**Analysis**

7. Have the data been interpreted and made sense of, not just paraphrased or described?
8. Do the extracts show what the analysis claims they show?
9. Does the analysis tell a convincing, well-organized story about the data and the topic?
10. Is there a good balance between the analyst's narrative and the extracts?

**Overall**

11. Was each phase given enough time, with none rushed or skimmed? For an AI run, the honest evidence is what was read: every item in full, twice, or less.

**The written report**

12. Are the assumptions behind the analysis and its specific approach stated?
13. Does what the report says was done match what was done?
14. Do the language and concepts of the report fit the stance chosen on how to treat what people say?
15. Is the analyst shown as active? Themes do not "emerge" and are not "discovered". Someone built them.

## The five pitfalls

From Braun and Clarke (2006).

1. **No analysis.** Extracts strung together, or commentary that only repeats what an extract says. Test: delete the extract. If the paragraph loses nothing but an illustration and still makes a claim, there is analysis.
2. **The interview questions used as themes.** Test: set the theme names beside the interview guide.
3. **A weak or unconvincing analysis.** Themes that overlap, that do not hold together around one idea, or that rest on one or two extracts. A few striking instances presented as a pattern.
4. **Claims the data do not support.** Extracts that suggest another reading, or contradict the claim. No other reading considered. A pattern presented as complete.
5. **A mismatch between the stance and the claims.** An experience-based analysis that makes claims about social construction, or the reverse. Or an analysis that never states its assumptions and how it was done.

## Checks for an AI analyst

These are not in the paper. They cover what a language model gets wrong in this method.

- **Every quote is in the data.** `check_extracts.py` was run on `codes.json` and on the report, and reports no mismatch.
- **No quote was fixed to fit.** A mismatch was resolved by going back to the data item, not by editing the claim around a reworded quote.
- **Themes are not too tidy.** Three to five themes of equal size, each with three sub-themes, is the shape a model produces by habit. Check that the number and size of themes follow the data.
- **Themes are not topic summaries.** Each theme name could be read as a claim about the question.
- **Speakers are not blurred.** Each extract belongs to the participant it is credited to, and interviewer speech is not quoted as a participant's.
- **Who decided is stated.** `decisions.md` records each interpretive call and whether a person or the stand-in made it, and the Method section says the same.
- **Groups were not read differently.** Where participants differ by sex, language, or status, compare how densely and how charitably each group's items were coded. Coding by a language model can err more for some kinds of respondent than for others.
