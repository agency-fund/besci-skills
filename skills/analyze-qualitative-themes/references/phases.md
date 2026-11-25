# The six phases, with who does what

How each of Braun and Clarke's (2006) six phases is run by a lead and sub-agents, what each phase writes to the working folder, and where the researcher's judgment (or a stand-in for it) comes in.

Before anything else, the user hears the caveat at the top of `SKILL.md`: the method's authors reject generative AI for this analysis. Every sub-agent brief carries it too, so no agent writes as if it were the researcher.

The phases are a guide, not a rule. Analysis moves back and forth: reviewing themes sends you back to coding, and writing changes a definition. Writing starts in phase 1 and does not stop.

## Roles

- **Lead:** the main conversation. Holds the plan, briefs the others, merges their work, and writes.
- **Reader:** one per data item. Reads that item in full and reports on it. A reader for every item is how each item gets full and equal attention, which a single pass over forty transcripts does not give.
- **Challenger:** argues against the lead's themes from the data: extracts that do not fit, another way to read them, a theme that is only a topic.
- **Stand-in analyst (autonomous mode only):** makes the calls a researcher would make and writes the reason for each in `working/decisions.md`. The challenger reviews each call before it stands.

If the host cannot start sub-agents, the lead plays each role in turn, one data item at a time, and writes each role's output to the working folder before starting the next. Do not shorten the reading to save time. If the data set is too large to read in full this way, tell the user how much was read. Never sample silently.

Give every sub-agent the same brief: the question, the choices in `working/plan.md`, the definitions of code and theme, the file to read, the exact output format, and the instruction to copy extracts character for character.

## The two ways to run it

| | With the researcher | On its own |
|---|---|---|
| Who makes the interpretive calls | The researcher, at three checkpoints | The stand-in analyst, checked by the challenger |
| Checkpoint 1, after the plan | The researcher confirms the question and the choices | The stand-in sets them and records why |
| Checkpoint 2, after phase 3 | The researcher reads the candidate themes and map, and merges, splits, renames, or sends themes back | The challenger's objections are answered in writing, then the lead goes on |
| Checkpoint 3, after phase 5 | The researcher approves definitions and names | Same as checkpoint 2 |
| What the report says | Who decided what | That no person made the interpretive calls, and what a person should check |

At a checkpoint, show the work, say what you would lean toward and why, and ask. A researcher who collected the data knows things the transcripts do not hold: ask what they noticed in the field, and what they expected to find, so the analysis can be read against it.

## Working folder

```
thematic-analysis/
├── report.docx              the report
├── thematic-map.png         the final map
└── working/
    ├── plan.md              question, data set, the choices, the mode
    ├── decisions.md         each interpretive call, who made it, and why
    ├── familiarization.md   notes on each item, and first ideas
    ├── codes.json           every coded extract
    ├── code-list.md         every code with its extracts, grouped
    ├── candidate-map.json   themes after phase 3, drawn as candidate-map.png
    ├── review.md            what phase 4 changed, and the challenger's points
    ├── themes.md            definitions, scope, sub-themes, names
    ├── map.json             the final map
    ├── quality-check.md     the 15 criteria and the pitfalls, each answered
    └── report.md            the report as written, before layout
```

## Phase 1: get to know the data

1. Check what the data are: a word-for-word transcript, an interviewer's notes, or a translation. Notes and translations are already someone's interpretation. Mark them in the plan and in every extract taken from them. Ask whether transcripts were checked against the recordings.
2. One reader per item reads it from start to end, then again, looking for meanings and patterns, and writes: who is speaking and in what setting, what the item is about, what stood out, what surprised, what contradicts itself, and first ideas for codes.
3. The lead reads all the notes and as much of the data as fits, and writes a short list of ideas across the data set. In the mode with the researcher, add what they noticed while collecting the data.

Writes `familiarization.md`. Do not skip or shorten this phase: everything later rests on it.

## Phase 2: code

1. One reader per item codes the whole item, start to end, giving every part the same attention. A code is a short label for one feature of the data that bears on the question. In a data-driven analysis, code widely: anything that might matter later. In a theory-driven one, code for what the framework points to and keep a code for what it did not predict.
2. Each coded extract is copied exactly, with a little surrounding talk so its meaning survives being lifted out. An extract can carry several codes. Some passages carry none.
3. Keep accounts that go against the main story. No data set is free of contradiction, and the analysis is not meant to smooth it out.
4. The lead merges labels that mean the same thing into one code list. This is tidying, not a test: readers who agree have not shown that a code is right, and their agreement is not reported. Versions of thematic analysis that measure agreement between coders are a different approach from Braun and Clarke's.
5. Collate: every extract under every code it carries.
6. Run `scripts/check_extracts.py working/codes.json --data <data folder>`. Fix every extract it lists by going back to the data. Read again any item it reports as lightly coded.

Writes `codes.json` and `code-list.md`.

## Phase 3: build candidate themes

1. Sort the codes into candidate themes. Ask of each group: what is the one idea that holds these together, and what does it say about the question? Some codes become themes, some sub-themes, some go nowhere yet.
2. Keep a "set aside" pile for codes that fit nowhere. Discard nothing at this stage.
3. Think about how themes relate: which sit under a broader theme, which pull against each other.
4. Write `candidate-map.json` and draw it with `scripts/draw_map.py`.

A candidate theme that is a topic ("problems with the app") or one of the interview questions is not a theme yet. Name what the data say about the topic.

Checkpoint 2.

## Phase 4: review the themes

Two levels, in this order.

1. **Against the coded extracts.** Read every extract under each candidate theme. Do they form one coherent pattern? If not, either the theme is wrong (rework it, split it, or drop it) or some extracts belong elsewhere (move them, or set them aside). Themes should hold together inside and be clearly different from each other.
2. **Against the whole data set.** One reader per item reads the item again with the candidate map beside it and reports: does the map reflect what is in this item, what does it miss, and which passages should have been coded for these themes and were not. Code what was missed.
3. **The challenger** takes each theme and looks for the extracts that fit it worst, a different reading of the same extracts, and whether one or two vivid speakers carry the theme. A pattern is rarely complete: a theme reported with nothing against it invites doubt.
4. Revise, and write what changed in `review.md`.

Stop when another round only fine-tunes a map that already fits. Recoding can go on forever. More rounds past that point add nothing.

## Phase 5: define and name

For each theme write, in `themes.md`:

1. **The central idea**, in one sentence.
2. **The scope:** what the theme covers and what it does not, in two or three sentences. If that cannot be done, the theme is trying to do too much. Go back to phase 4.
3. **Sub-themes**, where a theme is large enough to need structure.
4. **How it relates** to the other themes, and its part in the overall story the analysis tells about the question. Check that no two themes overlap.
5. **The name:** short, and telling the reader at once what the theme is about. Definitions come before names. A name chosen first tends to bend the theme to fit.

Write the final `map.json`.

Checkpoint 3.

## Phase 6: write the report

See `report-guide.md`. Writing is the last stage of analysis, not a summary of it: choosing extracts and saying what they mean still changes themes. If it does, go back, change `themes.md`, and redraw the map.
