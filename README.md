# Research and data analysis portfolio

**Edwige Mpore Rwagasana**

Two individual coursework projects demonstrating data preparation, model evaluation, interpretation, and communication of limitations. This repository documents analyses already present in the source notebooks. It does not claim new experiments, deployed systems, or business impact.

| Project | Research question | Methods | Selected saved result |
|---|---|---|---|
| [Instacart recommendations](projects/instacart/) | How well do shopping histories predict the next basket, and can related products improve discovery? | Time-ordered validation, popularity and personal baselines, item-item collaborative filtering, paired customer bootstrap, sensitivity checks | Recency-frequency validation F1@10 **0.2645**, NDCG@10 **0.4070** |
| [Telco churn](projects/telco-churn/) | How well can selected customer characteristics distinguish churners from customers who stay? | Exploratory analysis, manual indicator variables, training-only scaling, binomial GLM, held-out evaluation | Test ROC AUC **0.831**; churn recall **0.55** at threshold 0.50 |

Start with Instacart for the more extensive evaluation workflow, then Telco for an interpretable statistical model. Open each `analysis.ipynb` to inspect code, saved outputs, and interpretations. Project READMEs give the study scope, findings, limitations, and rerun instructions.

## Scope and authorship

The author confirmed these two projects were individual work. The Telco notebook includes a course assignment template; the Instacart notebook references course checkpoints and examples. Individual completion does not imply that every line of scaffolding was independently authored. The exact extent of instructor-provided code and prior AI assistance has not been independently established.

AI assistance for this repository was used to review existing files, select samples, and prepare documentation and sharing copies. No additional analysis was performed to improve the reported results. See [provenance](PROVENANCE.md) for the source files, evidence locations, and exact packaging changes.

## Reproduction status

Saved outputs are available for inspection. These portfolio copies have been structurally checked, but have **not** been executed from a fresh environment. Dependencies are unpinned because the original environments were not recorded. Raw datasets are omitted; obtain the exact authorized course/source files before running. General public dataset versions may differ from the course samples and may not reproduce these numbers.

## Rights

No redistribution license is asserted over course-provided material or source datasets. No raw company datasets, instructor slide decks, or unrelated files are included.
