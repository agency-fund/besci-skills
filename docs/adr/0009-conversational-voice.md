---
status: proposed
date: 2026-11-11
---
# Skills talk with the user: conversation by default, marked runs, and next moves offered with reasons

Testing the navigator and two atomic skills on a realistic case (a farmer-advice chatbot in rural Kenya with low repeat use) showed three problems the November 2026 standard did not address. A skill explained itself before answering what the user asked ("how do I know if my intervention is ethical?" got a description of the ethics skill first). The user could not tell whether they were talking with a general AI that knows the library or running a skill whose method and evidence were in force. And the output read as cold and directive: internal labels such as "Persistence test" and "Discriminates because" shown to the user, and templates that ended in "Next action: <the single thing to do today>" or "Check first".

Three rules caused most of it. "Ask before producing" was applied to plain questions as well as to output. Output templates were the whole response, with no sentences to the person around them. And a skill could name another skill only under "Do not use it when", so it had no permitted way to suggest a next move with a reason.

**Conversation is the default.** The navigator's first mode is conversation: it answers a question as a thought partner, says what comes from the library and what is general knowledge, and mentions a skill only when the user wants to do something, with what the skill would add. Route and guide modes remain for a concrete task and a multi-stage plan.

**Runs are marked.** A skill run opens with one plain line naming the skill and what it will produce, and says when it is finished. A workflow run says which step the user is on.

**Answer first, then ask.** A question the user asked is answered in a few plain sentences before the skill offers its run. "Before you start" questions still come before the output, so a skill does not produce on a guess.

**Every skill carries one shared voice block.** The text lives in `template/shared/voice.md` and is copied between markers into the "Output template" section of every `SKILL.md` by `scripts/check_sync.py`. It is inside each skill because a model reliably reads only the `SKILL.md` that fired; a reference file it may skip, and a host instruction reaches only some tools. The block does not count toward the length limit.

**Templates open with a plain lead-in, use plain labels, and close with next moves.** The closing, "Where you could go from here", offers two or three next moves that fit what the run found, each with its reason and when it fits, and one or two questions the user could ask next. The skill may say which it would lean toward; the user decides. "Next action", "Check first", and "Next steps" lines are not allowed.

**Skills may name next moves.** This replaces ADR 0008's rule that a skill names another skill only under "Do not use it when". The input rule that sentence protected stays: a skill asks for an input by what it is, never by the skill that made it. The last step of "How to do it" lists candidate next moves with their conditions, including at least one step outside the library where one fits.

**Not done now.** No plugin hook adds library instructions to every Claude Code session; the voice block travels with every skill, and the navigator covers conversation before a skill fires. We revisit this if conversation fails before any skill loads. The site gets an optional paste-in for Claude Desktop and claude.ai Projects, and "Try asking" examples on each skill page.

**Consequences.** The spec, the template, the checklist, and `besci-skill-creator` describe the rules. The validator checks the voice block, the closing, and directive closings as warnings W053 to W055 behind `STRICT_VOICE` while the library is revised, then as errors; it fails on any named skill or workflow that does not exist (E056); W051 now checks only "Before you start". `besci-eval` adds a ninth rubric criterion, Conversation, and rewords "Asked first" so a brief answer before the questions is not penalized. Skills move to the next minor version, because the template's shape changes. Three skills (the navigator, `decompose-comb-barriers`, `audit-intervention-ethics`) are revised first and tested on the case that surfaced the problem before the rest follow. This changes the spec and the validator, so it needs agreement from maintainers of both organizations before it is accepted.
