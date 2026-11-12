# Changelog

## 0.2.0 - 2026-11-11
Follows the conversational-voice standard (ADR 0009). The output opens with a few plain sentences to the user (who tries the draft and how, what the test most needs to find out, and that it cannot show whether behavior changes), is titled "Trying <the draft> with a few people before the pilot" instead of "Prototype test plan", and "Decision this test feeds" becomes "What the team will decide with it". The output ends with next moves and their reasons, chosen from candidates listed in the closing, and the skill carries the shared voice block. The method is unchanged. Edited with Claude.

## 0.1.0 - 2026-11-11
New skill. It plans a test of a draft intervention with a few people from the audience before any pilot. It replaces `plan-trials-of-improved-practices` and keeps that method as one option, the home trial, described in `references/trials-of-improved-practices.md`. Written with Claude.
