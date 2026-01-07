"""Tests for feature engineering."""

import pandas as pd

from features import FEATURE_COLUMNS, TARGET, prepare_features


def test_prepare_features_shape():
    df = pd.read_csv("data/resource_utilization.csv")
    X, y = prepare_features(df)
    assert X.shape[0] == len(df)
    assert len(y) == len(df)
    assert list(X.columns) == FEATURE_COLUMNS


def test_target_not_in_feature_matrix():
    df = pd.read_csv("data/resource_utilization.csv")
    X, _ = prepare_features(df)
    assert TARGET not in X.columns
