# Verification

## Subsequent IPython execution

The supplied execution record reports that the original CSV files were retrieved from my Drive, matching the source filenames used in the original notebooks. No raw data or source-file fingerprints are distributed. Matching source locations and reproduced results support sample identity, but do not establish an upstream release or redistribution license.

Both notebooks' unchanged Python code cells ran in order in separate fresh IPython processes in a new isolated Python 3.12 environment. All code cells completed without execution errors and embedded data/split assertions passed. The Jupyter/nbclient kernel could not start because of the environment's transport restrictions; this is an in-process code-execution verification, not a verified Jupyter UI/kernel session. The notebook files retain their historical saved outputs.

## Checked results

| Analysis | Reproduced result |
|---|---|
| Telco | AUC 0.831 at three decimals; confusion matrix [[904, 129], [169, 205]]; precision 0.61, recall 0.55, F1 0.58 for churn at two decimals |
| Instacart | Selected lambda 0.25; recency-frequency validation precision 0.2719, eligible recall 0.3530, F1 0.2645, NDCG 0.4070 at four decimals |
| Instacart comparisons | Repeat-frequency NDCG 0.3889; global-popularity NDCG 0.0918; item-item minus recency-frequency NDCG −0.3375, interval [−0.3455, −0.3296] at four decimals |

These checks reproduce selected published summaries, not every historical output byte. Display formatting and plots may differ by library version. No model, feature set, threshold, or hyperparameter was changed. No extra validation split or final-test evaluation was performed.

## Reproduce the check

Install [requirements-tested.txt](requirements-tested.txt), supply the original CSVs at the paths in each project's data README, then run:

```bash
python scripts/verify_analysis.py telco-churn
python scripts/verify_analysis.py instacart
```

The script checks required filenames before execution and selected result strings afterwards. It cannot establish source identity from filenames alone; use the original course files. It captures local stdout/stderr and display text in `.verification/`, excluded by `.gitignore`. Do not commit these logs or the raw data. Tested package versions describe the new verification environment, not the original coursework environment. The JupyterLab package is installed, but interactive server/kernel operation was not verified.

## Presentation review

This repository update applied the supplied execution record; it did not rerun either analysis. Both notebooks were validated for notebook format and unique cell IDs, and Python syntax was checked. Executable analysis cells and saved outputs were compared with the earlier PR revision and remain unchanged. Documentation links, image references, reported summaries, and the final diff were reviewed. The two results figures were inspected for legibility.

## Environment and scope

[requirements-tested.txt](requirements-tested.txt) records the supplied Python 3.12 execution environment, not the historical coursework environment. No new package installation or analytical execution was performed as part of this presentation review.

For an interactive session, activate the environment, change to `projects/instacart/` or `projects/telco-churn/`, then run `python -m jupyterlab` and open `analysis.ipynb`. This route was not verified in the execution environment. Instacart final-test evaluation remains future work; the reserved baskets were not used.
