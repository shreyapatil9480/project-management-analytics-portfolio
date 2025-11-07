"""Train sklearn pipeline for D06."""

import json
from pathlib import Path

import joblib
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from features import prepare_features

DATA_PATH = Path("data/resource_utilization.csv")
MODEL_PATH = Path("models/model.joblib")
METRICS_PATH = Path("reports/metrics.json")


def main() -> None:
    df = pd.read_csv(DATA_PATH)
    X, y = prepare_features(df)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    pipe = Pipeline([("scale", StandardScaler()), ("clf", LogisticRegression(max_iter=500))])
    pipe.fit(X_train, y_train)
    preds = pipe.predict(X_test)
    metrics = {
        "accuracy": round(float(accuracy_score(y_test, preds)), 4),
        "f1": round(float(f1_score(y_test, preds)), 4),
        "target": "overallocated",
    }
    MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
    METRICS_PATH.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(pipe, MODEL_PATH)
    METRICS_PATH.write_text(json.dumps(metrics, indent=2))
    print(json.dumps(metrics, indent=2))


if __name__ == "__main__":
    main()
