# Research and data analysis portfolio

**Edwige Mpore Rwagasana**

I use data to investigate questions, compare methods, and explain findings and their limits. These two individual coursework projects demonstrate data preparation, statistical analysis, and model evaluation.

| Project | Research question | Methods | Key result |
|---|---|---|---|
| [Instacart recommendations](projects/instacart/README.md) · [Analysis](projects/instacart/analysis.ipynb) | Can shopping histories predict the next basket and support discovery? | Time-ordered validation, recommendation baselines, item-item filtering, paired bootstrap | **Validation:** recency-frequency NDCG@10 **0.4070**, F1@10 **0.2645** |
| [Telco churn](projects/telco-churn/README.md) · [Analysis](projects/telco-churn/analysis.ipynb) | How well do customer characteristics distinguish churners from customers who stay? | Binomial GLM, training-only scaling, held-out evaluation | **Test, n=1,407:** AUC **0.831**, churn recall **0.55** at threshold 0.50 |

Start with Instacart for the evaluation workflow, then Telco for statistical interpretation. The notebooks retain historical outputs; subsequent IPython execution reproduced selected reported results. See [verification and environment limits](VERIFICATION.md).

## Authorship and AI assistance

I used AI to draft code, which I refined. I analyzed the results and wrote the reports.

Both projects use course materials: Telco began with an assignment template, and Instacart builds on course checkpoints and examples. See [provenance](PROVENANCE.md).
