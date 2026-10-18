# Nighttime Smartphone Usage and Sleep Quality Among University Students

**Authors:** Karabai Eldos; Serikova Zhanel  
**Course:** Research Methods — Task 2  
**Research design:** Quantitative, cross-sectional observational study

## Overview
This repository provides a reproducible **pilot measurement pipeline** for the study proposed in Task 1. It measures the Pearson correlation between daily smartphone screen time (hours/day) and PSQI sleep-quality scores (0–21; higher means worse sleep). It also summarizes sleep quality for participants who disconnect from their phones at least 30 minutes before bedtime versus those who do not.

**The included ten records are entirely synthetic. They demonstrate code execution only and cannot support scientific conclusions.** This pilot does not yet compute p-values, adjusted regression, or causal effects. Real participant data and a pre-specified analysis plan are required before hypothesis testing.

## Research questions
- RQ1: Is daily smartphone screen time associated with global PSQI scores?
- RQ2: Is active smartphone use before bedtime associated with longer sleep latency after adjustment for stress and caffeine?
- RQ3: Is disconnection for at least 30 minutes associated with a higher probability of good sleep (PSQI <= 5)?

## Hypotheses for the primary analysis (RQ1)
- **H0:** Population correlation between daily screen time and PSQI equals zero (rho = 0).
- **H1:** Population correlation between daily screen time and PSQI is positive (rho > 0).

The original Task 1 also proposed a target correlation r >= 0.40. This is a prospective effect-size target, **not** part of the statistical definition of H1.

## Planned benchmarks

| Analysis | Input | Metric | Baseline/comparator | Implementation status |
|---|---|---|---|---|
| RQ1 | Daily screen time and PSQI | Pearson r (primary), eventual p-value and confidence interval | Null rho = 0 | Descriptive r implemented |
| RQ2 | Usage mode, sleep latency, caffeine, stress | Adjusted latency difference (minutes) | No usage in the hour before sleep | Planned |
| RQ3 | Disconnection minutes and PSQI | Good-sleep rate and eventual adjusted odds ratio | Less than 30 minutes disconnection | Descriptive group rates implemented |

Guardrail: invalid/missing records must not exceed 10%; PSQI must lie in 0–21, efficiency in 0–100%, and time values must be nonnegative. No personal identifiers or real student responses are committed.

## System requirements
- Python **3.12.3** for local execution (no external dependencies)
- Optional: Docker Desktop with a working Linux container engine
- Windows PowerShell, macOS Terminal, or Linux shell

## Quickstart
From the project root, run:

```bash
python src/benchmark.py
```

On Windows, if `python` is not available but `py` is:

```powershell
py -3.12 src/benchmark.py
```

Docker alternative (two commands):

```bash
docker build -t smartphone-sleep-research .
docker run --rm smartphone-sleep-research
```

The script prints JSON results and saves `results/benchmark_results.json`. The container prints the same analysis, but its output file stays inside the ephemeral container unless a volume is mounted.

## Repository layout

```text
.
├── README.md
├── .gitignore
├── .dockerignore
├── Dockerfile
├── requirements.txt
├── LICENSE
├── configs/config.json
├── data/sample/students.csv
├── docs/methodology.md
├── src/benchmark.py
├── notebooks/.gitkeep
└── results/            # generated results excluded from Git
```

## Data dictionary
`student_id` is a synthetic row ID; `screen_time_hours` is hours/day; `pre_bedtime_minutes` is minutes of use within the pre-sleep period; `disconnection_minutes` is time between last use and intended sleep; `psqi_score` is global PSQI (0–21); `sleep_latency_minutes` is minutes to fall asleep; `sleep_efficiency_percent` is percentage; `usage_mode` is active/passive/none; `caffeine_mg` is daily caffeine in milligrams; `academic_stress_score` is an illustrative pilot scale, **not a validated PSS measure**.

## Reproducibility and limitations
Configuration lives in `configs/config.json`. The runtime is Python 3.12.3 with standard-library dependencies only. `Dockerfile` uses a versioned base image; for stronger long-term immutability, resolve and pin its digest on the target architecture. Docker build has not been independently verified in this delivery environment. PSQI scoring requires properly licensed/authorized questionnaire use and validated calculation; the synthetic CSV already contains demonstration PSQI totals. The study is observational, so associations cannot establish causality.

## Citation and license
Research proposal: Karabai, E., & Serikova, Z. (2026). *Nighttime Smartphone Usage and Sleep Quality Among University Students: A Quantitative Cross-Sectional Analysis*. Research Methods, Task 1 (unpublished course report).

Software is released under the [MIT License](LICENSE).
