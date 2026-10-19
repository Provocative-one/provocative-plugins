# Heritage Hub

The architecture and estimate for Heritage Hub, a headless content management platform for the Example Heritage Trust. This repository is a teaching fixture for the `architecture-authoring` plugin: every organization, person, figure and address in it is invented, and `example.com` stands in for every domain.

**Versions:** Architecture 0.3.1 · Estimate 0.2.0

| Document | What it holds |
|---|---|
| [arc42/hhb-architecture-arc42.md](arc42/hhb-architecture-arc42.md) | The architecture document: the system, its registers and decisions |
| [arc42/hhb-estimate-arc42.md](arc42/hhb-estimate-arc42.md) | The estimate document: arc42 read as a plan, pricing the architecture |
| [briefs/hhb-ctx-01.md](briefs/hhb-ctx-01.md) | Brief for the system context diagram |
| [briefs/hhb-cnt-01.md](briefs/hhb-cnt-01.md) | Brief for the container view, written before its build |
| [briefs/heritage-hub-milestone-plan.md](briefs/heritage-hub-milestone-plan.md) | Brief for the client-facing milestone plan |
| [published/heritage-hub-milestone-plan-1.0.0.md](published/heritage-hub-milestone-plan-1.0.0.md) | The milestone plan as sent |

## Owners of commitments

| Class | Owner |
|---|---|
| Commercial terms and pricing | Priya Raman, commercial lead |
| Service levels | Lena Okafor |
| Scope | Maya Lindqvist, for the Trust |
| Staffing and dates | Lena Okafor |

## Checks

Run `python3 tools/audit.py --root .` before cutting any version. The audit configuration is `tools/audit-config.json`.
