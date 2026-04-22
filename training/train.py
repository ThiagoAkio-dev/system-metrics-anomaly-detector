from pathlib import Path
import joblib
import pandas as pd
from sklearn.ensemble import IsolationForest


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "metrics.csv"
MODEL_PATH = BASE_DIR / "models" / "anomaly_detector.joblib"


FEATURES = [
    "cpu_usage",
    "memory_usage",
    "latency_ms",
    "error_rate",
    "requests_per_minute",
]


def main() -> None:
    df = pd.read_csv(DATA_PATH)

    missing = [col for col in FEATURES if col not in df.columns]
    if missing:
        raise ValueError(f"Missing columns: {missing}")

    X = df[FEATURES]

    model = IsolationForest(
        n_estimators=200,
        contamination=0.08,
        random_state=42,
    )

    model.fit(X)

    MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, MODEL_PATH)

    print(f"Model saved to: {MODEL_PATH}")


if __name__ == "__main__":
    main()