import math

INF = math.inf

class Gate91Reference:
    """
    Reference-only Gate 91 checker.
    - Uses mock rules (string prefix + numeric threshold)
    - No real ZKP verification / no real hardware attestation.
    """

    def check(self, payload: dict) -> dict:
        req_id = payload.get("request_id", "unknown")
        mult = float(payload.get("tau_work_multiplier", 1.0))

        thermo = payload.get("thermo_audit_group", {})
        zkp = str(thermo.get("pi_thermo_zkp", ""))

        delta_s = float(thermo.get("delta_s_t", 0.0))
        tau = float(thermo.get("tau_work_required", 1e9)) * mult

        zkp_ok = zkp.startswith("zkp_valid_")
        work_ok = (delta_s >= tau)

        if zkp_ok and work_ok:
            return {"request_id": req_id, "i_91": 0, "reason_code": "RC_SUCCESS"}

        return {"request_id": req_id, "i_91": "+∞", "reason_code": "RC_THERMO_FORGERY"}
