# Evidence: Work out how big the sample must be

## Sources

The task is a named step or tool in these guides:

- Gupta, S., & Kopper, S. (2021). *Power calculations*. J-PAL Research Resources. https://www.povertyactionlab.org/resource/power-calculations Supports: the formulas in `scripts/power_calc.py`. The page gives the minimum detectable effect, "the smallest effect that, if true, has (1-β)% chance of producing an estimate that is statistically significant at the α% level (Bloom 1995)"; the design effect, 1 + (m − 1) × ICC; and the rule that with incomplete take-up the effect is divided by the difference in take-up between the arms, so that if half the treatment group takes up the treatment the sample "would be four times larger". It says the ICC can be estimated from "baseline data, surveys, and papers--all preferably in the same or a similar population"; to run sensitivity analysis on "minimum effect size, take-up rates and intracluster correlation"; and to "Be realistic and, if anything, overly pessimistic about take-up rates". Its formulas use the t distribution; the script uses the normal. Read in full.
- Doyle, M.-A., & Feeney, L. (2021). *Quick guide to power calculations*. J-PAL Research Resources. https://www.povertyactionlab.org/resource/quick-guide-power-calculations Supports: the attention to take-up. "To be powered to detect the same effect size with 25% take-up, we would need to offer treatment to 16 times more people". It also warns that an underpowered study that finds no effect "may be misinterpreted as the program not having any effect at all". Read in full.
- Kettle, S., & Persian, R. (2022). *Target, Explore, Solution, Trial, Scale: An introduction to running simple behavioural insights projects*. The Behavioural Insights Team. https://www.bi.team/wp-content/uploads/2022/11/BIT-Handbook-How-to-run-simple-BI-projects.pdf Supports: running the calculation both ways and the options in the verdict. Chapter 4 describes determining "how big your sample needs to be to detect a certain effect size" and calculating "which effect size you would be able to detect" with a fixed sample; if that effect is not realistic, "decide whether you want to redesign the intervention to make it more impactful, find a way to increase your sample size, or live with a lower level of power". Its rules of thumb say a two-group trial of under 500 people is "Very unlikely" to have enough power "unless your intervention is extremely powerful". Read in full.
- Haynes, L., Service, O., Goldacre, B., & Torgerson, D. (2012). *Test, Learn, Adapt*. Cabinet Office. https://assets.publishing.service.gov.uk/media/5a7488c8e5274a7f9c586c23/TLA-1906126.pdf Supports: the task. Step 4, "Determine how many units are required for robust results", recommends "working with academics who have experience in RCTs to ensure this key technical calculation is done correctly", and gives the example that 400 people per group give "about an 8 out of 10 chance" of detecting a change from 50% to 60%; the script gives 388 per arm for that case. Step 4 read.
- OECD (2019). *Tools and Ethics for Applied Behavioural Insights: The BASIC Toolkit*. https://doi.org/10.1787/9ea76a8f-en Supports: the task. Box 2.10, "Power analysis", says it "allows researchers and practitioners to determine the sample size required to detect an effect of a given size", and that "practitioners will often be well advised to seek out external expertise on this matter". Box 2.10 read.
- Jang, C., Koki, E., Nyaga, R., Okafor, A., Singh, J., Vang, A., & Wendel, S. (2024). *The Busara toolkit: leveraging behavioral science for development*. Busara Groundwork No. 10. https://doi.org/10.62372/WQSB6195 Supports: the task. Step 4 of its guidance on running a randomized trial is "Sample size, sample design and statistical power". That passage read.

The methods behind the script:

