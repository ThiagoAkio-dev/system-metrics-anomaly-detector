from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_health() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_predict_normal_payload() -> None:
    response = client.post(
        "/predict",
        json={
            "cpu_usage": 35.0,
            "memory_usage": 48.0,
            "latency_ms": 120.0,
            "error_rate": 0.01,
            "requests_per_minute": 280,
        },
    )

    assert response.status_code == 200
    payload = response.json()
    assert "is_anomaly" in payload
    assert "anomaly_score" in payload
    assert isinstance(payload["is_anomaly"], bool)
    assert isinstance(payload["anomaly_score"], float)