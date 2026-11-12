# Changelog

## 0.3.0 - 2026-11-11
Follows the conversational-voice standard (ADR 0009). The script opens with a few plain sentences to the user (what it covers, the plan, and that the interviews show misreading, not true answers); the title says what the interviews test, and "probes" is glossed as follow-up questions the first time it appears. The output ends with next moves and their reasons, chosen from candidates listed in the closing, and the skill carries the shared voice block. The method is unchanged. Edited with Claude.

## 0.2.0 - 2026-11-11
Rewritten to the November 2026 standard: scripted probes are now the default in place of thinking aloud, probes outside the script are limited to named cues, and the output gains a stop rule for upset respondents, a three-minute budget per question, and a worked example. The evidence was rechecked against the sources: two claims the earlier version attributed to papers that do not make them in their abstracts were replaced with field studies from India, Bangladesh, Ethiopia, Kenya, and Uganda and with studies of how reliably the method finds problems. The title changed from "Cognitive interview script drafter". Rewritten with Claude.

## 0.1.0 - 2026-10-08
First draft by Zezhen Wu as the library's reference skill. Four evals, probe bank in references. Not yet reviewed.
