# Trinity Architecture: Gate 90 + Gate 91 + LSE

## Why Trinity is necessary
Industrial distillation thrives on cheap automation. A single-layer defense either:
- gets bypassed (software-only), or
- becomes too expensive and DoS-prone (physical-only).

Trinity solves both:
- Gate 90: cheap filter + temporal continuity (protects cost)
- Gate 91: physical anchor (protects assets)
- LSE: binds them into a single fail-closed logic (no isolated bypass)

## Routing philosophy
- Any failure → Fail-Closed
- Fail-Closed means: no high-fidelity dataset leakage
- Output downgrade: ShadowOnly / EvidencePlan
