from fastapi import FastAPI
from app.detector import MetricsAnomalyDetector
from app.schemas import MetricsRequest, MetricsResponse


app = FastAPI(title="System Metrics Anomaly Detector", version="0.1.0")

detector = MetricsAnomalyDetector()


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/predict", response_model=MetricsResponse)
def predict(request: MetricsRequest) -> MetricsResponse:
    is_anomaly, score = detector.predict(request.model_dump())
    return MetricsResponse(is_anomaly=is_anomaly, anomaly_score=score)