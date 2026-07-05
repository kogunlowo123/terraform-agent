"""Test configuration for Terraform Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "terraform-agent", "category": "DevOps & Platform Engineering"}
