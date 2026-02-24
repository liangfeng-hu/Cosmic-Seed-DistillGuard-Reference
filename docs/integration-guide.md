# Integration Guide (PoC)

## Deployment
Inference Gateway → Pre-Commit Hook → DistillGuard Sidecar → Verdict → Output Router

## Minimal calls
1) POST /v1/gates/90/check
2) If i_90==0: POST /v1/gates/91/check (with tau_work_multiplier applied)
3) POST /v1/meta/lse/check (bind gate results + infra support)

## Data minimization
PoC can run without raw prompts/completions.
Use only canonicalized hashes/telemetry and proof placeholders.

## Routing
- If any gate fails → WorldWriteback=0
- OutLevel downgraded (ShadowOnly/EvidencePlan)
- Return decoy/empty output to prevent dataset harvesting
