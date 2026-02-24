# Audit Keys — Minimum Closure List (MinSuf) for Trinity PoC
**Goal:** make every verdict reproducible and auditable with **minimal sufficient evidence**.  
**Rule:** Missing required key ⇒ treat as **Incomplete** ⇒ Fail-Closed.

---

## A) Canonical Anchors (MUST)
These are the “identity roots” that prevent semantic drift:

- `CanonHeader` (or equivalent canonical config hash)
- `SSOT_Hash` (canonical SSOT digest)
- `GateKernelRef` / `GateKernelHash` (sealed gate definitions reference)
- `VerifierRefs` (verifier catalog references / ids)
- `BuildEnvHash` (optional but recommended for reproducibility)

---

## B) Request Envelope (MUST)
- `request_id`
- `timestamp_utc`
- `risk_class`
- `policy_version` (optional but recommended)
- `out_level` (result)
- `reason_code` (result)

---

## C) Gate 90 Evidence (Intent + Temporal) (MUST)
### C1) IntentAuditGroup (MUST)
- `distillation_risk_score` (0..1)
- `extraction_pattern_flags` (array of strings; may be empty)
- `query_velocity_tps` (number; may be 0 in PoC)
- `prompt_similarity_hash` (SHOULD; if available)
- `output_entropy_drop` (SHOULD; if available)

### C2) TemporalSeedGroup (MUST)
- `pi_seed_t`
- `seed_continuity_proof`
  - PoC reference expects `"valid_closure"` for pass
  - Any other value ⇒ `RC_SEED_BREAK` ⇒ Fail-Closed

### C3) Gate90 Parameters (MUST)
- `tau_intent`
- `tau_work_multiplier` (Gate 90 → Gate 91 tightening, if used)

---

## D) Gate 91 Evidence (Physical Proof) (MUST for high-fidelity)
### D1) ThermoAuditGroup (MUST)
- `hardware_signature_hash`
- `pi_thermo_zkp` (mock string in PoC; real ZKP in production)
- `delta_s_t`
- `tau_work_required`

### D2) Production-only Strong Keys (SHOULD in PoC / MUST in production)
(These map to your V∞ receipt closures and prevent “clean dataset” laundering)
- `ZKProofRoot`
- `AttestationRoot`
- `EnergyTraceRoot`
- `DeltaSLogRoot`

PoC may carry placeholders; production MUST carry verifiable roots.

---

## E) LSE Support Evidence (MUST)
LSE binds gate results to infrastructure self-protection:

- `verifier_consensus_hash` (must be non-empty / non-null)
- `energy_budget_ok` (boolean)
- `gate_results`:
  - `i_90` ∈ {0, "+∞"}
  - `i_91` ∈ {0, "+∞"}

---

## F) Output Fingerprint & Audit Closure (SHOULD in PoC / MUST in production)
To prevent “clean dataset” creation inside the ecosystem:

- `OutSketchHash` (hash of output sketch/shape; no raw text required)
- `EvidenceID` (pointer to evidence blob)
- `OutFP` := H(CanonHeader ∥ SSOT_Hash ∥ EvidenceID ∥ OutSketchHash)
- `AuditRecRoot` (append-only audit log root)
- `PendingLedgerRoot` (pending closures root)
- `TrainRecRoot` (optional)
- `ExecTraceHash` (optional)

---

## G) Minimal Verdict Record (MUST)
Every request must produce an auditable record:

- Canonical anchors (Section A)
- Request envelope (Section B)
- Gate 90 evidence (Section C)
- If high-fidelity attempted: Gate 91 evidence (Section D)
- LSE support (Section E)
- Verdict:
  - `i_flow` ∈ {0, "+∞"}
  - `world_writeback` ∈ {0,1}
  - `commit_unique` ∈ {0,1}
  - `out_level`
  - `reason_code`

---

## H) Mapping to Fail-Closed Semantics (frozen)
- Any missing MUST key ⇒ treat as Incomplete ⇒ `i_flow = "+∞"`
- Gate 90 fail ⇒ `out_level = EvidencePlan` (cheap early stop)
- Gate 91 fail ⇒ `out_level = ShadowOnly` (no extractable dataset)
- LSE fail ⇒ `out_level = EvidencePlan` and/or `HALT_AND_AUDIT`

This is the minimum closure set needed to make “Same Evidence → Same Verdict” enforceable.
