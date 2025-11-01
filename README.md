# Project Management Analytics

This repository contains a self‑contained project designed to showcase data analysis, business analytics, and program management skills. It uses a **synthetic dataset** to simulate real‑world project management scenarios. The project includes exploratory data analysis (EDA), data visualizations, and a simple predictive model.

## Contents

- **`synthetic_project_data.csv`** – A synthetic dataset with 200 project records and the following columns:

  | Column | Description |
  |--------|------------|
  | `project_id` | Unique identifier for each project |
  | `project_name` | Name of the project |
  | `start_date` | Project start date |
  | `end_date` | Project end date |
  | `budget` | Budget allocated to the project (USD) |
  | `actual_cost` | Actual cost incurred by the project (USD) |
  | `team_size` | Number of team members involved |
  | `tasks_total` | Total number of tasks in the project |
  | `tasks_completed` | Number of tasks completed |
  | `risk_score` | Risk score on a scale from 0 (low risk) to 10 (high risk) |
  | `success` | Binary indicator (1 if the project met success criteria, 0 otherwise) |

- **`analysis.ipynb`** – A Jupyter notebook that walks through the analysis: loading the dataset, exploring its structure, visualizing key metrics, and building a logistic regression model to predict project success.

- **`requirements.txt`** – A list of Python dependencies needed to run the notebook.

## Getting Started

1. **Clone the repository**
   ```bash
   git clone https://github.com/your_username/project-management-analytics.git
   cd project-management-analytics
   ```

2. **Create a virtual environment (optional but recommended)**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install the required packages**
   ```bash
   pip install -r requirements.txt
   ```

4. **Open the notebook**
   ```bash
   jupyter notebook analysis.ipynb
   ```

   Alternatively, you can use `jupyter lab` or any other Jupyter environment to open and run the notebook.

## Analysis Overview

The `analysis.ipynb` notebook demonstrates:

- **Data loading and inspection** – Reading the CSV file into a pandas DataFrame and examining the structure of the data.
- **Descriptive statistics** – Summarizing numerical and categorical variables to understand the dataset's distribution.
- **Data visualizations** – Creating histograms, scatter plots, and bar charts to explore relationships between features such as budget vs. actual cost and risk score vs. success.
- **Predictive modeling** – Preparing the data, standardizing features, and training a logistic regression model to predict project success. Performance is evaluated using a confusion matrix and classification report.

## Use Cases

This project is designed for individuals preparing for roles such as **Business Analyst**, **Program Manager**, or **Data Analyst**. It demonstrates the ability to:

- Generate and work with structured datasets.
- Perform exploratory data analysis and communicate insights through visualizations.
- Build and evaluate a simple predictive model using real‑world‑inspired data.
- Write clear documentation and make projects reproducible through a requirements file and instructions.

## License

This project is released under the MIT License. Feel free to use and adapt it for your own learning and portfolio projects.

## Additional Notes

This update demonstrates how to create a branch and open a pull request on GitHub.

