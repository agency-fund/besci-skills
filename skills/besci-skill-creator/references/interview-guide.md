# Interview guide

Question bank for each phase of besci-skill-creator, with a recommended-answer pattern and examples of good and weak answers. One question per turn. Lead with the recommendation when you have one.

## Phase 1: Atomicity gate

**Ask:** "In one sentence, what does the skill do? No 'and'."

Tests to apply silently:
- One verb at the front: decompose, draft, define, design, measure, score, map, adjust.
- One input, one output: "takes `<input>` and produces `<output>`" with no "and" on either side.
- Could a behavioral scientist do it in one sitting with one method?

| Good | Why |
|---|---|
| Decompose a defined behavior into COM-B barrier hypotheses | one verb, one input, one output |
| Draft a saying-is-believing exercise for a target population | one artifact out |
| Adjust a published effect size for publication bias | one operation |

| Too broad | Split into |
|---|---|
| Design a behavior change program | define behavior; diagnose barriers; select levers; draft content; plan test |
| Apply behavioral science to a chatbot | which operation? ask |
| Analyze this program and tell me what's wrong | diagnose barriers; audit psychological needs; pre-mortem |

**If it fails:** "That reads as two skills: A and B. B would take A's output as its input. Which one do we build now?"

**Then ask the two questions that decide whether the skill earns a place** (`skill-spec.md` section 1):
- "Which two sources in `docs/canonical-sources.md` name this task as a step or tool?" If the author can name only one, say so; the skill needs a maintainer's decision to carry the framework.
- "What does this skill make the AI do that it would not do unprompted?" Push past "it's more rigorous" to a fixed output, a required check, a decision rule, verified sources, or a search or script call. The answer becomes the `**What this adds:**` line.

## Phase 2: Name and trigger rule

**Ask for the name:** propose one. "I'd call it `decompose-comb-barriers`. Verb first, kebab-case, under 64 characters. OK?"

**Ask for should-fire phrasings:** "Give me three things a colleague might type that should make this skill fire. In their words, not the method's." Recommended pattern: one phrasing that names the method, one that describes the situation without naming it, one that is a near-miss that should still fire.

**Ask for should-not-fire intents:** "What is the nearest thing someone might ask that this skill should NOT handle, and where should they go instead?" Get at least two.

**Draft the description:** Use when + situation + phrasings + do not use when + nearest adjacent intent + not for + second adjacent intent. Aim for about 500 characters and leave citations out; the navigator does the routing. Read it back and ask "would a model that only sees this sentence fire at the right moments?"

Weak description: "This skill helps you decompose barriers using COM-B." (summary, no trigger, no exclusion)

Strong description: "Use when one behavior is already defined (who does what, when) and you need to know why it is not happening... Do not use when the goal is still vague; run define-key-behavior first. Not for choosing interventions."

## Phase 3: Before you start

**Ask:** "What must the skill know before it can give a good answer? And what should it assume if the user doesn't say?"

Recommended pattern: two or three required questions that change the output, two optional ones that improve it, and an explicit assumption line. Name each input by what it is ("a confirmed barrier, from interviews or any diagnosis"), not by which skill made it.

**If the author says nothing is needed:** "What is the most common way a user gives too little context, and what goes wrong when the model guesses?" If the answer is still "nothing", accept "Not applicable: <reason>" and write the reason verbatim.

## Phase 4: Evidence base

**Ask:** "What does this method rest on? Framework, paper, playbook, or your own practice."

Get: authors, year, title, venue, link, and one line on what each source supports in the skill. Check each one: resolve the DOI or open the page and confirm author, year, and title. Leave out anything that cannot be checked.

**Run the evidence scan** (`skill-spec.md` section 7): reviews and meta-analyses first, then the two or three strongest studies outside wealthy Western countries, then an explicit "none found" naming what was searched. About five searches. It sets `tested_in` and fills `references/evidence.md`.

**Ask where the evidence comes from:** "Which countries and populations were studied, and what should someone working elsewhere check before trusting it?"

**Ask the replication question:** "Has this replicated? Mixed? Contested? Single study?"

Weak: "It's based on best practice." Push: "Whose practice, written down where?"

## Phase 5: Procedure

**Ask:** "Walk me through the steps as you'd do them. At each step, what does a novice get wrong?"

Convert to imperative instructions. Add a "because" clause where the reason isn't obvious. Move anything longer than a screen (question banks, tables, worked examples) to `references/<file>.md` and point to it from the step.

## Phase 6: Output template

**Ask:** "What does a finished output look like? Headings, tables, a checklist?"

Draft the fenced block. Check: could a reviewer, seeing only this template and a run, tell if the run did the job? Add a final "What to check before relying on this" line to every template; it is where the skill names its own weakest assumption.

Then three things every template has (spec section 4, ADR 0009). Open with a placeholder for two or three plain sentences to the user. Read every label aloud: would a program designer say it? Replace method shorthand with plain words, and keep a method's term only where the user needs it for the literature, glossed. End with the "Where you could go from here" closing. **Ask:** "After this output, what do people usually do next, and when would each of those be the wrong move?" Their answer becomes the last step of "How to do it": next moves with conditions, including one outside the library. Copy the shared voice-block markers from the template after the fenced block; `check_sync.py --fix` fills them.

## Phase 7: Failure modes

**Ask:** "When have you seen this method go wrong in practice?" Then: "What would a model do here that an expert never would?"

A failure mode that only repeats a step of the procedure does not count. Patterns worth asking about explicitly: leading questions, confident output on thin input, mislabeling (the COM-B persistence test), too-long outputs, moralizing, recommending the fashionable technique regardless of fit.

## Phase 8: Escalation point

**Ask:** "When should a user stop and get a human specialist? What kind? What should they bring?"

Push on "never": "Imagine a high-stakes case: clinical, legal, children, large budget. Is there still no point where you'd want a specialist?" Accept "Not applicable: <reason>" only for narrow technical transforms.

## Phase 9: Test cases

**Ask:** "Here are four test prompts I'd use. Do they sound like your users?"

Draft them first, named and in this order:
1. `Full run`: a complete request with realistic context; expects the full output.
2. `Missing context`: a thin request; expects the Before-you-start questions and nothing else.
3. `Near the escalation point`: expects what the skill can safely do plus the escalation message.
4. `Wrong skill`: a request that belongs to a neighboring skill; expects a redirect.

`expected_output` is one sentence. `assertions` holds three to six short statements a reviewer can tick yes or no, never the answer text.

## Phase 10: Metadata

Recommend a stage and say why. Suggest two or three tags from the taxonomy's suggested list. Set `produces` to the one thing the output template is, and `consumes` to the inputs the skill cannot run without, matching the required questions in "Before you start". Set `tested_in` from the evidence scan.

## Phases 11 to 14

Write, validate, self-test, package. See SKILL.md. When reporting the self-test, be honest: "partly" is the common verdict for a first draft.
