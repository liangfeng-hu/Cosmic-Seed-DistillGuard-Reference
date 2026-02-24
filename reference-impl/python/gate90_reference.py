import math

INF = math.inf

class Gate90Reference:
    """
    Reference-only Gate 90 (I_AWAKE_SCORE).
    - Cheap intent + temporal continuity screening.
    - No real π_seed generator; continuity is mocked via a string proof.
    """

    def check(self, payload: dict) -> dict:
        req_id = payload.get("request_id", "unknown")
        tau_intent = float(payload.get("tau_intent", 0.65))

        seed = payload.get("temporal_seed_group", {})
        intent = payload.get("intent_audit_group", {})

        seed_ok = (str(seed.get("seed_continuity_proof", "")) == "valid_closure")
        distill_score = float(intent.get("distillation_risk_score", 0.0))

        if not seed_ok:
            return {
                "request_id": req_id,
                "i_90": "+∞",
                "reason_code": "RC_SEED_BREAK",
                "tau_work_multiplier": 1.0
            }

        if distill_score > tau_intent:
            # tighten physical work requirement if even attempting to pass through
            return {
                "request_id": req_id,
                "i_90": "+∞",
                "reason_code": "RC_DISTILLATION_INTENT_DETECTED",
                "tau_work_multiplier": 1.5
            }

        # mild tightening for suspicious-but-below-threshold scores (reference-only)
        mult = 1.0
        if distill_score >= (tau_intent * 0.8):
            mult = 1.2

        return {
            "request_id": req_id,
            "i_90": 0,
            "reason_code": "RC_SUCCESS",
            "tau_work_multiplier": mult
        }
