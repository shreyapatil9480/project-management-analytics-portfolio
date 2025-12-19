import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from features import FEATURE_COLUMNS, prepare_features


def test_prepare_features_shape():
    df = pd.read_csv("data/resource_utilization.csv")
    X, y = prepare_features(df)
    assert X.shape[0] == len(df)
    assert len(y) == len(df)
    assert list(X.columns) == FEATURE_COLUMNS
