# Testing agency measures (step 6)

Use this to choose the cheapest check that supports the claim the team will make, and to say what its result would mean for each measure. Full citations are in `evidence.md`.

## What a check can establish

Wu, Goldberg & Xu (2026) ask four things of a measure before it supports a claim about agency:

- **Reliability:** it gives consistent results under similar conditions. A precondition for validity, not a substitute.
- **Construct validity:** it captures agency as the team defined it, not a neighbor such as mood, satisfaction, or engagement.
- **Content validity:** it covers the parts of agency that matter here, not only the parts that are easy to ask about.
- **Criterion validity:** its scores line up with an outcome or behavior the team has reason to trust.

## Size the check to the claim

| The claim the team will make | What is usually enough |
|---|---|
| Internal product iteration ("version B seems to support more revision") | Review of each item by people who know the users; a hand-read sample of what each log signal or model code flags; one agreement check for any coded measure |
| A comparison between versions or arms | The above, plus the same instrument and coding applied identically in every arm, and reliability reported per arm |
| A claim to a funder, the public, or a journal that agency changed | The above, plus a pretested and, where needed, translated instrument; reliability and structure checked in this population; a check against a trusted outcome; a specialist's review |
| A comparison across languages, countries, or genders | All of the above, plus a measurement invariance test before any scores are compared |

## Surveys, on the platform or off it

- **Content:** review each item against the definition, then run cognitive interviews (asking users to say how they understood each item), 5 to 15 interviews in two to three rounds (Boateng et al., 2018).
- **Translation:** two independent forward translations and a reconciliation before any pretest in a new language.
- **Reliability and structure:** internal consistency and, for a multi-item scale, its factor structure, with about 10 respondents per item or 200 to 300 observations (Boateng et al., 2018). Building or validating a new scale needs a psychometrician.
- **Response format:** five-point response scales outperformed three-point ones for four agency scales in six African countries (Clingain, Donald & Hernandez-de-Benito, 2026).
- **Comparing groups, languages, or time points:** test measurement invariance (whether the scale measures the same thing in each group) in order, configural, then metric, then scalar, before comparing means (Vandenberg & Lance, 2000; Putnick & Bornstein, 2016). This includes before-and-after comparisons, since the tool itself can change how users read the items. Partial invariance was reported in about a third of published tests (Putnick & Bornstein, 2016).
- **Low- and middle-income settings:** expect systematic error, not only noise. In Western Kenya, error in self-reported noncognitive skills was nonclassical, and standard psychometric corrections improved it only in part (Laajaj & Macours, 2021). Pilot with cognitive interviews, check test-retest, and hold enumerators constant across arms.
- **Short modules:** choose the few questions that best track coded qualitative interviews with a sample of users (Jayachandran, Biradavolu & Cooper, 2023).

## Observation and rubrics

Train raters on anchored examples, double-score a sample and report their agreement (Cohen's kappa or the intraclass correlation), and revise the anchors where raters disagree.

## Records

Check coverage, and check that the agency measure comes before the outcome it is meant to predict.

## Digital traces and logs

- Name each signal's likely errors, with the questions in `measurement-options.md`.
- Hand-read a random sample of the events each signal flags, to confirm they mean what the plan says.
- Link surveys to logs with a platform identifier, not one the user types.

## A language model as a measure (experimental)

How well a model codes depends on the dataset and the task, so validate it for this prompt, model version, setting, population, and language (Pangakis, Wolken & Fasching, 2023).

1. **Write a codebook both people and the model can use:** definition, inclusion and exclusion rules, low, medium, and high anchors, and examples. Test the model's basic grasp of the codebook before measuring its accuracy (Halterman & Keith, 2026).
2. **Draw the human-coded sample at random, with recorded sampling probabilities,** stratified by the groups and arms the plan will compare. Using model labels directly in an analysis can bias it even when the labels are 80% to 90% accurate; a random human-coded sample lets the analysis correct for that (Egami et al., 2023; Angelopoulos et al., 2023).
3. **Settle agreement between people first.** Two trained coders code the sample and refine the codebook until they agree. Trust the model only when its agreement with them is high: above 0.8, in the playbook's rule (Wu et al., 2025).
4. **Report the model's agreement with the coders beside the coders' agreement with each other.**
5. **Look at errors by subgroup and by language.** In interviews with Rohingya refugees and their Bangladeshi hosts, a model's coding errors were related to who was being interviewed (Ashwin, Chhabra & Rao, 2026). Model judges can do poorly in low-resource languages (Wu et al., 2025); in Marathi, leading models trailed fine-tuned smaller models (Jadhav et al., 2024).
6. **Fix and record the model, version, prompt, and settings, and test repeat runs.** Identical inputs and small changes to a prompt's wording can change the codes (Reiss, 2023).
7. **Guard against a judge's biases** toward position, length, and its own kind of output (Zheng et al., 2023): randomize option order, control for length, and do not let a model from the deployed tool's family judge that tool's conversations.
8. **State the reach.** A transcript shows what users wrote, not what they did afterward or why they asked; users' reasons were hard for frontier models to infer from the conversation (Jin et al., 2026). Pair a transcript measure with an in-the-moment question or an off-platform check.
9. **Protect the data:** consent that covers this use, de-identification before transcripts reach an outside model, and a retention limit.

## Signals that move the wrong way

- **Approval is not agency.** The designs that most reduced over-reliance on an AI got the least favorable ratings (Buçinca, Malaya & Gajos, 2021), and chatbot conversations with more potential to disempower got higher approval ratings (Sharma et al., 2026). Never validate an agency measure against ratings.
- **Assisted performance is not capability.** Practice grades rose with an unguarded AI tutor while performance without it fell (Bastani et al., 2025). Where the goal is capability, check against an outcome measured with the tool removed.

## Reading the results

| What the check shows | What it suggests | Next move |
|---|---|---|
| In cognitive interviews, users read an item differently from the definition | The item measures something else here | Reword or drop it; if many items fail the same way, the construct may not hold here and the definition needs revisiting |
| Low internal consistency or poor test-retest | Noise from wording, translation, response format, or enumerators, or items that do not belong together | Check translation, response options, and enumerator effects before dropping items |
| The factor structure differs from the published one | The construct is organized differently in this population | Do not sum items into the published subscales; report items or a structure the data support |
| The one-item in-app check does not track the off-platform scale | The pulse is not a stand-in for the scale | Keep it as a separate signal or drop it; do not report it as the construct |
| The measure does not relate to an outcome the team trusts | It may capture a neighbor (mood, satisfaction, knowledge), or the outcome may not depend on agency | Check what it does correlate with; revisit the construct before scaling the measure |
| Invariance fails across groups, languages, or arms | Scores do not mean the same thing across them | Do not compare means; report within groups, or test partial invariance with a specialist |
| The model's agreement with coders is well below theirs with each other, or its errors cluster in a subgroup | The model is not measuring the construct, at least for that subgroup | Do not use model codes for that claim or subgroup; revise the codebook or keep human coding |
| Log signals and self-reports move in opposite directions | Users may feel more capable while relying more on the tool, or the reverse | Report both; this is the pattern the grid is built to catch |

Evidence that keeps contradicting the definition is a finding in itself. Record it and revise the definition rather than forcing the data into the original construct.
