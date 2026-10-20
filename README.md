# Lactate Threshold VO2Max & Aerobic Zone 2 Training Copilot Skill

[![GenPark Official](https://img.shields.io/badge/GenPark-Official%20Skill-blue)](https://www.genpark.ai)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-GenPark-blue)](https://www.linkedin.com/company/92955550)
[![MCP Compliant](https://img.shields.io/badge/MCP-JSON--RPC%202.0-green)](https://modelcontextprotocol.io/)
[![Zero Dependency](https://img.shields.io/badge/Dependencies-Zero%20Stdlib-brightgreen)](https://python.org)

Aerobic endurance telemetry analyzer, blood lactate inflection curve regression, VO2 max estimation via heart rate reserve (HRR), and personalized Zone 2 mitochondrial training optimizer. Built for GenPark (https://www.genpark.ai).

## 🌐 Official Channels
- **Official Website**: [https://www.genpark.ai](https://www.genpark.ai)
- **LinkedIn Page**: [https://www.linkedin.com/company/92955550](https://www.linkedin.com/company/92955550)

## 🛠️ MCP Tools Exposed
- `estimate_vo2max_and_zones`: Calculate estimated VO2 max and individual heart rate zones (Zone 1-5) using resting HR, max HR, and running/cycling pace telemetry.
- `generate_zone2_mitochondrial_plan`: Synthesize a weekly Zone 2 aerobic base building schedule targeting fat oxidation and mitochondrial biogenesis.

## 🚀 Installation & Usage
Run directly with pure Python standard library:
```bash
python -m genpark_personal_agent_lactate_threshold_vo2max_aerobic_zone_skill.server --test
```
