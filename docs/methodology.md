# Methodology Passport Card — Task 2

## 1. Project information
**Title:** Nighttime Smartphone Usage and Sleep Quality Among University Students: A Quantitative Cross-Sectional Analysis  
**Authors:** Karabai Eldos; Serikova Zhanel  
**Source:** Research Methods, Task 1 proposal (2026).

## 2. Research type
**Quantitative, cross-sectional observational study.** Data will be collected once per participant through an anonymous survey and, where feasible, screen-time records. The planned target is at least 150 university students. Cross-sectional associations do not prove causality.

## 3. Hypotheses
**Primary RQ1** — H0: Population Pearson correlation between daily smartphone screen time and global PSQI score equals zero (rho = 0). H1: The correlation is positive (rho > 0). Two-sided testing can be used if direction is not preregistered; the intended directional alternative should be selected before real data collection. The original Task 1 proposed an effect-size target of r >= 0.40, which is distinct from the null-hypothesis test.

**Secondary RQ2** — H0: After adjusting for caffeine and academic stress, active pre-bedtime smartphone usage has no association with sleep onset latency relative to no use. H1: Active usage is associated with greater sleep onset latency. The original Task 1 proposed a 20-minute minimum difference as a substantive target.

**Secondary RQ3** — H0: The probability of PSQI <= 5 is the same for students disconnecting >= 30 minutes and those disconnecting < 30 minutes before sleep. H1: The probability is higher for students disconnecting >= 30 minutes.

## 4. Variable matrix

| Research question | Independent variable | Dependent variable | Controlled variables |
|---|---|---|---|
| RQ1 | Total screen time, hours/day | Global PSQI score, 0–21 | Age, gender, academic workload/major |
| RQ2 | Usage mode within 60 min before bed: active/passive/none | Sleep latency (min), sleep efficiency (%) | Caffeine (mg/day), academic stress (validated PSS when available) |
| RQ3 | Digital disconnection time (minutes), grouped at 30 | Good sleep: PSQI <= 5 | Lighting, room temperature, and relevant measured confounders |

These are observed exposure variables, not experimentally manipulated treatments.

## 5. Metrics, guardrails and baseline
**Primary metric:** Pearson r for daily screen time versus PSQI. Planned inferential analysis on real data will include p-value and 95% confidence interval at alpha = 0.05, with Spearman sensitivity analysis if warranted.

**Secondary metrics:** Adjusted mean difference in sleep latency (min), sleep efficiency (%), proportion with PSQI <= 5, and adjusted odds ratio for good sleep.

**Guardrails:** At most 10% missing/invalid rows in the pilot; PSQI 0–21; sleep efficiency 0–100%; nonnegative time measures; no personally identifying information in the repository. If guardrails fail, results must be reviewed before inference.

**Baseline:** For RQ1, the null association rho = 0. For RQ2, the no-use-before-bed group. For RQ3, disconnection < 30 minutes.

## 6. Pipeline and reproducibility
- `data/sample/students.csv`: ten **synthetic** test rows only.
- `configs/config.json`: paths, primary metric, threshold and guardrail settings.
- `src/benchmark.py`: validates records, computes descriptive Pearson r and group summaries, saves JSON output.
- `Dockerfile`: Python 3.12.3 runtime; standard-library only.
- Quickstart: `python src/benchmark.py`, or build/run via Docker.

**Current scope:** This is a tested local pilot pipeline, not a completed study. It does not yet calculate p-values, adjusted regression, or validated questionnaire scores. No conclusion about H0/H1 should be drawn from synthetic rows.

## 7. Ethics and planned data collection
Obtain informed consent and required course/institutional approvals before collecting real student responses. Avoid names, emails, phone numbers, and raw personal logs in the public repository. Keep private research data outside GitHub; publish only de-identified or aggregated outputs as appropriate.

## 8. References
Karabai, E., & Serikova, Z. (2026). *Nighttime Smartphone Usage and Sleep Quality Among University Students: A Quantitative Cross-Sectional Analysis*. Unpublished Research Methods Task 1 report.

Sohn, S. Y., Rees, P., Wildridge, B., Kalk, N. J., & Carter, B. (2019). The association between problematic smartphone use and sleep disturbance in children and young people: A systematic review and meta-analysis. *BMC Psychiatry, 19*, 356. https://doi.org/10.1186/s12888-019-2350-x
