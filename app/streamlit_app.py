"""Streamlit inference dashboard."""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))


import joblib
import pandas as pd
import streamlit as st

from features import prepare_features

st.set_page_config(page_title="project-management-analytics-portfolio", layout="wide")
st.title("Project Management Analytics Portfolio")
data_path = Path("data/resource_utilization.csv")
if data_path.exists():
    df = pd.read_csv(data_path)
    st.dataframe(df.head(20), use_container_width=True)
    model_path = Path("models/model.joblib")
    if model_path.exists():
        model = joblib.load(model_path)
        X, _ = prepare_features(df)
        preds = model.predict(X)
        st.subheader("Predictions")
        st.dataframe(pd.DataFrame({"prediction": preds}).head(20))
    else:
        st.info("Train a model first: python src/train.py")
else:
    st.warning("Dataset not found. Run training pipeline first.")
