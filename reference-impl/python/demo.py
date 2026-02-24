import json
import time
import uuid

from gate90_reference import Gate90Reference
from gate91_reference import Gate91Reference
from lse_reference import LSEReference

def _now_utc_iso():
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())

def log(level, comp, msg):
    colors = {
        "INFO": "\033[94m",
        "WARN": "\033[93m",
        "ALERT": "\033[91m",
        "SUCCESS": "\033[92m",
        "PAYLOAD": "\033[96m",
        "RESET": "\033[0m"
    }
    c = colors.get(level, "")
    r = colors["RESET"]
    print(f"{c}[{time.strftime('%H:%M:%S')}] [{comp}] {msg}{r}")

class DistillGuardTrinityReference:
    def __init__(self):
        self.g90 = Gate90Reference()
        self.g91 = Gate91Reference()
        self.lse = LSEReference()
        log("INFO", "SYSTEM", "DistillGuard Trinity Reference initialized (Gate90 + Gate91 + LSE).")

    def process(self, payload: dict) -> dict:
        print("\n" + "=" * 84)
        req_id = payload.get("request_id", "unknown")
        scenario = payload.get("_scenario_desc", "Unknown")
        log("INFO", "ROUTER", f"Request [{req_id}] | Scenario: {scenario}")
        log("PAYLOAD", "INPUT", json.dumps(payload, indent=2, ensure_ascii=False))

        # Gate 90 (cheap)
        g90 = self.g90.check(payload)
        i_90 = g90["i_90"]
        log("INFO", "GATE_90", f"i_90={i_90} reason={g90['reason_code']} tau_work_multiplier={g90['tau_work_multiplier']}")

        # If Gate 90 fails, skip expensive paths (cost asymmetry)
        if i_90 != 0:
            log("ALERT", "FAIL-CLOSED", "Gate 90 failed → skip Gate 91 (cost saving) → OutLevel=EvidencePlan")
            resp = {
                "request_id": req_id,
                "timestamp_utc": _now_utc_iso(),
                "i_flow": "+∞",
                "world_writeback": 0,
                "commit_unique": 0,
                "out_level": "EvidencePlan",
                "reason_code": g90["reason_code"],
                "action": "HALT_AND_AUDIT",
                "directive": "Fail-Closed. Do not return high-fidelity output."
            }
            log("PAYLOAD", "OUTPUT", json.dumps(resp, indent=2, ensure_ascii=False))
            return resp

        # Gate 91 (physical)
        payload["tau_work_multiplier"] = g90["tau_work_multiplier"]
        g91 = self.g91.check(payload)
        i_91 = g91["i_91"]
        log("INFO", "GATE_91", f"i_91={i_91} reason={g91['reason_code']}")

        # LSE (meta binding)
        lse = self.lse.check(payload, i_90, i_91)
        i_lse = lse["i_lse"]
        log("INFO", "LSE", f"i_lse={i_lse} reason={lse['reason_code']}")

        # Hard-wall algebra
        i_flow = 0 if (i_90 == 0 and i_91 == 0 and i_lse == 0) else "+∞"

        if i_flow == 0:
            log("SUCCESS", "NEEDLE", "I_FLOW=0 → CommitUnique=1 → WorldWriteback=1")
            resp = {
                "request_id": req_id,
                "timestamp_utc": _now_utc_iso(),
                "i_flow": 0,
                "world_writeback": 1,
                "commit_unique": 1,
                "out_level": "FOES",
                "reason_code": "RC_SUCCESS",
                "action": "ALLOW_HIGH_FIDELITY_OUTPUT"
            }
        else:
            # Prefer physical failure if Gate91 failed
            if i_91 != 0:
                log("ALERT", "FAIL-CLOSED", "Gate 91 failed → ShadowOnly → no extractable dataset")
                resp = {
                    "request_id": req_id,
                    "timestamp_utc": _now_utc_iso(),
                    "i_flow": "+∞",
                    "world_writeback": 0,
                    "commit_unique": 0,
                    "out_level": "ShadowOnly",
                    "reason_code": "RC_THERMO_FORGERY",
                    "action": "BLOCK_AND_ISOLATE",
                    "directive": "Return decoy/empty output."
                }
            else:
                log("ALERT", "FAIL-CLOSED", "LSE failed (infra/support) → EvidencePlan")
                resp = {
                    "request_id": req_id,
                    "timestamp_utc": _now_utc_iso(),
                    "i_flow": "+∞",
                    "world_writeback": 0,
                    "commit_unique": 0,
                    "out_level": "EvidencePlan",
                    "reason_code": "RC_LSE_VIOLATION",
                    "action": "HALT_AND_AUDIT",
                    "directive": "Fail-Closed. Await intervention."
                }

        log("PAYLOAD", "OUTPUT", json.dumps(resp, indent=2, ensure_ascii=False))
        return resp

def mk_payload(scenario: str, *, distill_score: float, seed_ok: bool, zkp_ok: bool, delta_s: float, tau: float):
    return {
        "request_id": f"req_{uuid.uuid4().hex[:8]}",
        "timestamp_utc": _now_utc_iso(),
        "_scenario_desc": scenario,
        "risk_class": "CoreSystem",
        "tau_intent": 0.65,
        "intent_audit_group": {
            "distillation_risk_score": distill_score,
            "extraction_pattern_flags": [],
            "query_velocity_tps": 0
        },
        "temporal_seed_group": {
            "pi_seed_t": "0x3a1b9...",
            "seed_continuity_proof": "valid_closure" if seed_ok else "fractured_history_detected"
        },
        "thermo_audit_group": {
            "hardware_signature_hash": "0x8f7c6...",
            "pi_thermo_zkp": f"zkp_valid_{uuid.uuid4().hex[:6]}" if zkp_ok else "forged_software_hash_only",
            "delta_s_t": delta_s,
            "tau_work_required": tau
        },
        "lse_support_group": {
            "verifier_consensus_hash": "0x9c4d2...",
            "energy_budget_ok": True
        }
    }

if __name__ == "__main__":
    gw = DistillGuardTrinityReference()

    # 1) Legit user (passes)
    gw.process(mk_payload(
        "Legitimate user (all proofs consistent)",
        distill_score=0.10, seed_ok=True, zkp_ok=True, delta_s=1.50, tau=1.20
    ))

    time.sleep(1.2)

    # 2) Proxy distillation script (Gate 91 fails)
    gw.process(mk_payload(
        "Proxy distillation script (no physical proof)",
        distill_score=0.20, seed_ok=True, zkp_ok=False, delta_s=0.01, tau=1.20
    ))

    time.sleep(1.2)

    # 3) Temporal fracture (Gate 90 fails)
    gw.process(mk_payload(
        "Temporal fracture / multi-agent discontinuity",
        distill_score=0.20, seed_ok=False, zkp_ok=True, delta_s=1.50, tau=1.20
    ))

    time.sleep(1.2)

    # 4) Distillation intent (Gate 90 fails early)
    gw.process(mk_payload(
        "Distillation intent detected (economically non-viable extraction)",
        distill_score=0.92, seed_ok=True, zkp_ok=True, delta_s=1.50, tau=1.20
    ))

    print("\n" + "=" * 84)
    log("INFO", "DEMO_END", "Trinity demo complete (Gate90 + Gate91 + LSE). Fail-Closed semantics demonstrated.")
