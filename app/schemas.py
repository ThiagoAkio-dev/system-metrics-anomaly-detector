from pydantic import BaseModel, Field


class MetricsRequest(BaseModel):
    cpu_usage: float = Field(..., ge=0, le=100)
    memory_usage: float = Field(..., ge=0, le=100)
    latency_ms: float = Field(..., ge=0)
    error_rate: float = Field(..., ge=0, le=1)
    requests_per_minute: int = Field(..., ge=0)


class MetricsResponse(BaseModel):
    is_anomaly: bool
    anomaly_score: float