- Bloom, H. S. (1995). Minimum detectable effects. *Evaluation Review*, 19(5), 547–556. https://doi.org/10.1177/0193841X9501900504 Supports: reporting the minimum detectable effect, "the smallest true impact that an experiment has a good chance of detecting", for binary and continuous outcomes. Abstract only.
- McConnell, B., & Vera-Hernández, M. (2025). Going beyond simple sample size calculations: A practitioner's guide. *Fiscal Studies*, 46(3), 323–348. https://doi.org/10.1111/1475-5890.70005 Supports: the adjustments for clustering and covariates, and choosing between more groups and more people per group; the paper gives guidance on allocating the sample between the two. The paper compiles formulas for continuous and binary outcomes, with and without covariates, clustered or not, and covers simulation for more complex designs. Abstract only.
- Gelman, A., & Carlin, J. (2014). Beyond power calculations. *Perspectives on Psychological Science*, 9(6), 641–651. https://doi.org/10.1177/1745691614551642 Supports: the `--true-effect` report. The authors recommend estimating "the probability of an estimate being in the wrong direction (Type S [sign] error)" and "the factor by which the magnitude of an effect might be overestimated (Type M [magnitude] error or exaggeration ratio)". The script computes both in closed form. Abstract only.

Four rules are this skill's own and come from no source: the default ICC grid of 0.01, 0.05, 0.10, and 0.20 in the script's sensitivity table; the escalation below 30 groups, with the figure of about 30% for 10 groups computed by comparing normal with t critical values on 8 degrees of freedom (groups minus two); the escalation for baselines below 5% or above 95%; and the instruction to pass `--true-effect` as a positive number.

## Where it has been tested

Searched November 2026. The skill is arithmetic and makes no claim about how people behave, so this table records where its sources come from and where an ICC a user might borrow was measured.

| Source | Type | Countries | Finding |
|---|---|---|---|
| [Gupta & Kopper (2021)](https://www.povertyactionlab.org/resource/power-calculations) | Practitioner guide; full text | Written for randomized evaluations in any country | No test of the method is reported. It tells the user to take inputs from the same or a similar population |
| [Kettle & Persian (2022)](https://www.bi.team/wp-content/uploads/2022/11/BIT-Handbook-How-to-run-simple-BI-projects.pdf) | Practitioner guide; full text | Written by a UK team; its trial examples include Mexico and Moldova | No test of the method is reported |
| [Hedges & Hedberg (2007)](https://doi.org/10.3102/0162373707299706). Intraclass correlation values for planning group-randomized trials in education. *Educational Evaluation and Policy Analysis*, 29(1), 60–87 | Compilation of ICCs for academic achievement; read in its working-paper version | United States, from longitudinal surveys with national probability samples | Gives ICCs and covariate effects for planning school-randomized trials |
| [Kelcey, Shen & Spybrook (2016)](https://doi.org/10.1177/0193841X16660246). Intraclass correlation coefficients for designing cluster-randomized trials in sub-Saharan Africa education. *Evaluation Review*, 40(6), 500–525 | Compilation of ICCs; abstract only | 15 sub-Saharan African countries; over 60,000 sixth-grade students in 2,500 schools | Reading and mathematics scores were substantially clustered within schools, and the clustering varied considerably across countries, as did how much covariates reduced it |
| [Pagel et al. (2011)](https://doi.org/10.1186/1745-6215-12-151). Intracluster correlation coefficients and coefficients of variation for perinatal outcomes from five cluster-randomised controlled trials in low and middle-income countries. *Trials*, 12, 151 | ICCs from five community-based trials; abstract only | India, Bangladesh, Malawi | ICCs for mortality were lower than for process outcomes, and estimates for rare outcomes such as maternal mortality were much less reliable; for maternal mortality the authors advise planning with a range of estimates |

The formulas do not depend on the population. The ICC, the baseline, take-up, and attrition do, and the two compilations from Africa and South Asia show the ICC moving with country and outcome.

## Replication

Not applicable. The formulas are standard and not in dispute. They are approximations: the script uses normal critical values where the J-PAL page uses the t distribution, which matters when there are few groups, and the two-proportion formula is poor near rates of 0 or 1.

## What to check locally

1. The ICC, estimated from the program's own baseline or administrative data at the group level. If none exists, the sensitivity table is the answer, not a single number.
2. The baseline rate or standard deviation in this population, and whether it came from data or a guess.
3. Take-up in the treatment arm and any take-up in the control arm, from the program's enrollment records.
4. Attrition between enrollment and outcome measurement in earlier rounds.
5. Whether groups will be of similar size; the design effect assumes they are.
