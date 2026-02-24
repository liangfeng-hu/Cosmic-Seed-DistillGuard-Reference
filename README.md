# Cosmic-Seed DistillGuard Reference 🛡️

**Industrial anti-distillation defense via a Trinity architecture: Gate 90 + Gate 91 + Law (I_LSE) — Fail-Closed.**

This repository is a **reference implementation + interface contract** that demonstrates why industrial-scale automated distillation becomes **economically non-viable** when defenses are anchored in:

- **Intent + Temporal continuity screening (Gate 90)**
- **Physical work / entropy proof requirement (Gate 91)**
- **Meta-law binding (Law / I_LSE)**

> IMPORTANT: This repo intentionally EXCLUDES production-grade components:
> - real ZKP circuits & verification keys
> - real TEE / hardware attestation chain implementation
> - real π_seed generator and continuity proofs  
> You can run the demo and integrate mocks, but you cannot reverse-engineer the core.

---

## Why “Gate 90 + Gate 91 + Law (I_LSE)” (Trinity)
- **Gate 90 (I_AWAKE_SCORE)**: near-zero-cost filter for intent/extraction risk + temporal continuity.  
  Stops the majority of cheap automation and prevents expensive proof paths from being DoS’d.
- **Gate 91 (I_ENTROPY_CLONE)**: physical anchor requiring thermodynamic work proof (mocked here).  
  Blocks high-fidelity extraction by pure software/proxy farms that cannot produce real hardware-bound proof.
- **Law (I_LSE)**: meta-law that binds **Intent × Temporal × Physical** into a single fail-closed verdict.  
  Any fracture → absolute Fail-Closed.

---

## 🚀 Quick Start (30 seconds)

```bash
python reference-impl/python/demo.py

You will see 4 scenarios:

Legit user → all checks pass → I_FLOW=0 → WorldWriteback=1

Proxy distillation script → Gate 91 fails → RC_THERMO_FORGERY → ShadowOnly

Temporal fracture / multi-agent discontinuity → Gate 90 fails → RC_SEED_BREAK → EvidencePlan

Distillation intent detected → Gate 90 fails → RC_DISTILLATION_INTENT_DETECTED → EvidencePlan

Interfaces (OpenAPI, mockable)

spec/gate90.openapi.json → POST /v1/gates/90/check

spec/gate91.openapi.json → POST /v1/gates/91/check

spec/lse.openapi.json → POST /v1/meta/lse/check

Docs

docs/trinity-architecture.md — the closed-loop logic

docs/threat-model-and-solution.md — attack vectors vs. fail-closed outcomes

docs/integration-guide.md — Pre-Commit sidecar integration (data-minimizing)

docs/poc-spec-onepager.md — internal pilot spec (2–4 weeks)

docs/audit-keys-minimum.md — minimum evidence closure list for reproducible verdicts

docs/lse-meta-axiom.md — Law (I_LSE) definition (reference)

License

Apache-2.0

本防蒸馏网关是 V∞ AGI 操作系统底层总线的首个工业落地场景，查看完整战略架构请访问 [Repo 2](https://github.com/liangfeng-hu/V-infinity-Origin-Compiler-Executor-Reference/tree/main)。
