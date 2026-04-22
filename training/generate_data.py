from pathlib import Path
import random
import pandas as pd


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "metrics.csv"


def generate_normal_sample() -> dict:
    return {
        "cpu_usage": round(random.uniform(20, 65), 2),
        "memory_usage": round(random.uniform(30, 75), 2),
        "latency_ms": round(random.uniform(80, 220), 2),
        "error_rate": round(random.uniform(0.0, 0.03), 4),
        "requests_per_minute": random.randint(120, 600),
    }


def generate_anomaly_sample() -> dict:
    anomaly_type = random.choice(["high_load", "failure_spike", "traffic_drop"])

    if anomaly_type == "high_load":
        return {
            "cpu_usage": round(random.uniform(85, 100), 2),
            "memory_usage": round(random.uniform(85, 100), 2),
            "latency_ms": round(random.uniform(400, 1200), 2),
            "error_rate": round(random.uniform(0.05, 0.2), 4),
            "requests_per_minute": random.randint(300, 900),
        }

    if anomaly_type == "failure_spike":
        return {
            "cpu_usage": round(random.uniform(40, 80), 2),
            "memory_usage": round(random.uniform(40, 85), 2),
            "latency_ms": round(random.uniform(300, 900), 2),
            "error_rate": round(random.uniform(0.15, 0.5), 4),
            "requests_per_minute": random.randint(50, 500),
        }

    return {
        "cpu_usage": round(random.uniform(5, 30), 2),
        "memory_usage": round(random.uniform(10, 40), 2),
        "latency_ms": round(random.uniform(250, 900), 2),
        "error_rate": round(random.uniform(0.04, 0.2), 4),
        "requests_per_minute": random.randint(0, 50),
    }


def main() -> None:
    normal_samples = [generate_normal_sample() for _ in range(1000)]
    anomaly_samples = [generate_anomaly_sample() for _ in range(80)]

    df = pd.DataFrame(normal_samples + anomaly_samples)
    DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(DATA_PATH, index=False)

    print(f"Dataset saved to: {DATA_PATH}")


if __name__ == "__main__":
    main()