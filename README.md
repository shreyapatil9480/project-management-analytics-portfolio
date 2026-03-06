[![Python CI](https://github.com/shreyapatil9480/project-management-analytics-portfolio/actions/workflows/python-ci.yml/badge.svg)](https://github.com/shreyapatil9480/project-management-analytics-portfolio/actions/workflows/python-ci.yml)
![Python](https://img.shields.io/badge/python-3.11-blue)
![pytest](https://img.shields.io/badge/tested%20with-pytest-0A9EDC)

# Project Management Analytics Portfolio

Where are resources overallocated?

**Stakeholder:** Resource Manager

## Key Insights

- Bench time under 4 hours/week signals overallocation risk.
- Billable hours above 42/week precedes overallocation flags.
- FTE above 1.2 on a single initiative raises overload probability.

## Dataset

Primary file: `data/resource_utilization.csv`  
Target variable: `overallocated`

## Getting Started

```bash
pip install -r requirements.txt
jupyter notebook notebooks/01_exploration.ipynb
```


## Testing

```bash
pip install -r requirements.txt
pytest tests/ --cov=src
```

## CLI Usage

```bash
python src/train.py
python src/predict.py --input data/sample_input.csv
```
## Tests

```bash
pytest tests/
```

## Next Steps

Deploy Streamlit dashboard for business self-service.

---
*Analytics portfolio project — 2025-11*

<!-- build 8 -->

## Live Demo

**[Open app](https://project-management-analytics-portfolio-dibeart8u2vuibpyjbcjc3.streamlit.app/)** — Streamlit Community Cloud

Local run: `streamlit run app/streamlit_app.py`

### Implemented

```bash
pip install -r requirements.txt
streamlit run app/streamlit_app.py
```
