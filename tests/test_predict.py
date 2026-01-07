"""Tests for batch inference CLI."""

import subprocess
import sys
from pathlib import Path

import pandas as pd


def test_predict_writes_output_with_prediction_column():
    subprocess.run([sys.executable, "src/train.py"], check=True, cwd=Path.cwd())
    input_csv = Path("data/resource_utilization.csv")
    output_csv = Path("reports/test_predictions.csv")
    if output_csv.exists():
        output_csv.unlink()
    subprocess.run(
        [
            sys.executable,
            "src/predict.py",
            "--input",
            str(input_csv),
            "--output",
            str(output_csv),
        ],
        check=True,
        cwd=Path.cwd(),
    )
    assert output_csv.exists()
    out = pd.read_csv(output_csv)
    assert "prediction" in out.columns
    assert len(out) == len(pd.read_csv(input_csv))
