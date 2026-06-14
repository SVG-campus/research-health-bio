# Preregistration — `research-health-bio`
 
**Pillar:** `research-health-bio`  
**Title:** COVID-19 Social Mobility and Replication Rate Causality (ECT-2026-005)
**Date:** 2026-06-14  
**ORCID Identifier:** `0009-0004-9601-5617`

## Charter (one paragraph)

Separate observational wellness signals from clinical claims; require ethics + scope in truth_scope. This study investigates the causal link between community mobility indices (transit station and retail/recreation movement changes) and the subsequent transmission rate ($R_0$) of COVID-19. We evaluate whether mobility changes causally drive $R_0$ movements or if their relationship is spurious under OCCA's phase-shuffled Fourier null controls.

## Primary question (Layer A)

- **Question:** Do changes in transit and retail mobility (mobility_index) causally influence the COVID-19 reproduction rate ($R_0$) after a physical propagation lag (7 to 14 days)?
- **Expected DAG:** `mobility_index -> R_0` (with directed flow adhering to temporal priority).
- **Primary metric:** Discovered directed edges and lagged mutual information.
- **Direction / threshold:** $\alpha = 0.05$ for PC algorithm. The discovered edge must follow the temporal ordering (lagged mobility to $R_0$) and the information coefficient must exceed the p95 Spectral MC null distribution ($p < 0.05$).

## Null / negative controls

- **Null model:** Phase-shuffled Spectral Monte Carlo (FFT surrogate paths).
- **Caps:** Capped at $N = 25$ runs for local smokes (`runs/smoke.yaml`); $N = 1000$ for full remote promotion validation with run ID `charter_health_mobility_r0_run_01`.

## Truth scope & ethics

- **Scope:** Observational epidemiological and mobility records under the **ECT-2026** standard.
- **Data rights:** CSSE JHU COVID-19 and Google Mobility datasets.

## Promotion rules

Numbers enter `BEST_ANSWERS_OVERVIEW` (meta) only after `methodology_preamble.assert_run_card` passes in the same environment that produced the artifact. Follow the meta checklist [PROMOTION_CHECKLIST.md](https://github.com/SVG-campus/Research-Apriori/blob/main/docs/PROMOTION_CHECKLIST.md) before editing canonical summaries.
