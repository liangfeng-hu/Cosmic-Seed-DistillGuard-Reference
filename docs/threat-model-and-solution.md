# Threat Model & Solution (Reference)

## Threat: industrial automated distillation
Goal: collect a large, clean, high-fidelity dataset to train a student model.

## How Trinity blocks it

| Attack Vector | Why traditional defenses fail | Trinity blocking mechanism | Fail-Closed outcome |
|---|---|---|---|
| Proxy farm / account rotation | Rate limiting & semantics bypassed | Gate 91 requires physical proof | ShadowOnly, RC_THERMO_FORGERY |
| Slow extraction | Behavioral detection misses | Gate 90 temporal continuity + risk scoring | EvidencePlan, RC_SEED_BREAK / RC_DISTILLATION_INTENT |
| Multi-agent coordination | Intent masking | Gate 90 flags + LSE binding | EvidencePlan, RC_DISTILLATION_INTENT |
| Prompt-engineered high-fidelity leakage | “Looks legitimate” | Gate 90 tightens Gate 91 work threshold (multiplier) | Either blocked at 90 or forged at 91 |

## Note
This repo demonstrates semantics and interfaces only. Production requires real ZKP/TEE/π_seed.
