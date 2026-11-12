# Changelog

## 0.3.0 - 2026-11-11
Follows the conversational-voice standard (ADR 0009). The diagnosis opens with a few plain sentences to the user (the provisional call, what it rests on, and what is still to be asked), takes a plain title for "Social norm diagnosis", glosses each of Bicchieri's four questions where it first appears ("Empirical expectation: how many do they think do it?"), says what the call means in plain words, and renames "Classification" to "What kind of practice this is", "Gap between private belief and perceived expectation" to "Do people misjudge what others privately think?", and "Sanctions" to "Sanctions: what happens to people who don't follow it". The output ends with next moves and their reasons, chosen from candidates listed in the closing, and the skill carries the shared voice block. The method is unchanged. Edited with Claude.

## 0.2.0 - 2026-11-11
Rewritten to the November 2026 standard, about 40% shorter. The call is now marked provisional with what would confirm it, and the output lists what else holds the practice in place. The evidence was rechecked against each source: the two sanitation trials are gone because they test a program and not the diagnosis, the UNICEF manual was opened and is now cited, and field studies from Saudi Arabia and Sudan were added. Rewritten with Claude.

## 0.1.0 - 2026-10-12
First draft. Drafted with Claude from the verified evidence dossier (`docs/plan/2026-10-skill-expansion-dossier.md`) for Zezhen Wu's review; four evals; not yet reviewed.
