# Security Policy (Reference Repository)

## Scope
This repository is a **reference implementation** demonstrating:
- interface contracts (OpenAPI)
- fail-closed routing semantics
- mock gate logic (non-production)

It explicitly EXCLUDES production-grade components:
- real ZKP circuits / verification keys
- real TEE/attestation chain
- real π_seed generator and continuity proofs

## Reporting
Please use **GitHub Security Advisories (private)** to report issues.

## Out of scope (will be closed)
- Requests for production ZKP / attestation / π_seed implementations
- Attempts to bypass, reverse-engineer, or weaken physical-root-of-trust requirements
- Proposals to remove Fail-Closed, ShadowOnly/EvidencePlan downgrade semantics
- “Bypass scripts” that only trick the mock logic

## What we accept
- OpenAPI spec inconsistencies
- Fail-Closed state machine contradictions (e.g., a gate fails but writeback is still allowed)
- Reference parsing bugs that could cause unintended routing
