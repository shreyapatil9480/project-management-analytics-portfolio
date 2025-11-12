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
