# VC 10-Page Deck (EN) — YFCore PoAIW (Gate 91 + Law)
**Version/Date:** DistillGuard-Core v1.0 — 2026-02-24  
**Company:** YFCore Technology Limited  
**One-liner:** Make industrial-scale model distillation **economically non-viable** by enforcing **hardware-rooted proof of AI work** and **fail-closed output sovereignty** at runtime.

---

## Slide 01 — Title
- **PoAIW: Physical Proof of AI Work**
- **Subtitle:** Gate 91 (Entropy Non-Clonability) + **Law (I_LSE)**  
  — elevate “model distillation” from a software cat-and-mouse game to **physically non-forgeable output sovereignty**
- **Company:** YFCore Technology Limited
- **Version/Date:** DistillGuard-Core v1.0 — 2026-02-24

---

## Slide 02 — Problem: Distillation / Model Extraction is Industrialized
- **Reality:** Frontier model capability is being siphoned via automated, distributed, low-cost extraction.  
  Traditional defenses (rate limiting / ToS / semantic detection) do not hold up.
- **Industrial pattern:**  
  - Massive account farms + proxy rotation + slow/low-frequency extraction  
  - Objective is **clean, high-fidelity output datasets** to train student models
- **Public evidence (footnotes):**
  - OpenAI memo to U.S. House committee alleging distillation via programmatic/obfuscated routing. [Reuters][reuters-openai]  
  - Anthropic public disclosure: ~24,000 fraudulent accounts, 16M+ interactions for distillation/extraction. [Anthropic][anthropic-distill] (also reported by Reuters: [Reuters][reuters-anthropic-distill])  
  - Google/GTIG reporting >100k-prompt extraction-scale activity and rising distillation experimentation. [Google Cloud][google-gtig]

---

## Slide 03 — Root Cause: Output Has No Physical Provenance
- Current systems can judge **“what was said”**, but often cannot prove **“this high-value output was produced by trusted hardware doing real work.”**
- Attackers can blend extraction traffic into normal usage with proxies, account pools, and slow concurrency. [Anthropic][anthropic-distill]
- **Conclusion:** As long as defense stays purely software-layer, industrial extraction will keep iterating around it.

### Positioning Box (place at bottom of this slide)
| Dimension | Claude Code Security (Anthropic) | PoAIW / DistillGuard (YFCore) |
|---|---|---|
| Layer | Software/semantic/logical (DevSecOps) | Software + Time + Physical (Runtime) |
| Target | **Prevent vulnerabilities** (pre-deployment) | **Prevent capability theft** via high-fidelity dataset harvesting (inference-time) |
| Stage | Pre-Deployment (code review & fixes) | Pre-Commit gateway (output sovereignty) |
| Distillation | No direct protection | Physical proof + fail-closed makes scaling economically non-viable |
> Claude Code Security public positioning: security review for codebases and remediation suggestions in Claude Code. [Anthropic][anthropic-claude-code-security]

---

## Slide 04 — Paradigm Shift: PoAIW (Physical Proof of AI Work)
- **Core idea:** Stop mainly auditing “semantics”; audit **proof of work** (physical & verifiable).
- **Definition:** Every high-fidelity / high-value output must carry verifiable hardware-rooted evidence  
  (TEE / confidential compute / attestation / cryptographic verification), bound to energy/entropy closure.
- **Executive analogy:** From “anti-plagiarism checks” to an “anti-counterfeit mint” — not guessing attackers, but enforcing **non-forgeable physical receipts**.

---

## Slide 05 — Minimal Deliverable: Gate 91 + Law (I_LSE)
### Gate 91 — `I_ENTROPY_CLONE` (Entropy Non-Clonability Hard Gate)
- High-assurance output is allowed only if:
  - ZK/verification passes
  - hardware attestation passes
  - thermodynamic/energy gates pass
- Otherwise: **Fail-Closed** (downgrade to ShadowOnly / zero writeback)

