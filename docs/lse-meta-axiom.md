# LSE: Law (I_LSE)

LSE is a meta-gate. High-fidelity output is allowed only if:
- **Intent** constraints pass
- **Temporal continuity** holds
- **Physical proof** requirements pass

## Decision rule
I_LSE = 0 iff:
- gate results are satisfied (i_90 = 0 AND i_91 = 0)
- infrastructure support is OK (energy budget + verifier trust)

Else: I_LSE = +∞ → Fail-Closed

## Support clauses (reference)
- `energy_budget_ok` must be true
- `verifier_consensus_hash` must be non-empty / non-null
