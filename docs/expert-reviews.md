# Expert reviews

An expert review is written feedback on one version of a skill from staff at The Agency Fund or Irrational Labs, or from an expert they invite. Anyone with a Google account can also rate a skill and leave a public comment; this page is about the expert reviews.

## Writing one

1. On a skill's page, choose **Review this skill** and sign in with a work Google account. The site keeps your name and email address and nothing else from Google.
2. Pick a verdict (ready, small changes, needs revision, or not suitable), tick the parts of the skill the review concerns, and write it. Add sources where you have them.
3. The site files the review as a GitHub issue labeled `expert-review`. You do not need a GitHub account. The issue names you and your organization, never your email address.

A review is read against the exact version it was written for: the issue links to the skill's text at that commit.

## Answering one

Each review ends in one of two ways.

**A new version answers it.**

1. Revise the skill and bump `metadata.version`.
2. In the new CHANGELOG entry, cite the issue: `Addresses expert review #42 (Jane Doe): added a cost column to the scoring table.`
3. In the pull request description, write `Closes #42`. Merging closes the issue.

The site reads the CHANGELOG when it is built. From then on the review shows **Answered in v0.2.0** on the skill's Reviews tab, with that changelog sentence, so readers can see how the skill responded. One entry can answer several reviews; cite each number.

**No change.** Reply on the issue with the reason, add the label `review:declined`, and close it as "not planned". The skill's page shows it as **Closed without changes**.

An expert review does not change a skill's `status` or `reviewed_by`. Only a maintainer's review of a pull request does that (`GOVERNANCE.md`).

## Finding reviews

Each review issue is titled `[Expert review] <skill> v<version> by <name> (<org>)` and carries the labels `expert-review`, `skill:<name>`, `stage:<stage>`, `verdict:<verdict>`, and `org:<org>`.

```bash
gh issue list --label expert-review --state open                       # everything waiting
gh issue list --label expert-review --label skill:define-key-behavior  # one skill
gh issue list --label expert-review --label verdict:needs-revision     # the serious ones
```

## Working through reviews with an AI agent

The format is fixed so that an agent can do the clerical work. A prompt for Claude Code or a similar agent in this repository:

> Read the open expert reviews of `<skill-name>`: `gh issue list --label expert-review --label skill:<skill-name> --state open --json number,title,body`. List each review's points, grouped by the part of the skill it concerns. For each point, say whether you would change the skill and how, quoting the line it affects. Wait for my decisions, one review at a time. Then revise the skill with besci-skill-creator, bump the version, write a CHANGELOG entry that cites every review it answers ("Addresses expert review #N (reviewer): ..."), run the validator, and open a pull request whose description says "Closes #N" for each. For points we decline, draft a reply for each issue instead.

Keep a person on each decision. A review is expert judgment, and the agent's job is to organize it, not to settle it.
