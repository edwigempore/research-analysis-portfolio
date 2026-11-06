# Telco customer churn

## Question and data

How well do selected customer characteristics distinguish customers who churn from those who stay? This individual BUAI 435 assignment uses `Telco-Customer-Churn.csv`. After converting `TotalCharges` to numeric and dropping missing values, the saved analysis contains 7,032 customers with an overall churn rate of 26.58%.

## Existing workflow

The notebook inspects missing values, encodes churn, constructs six manual indicator variables, plots tenure and churn by contract, and specifies nine predictors. It uses a stratified 80/20 train/test split with random seed 42. Continuous variables are standardized using training statistics only; indicators remain 0/1. A statsmodels binomial GLM with an intercept predicts churn probabilities, evaluated at a 0.50 threshold.

| Type | Predictors |
|---|---|
| Continuous | tenure, MonthlyCharges, TotalCharges |
| Indicators | female gender; phone service yes; fiber-optic internet; no internet; one-year contract; two-year contract |
| Reference categories | Male, no phone service, DSL internet, month-to-month contract |

## Saved held-out results

| Metric | Value |
|---|---:|
| ROC AUC | 0.831 |
| Accuracy (rounded source report) | 0.79 |
| Churn precision | 0.61 |
| Churn recall | 0.55 |
| Churn F1 | 0.58 |
| Test customers | 1,407 |

| Actual / predicted | Stayed | Churned |
|---|---:|---:|
| Stayed | 904 | 129 |
| Churned | 169 | 205 |

At the specified threshold, 169 churners are missed and 129 non-churners are flagged. These errors illustrate the trade-off between missed retention opportunities and unnecessary outreach. The notebook does not quantify actual campaign costs or recovered revenue.

## Limits

Relationships are associations. Lower churn among longer contracts does not establish a causal effect of contract length. A single held-out split does not establish stability across time or other populations. The threshold follows the assignment rather than a validated cost analysis. No deployment, intervention benefit, or financial outcome is claimed.

## Inspect or run

Read `analysis.ipynb` for the saved model summary, ROC curve, confusion matrix, and interpretations. To rerun, obtain the exact authorized source CSV, place it at `data/Telco-Customer-Churn.csv`, install `requirements.txt`, launch Jupyter from this directory, and run top to bottom. The portfolio copy has not been rerun.
