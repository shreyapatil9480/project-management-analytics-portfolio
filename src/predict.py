"""Batch inference CLI."""

import argparse
from pathlib import Path

import joblib
import pandas as pd

from features import prepare_features


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", default="reports/predictions.csv")
    args = parser.parse_args()
    model = joblib.load("models/model.joblib")
    df = pd.read_csv(args.input)
    X, _ = prepare_features(df)
    preds = model.predict(X)
    out = df.copy()
    out["prediction"] = preds
    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    out.to_csv(args.output, index=False)
    print(f"Wrote {{args.output}}")


if __name__ == "__main__":
    main()
