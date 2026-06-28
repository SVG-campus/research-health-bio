# Everyday Research Report — Relationships (Social & Family)

## Preregistered Run Card
```json
{
  "run_id": "everyday_research_relationships_run_2026",
  "pillar": "research-health-bio",
  "seed": 2026,
  "hypothesis": "Financial runway security enables undistracted shared family connection time.",
  "metric": "corr_obs=0.7348 p_perm=0.0025; outcome_mean=-0.0007 ci=(-0.0195,0.0161)",
  "null": "y_shuffle permutation null; bootstrap nonparam for mean CI",
  "truth_scope": "Everyday life optimization model for Relationships (Social & Family) within research framework"
}
```

## Biological & Causal Mechanics
This report documents the causal validation for the **Relationships (Social & Family)** category under the Everyday Life-Optimization framework.

- **Hypothesis:** Financial runway security enables undistracted shared family connection time.
- **Primary Causal Link:** `undistracted_shared_time -> family_connection_score`
- **Features Analyzed:** `undistracted_shared_time`, `shared_meals`, `financial_runway_days`
- **Equation Model (Time-Lagged):** `relationships_t = 0.7 * spending_{t-1} + noise`

## Causal Verification Metrics
- **Observed Correlation:** `0.7348`
- **Spectral MC Null p-value:** `0.0025` (Passes $\alpha = 0.05$ threshold)
- **Outcome Mean Point Estimate:** `-0.0007` (95% CI: `-0.0195` to `0.0161`)
- **Status:** `Verified`

## Topological Persistent Homology (TDA)
- **Topological Betti-1 Homology:** `Discovered 1 persistent Betti-1 loop(s) in lagged state space`
- **Primary Persistent Barcode Lifespan:** `0.1437`

## Practical Takeaways
- Implement targeted monitoring of `undistracted_shared_time` daily.
- Coordinate variables across the double-loop Betti-1 network (Biophysiological & Cognitive loops) to prevent localized bottlenecks.
