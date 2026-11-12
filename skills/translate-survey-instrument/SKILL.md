---
name: translate-survey-instrument
description: >-
  Use when survey questions exist in one language and are needed in another
  ("translate our survey into Chichewa", "should we back-translate?"), or
  when a translation exists with no record of how it was made. Sets up two
  independent translations, a review by people who know the respondents, a
  recorded decision on back-translation, and an item-by-item log. Do not use
  when the questions are not written yet; use draft-survey-items. Not for
  checking that respondents understand a finished translation; use
  draft-cognitive-interview-script.
license: CC-BY-4.0
metadata:
  title: Translate a survey into another language
  type: atomic
  stage: measure
  version: "0.3.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  tested_in: mainly-western
  tags: "measurement, survey-design"
  consumes: "survey-items"
  produces: "survey-items"
---

## What it does

Carries an existing survey instrument into another language through two independent translations reviewed by people who know the respondents.

**What this adds:** requires each item's meaning before anyone translates; sorts items into close translation, adaptation, or concept in doubt; requires two translators working apart and a reviewer who knows how respondents speak; makes back-translation (translating the result back for comparison with the source) a recorded decision, never the only check; labels any wording the AI proposes as a draft; and logs every departure from the source, item by item.

## When to use it

### Use it when
- A team has questions in one language and will survey in another: "we need the Chichewa version"
- A translation exists with no record of how it was made
- Interviewers translate aloud during interviews
- Someone asks "should we back-translate?"

### Do not use it when
- The questions are not written yet; use `draft-survey-items`
- The translation is done and the need is to check that respondents understand it; use `draft-cognitive-interview-script`

## Before you start

Ask these before producing the translation record. Do not ask anything the user has already answered.

1. **Required.** The source items word for word, with answer options and consent text. For a published scale: its name, and whether a tested version in the target language exists (if unknown, tell the user to look first).
2. **Required.** The target language, the variety spoken where the survey runs, and whether items are read aloud.
3. **Required.** What each item is meant to measure, a phrase each.
4. **Required.** Who is available: fluent speakers, any trained translator, anyone who knows how respondents speak.
5. Optional. Translations the team already has.
6. Optional. Whether a funder or scale owner requires back-translation.

If 1, 2, or 3 is missing, ask and stop. If 4 is missing, plan for two translators and name the gap. If 5 is missing, fill the brief and mark the rest "pending". If 6 is missing, assume no requirement.

## What it draws on

- Kopper, S., & Parry, K. (2023). *Survey design*. J-PAL Research Resources. https://www.povertyactionlab.org/resource/survey-design Supports: a second independent translator, an adjudicator, translating consent text, everyday words, a trained translator.
- European Social Survey (2022). *ESS Round 11 Translation Guidelines*. ESS ERIC Headquarters. https://www.europeansocialsurvey.org/sites/default/files/2024-08/ESS_R11_Translation_Guidelines.pdf Supports: the sequence of translation, review, adjudication, pretesting, and documentation (known as TRAPD), with at least two translators.
- Behr, D., & Braun, M. (2023). How does back translation fare against team translation? An experimental case study in the language combination English–German. *Journal of Survey Statistics and Methodology*, 11(2), 285–315. https://doi.org/10.1093/jssam/smac005 Supports: back-translation is never the only check.
- Epstein, J., Osborne, R. H., Elsworth, G. R., Beaton, D. E., & Guillemin, F. (2015). Cross-cultural adaptation of the Health Education Impact Questionnaire: experimental study showed expert committee, not back-translation, added value. *Journal of Clinical Epidemiology*, 68(4), 360–369. https://doi.org/10.1016/j.jclinepi.2013.07.013 Supports: review by a group.

**Where the evidence comes from:** The two experiments that compare methods translated from English into German and French. In both, review by a team improved accuracy more than back-translation did, though in the German study most errors left in did not change survey answers. The scan found no such comparison in a low- or middle-income country; check locally which variety respondents speak and whether each idea exists in it.

**Replication status:** Contested. The experiments favor team review, yet a review of 31 guidelines found no consensus and little evidence on which method is best.

## How to do it

1. **Attach the meaning to every item.** Translators work from what the item measures, not from its words.
2. **Sort each item:** close translation; adapt (swap an example, unit, or place for the local one); or concept in doubt (the idea may not exist in this form). List doubts as open questions.
3. **Set the register:** the everyday spoken words of the respondents' variety, because items are heard, not read.
4. **Name the team:** two translators who do not see each other's version, a reviewer who knows how respondents speak, an adjudicator who knows what the survey measures and settles disagreements. Say which role nobody fills.
5. **Compare the versions item by item** once they exist. Where the two differ, the meaning is unstable: propose a choice or a merge, and leave the decision and its reason to the reviewer and adjudicator.
6. **Decide on back-translation and record the reason.** Do it when it is required or when no reviewer reads both languages, with a translator who has not seen the source. It raises false alarms and misses real errors, so a mismatch is a question for the reviewers and a clean result is not a pass.
7. **Log each departure** from a close translation, with the reason, so that later rounds do not undo it.
8. **List what to test with respondents:** items where the translators differed, and concepts in doubt.
9. **Mark your own wording.** Any target-language text you propose is a draft no speaker has checked; it replaces neither translator.

