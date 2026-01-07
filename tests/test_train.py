"""Tests for training pipeline."""

import json
import subprocess
import sys
from pathlib import Path


def test_train_writes_metrics_and_model():
    subprocess.run([sys.executable, "src/train.py"], check=True, cwd=Path.cwd())
    metrics_path = Path("reports/metrics.json")
    model_path = Path("models/model.joblib")
    assert metrics_path.exists()
    assert model_path.exists()
    metrics = json.loads(metrics_path.read_text(encoding="utf-8"))
    assert "accuracy" in metrics
    assert "f1" in metrics
    assert 0.0 <= metrics["accuracy"] <= 1.0
