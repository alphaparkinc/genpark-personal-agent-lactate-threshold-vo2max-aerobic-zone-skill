# -*- coding: utf-8 -*-
"""MCP Server for Lactate Threshold VO2Max & Aerobic Zone 2 Training Copilot Skill."""
import sys
import json
import logging
from typing import Dict, Any

from .core import LactateThresholdVO2MaxOptimizer

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

TOOLS_SCHEMA = [
    {
        "name": "estimate_vo2max_and_zones",
        "description": "Calculate estimated VO2 max and individual heart rate zones (Zone 1-5) using resting HR, max HR, and running/cycling pace telemetry.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "resting_heart_rate": {
                    "type": "integer"
                },
                "max_heart_rate": {
                    "type": "integer"
                },
                "age_years": {
                    "type": "integer"
                },
                "sex": {
                    "type": "string",
                    "enum": [
                        "male",
                        "female"
                    ]
                },
                "best_5k_time_minutes": {
                    "type": "number"
                }
            },
            "required": [
                "resting_heart_rate",
                "max_heart_rate",
                "age_years",
                "sex"
            ]
        }
    },
    {
        "name": "generate_zone2_mitochondrial_plan",
        "description": "Synthesize a weekly Zone 2 aerobic base building schedule targeting fat oxidation and mitochondrial biogenesis.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "weekly_available_hours": {
                    "type": "number"
                },
                "current_vo2max": {
                    "type": "number"
                },
                "zone2_lower_hr": {
                    "type": "integer"
                },
                "zone2_upper_hr": {
                    "type": "integer"
                }
            },
            "required": [
                "weekly_available_hours",
                "zone2_lower_hr",
                "zone2_upper_hr"
            ]
        }
    }
]

def handle_rpc(line: str) -> str:
    try:
        req = json.loads(line)
        method = req.get("method")
        msg_id = req.get("id")

        if method == "initialize":
            res = {
                "protocolVersion": "2024-11-05",
                "capabilities": {"tools": {}},
                "serverInfo": {"name": "genpark-personal-agent-lactate-threshold-vo2max-aerobic-zone-skill", "version": "1.0.0"}
            }
            return json.dumps({"jsonrpc": "2.0", "id": msg_id, "result": res})

        elif method == "tools/list":
            return json.dumps({"jsonrpc": "2.0", "id": msg_id, "result": {"tools": TOOLS_SCHEMA}})

        elif method == "tools/call":
            params = req.get("params", {})
            tool_name = params.get("name")
            args = params.get("arguments", {})

            target_func = getattr(LactateThresholdVO2MaxOptimizer, tool_name, None)
            if not target_func:
                return json.dumps({"jsonrpc": "2.0", "id": msg_id, "error": {"code": -32601, "message": f"Method not found: {tool_name}"}})

            result = target_func(**args)
            return json.dumps({
                "jsonrpc": "2.0",
                "id": msg_id,
                "result": {
                    "content": [{"type": "text", "text": json.dumps(result, indent=2)}]
                }
            })

        else:
            return json.dumps({"jsonrpc": "2.0", "id": msg_id, "error": {"code": -32601, "message": f"Method not found: {method}"}})

    except Exception as e:
        return json.dumps({"jsonrpc": "2.0", "id": req.get("id") if "req" in locals() else None, "error": {"code": -32000, "message": str(e)}})

def run_test():
    print("[TEST] Running internal RPC self-test for genpark-personal-agent-lactate-threshold-vo2max-aerobic-zone-skill...")
    init_req = json.dumps({"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {}})
    init_res = json.loads(handle_rpc(init_req))
    assert init_res.get("result", {}).get("serverInfo", {}).get("name") == "genpark-personal-agent-lactate-threshold-vo2max-aerobic-zone-skill"

    list_req = json.dumps({"jsonrpc": "2.0", "id": 2, "method": "tools/list", "params": {}})
    list_res = json.loads(handle_rpc(list_req))
    assert len(list_res.get("result", {}).get("tools", [])) == 2
    print(f"[TEST] SUCCESS: {len(list_res['result']['tools'])} tools verified.")
    return True

if __name__ == "__main__":
    if "--test" in sys.argv:
        if run_test():
            sys.exit(0)
        sys.exit(1)

    for line in sys.stdin:
        if not line.strip():
            continue
        out = handle_rpc(line)
        sys.stdout.write(out + "\n")
        sys.stdout.flush()