### Law — `I_LSE` (Meta-law / “Gate 0”)
- High-fidelity output is allowed only if **Intent × Temporal continuity × Physical proof** are simultaneously satisfied.
- Self-protecting clauses:
  - verifier trust
  - energy budget self-protection
  - shadow isolation (no dataset leakage)
- **Value:** A closed-loop story: not only blocks extraction, but enforces **self-consistency** and auditability.

---

## Slide 06 — Integration: No Model Retraining, Pluggable High-Assurance Runtime Core
- **Insertion point:** API output gateway / Pre-Commit stage as a sidecar or in-gateway module.
- **Dependencies:** Reuse existing TEE/confidential compute, attestation, signature verification, energy telemetry.
- **Deliverables:**
  1) **Open-source reference** — formal specs + mock interfaces + demo/CI proofs  
  2) **Production integration (evaluation/NDA)** — real hardware binding, evidence chain, audit & performance engineering

---

## Slide 07 — Why Customers Buy: Turn “Asset Leakage” into a Physical Constraint
- **Model providers:** Raise marginal extraction cost sharply — no hardware work proof, no trainable high-fidelity dataset.
- **Cloud vendors:** Upgrade “confidential computing” from “data-in-use protection” to **output sovereignty protection** (premium SKU).
- **Regulators/enterprise audit:** Natural fit for decidable, replayable, evidence-first governance.

---

## Slide 08 — Beachheads (Easy → Hard)
- **P0 (fastest to land):** high-assurance inference, critical infrastructure, financial risk engines, defense supply chains
- **P1:** cloud confidential compute + “high assurance inference” product line
- **P2:** frontier lab safety teams (joint research / pilots)
- **Macro framing:** International AI Safety Report 2026 emphasizes governance needs around advanced capability risks. [IASR][iasr-2026]

---

## Slide 09 — Business Model: Sell the Spearhead, Then Expand the Constitution
- **Revenue:**
  - SDK/gateway licensing (per node / per usage / per assurance tier)
  - cloud/hardware co-sell (attestation/TEE-linked premium share)
  - high-assurance integration services (audit, compliance, red-teaming, performance)
- **Upsell path:** Start with Gate 91 + Law (`I_LSE`), then expand into the full Trinity (add Gate 90: intent/extraction risk + temporal continuity).

---

## Slide 10 — Pilot Proposal (What You Need to Say Externally)
- **We provide:** minimal runnable PoC, integration guide, attack simulation, audit/replay report
- **We need:** isolated test environment + de-identified traffic samples + TEE/confidential compute verification interface (mock first is OK)
- **Milestones (weeks):** PoC → small-traffic grey rollout → high-assurance production lane

---

# References (Footnotes)
[reuters-openai]: https://www.reuters.com/world/china/openai-accuses-deepseek-distilling-us-models-gain-advantage-bloomberg-news-2026-02-12/ "Reuters: OpenAI memo alleging distillation (Feb 12, 2026)"
[anthropic-distill]: https://www.anthropic.com/news/detecting-and-preventing-distillation-attacks "Anthropic: Detecting and preventing distillation attacks"
[reuters-anthropic-distill]: https://www.reuters.com/world/china/chinese-companies-used-claude-improve-own-models-anthropic-says-2026-02-23/ "Reuters: Distillation/extraction reporting (Feb 23, 2026)"
[google-gtig]: https://cloud.google.com/blog/topics/threat-intelligence/distillation-experimentation-integration-ai-adversarial-use "Google Cloud: GTIG AI Threat Tracker (Feb 12, 2026)"
[iasr-2026]: https://internationalaisafetyreport.org/publication/international-ai-safety-report-2026 "International AI Safety Report 2026"
[anthropic-claude-code-security]: https://www.anthropic.com/news/claude-code-security "Anthropic: Claude Code Security (Feb 20, 2026)"
