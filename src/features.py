"""Feature engineering for D06."""

import pandas as pd


FEATURE_COLUMNS = ['fte_assigned', 'billable_hours', 'bench_time']
TARGET = "overallocated"


def prepare_features(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.Series]:
    """Select model features and target."""
    X = df[FEATURE_COLUMNS].copy()
    for col in X.select_dtypes(include="object").columns:
        X[col] = X[col].astype("category").cat.codes
    y = df[TARGET]
    return X, y
