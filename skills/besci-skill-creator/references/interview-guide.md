# Interview guide

Questions that work when interviewing an author about a method, and how to turn the answers into a library skill. The interview follows the method and the author; this file is a map of the ground, to check against, and not a script to read out. Put these to the author one at a time, with your recommended answer when the question is a decision, and ask a question only once the ones it depends on are settled.

## The gates

**One thing.** Ask: "In one sentence, what does the skill do?" Listen for "and". Tests to apply silently:

- One verb at the front: decompose, draft, define, design, measure, score, map, adjust.
- One input, one output.
- A behavioral scientist could do it in one sitting with one method.

| Good | Why |
|---|---|
| Decompose a defined behavior into COM-B barrier hypotheses | one verb, one input, one output |
| Draft a saying-is-believing exercise for a target population | one thing out |
| Adjust a published effect size for publication bias | one operation |

| Too broad | Split into |
|---|---|
| Design a behavior change program | define the behavior; diagnose barriers; select levers; draft content; plan the test |
| Apply behavioral science to a chatbot | which operation? ask |
| Analyze this program and tell me what's wrong | diagnose barriers; review a prior intervention; audit the ethics |

When it fails: "That reads as two skills, A and B. B would take A's output as its input. Which one do we build now?"

**Common.** "Which two sources on the library's list name this task as a step or tool?" Read `canonical-sources.md` yourself first and offer the two you would pick. If only one names it, say so: the skill needs a maintainer to decide whether the library carries the framework.

**Adds something.** "If I asked a good AI model to do this with no skill, what would it get wrong or leave out?" The answer becomes the `**What this adds:**` line. "It would be less rigorous" is not an answer yet. Push to a fixed output, a required check, a decision rule, verified sources, or a search or script call.

**Distinct.** Read the catalog and name the nearest existing skill: "The library has `decompose-comb-barriers`. How is what yours produces different from that?"

## The ground, with questions that work

**What it is for, and who reaches for it.**
- "Who is stuck, and on what, at the moment they need this?"
- "Give me three things a colleague might type when they need it. In their words, not the method's." Aim for one that names the method, one that describes the situation and does not name it, and one near-miss that should still fire.
- "What is the nearest thing someone might ask that this should not handle? Where should they go?" Get at least two.

**How an expert does it.**
- "Walk me through it as you would do it on a real case. What is the first thing you look at?"
- At each step: "What does someone new get wrong here?" and "Why does this step come before the next?"
- "Is there a step people skip that you never would?"

**What it needs before it starts.**
- "What do you need to know before you can do this well?"
- "What is the most common way someone gives you too little, and what goes wrong when you guess?"
- If the author says nothing is needed, ask the second question once more with an example. If the answer is still nothing, accept it and write their reason into the section.

**What good looks like.**
- "Show me, or describe, a result you were happy with. What is on the page?"
- "If I handed you two results, how would you tell the good one from the bad one in thirty seconds?"
- "What would you tell the reader to check before relying on it?"

**Where it goes wrong.**
- "When have you seen this method go wrong in practice?"
- "What would an AI model do with this that an expert never would?"
- A failure that only repeats a step does not count. Patterns worth asking about by name: leading questions, a confident result from thin input, mislabeling, results that run too long, moralizing, reaching for the fashionable technique whatever the fit.

**Where a specialist takes over.**
- "When would you tell someone to stop and call you, or someone like you?"
- "What kind of specialist, and what should they bring to that conversation?"
- Push on "never": "Take a high-stakes case: clinical, legal, children, a large budget. Still no point where you would want a specialist in the room?"

**What it rests on.**
- "What does this rest on? A framework, a paper, a playbook, or your own practice?"
- "Which countries and populations was it studied in, and what should someone working elsewhere check before trusting it?"
- "Has it replicated? Mixed, contested, a single study?"
- For each source, get enough to find it, then open it yourself and confirm author, year, and title. Leave out what you cannot open.

**What happens next.**
- "After someone has this result, what do they usually do? When would each of those be the wrong move?"

Weak answers and how to push:

| The author says | Ask |
|---|---|
| "It's based on best practice." | "Whose practice, written down where?" |
| "It helps teams think about barriers." | "What does a team have at the end that it did not have at the start?" |
| "It depends." | "On what? Give me the two cases that differ most." |
| "The model should use judgment." | "What would you look at to make that call?" |

## From the interview to the eight sections

The author never sees this table. It is how you sort what you heard.

| What you heard | Where it goes |
|---|---|
| The one sentence; what the AI gets wrong unprompted | `## What it does`, with the `**What this adds:**` line |
| What people type; the nearest things it should not handle | `description`, and `## When to use it` with its two lists |
| What the expert needs first, and what to assume when it is missing | `## Before you start`. Name each input by what it is, not by the skill that made it |
| Frameworks and sources; where tested; replication | `## What it draws on`, `references/evidence.md`, `metadata.tested_in` |
| The steps, with the reason for each | `## How to do it`, in the imperative. Anything longer than a screen moves to `references/` |
| What a good result looks like; what to check before relying on it; what people do next | `## Output template`: a fenced block that opens with a plain lead-in, uses labels a program designer would use, and ends with "Where you could go from here". The shared voice block follows it; copy the markers from the template |
| When it has gone wrong; what a model would do | `## Where it goes wrong`, at least three, plus what is out of scope |
| When to stop and call someone | `## When to bring in a specialist` |
| A real case the author described | `references/worked-example.md`, and the "Full run" test case |

**The description.** "Use when" plus the situation, the phrasings, "Do not use when" plus the nearest neighbor, "Not for" plus the second neighbor. About 500 characters, no citations. Read it back and ask: would a model that sees only this fire at the right moments?

- Weak: "This skill helps you decompose barriers using COM-B." A summary, with no trigger and no exclusion.
- Strong: "Use when one behavior is already defined (who does what, when) and you need to know why it is not happening... Do not use when the goal is still vague; use define-key-behavior. Not for choosing interventions."

**The name.** Verb first, kebab-case, a verb from the taxonomy's list, American spelling: `decompose-comb-barriers`, not `comb-barrier-decomposer`.

**The four test cases**, named and in this order. Draft them, then ask the author: "Do these sound like your users?"

1. `Full run`: a complete request with realistic context; expects the whole output.
2. `Missing context`: a thin request; expects the skill's questions and nothing else.
3. `Near the escalation point`: expects what the skill can safely do, and the specialist named.
4. `Wrong skill`: a request that belongs to a neighboring skill; expects to be sent there.

`expected_output` is one sentence. `assertions` holds three to six statements a reviewer can tick yes or no, and never the answer text.

**Metadata.** Recommend a stage and say why. Two or three tags from the taxonomy's suggested list. `produces` is the one thing the output template is; `consumes` lists only the inputs the skill cannot run without. `tested_in` comes from the evidence scan.

## Showing the output

When you show the author the "Full run" output, be plain about how it did. "Partly" is the common verdict on a first draft. Useful questions: "What would you cross out?", "What is missing that you would have said?", "Would you put your name on this?"
