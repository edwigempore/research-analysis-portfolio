# Provenance and verification

## Coursework sources

**Edwige Mpore Rwagasana** completed these as individual coursework projects. Course scaffolding remains acknowledged; individual completion is not a claim of independently writing every line.

| Project | Original source filename | Origin visible in the source |
|---|---|---|
| Instacart | `Instacart_Project_code.ipynb` | Course checkpoints, validation counts, and Jaccard examples |
| Telco | `Edwige_Churn_Prediction_Assignment_1 (1).ipynb` | BUAI 435 assignment template and specified modeling workflow |

The exact extent of course-provided code and AI assistance during the original analyses still needs author clarification before application submission. Dataset filenames are documented in each project's `data/README.md`; the package does not establish the exact upstream releases or redistribution rights.

## Presentation changes

Initial sharing preparation replaced Drive setup and input paths with local `data/` paths, removed identity and interactive display metadata, and cleared setup/loader outputs containing logs or source-row previews. It retained analytical code and text/PNG results and supplied documentation and unpinned dependency lists. The initial upload added missing introductory cell IDs.

This polish pass rewrote project guides and notebook summaries, removed grading/submission instructions and completed comment-only placeholders, corrected headings, and added explanations of validation denominators and saved GLM coefficients. It removed private Drive identifiers and unrelated selection history from documentation. No executable analysis code, model settings, numerical outputs, or existing output images were changed in this pass.

The Instacart chart was recreated from saved four-method NDCG@10 results; the Telco ROC PNG was extracted unchanged from its saved output. `python scripts/render_portfolio_figures.py` regenerates these presentation assets without executing either notebook. No new model or experiment was added.

## AI assistance

AI assisted with source review, documentation, notebook presentation, results-figure preparation, and repository checks. Original-analysis assistance and the division between course scaffolding and the author's code require the clarification noted above. Added coefficient interpretations summarize saved estimates, not a newly fitted model.

## Verification performed during this update

- Reviewed methods, sample counts, metrics, and selected coefficient estimates against code and historical outputs. No material numerical discrepancy was found in the project README results.
- Validated notebook format and unique cell IDs; parsed Python syntax without executing analysis cells.
- Compared executable cells and saved outputs against the pre-polish repository revision; they are unchanged.
- Checked relative Markdown links, anchors, and image references; inspected the two README figures.
- Checked for remaining homework placeholders, private paths, student-ID/credential patterns, and accidental unrelated changes.

These checks are static review, not numerical replication. Validation/plotting tools ran in a new temporary environment (Python 3.9.6, nbformat 5.10.4, matplotlib 3.9.4); this is **not** a tested environment for either full analysis. Project dependencies remain unpinned.

## Execution blocker and future work

The exact source CSVs were not found in the repository, supplied package, or accessible local folders searched. Some local folders could not be searched because of OS access restrictions. No substitute dataset was downloaded. Neither notebook was executed end to end during this update; historical outputs do not demonstrate a fresh successful run.

Missing files are `aisles.csv`, `departments.csv`, `order_products.csv`, `orders.csv`, and `products.csv` under `projects/instacart/data/`, plus `Telco-Customer-Churn.csv` under `projects/telco-churn/data/`. Exact authorized files are needed to test an isolated analysis environment, compare regenerated results, and record tested versions. The original environment was not recorded.

Final-test evaluation for Instacart and additional Telco validation remain future work. No deployment, intervention benefit, or causal effect is claimed. No redistribution license is asserted over course material or source data.
