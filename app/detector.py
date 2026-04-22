from pathlib import Path
import joblib
import pandas as pd


BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "models" / "anomaly_detector.joblib"

FEATURES = [
    "cpu_usage",
    "memory_usage",
    "latency_ms",
    "error_rate",
    "requests_per_minute",
]


class MetricsAnomalyDetector:
    def __init__(self) -> None:
        if not MODEL_PATH.exists():
            raise FileNotFoundError(
                f"Model file not found at {MODEL_PATH}. Run training first."
            )
        self.model = joblib.load(MODEL_PATH)

    def predict(self, metrics: dict) -> tuple[bool, float]:
        row = pd.DataFrame([[metrics[f] for f in FEATURES]], columns=FEATURES)

        prediction = self.model.predict(row)[0]
        score = float(self.model.decision_function(row)[0])

        is_anomaly = prediction == -1
        return is_anomaly, score