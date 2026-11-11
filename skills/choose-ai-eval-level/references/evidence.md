# Evidence: Choose which AI evaluations to run next

## Sources

The playbook, in its two editions:

- Wu, Z., On, R., Walsh, J., Korley, E., Madon, T., & Wong, L. (2025). *AI Evaluation in the Social Sector: A Living Playbook*. The Agency Fund. The August 2025 edition is linked from the launch post, https://theagencyfund.substack.com/p/rethinking-ai-evaluation-for-the Supports: the idea of staged evaluation. This edition names the six authors and asks: "Does the AI model produce the desired responses?", "Does the product facilitate meaningful interactions?", "Does the product positively support users' thoughts, feelings, and actions?", and "Does access to the product improve human development outcomes?". It says the levels "often follow a natural progression", and that the tech sector typically stops at Levels 1 and 2 while "in the social sector, our bar is higher". Read in part: the preface, the introduction, and the section on randomized trials.
- *AI Evaluation Playbook* (2026). Maintained by a steering committee staffed by the Center for Global Development, IDinsight, and The Agency Fund. https://eval.playbook.org.ai/ Supports: the four questions as worded in the output template, step 3, the three conditions in step 4, and step 7. This is the current edition, at the address the 2025 edition was published at. A working group of more than 30 experts convened by the Center for Global Development revised the playbook, and that version was first published in March 2026. The site names working group members and contributors, not authors. What this skill takes from it:
  - The questions: "Does the AI system perform as intended?", "Does the overall product engage and retain users?", "Does the product change users' thoughts, feelings, knowledge and behaviour towards the development outcome?", "Do users with access to the product improve development outcomes?".
  - The order: "The four levels form a logical progression. Users are unlikely to stay engaged (Level 2) if the GenAI system fails to perform (Level 1), and development outcomes are unlikely to improve (Level 4) if users disengage or their feelings, knowledge, and behaviors are harmed (Level 3)."
  - Its limits: "The levels are not strictly sequential. Teams may run Levels 1, 2, and 3 in parallel, and revisit earlier levels as new results emerge".
  - When to evaluate impact: "Level 4 is typically pursued once Levels 1–3 show consistent, promising evidence". Consider it when "Levels 1–3 are strong", "You are preparing to scale", and "You have bandwidth". "You do not need to run an IE if your product is still in early design or usage is too inconsistent to expect impacts. In such cases, Level 3 evaluations—focused on user cognition and behavior—are more appropriate."
  - What to build early: "Building in features like holdout groups, staged rollouts, or embedded randomization from the start (also useful for A/B testing) preserves the ability to estimate causal effects without disruptive redesigns." And, for a product that changes during a study: "Tag each release with a unique version label."
  - Who runs an impact evaluation: it recommends "working with an independent evaluator".

  Pages read: About this playbook; the overview of each level; Minimum Viable Evaluations; Frequently Asked Questions; Level Linkages; and, under Level 4, the pages on design considerations and common pitfalls.

The two editions word the questions differently, and their conditions for an impact evaluation differ in one respect: the 2025 edition has a fourth condition, that the team's own research gives it "confident priors" of an effect, which the current edition leaves out. This skill uses the current edition's three.

Other sources:

- Chia, H. S., Carter, S., Abrol, F., Madon, T., On, R., Walsh, J., & Wu, Z. (2025, April 16). *An AI evaluation framework for the development sector*. Center for Global Development. https://www.cgdev.org/blog/ai-evaluation-framework-for-the-development-sector Supports: explaining a premature stage to a funder. The post introduces the four levels and recommends that funders "match evaluation requirements to the product's development stage", "avoiding premature requests for impact evaluations". Title, authors, date, and these phrases were confirmed on the page.
- Fuletra, I., & You, S. (2026, February 25). *How AI evaluation works in practice: Insights from implementers*. IDinsight. https://www.idinsight.org/article/how-ai-evaluation-works-in-practice-insights-from-implementers/ Supports: the failure mode of reading the order as a rule about where to start, and the domain expert under "When to bring in a specialist". Read in full.

Three things are this skill's own and come from no source: the verdict labels, the requirement that every verdict name its evidence, and the rule that a team's description or a funder's request does not count as evidence.

## Where it has been tested

Searched November 2026. The skill is a procedure for ordering evaluations and makes no claim about how people behave, so this table records where its sources come from and where the framework has been applied.

| Source | Type | Countries | Finding |
|---|---|---|---|
| [Wu et al. (2025)](https://theagencyfund.substack.com/p/rethinking-ai-evaluation-for-the) | Practitioner playbook; read in part | Written by The Agency Fund from work with eight nonprofits in education, health, and agricultural livelihoods; countries not stated in the parts read | Sets out the four levels. Reports no test of them |
| [*AI Evaluation Playbook* (2026)](https://eval.playbook.org.ai/) | Practitioner playbook; pages listed above | Written for generative AI products in low- and middle-income countries; working group members from Asia, Africa, North America, and Europe | Calls the framework "a guideline to shape to your own purpose and methodology, not a definitive instruction". Reports no test of it |
| [Fuletra & You (2026)](https://www.idinsight.org/article/how-ai-evaluation-works-in-practice-insights-from-implementers/) | Interviews with practitioners; eleven organizations are thanked; read in full | Not stated; the organizations work in health, social protection, justice, and behavior change | Teams started from their most consequential risk "rather than following a strictly linear path". The four levels "provided an initial lens", while practitioners aimed for "enough clarity, at the right time, to decide whether to continue, adapt, or pause". Product and user evaluation were hard to separate in practice |
| [Kemayou, Houdji, Maïga & Gandolfi (2026)](https://neurips.cc/virtual/2026/162759) | Poster, GlobalSouthAI affinity event at NeurIPS 2026; abstract only | West Africa | Applied the four levels to a WhatsApp training system for young people's livelihoods. Adequate technical performance sat alongside a fast drop in engagement; the authors call the framework's value "diagnostic rather than evaluative" |

No study was found that compares teams who ordered their evaluations this way with teams who did not, or that checks whether two teams give the same product the same verdicts. The searches were for applications and critiques of the four-level framework and for guidance on when an impact evaluation of a generative AI product is premature. What depends on the place is the evidence at each stage: who is qualified to judge an answer correct and safe, what counts as real use on a shared phone or a patchy connection, and which outcome matters to the people served.

## Replication

Not applicable. The framework orders evaluations; it is not an intervention with an effect to replicate. The one account of how implementers use it found that they treat it as a starting lens, begin with the risk that matters most, and evaluate product and users together.

## What to check locally

1. Who can judge whether an answer is correct and safe for these users, in their language.
2. What real use looks like here: one account may be several people, and a short exchange that leads to a clinic visit can matter more than a long chat.
3. Whether the product can be released to some users before others, and whether every conversation can be tagged with the version that produced it.
4. Whether a funder or government is in fact considering wider adoption, or only asking about it.
