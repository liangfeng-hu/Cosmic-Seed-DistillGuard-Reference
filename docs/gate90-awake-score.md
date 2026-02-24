# Gate 90: I_AWAKE_SCORE (Intent + Temporal Continuity)

Gate 90 is the **near-zero-cost moat** that filters automation and enforces temporal continuity before any expensive physical proof path.

## Core rule (hard-wall algebra)

I_AWAKE_SCORE = 0 iff:
- distillation_risk_score ≤ τ_intent
- SeedContinuity is valid (temporal continuity proof)

Otherwise: I_90 = +∞ (Fail-Closed routing)

## Reference payload fields (mockable)

intent_audit_group:
- distillation_risk_score: [0,1]
- extraction_pattern_flags: string[]
- query_velocity_tps: number

temporal_seed_group:
- seed_continuity_proof: string (reference expects "valid_closure")

## Output
- i_90 ∈ {0, "+∞"}
- reason_code ∈ {RC_SUCCESS, RC_SEED_BREAK, RC_DISTILLATION_INTENT_DETECTED}
- tau_work_multiplier: for Gate 91 tightening (reference-only placeholder)
