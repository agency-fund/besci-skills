# Evidence: Find out who benefited most from a program

## Sources

- Skivington, K., Matthews, L., Simpson, S. A., et al. (2021). A new framework for developing and evaluating complex interventions: update of Medical Research Council guidance. *BMJ*, 374, n2061. https://doi.org/10.1136/bmj.n2061 Supports: the confirmatory table. "Where needed to support the research questions, prespecified subgroup analyses should be carried out and reported. Even where such analyses are underpowered, they should be included in the protocol because they might be useful for subsequent meta-analyses, or for developing hypotheses for testing in further research." Full text.
- Haynes, L., Service, O., Goldacre, B., & Torgerson, D. (2012). *Test, Learn, Adapt*. Cabinet Office. https://www.gov.uk/government/publications/test-learn-adapt-developing-public-policy-with-randomised-controlled-trials Supports: the line between named and exploratory subgroups. "It is important to decide at the outset if we are interested in segmenting the sample in this way – if we do this after the data has been collected, sub-group analyses run a high risk of lacking both statistical power and validity." An unexpected subgroup trend is a reason to consider a future trial; as an unplanned analysis, its results "can't be considered definitive". Full text.
- Chernozhukov, V., Demirer, M., Duflo, E., & Fernández-Val, I. (2025). Fisher–Schultz Lecture: Generic machine learning inference on heterogeneous treatment effects in randomized experiments, with an application to immunization in India. *Econometrica*, 93(4), 1121–1164. https://doi.org/10.3982/ECTA19303 Supports: the three exploratory outputs (the best linear predictor of the effect, average effects by group of predicted impact, and the average characteristics of the most and least affected); repeated data splitting with medians across splits; and the reading of the heterogeneity coefficient, which is 1 for a perfect predictor and 0 when the predictor is noise or there are no differences to find. Full text of the 2023 preprint, https://arxiv.org/abs/1712.04802.
- Bryan, C. J., Tipton, E., & Yeager, D. S. (2021). Behavioural science is unlikely to change the world without a heterogeneity revolution. *Nature Human Behaviour*, 5(8), 980–989. https://doi.org/10.1038/s41562-021-01143-3 Supports: the sample line, since early tests in convenience samples usually overestimate the average effect in the population; drawing a probability sample and over-sampling subgroups of interest to power the comparison; and the advice to "exercise caution in interpreting measured moderators as causal variables". Full text.
- Athey, S., & Imbens, G. (2016). Recursive partitioning for heterogeneous causal effects. *Proceedings of the National Academy of Sciences*, 113(27), 7353–7360. https://doi.org/10.1073/pnas.1510489113 Supports: fitting on one sample and estimating on another. In the authors' simulations this "honest" approach gave nominal coverage for 90% confidence intervals, against 74% to 84% without it. Abstract only.
- Wager, S., & Athey, S. (2018). Estimation and inference of heterogeneous treatment effects using random forests. *Journal of the American Statistical Association*, 113(523), 1228–1242. https://doi.org/10.1080/01621459.2017.1319839 Supports: the causal forest as the flexible model, with valid confidence intervals for the effect at each point. Abstract only.
- Duru, M., & Kopper, S. (2023). *Data analysis*. J-PAL Research Resources. https://www.povertyactionlab.org/resource/data-analysis Supports: planning subgroups in advance so the study has the power to detect them, and the corrections for testing several hypotheses, Bonferroni and Benjamini-Hochberg.
- Benjamini, Y., & Hochberg, Y. (1995). Controlling the false discovery rate: A practical and powerful approach to multiple testing. *Journal of the Royal Statistical Society Series B: Statistical Methodology*, 57(1), 289–300. https://doi.org/10.1111/j.2517-6161.1995.tb02031.x Supports: the default correction, which controls the expected share of false findings among those declared and has more power than controlling the chance of any false finding. Abstract only.
- Jang, C., Koki, E., Nyaga, R., Okafor, A., Singh, J., Vang, A., & Wendel, S. (2024). *The Busara toolkit: leveraging behavioral science for development*. Busara Groundwork No. 10. https://doi.org/10.62372/WQSB6195 Supports: the task. Its assessment phase asks "For whom is the intervention impactful? (Conditional or by segment)". Full text.
- Walton, G. M., & Wilson, T. D. (2018). Wise interventions: Psychological remedies for social and personal problems. *Psychological Review*, 125(5), 617–655. https://doi.org/10.1037/rev0000115 Supports: choosing subgroups from how the program works. Their table of sources of heterogeneity says an intervention works where a specific harmful meaning undermines a group and where the situation and the people have the capacity to do better. Full text.

## Where it has been tested

Searched November 2026. The skill is a statistical procedure, so this table records where its sources come from.

| Source | Type | Countries | Finding |
|---|---|---|---|
| [Chernozhukov et al. (2025)](https://doi.org/10.3982/ECTA19303) | Methods paper with a field application; full text of the preprint | India (Haryana) | A combination of small incentives, information hubs, and SMS reminders had very large effects on immunization in some villages where it was low at baseline, and backfired in others |
| [Athey & Imbens (2016)](https://doi.org/10.1073/pnas.1510489113) | Methods paper with simulations; abstract only | Simulated data | Splitting the sample kept confidence intervals honest; not splitting left them too narrow |
| [Wager & Athey (2018)](https://doi.org/10.1080/01621459.2017.1319839) | Methods paper with simulations; abstract only | Simulated data | Causal forests were more powerful than nearest-neighbor matching, especially with irrelevant covariates |
| [Bryan, Tipton & Yeager (2021)](https://doi.org/10.1038/s41562-021-01143-3) | Perspective; full text | Examples from the United States | Pre-registered analyses in a national probability sample found a growth-mindset program helped lower-achieving students in supportive schools most |
| [Haynes et al. (2012)](https://www.gov.uk/government/publications/test-learn-adapt-developing-public-policy-with-randomised-controlled-trials) and [Skivington et al. (2021)](https://doi.org/10.1136/bmj.n2061) | Trial guidance; full text | United Kingdom | No test reported |

The methods do not depend on the population. Who the result speaks for does: it describes the people in the trial, and a wider population only if they were drawn from it at random.

## Replication

Not applicable to the methods, which rest on proofs and simulations. The trial guidance warns that subgroups chosen after the data lack power and validity; the skill labels every such result a hypothesis for that reason.

## What to check locally

1. How the sample was drawn, and which population, if any, it can speak for.
2. Which subgroups the plan names, with their expected direction, and whether the trial was sized for any of them.
3. The unit of randomization and the number of clusters.
4. Whether every characteristic used to define a subgroup was measured before assignment; anything measured after treatment cannot define one.
5. What decision the result will feed; deciding who gets the program is the case for a specialist.
