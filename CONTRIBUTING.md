# Contributing Guidelines (Reference Only)

Thank you for your interest.

## We accept
- Documentation improvements (docs/, README)
- OpenAPI spec fixes (spec/)
- CI improvements (.github/workflows)
- Reference mock logic cleanup (reference-impl/python), as long as semantics remain Fail-Closed

## We do NOT accept
- Any PR that weakens Fail-Closed semantics
- Requests for real ZKP circuits / TEE attestation / π_seed generator
- PRs that attempt to enable distillation-style extraction
- Large architectural rewrites (this repo is intentionally minimal & stable)

## PR rules
- Keep dependencies at zero unless absolutely necessary
- CI must continue to pass (`.github/workflows/demo.yml`)