See `references/worked-example.md` for a complete run.

## Output template

```markdown
<Two or three plain sentences to the user: where the translation stands, the items or concepts most likely to shift in meaning, and that it is untested until respondents have been asked what the items mean.>

# Translation record: <instrument>, <source language> to <target language and variety>

**Respondents:** <who, region, schooling; read aloud or self-completed>
**Published scale:** <no / yes: name; existing version in the target language; whether scores must stay comparable>
**Team:** <translator A; translator B; reviewer who knows the respondents; adjudicator; first language and training of each; roles nobody fills>
**Status:** <before translation / translations in, review pending / agreed by the reviewers, not yet tested with respondents>

## 1. Brief for the translators
| Item | Source text | Meant to measure | Approach | Watch for |
|---|---|---|---|---|
| <1> | <word for word, with options> | <...> | <close / adapt / concept in doubt> | <term, time period, or scale label likely to shift> |

**Also translate:** <consent text, instructions, transitions, answer options>
**Register (the kind of words to use):** <everyday spoken words of <variety>; technical terms that stay in <source language>>

## 2. The two translations and the version agreed
| Item | Translation A | Translation B | Proposed or agreed version | Decided by, and why |
|---|---|---|---|---|
| <1> | <text; or "pending"> | <...> | <...> | <"proposal, for the reviewers" until they decide> |

## 3. Back-translation (translating the result back for comparison)
**Decision:** <not done / done for all items / done for items ...>, because <...>
<if done: by whom; the mismatches the reviewers discussed; what changed>

## 4. Agreed instrument, as read aloud
<consent text, instructions, each item with its options; or "pending">

## 5. Decision log
| Item | Departs from a close translation? | Why | Leave as is in later rounds? |
|---|---|---|---|
| <1> | <...> | <...> | <yes: reason / no> |

## 6. To test with respondents
This translation is untested until respondents have been asked what the items mean.
- <item the translators disagreed on, or concept in doubt, and what to listen for>

## Open questions
- <a concept the reviewers could not place; a comparability concern for a published scale>

## Where you could go from here
<One line saying the translation record is done, and what in it is still pending.>
<Two or three next moves that fit what this run found, each with why it would help and when it fits. Candidates:
- `draft-cognitive-interview-script`, when a version is agreed and the items listed to test, especially concepts in doubt, need trying with respondents
- `adapt-survey-for-phone-mode`, when the translated instrument will be asked by phone
- `draft-survey-items`, when the team found a fault in a source item, so it is fixed in the source and translated again rather than repaired in translation
- the review meeting, when translations are in and the proposals still need the reviewer and adjudicator
- a search for a tested version in the target language, when the instrument is a published scale and nobody has looked
- a psychometrician or a specialist in cross-cultural surveys, when a cut-off decides referral or eligibility, or scores will be compared across languages>
Questions you could ask next: "<question>" · "<question>"
```

<!-- shared: template/shared/voice.md. Edit it there, then run scripts/check_sync.py --fix. -->
**How to talk with the user**

- If the user asked a question rather than asked for this skill's output, answer the question first, in a few plain sentences. Then offer the run and say what it would add.
- Mark the run. When it starts, say so in one line: the skill, and what it will produce. When the output is done, say the run is finished. The user should always know when the library's method is in force.
- Talk with the person, not at them. Use their words for their program and the people in it, say why you ask each question, and say what you are unsure of. No praise, no filler.
- Say where each claim comes from: this skill's sources, your general knowledge, or nothing in the library. A number the sources do not give, such as how many interviews to run, is your judgment; say so, and why you chose it.
- End with the template's closing: two or three next moves that fit what this run found, each with its reason and when it fits, and one or two questions the user could ask next. Say which move you would lean toward and why; the user decides.
<!-- /shared -->

## Where it goes wrong

- **Improving the source.** The model tidies a clumsy source item while translating it, and the two versions then ask different things. Report the fault; do not repair it in translation.
- **Changes that never reach the record.** Fixes agreed aloud in interviewer training, or made in the field, leave several versions in use. Every later change goes into the log.
- **Calling it equivalent.** A reconciled translation has not been shown to measure what the source measures; never call it validated.

## When to bring in a specialist

Tell the user to consult a psychometrician (who tests whether scores mean what they claim) or a specialist in cross-cultural surveys when:
- The instrument is a clinical screener whose cut-off decides referral or eligibility; a cut-off does not carry over to a translation
- Scores will be compared across languages or countries, or against a published norm
- The reviewers cannot find words for a concept, which may not exist here in the same form

Bring them: the decision log, the items the translators disagreed on, and notes from any testing with respondents.
