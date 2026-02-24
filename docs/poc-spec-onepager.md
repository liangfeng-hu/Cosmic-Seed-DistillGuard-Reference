# PoC One-Pager — DistillGuard Trinity (Gate 90 + Gate 91 + LSE)
**Version:** 1.0 (Reference)  
**Scope:** Pre-Commit sidecar / gateway integration (no model weight changes)  
**Repo Type:** Reference implementation + OpenAPI contracts (production ZKP/TEE/π_seed excluded)

---

## 1) Goal (What we prove in a real environment)
Demonstrate that industrial-scale distillation becomes **economically non-viable** when high-fidelity outputs require:
- **Gate 90 (I_AWAKE_SCORE):** Intent risk + Temporal continuity (cheap screening)
- **Gate 91 (I_ENTROPY_CLONE):** Hardware-rooted physical work proof (mocked here)
- **LSE (I_LSE):** Meta-gate binding Intent × Temporal × Physical into a single Fail-Closed verdict

**Key claim to validate:**  
Even with “合法API调用 + 账号/代理轮换 + 慢速提取”，攻击者无法稳定收集“可用于训练学生模型的干净高保真数据集”。

---

## 2) Minimal Deployment Shape (Recommended)
**Inference Gateway** → **Pre-Commit Hook** → **DistillGuard Sidecar (this PoC)** → **Verdict** → **Output Router**

- Works as a sidecar (HTTP) or in-gateway plugin.
- No raw prompt/response needed for PoC; evidence-only payload is sufficient.

---

## 3) Interfaces (OpenAPI, mockable immediately)
- **Gate 90:** `POST /v1/gates/90/check`
- **Gate 91:** `POST /v1/gates/91/check`
- **LSE:** `POST /v1/meta/lse/check`

**Canonical routing rule:**  
If any gate returns `+∞` → **Fail-Closed** (`WorldWriteback=0`, downgrade output level).

---

## 4) Routing Semantics (Fail-Closed is the product)
**Pass (I_FLOW=0):**
- `WorldWriteback=1`, `CommitUnique=1`, `OutLevel=FOES`
- Action: `ALLOW_HIGH_FIDELITY_OUTPUT`

**Fail (I_FLOW=+∞):**
- `WorldWriteback=0`, `CommitUnique=0`
- Prefer:
  - `OutLevel=ShadowOnly` when Gate 91 fails (`RC_THERMO_FORGERY`)
  - `OutLevel=EvidencePlan` when Gate 90 or LSE fails (`RC_SEED_BREAK`, `RC_DISTILLATION_INTENT_DETECTED`, `RC_LSE_VIOLATION`)
- Action: `BLOCK_AND_ISOLATE` or `HALT_AND_AUDIT`

**Important:** PoC success is measured by *no extractable high-fidelity dataset leakage*, not by “catching bad intent”.

---

## 5) Success Criteria (Suggested, adjustable)
**Security / Asset Protection**
- High-fidelity output leakage for suspected automation: **≤ 1%**
- Gate 90 early stop rate for automation-like traffic: **high**, while keeping legit pass rate stable

**Legit UX**
- Legit requests pass rate: **≥ 99.5%** (with proper evidence continuity & proof placeholders)
- Added latency at gateway: **target ≤ 5ms** for PoC (mock), measure p50/p95

**Auditability**
- For every blocked request: ReasonCode + OutLevel + minimal audit keys recorded (see `docs/audit-keys-minimum.md`)

---

## 6) Timeline (2–4 weeks, practical)
**Week 1**
- Integrate sidecar calls
- Run controlled attack simulation (proxy farm / slow extraction / multi-agent temporal fracture)

**Week 2**
- Limited grey traffic (de-identified / internal)
- Produce audit report: pass/fail counts by ReasonCode + latency

**Optional Week 3–4**
- Tighten Gate 90 thresholds (tau_intent) and Gate 91 multiplier logic (tau_work_multiplier)
- Repeat red-team simulation

---

## 7) What we provide (from this repo)
- OpenAPI contracts (Gate90/Gate91/LSE)
- Reference gate logic (mock) + Trinity demo
- Fail-Closed routing semantics and reason-code discipline
- Documentation: threat model, trinity architecture, integration guide

---

## 8) What partner provides (for realistic PoC)
- A staging gateway (or a sidecar insertion point)
- De-identified request metadata streams (no raw prompts required)
- Optional: confidential-compute/TEE attestation endpoint (can be mocked in PoC)
- A contact for security review and sign-off

---

## 9) Explicit Non-Goals (to avoid confusion)
This PoC does **not** deliver:
- Production ZKP circuits / verification keys
- Real TEE attestation implementation
- Real π_seed generator or continuity prover

Those are part of production integration under research/commercial evaluation.

---

## 10) Next Step (15-minute alignment)
- Confirm insertion point and routing semantics
- Confirm minimal audit keys and data minimization policy
- Start PoC with mock proofs, then progressively harden
