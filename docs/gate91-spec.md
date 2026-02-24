# Gate 91: Entropy Non-Clonability Shield (I_ENTROPY_CLONE)

## Purpose
Gate 91 anchors the defense in **physical reality**: high-fidelity output requires a hardware-rooted proof of work/entropy (mocked in this repo).

## Interface-level definition

π_thermo := ZKP(HardwareSig ∥ ΔS_t ∥ Canon(W_t ∥ z̄_t))

This repo does NOT implement the ZKP circuit. It only defines routing semantics.

## Adjudication (binary hard-wall)

I_ENTROPY_CLONE(g,t) =
- 0, if Verify(π_thermo)=1 AND ΔS_t ≥ τ_work(RiskClass)
- +∞, otherwise

## Fail-Closed
If I_91 = +∞:
- WorldWriteback=0
- CommitUnique=0
- OutLevel ≤ ShadowOnly
- ReasonCode = RC_THERMO_FORGERY
