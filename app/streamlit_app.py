"""Resource utilization dashboard — D06."""

import sys
from pathlib import Path

import joblib
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))

from features import TARGET, prepare_features

st.set_page_config(page_title="project-management-analytics-portfolio", page_icon="👥", layout="wide")

st.title("Project Management Analytics Portfolio")
st.caption("Where are resources overallocated? — Resource Manager view")

DATA_PATH = Path("data/resource_utilization.csv")
MODEL_PATH = Path("models/model.joblib")

if not DATA_PATH.exists():
    st.warning("Dataset not found. Run `python src/train.py` first.")
    st.stop()

df = pd.read_csv(DATA_PATH)
df["allocation_label"] = df[TARGET].map({0: "Balanced", 1: "Overallocated"})
df["utilization_pct"] = (df["billable_hours"] / (df["billable_hours"] + df["bench_time"].clip(lower=1)) * 100).clip(0, 100)

st.sidebar.header("Filters")
fte_range = st.sidebar.slider(
    "FTE assigned range",
    float(df["fte_assigned"].min()), float(df["fte_assigned"].max()),
    (float(df["fte_assigned"].min()), float(df["fte_assigned"].max())),
)
min_billable = st.sidebar.slider("Min billable hours", 0.0, float(df["billable_hours"].max()), 0.0)
show_overonly = st.sidebar.checkbox("Overallocated only", value=False)

filtered = df[
    df["fte_assigned"].between(fte_range[0], fte_range[1])
    & (df["billable_hours"] >= min_billable)
]
if show_overonly:
    filtered = filtered[filtered[TARGET] == 1]

overload_pct = filtered[TARGET].mean() * 100 if len(filtered) else 0
c1, c2, c3, c4 = st.columns(4)
c1.metric("Resources", f"{len(filtered):,}")
c2.metric("Overallocation rate", f"{overload_pct:.1f}%")
c3.metric("Avg billable hrs", f"{filtered['billable_hours'].mean():.1f}" if len(filtered) else "—")
c4.metric("Avg utilization %", f"{filtered['utilization_pct'].mean():.1f}" if len(filtered) else "—")

tab_capacity, tab_risk, tab_predict = st.tabs(["Capacity", "Risk signals", "Overload predictor"])

with tab_capacity:
    fig_scatter = px.scatter(
        filtered, x="billable_hours", y="bench_time", color="allocation_label",
        size="fte_assigned", hover_data=["resource_id", "utilization_pct"],
        title="Billable hours vs bench time (size = FTE)",
        color_discrete_map={"Balanced": "#3498db", "Overallocated": "#e67e22"},
    )
    st.plotly_chart(fig_scatter, use_container_width=True)

    fig_hist = px.histogram(
        filtered, x="fte_assigned", color="allocation_label", nbins=20, barmode="overlay",
        opacity=0.7, title="FTE distribution",
        color_discrete_map={"Balanced": "#3498db", "Overallocated": "#e67e22"},
    )
    st.plotly_chart(fig_hist, use_container_width=True)

with tab_risk:
    fig_util = px.box(
        filtered, x="allocation_label", y="utilization_pct", color="allocation_label",
        title="Utilization % by allocation status",
        color_discrete_map={"Balanced": "#3498db", "Overallocated": "#e67e22"},
    )
    st.plotly_chart(fig_util, use_container_width=True)

    top_risk = filtered.nlargest(12, "fte_assigned")
    fig_bar = px.bar(
        top_risk, x="resource_id", y="fte_assigned", color="allocation_label",
        title="Highest FTE assignments",
        color_discrete_map={"Balanced": "#3498db", "Overallocated": "#e67e22"},
    )
    st.plotly_chart(fig_bar, use_container_width=True)

with tab_predict:
    if not MODEL_PATH.exists():
        st.info("Train a model first: `python src/train.py`")
    else:
        model = joblib.load(MODEL_PATH)
        X, _ = prepare_features(filtered)
        preds = model.predict(X)
        proba = model.predict_proba(X)[:, 1] if hasattr(model, "predict_proba") else preds.astype(float)

        result = filtered.copy()
        result["predicted_over"] = preds
        result["p_overallocated"] = proba.astype(float)

        result["billable_bin"] = pd.cut(result["billable_hours"], bins=8).astype(str)
        result["bench_bin"] = pd.cut(result["bench_time"], bins=8).astype(str)
        heat = (
            result.pivot_table(
                values="p_overallocated", index="billable_bin", columns="bench_bin", aggfunc="mean",
            )
            .fillna(0.0)
            .astype(float)
        )
        if heat.empty:
            st.info("Not enough data for heatmap with current filters.")
        else:
            fig_heat = px.imshow(
                heat,
                labels=dict(x="Bench time band", y="Billable hours band", color="P(overload)"),
                title="Overload probability heatmap (billable × bench)",
                color_continuous_scale="YlOrRd",
                aspect="auto",
            )
            st.plotly_chart(fig_heat, use_container_width=True)

        sel = st.selectbox("Inspect resource", result["resource_id"].astype(str).tolist())
        row = result[result["resource_id"].astype(str) == sel].iloc[0]
        m1, m2, m3 = st.columns(3)
        m1.metric("Billable hrs", f"{row['billable_hours']:.0f}")
        m2.metric("Bench time", f"{row['bench_time']:.1f}")
        m3.metric("P(overallocated)", f"{row['p_overallocated']:.0%}")

        fig_gauge = go.Figure(go.Indicator(
            mode="gauge+number", value=row["p_overallocated"] * 100,
            title={"text": f"Resource {sel} — overload risk"},
            gauge={"axis": {"range": [0, 100]}, "bar": {"color": "#e67e22"}},
        ))
        st.plotly_chart(fig_gauge, use_container_width=True)

        st.dataframe(
            result[["resource_id", "fte_assigned", "billable_hours", "bench_time", TARGET, "p_overallocated"]]
            .sort_values("p_overallocated", ascending=False).head(20),
            use_container_width=True,
        )
