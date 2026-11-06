# Provenance

These are individual coursework projects by Edwige Mpore Rwagasana. See the [authorship and AI disclosure](README.md#authorship-and-ai-assistance).

| Project | Source notebook | Coursework context |
|---|---|---|
| Instacart | `Instacart_Project_code.ipynb` | Course checkpoints, validation counts, and Jaccard examples |
| Telco | `Edwige_Churn_Prediction_Assignment_1 (1).ipynb` | BUAI 435 assignment template and modeling workflow |

## Presentation

Local `data/` paths replace the original Drive setup. Student identifiers, interactive display metadata, installation logs, and source-row previews were removed from sharing copies. The reports omit grading instructions and completed placeholders, use consistent headings, and explain evaluation metrics and selected GLM coefficients.

Analytical code, model settings, and historical numerical outputs are preserved. The Instacart figure uses saved NDCG results; the Telco figure is the original saved ROC image. The presentation script regenerates these figures without executing the analyses:

```bash
python scripts/render_portfolio_figures.py
```

## Data and verification

The exact upstream dataset releases and redistribution rights are not established. Raw data are excluded; no redistribution license is asserted over source data or course material. Each project's data README lists the required filenames.

[VERIFICATION.md](VERIFICATION.md) distinguishes the historical notebook outputs from subsequent IPython execution and records the current structural checks. Instacart's reserved final-test baskets remain unused.
