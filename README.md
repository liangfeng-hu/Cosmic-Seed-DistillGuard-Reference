# Cosmic-Seed DistillGuard Reference 🛡️

**Industrial anti-distillation defense via a Trinity architecture: Gate 90 + Gate 91 + LSE (Fail-Closed).**

This repository is a **reference implementation + interface contract** that demonstrates why industrial-scale automated distillation becomes **economically non-viable** when defenses are anchored in:
- **Intent/Temporal continuity (Gate 90)**
- **Physical work / entropy proof requirement (Gate 91)**
- **Superposed emergence meta-law (LSE)**

> IMPORTANT: This repo intentionally EXCLUDES production-grade components:
> - real ZKP circuits & verification keys
> - real TEE/attestation chain implementation
> - real π_seed generator and continuity proofs
> You can run the demo and integrate mocks, but you cannot reverse-engineer the core.

---

## Why “90 + 91 + LSE” (not just one gate)

- **Gate 90 (I_AWAKE_SCORE)**: near-zero-cost filter for intent/extraction risk + temporal continuity.  
  Stops the majority of cheap automation and prevents expensive proof paths from being DoS’d.

- **Gate 91 (I_ENTROPY_CLONE)**: physical anchor requiring thermodynamic work proof (mocked here).  
  Blocks high-fidelity extraction by pure software/proxy farms that cannot produce real hardware-bound proof.

- **LSE (I_LSE)**: meta-axiom that forces **Intent × Temporal × Physical** to be simultaneously satisfied.  
  Any fracture → absolute Fail-Closed.

---

## 🚀 Quick Start (30 seconds)

```bash
python reference-impl/python/demo.py

You will see 4 scenarios:

Legit user → all gates pass → I_FLOW=0 → WorldWriteback=1

Proxy distillation script → Gate 91 fails → RC_THERMO_FORGERY → ShadowOnly

Temporal fracture / multi-agent discontinuity → Gate 90 fails → RC_SEED_BREAK → EvidencePlan

Distillation intent detected → Gate 90 fails → RC_DISTILLATION_INTENT_DETECTED → EvidencePlan

Interfaces (OpenAPI, mockable)

spec/gate90.openapi.json → POST /v1/gates/90/check

spec/gate91.openapi.json → POST /v1/gates/91/check

spec/lse.openapi.json → POST /v1/meta/lse/check

Docs

docs/trinity-architecture.md – the closed-loop logic

docs/threat-model-and-solution.md – attack vectors vs. fail-closed outcomes

docs/integration-guide.md – Pre-Commit sidecar integration (data-minimizing)

License

Apache-2.0


---

文件名称：《NOTICE》
```text
Cosmic-Seed DistillGuard Reference
Copyright 2026 YFCore Technology Limited.

This repository provides a reference implementation and interface specification for a
fail-closed anti-distillation gateway (Gate 90 + Gate 91 + LSE).
It intentionally excludes all production-grade cryptographic circuits and hardware attestation.
