# Research and data analysis portfolio

**Edwige Mpore Rwagasana**

I use data to investigate questions, compare methods, and explain what the evidence can—and cannot—support. These two individual coursework projects demonstrate data preparation, statistical analysis, model evaluation, and communication of findings.

| Project | Research question | Methods | Results from saved outputs |
|---|---|---|---|
| **[Instacart recommendations](projects/instacart/README.md)** · [Notebook](projects/instacart/analysis.ipynb) | Can shopping histories predict the next basket, and can related products improve discovery? | Time-ordered validation; popularity and personal baselines; item-item collaborative filtering; paired bootstrap; sensitivity checks | **Validation**, K=10: recency-frequency F1 **0.2645**, NDCG **0.4070**. Reserved final-test baskets were not evaluated. |
| **[Telco churn](projects/telco-churn/README.md)** · [Notebook](projects/telco-churn/analysis.ipynb) | How well do selected customer characteristics distinguish churners from customers who stay? | Exploratory analysis; binomial GLM; training-only scaling; stratified held-out evaluation | **Held-out test**, n=1,407: ROC AUC **0.831**; churn recall **0.55** at threshold 0.50. |

## Where to start

Start with the **Instacart project README** for the fuller evaluation workflow, including uncertainty, sensitivity checks, and a method that did not outperform the baseline. Then read **Telco** for an interpretable statistical model and the trade-off between false positives and missed churners. Each README includes a results figure; the notebooks contain the code and historical outputs behind the findings.

## Coursework and AI assistance

Both projects originated as individual coursework. Telco uses a course assignment template; Instacart builds on course checkpoints and examples. Course scaffolding is acknowledged rather than presented as entirely original code.

AI assisted with portfolio file review, documentation, notebook presentation, and a figure drawn from saved results. The extent of AI assistance and course-provided code in the original analyses still needs clarification before application submission. See [provenance](PROVENANCE.md) for the source notebooks and presentation changes.

## Reproduction status

The portfolio notebooks retain their saved outputs. Structure, Python syntax, documentation links, and reported summary results have been checked; **neither notebook has been executed end to end during this portfolio update**. The exact authorized source datasets were not found in the accessible local folders checked. Project [Instacart setup](projects/instacart/README.md#reproduce) and [Telco setup](projects/telco-churn/README.md#reproduce) instructions list the required files and working directories.

Dependencies remain unpinned because no complete analysis environment has been tested. A similarly named public dataset may differ from the course sample. Results describe these coursework samples, not deployment, causal effects, or measured business impact. No redistribution license is asserted over course material or source data.
