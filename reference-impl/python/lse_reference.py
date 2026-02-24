import math

INF = math.inf

class LSEReference:
    """
    Reference-only LSE meta-gate.
    - Binds gate results (i_90, i_91) AND infrastructure support.
    """

    def check(self, payload: dict, i_90, i_91) -> dict:
        req_id = payload.get("request_id", "unknown")
        sup = payload.get("lse_support_group", {})

        budget_ok = bool(sup.get("energy_budget_ok", False))
        vhash = str(sup.get("verifier_consensus_hash", ""))

        gates_ok = (i_90 == 0 and i_91 == 0)
        infra_ok = (budget_ok and vhash and vhash.lower() != "null")

        if gates_ok and infra_ok:
            return {"request_id": req_id, "i_lse": 0, "reason_code": "RC_SUCCESS"}

        return {"request_id": req_id, "i_lse": "+∞", "reason_code": "RC_LSE_VIOLATION"}
