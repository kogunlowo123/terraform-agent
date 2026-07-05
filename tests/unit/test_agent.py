"""Terraform Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_generate_terraform():
    """Test Generate Terraform configuration from natural language."""
    tools = AgentTools()
    result = await tools.generate_terraform(description="test", provider="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_detect_drift():
    """Test Compare Terraform state with actual cloud resources."""
    tools = AgentTools()
    result = await tools.detect_drift(workspace="test", resource_types="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_plan_remediation():
    """Test Generate terraform plan to fix detected drift."""
    tools = AgentTools()
    result = await tools.plan_remediation(drift_report="test", auto_apply=True)
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_validate_compliance():
    """Test Check Terraform plan against OPA/Sentinel policies."""
    tools = AgentTools()
    result = await tools.validate_compliance(plan_file="test", policy_set="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.terraform_agent_agent import TerraformAgentAgent
    agent = TerraformAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
