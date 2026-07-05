# Terraform Agent Architecture

Infrastructure-as-code agent that generates Terraform configurations, detects drift between state and reality, auto-remediates configuration drift, validates compliance policies, and manages state across multi-cloud environments.

## Domain Tools

- **generate_terraform**: Generate Terraform configuration from natural language
- **detect_drift**: Compare Terraform state with actual cloud resources
- **plan_remediation**: Generate terraform plan to fix detected drift
- **validate_compliance**: Check Terraform plan against OPA/Sentinel policies
- **import_resource**: Import existing cloud resource into Terraform state
- **estimate_cost**: Estimate monthly cost of Terraform plan using Infracost