---
name: map-reference-network
description: >-
  Use when a practice appears to depend on what other people do or approve of
  and the team needs to know who those people are: "who are they really
  listening to?", "who do we need in the room?". Also use when a program
  suspects it is talking to the wrong people. Writes questions that get people
  to name who matters for one practice, and tabulates the answers by role,
  separating influence from the power to block. Do not use when it is not yet
  known whether others' expectations matter; use diagnose-social-norm. Not
  for choosing a messenger; use select-messenger.
license: CC-BY-4.0
metadata:
  title: Find out whose opinion really matters
  type: atomic
  stage: diagnose
  version: "0.2.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  tested_in: beyond-western-holds
  tags: "social-norms, qualitative"
  consumes: "social-norm-diagnosis"
  produces: "reference-network-map"
---

## What it does

Finds whose behavior or approval people track when they decide whether to follow one practice.

**What this adds:** asks questions written for the one practice, never "who do you talk to?"; counts a role as influential only when respondents say they would act differently if that person did; lists separately who can block the behavior; compares the result with who the program reaches; and records roles, never names.

A reference group, or reference network, is the set of people whose actions and opinions a person weighs for one practice. It differs by practice and need not be local.

## When to use it

### Use it when
- Interviews or a diagnosis suggest a practice depends on what others do or approve of, and who those others are is a guess
- Someone asks "who are they really listening to?" or "who needs to be in the room?"
- A program suspects it is addressing the wrong people, such as counseling pregnant women when husbands decide

### Do not use it when
- It is not known whether others' expectations hold the practice in place; use `diagnose-social-norm`
- The question is who the audience is or which channels reach them; use `map-audience-context`
- The map exists and the question is who should deliver a message; use `select-messenger`

## Before you start

Ask these before producing anything. Do not ask anything the user has already answered.

1. **Required.** The practice (who does what, when) and why others are thought to matter for it: a norm diagnosis, or interview answers that point to other people.
2. **Required.** The population: bounded (one village) or open (a city district), its rough size, and how many interviews are possible.
3. **Required.** Who the program reaches now, through which channel.
4. Optional. Whether naming people could put respondents at risk.

If 1, 2, or 3 is missing, ask and stop. If no answers exist yet, give the design and the questions, mark the table "pending field answers", and stop. If 4 is missing and the practice is illegal or violent, assume the risk.

## What it draws on

- Bicchieri, C., & Penn Social Norms Training and Consulting Group (2016). *Why Do People Do What They Do? A Social Norms Manual for Viet Nam, Indonesia and the Philippines*. UNICEF Office of Research – Innocenti. https://repository.upenn.edu/pennsong/12 Supports: step 1, the three ways to uncover a network.
- Institute for Reproductive Health, Georgetown University (2020). *Social Norms Exploration Tool*. https://www.irh.org/social-norms-exploration/ Supports: steps 2 to 4: short private interviews about one behavior, roles in place of names, a count of how often each role is named.
- The TOPS Program (2017). *Designing for Behavior Change: A Practical Field Guide*. https://web.archive.org/web/20180329030310/http://fsnnetwork.org/sites/default/files/designing_for_behavior_change_a_practical_field_guide.pdf Supports: asking "Who approves?" and "Who disapproves?" to find who can support or prevent a behavior.

**Where the evidence comes from:** The manual was written for UNICEF courses in Southeast Asia, and the tool was piloted in the Democratic Republic of Congo. In 75 Indian villages a person's network community predicted latrine ownership better than the village did. Check locally whether people will name anyone, and whether women name men freely.

**Replication status:** A practitioner method; no study has checked how accurately a count of roles finds a reference group. The finding beneath it rests mostly on observational studies.

## How to do it

1. **Choose how to collect names,** and say what the choice cannot show.
   - Full network: ask everyone in a small bounded group. Most complete, most costly, impossible for a city.
   - Snowball: ask a few people, then interview those they name, until no new roles appear. The usual choice. Vary the starting points, or a group cut off from them is missed.
   - Egocentric: ask people about their own contacts and stop. Cheapest, least reliable. For a large open population, or where following the chain would expose respondents.
2. **Write three to five questions for this practice:** "When you decide whether to X, whose opinion matters?", "Who would disapprove?". A general question about friends maps a different network. For each role named, ask whether they do X, approve of it, or can stop it, and "if they changed their mind, would you?"
3. **Interview people alone and record roles** ("mother-in-law"), never names. Choose respondents across the groups likely to differ.
4. **Tabulate by role:** named by how many; influence (respondents would act differently if this person did); gatekeeping (controls money, transport, or permission); does X; approves of X.
5. **Make three lists:** influential; gatekeepers; named often but not influential.
6. **Compare with who the program reaches:** who is in the reference group that the program never meets, and whom it meets that nobody named.
7. **Show the role table to a few respondents** and record what they correct, or say it was not done.
8. **State which roles must be reached,** in what capacity. Do not pick a messenger.

See `references/worked-example.md` for a complete run.

## Output template

```markdown
# Reference network map

**Practice:** <who does what, when>
**Why others are thought to matter:** <the diagnosis or the interview evidence>
**Program reaches now:** <who, through which channel; or "not stated">

## Design
- **Chosen:** <full network / snowball / egocentric>
- **Why, and what it cannot show:** <population size and boundary; number of interviews; the limit>
- **Who answered:** <how many; who; how chosen; or "pending field answers">

## Questions asked
1. <question, with the practice spelled out>
**Asked about each role named:** <do they do X; do they approve; can they block or permit; "if they changed their mind, would you?">

## Reference group by role

| Role, no names | Named by | Influence: would act differently if they did | Gatekeeping: can permit or block | Does X | Approves of X |
|---|---|---|---|---|---|
| <role> | <n of N> | <yes / partly / no: n of those who named them> | <yes: how / no> | <yes / no / mixed / not applicable> | <yes / no / mixed; "as reported" unless that role was interviewed> |

## Three lists
- **Influential:** <roles>
- **Gatekeepers:** <roles, and what they control>
- **Named often but not influential:** <roles; or "none">

## Reference group against the program's reach
<who is in the reference group that the program does not reach; whom the program reaches that nobody named>

## Checked with respondents
<who saw the role table and what they corrected; or "not yet done">

## Who must be reached
<roles, and in what capacity: to approve, to permit, to stop blocking>

## What to check before relying on this
- <the group of respondents with the fewest answers>
- <the role most likely named out of politeness>
```

## Where it goes wrong

- **The program's own contacts.** Health workers, village heads, and volunteers get onto the map because the team knows them. Count only roles given in answer to the questions.
- **Second-hand views.** "Approves" is the respondent's belief about another person, and people are often wrong about others. Mark it "as reported" until that role is interviewed.
- **Distant people dropped.** A husband working away, a mother-in-law in another village, an employer: absent from the village, present in the decision.

## When to bring in a specialist

Tell the user to consult a specialist before collecting anything when:
- Naming who punishes or blocks could bring violence, legal trouble, or loss of livelihood: a local qualitative researcher and an ethics reviewer approve the questions, consent, and storage first. Give roles only, and refuse a named list of who is blocking
- The design is a full network: a network analyst handles the data
- Respondents split into groups that track different people: a survey researcher designs a sample for each

Bring them: the practice, the design, the questions, and the role table.
