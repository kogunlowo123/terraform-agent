"""Terraform Agent - Domain-Specific Schemas."""

from datetime import datetime
from uuid import UUID, uuid4
from typing import Any, Optional
from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    """Chat request."""
    message: str
    conversation_id: UUID | None = None
    stream: bool = False
    context: dict[str, Any] | None = None


class ChatResponse(BaseModel):
    """Chat response."""
    message: str
    conversation_id: UUID
    message_id: UUID
    sources: list[dict[str, Any]] = []
    tool_results: list[dict[str, Any]] = []
    model: str
    latency_ms: float
    timestamp: datetime


class StreamChunk(BaseModel):
    """Streaming response chunk."""
    chunk: str
    conversation_id: UUID
    done: bool = False


class HealthResponse(BaseModel):
    """Health check response."""
    status: str
    version: str
    uptime_seconds: float
    agent: str
    features: list[str]


class TerraformGenerateRequest(BaseModel):
    """TerraformGenerateRequest for Terraform Agent."""
    description: str
    provider: str
    environment: str = 'production'
    module_style: bool = True


class DriftReport(BaseModel):
    """DriftReport for Terraform Agent."""
    workspace: str
    drifted_resources: list[dict]
    missing_resources: list[str]
    extra_resources: list[str]
    severity: str


class CostEstimate(BaseModel):
    """CostEstimate for Terraform Agent."""
    monthly_cost: float
    currency: str
    breakdown: list[dict]
    diff_from_current: float | None

