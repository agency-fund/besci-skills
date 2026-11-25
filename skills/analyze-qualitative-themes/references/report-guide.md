# Writing the report

How to write phase 6: what each section of the report holds, how to use extracts, what the Method section must say about who did the analysis, and how to turn the Markdown report into a Word file with the map.

Write the report as `working/report.md` in the shape of the output template in `SKILL.md`, from the title to the references. The lead-in and "Where you could go from here" are said in the conversation and stay out of the file.

## What the report has to do

Braun and Clarke (2006) set the task: tell the story of the data in a way that convinces a reader who has not read the data set that the analysis has merit. The account should be concise, coherent, logical, and free of repetition, with enough extracts to show each theme, set inside a narrative that makes an argument about the question.

## Section by section

**Introduction.** The question and why it matters to this program. Cite literature only from sources the user supplied.

**Method.** A reader should be able to tell what was done and why. Cover:

- The data: how many items, of what kind, from whom, collected by whom and when, in what language, and whether they are transcripts, notes, or translations.
- The choices from `working/plan.md`, each with a reason.
- The procedure, phase by phase, citing Braun and Clarke (2006).
- Who did the analysis. Use the statement for the mode, below.
- The quality checks: how many extracts were checked against the data and how many needed correcting, and any of the fifteen criteria not met.

**Findings.** Open with one paragraph that names the themes and the story they tell together. Then the map as Figure 1, a summary table, and one section per theme.

**Discussion.** The overall story and what it means for the question. How it sits with the literature the user supplied. What the analysis cannot claim: who was not interviewed, what was not asked, what rests on notes or translation.

**What to check before relying on this.** The limits that matter for the decision at hand.

**References.** APA 7th edition.

## Writing a theme

Each theme section has a definition, a narrative, and extracts.

1. Start from the definition in `working/themes.md`: the central idea, then what the theme covers and what it does not.
2. Make the analytic point, then show it with an extract, then say what the extract shows that a reader would not get from the extract alone. Vary this order between paragraphs so the section does not read as a form.
3. Go past paraphrase. Braun and Clarke give the questions to ask of each theme: What does it mean? What assumptions lie under it? What follows from it? What conditions are likely to have produced it? Why do people talk about this in this way and not another? What story do the themes tell together?
4. Report what goes against the theme: the participant who said the opposite, the site where the pattern is absent.
5. Even a surface-meaning analysis interprets. The difference from an underlying-meaning analysis is where the themes are found, not whether the analyst thinks.

## Extracts

- Copy every extract word for word from `working/codes.json`. Do not tidy grammar, merge two speakers, or translate again. Use `[...]` where words are left out.
- Put every extract in a block quote that ends with the participant's label in brackets, such as `(CHW-03)`. Block quotes are what `check_extracts.py --report` checks, so a quote placed anywhere else goes unchecked.
- Use labels or pseudonyms, never names. Remove place names and details that would identify someone in a small community.
- Choose extracts that show the point plainly. Two to four for a theme, from different data items. A theme shown only by one speaker is an anecdote, and the reader should be told if that is all there is.
- Mark an extract that comes from an interviewer's notes or a translation.

## Prevalence

Use the unit fixed in the plan. Give counts with their base ("in 9 of the 12 interviews") and keep words such as "most" and "a few" tied to those counts. A count describes the people in the data set. Do not turn it into a percentage or a statement about a population.

## Who did the analysis

The method's authors hold that reflexive thematic analysis is a human practice that needs a positioned, reflexive researcher, and they reject the use of generative AI for it (Jowsey et al., 2026). The report must not present an AI run as their method carried out as they intend. Say which of these applies, in the Method section, in the report's own words:

- **With the researcher.** "The analysis followed the six phases of Braun and Clarke (2006). An AI system (<model, version, date>) read and coded each data item, collated extracts, and drafted candidate themes. <Name or role> set the question and the analytic choices, revised the candidate themes, and approved the final definitions and names. Braun and Clarke consider reflexive thematic analysis a human practice and reject generative AI for it (Jowsey et al., 2026). We report the division of work so readers can judge the analysis with that in mind."
- **On its own.** "This analysis was produced by an AI system (<model, version, date>) following the six phases of Braun and Clarke (2006). No person made the interpretive decisions: one AI agent made each analytic choice and a second argued against it from the data. Braun and Clarke reject the use of generative AI for reflexive thematic analysis (Jowsey et al., 2026), and this report does not claim to be one. It is a first reading of the data, to be checked by someone who knows the participants and the setting."

Then use an actor that is true. Where a researcher decided, write "we" or "I". Where the AI system decided, name it ("the AI analyst grouped"). Never write that themes "emerged" or were "found": someone built them, and the sentence says who.

In the autonomous mode, "What to check before relying on this" always includes: that no person has read the data against the themes, which two or three items a person should read first, and which themes rest most on interpretation.

## Citations

- Cite Braun and Clarke (2006) for the procedure, Clarke and Braun (2017) for the definitions of code and theme, and Jowsey et al. (2026) for the authors' position on AI. Their reference entries are in `evidence.md`.
- Cite any other source only if the user supplied it. Resolve its DOI or open its page and confirm authors, year, and title before it goes in. Leave out what cannot be confirmed, and say so.
- Participants' words are data, not references. They get a label, not a reference entry.
- In text: (Braun & Clarke, 2006). Reference entries in alphabetical order, DOI as a URL.

## Voice

Follow `academic-voice.md`. Two things matter most in a findings section: claims no stronger than the extracts support, and one term for one theme throughout. Use American spelling in the report's own prose and leave participants' words as they are.

## The map and the Word file

1. Write `working/map.json` from `working/themes.md`: the question, each theme with its sub-themes, the relationships worth showing, and the codes set aside. The format is at the top of `scripts/draw_map.py`.
2. Draw it: `python scripts/draw_map.py working/map.json --out thematic-map`. This writes a PNG, an SVG, and a Mermaid file. Look at the picture. If labels touch, shorten the longest names.
3. Put the figure in the report: `![Figure 1. Thematic map of <topic>](../thematic-map.png)`, with a note under it saying what the dashed lines mean.
4. Check the quotes: `python scripts/check_extracts.py working/codes.json --data <data folder> --report working/report.md`.
5. Build the Word file: `python scripts/build_report.py working/report.md --out report.docx`. It sets the report as an APA-style manuscript. Add `--spacing 1.5` for a report that will not go to a journal.

The scripts need matplotlib and python-docx. `uv run` installs them on its own; otherwise `pip install matplotlib python-docx`. If the host has its own tool for Word documents, it can be used instead, with the same structure.

Where no code can run, give the report in the conversation, with the map as the Mermaid block in place of the figure, and say that the quotes were checked by re-reading, not by the script.
