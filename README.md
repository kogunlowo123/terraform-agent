# Terraform Agent

[![CI](https://github.com/kogunlowo123/terraform-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/terraform-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: DevOps & Platform Engineering | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

Infrastructure-as-code agent that generates Terraform configurations, detects drift between state and reality, auto-remediates configuration drift, validates compliance policies, and manages state across multi-cloud environments.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `generate_terraform` | Generate Terraform configuration from natural language |
| `detect_drift` | Compare Terraform state with actual cloud resources |
| `plan_remediation` | Generate terraform plan to fix detected drift |
| `validate_compliance` | Check Terraform plan against OPA/Sentinel policies |
| `import_resource` | Import existing cloud resource into Terraform state |
| `estimate_cost` | Estimate monthly cost of Terraform plan using Infracost |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/terraform/generate` | Generate Terraform config |
| `POST` | `/api/v1/terraform/drift` | Detect configuration drift |
| `POST` | `/api/v1/terraform/remediate` | Plan drift remediation |
| `POST` | `/api/v1/terraform/validate` | Validate against policies |
| `POST` | `/api/v1/terraform/import` | Import existing resource |
| `POST` | `/api/v1/terraform/cost` | Estimate infrastructure cost |

## Features

- Tf Generation
- Drift Detection
- Auto Remediation
- Policy Validation
- State Management
- Module Library

## Integrations

- Terraform Cli
- Aws Provider
- Azure Provider
- Gcp Provider
- Infracost
- Opa Engine

## Architecture

```
terraform-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── terraform_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 6 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 6 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 6 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**Terraform + LLM + OPA**

---

Built as part of the Enterprise AI Agent Platform.
