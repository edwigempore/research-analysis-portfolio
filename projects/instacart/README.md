# Instacart next-basket recommendations

## Question and data

Can purchase history support useful next-basket reminders, and can product relationships add discovery? The saved notebook uses five course-supplied CSV tables: `aisles.csv`, `departments.csv`, `order_products.csv`, `orders.csv`, and `products.csv`.

The main validation split contains 5,000 customers, 33,230 fitting orders, 328,487 fitting product rows, and 24,367 candidate products. Of 50,638 validation item occurrences, 1,270 are absent from fitting history. Ranking metrics average across 4,994 customers with eligible targets; end-to-end recall includes all 5,000.

## Existing workflow

The notebook validates joins and uniqueness, uses earlier orders for fitting and each customer's last prior order for validation, compares global popularity, repeat frequency, and recency-frequency, and tunes recency weight on validation NDCG. It checks paired customer bootstrap intervals, list lengths of 5/10/15/20, short-list filling, earlier validation baskets, history length, popularity, and repeat versus discovery behavior. A fixed Jaccard-based item-item experiment is evaluated using the same metrics.

## Saved main validation results at K=10

| Model | Precision | Eligible recall | F1 | NDCG |
|---|---:|---:|---:|---:|
| Global popularity | 0.0668 | 0.0685 | 0.0602 | 0.0918 |
| Repeat frequency | 0.2594 | 0.3359 | 0.2518 | 0.3889 |
| Recency-frequency | 0.2719 | 0.3530 | 0.2645 | 0.4070 |
| Item-item CF | 0.0589 | 0.0602 | 0.0526 | 0.0695 |

The selected recency weight is 0.25. The paired NDCG advantage over repeat frequency is 0.0181, with a saved 95% interval of 0.0157–0.0205. The notebook compares that interval with a course practical margin of 0.01.

Recency-frequency recovers 50.76% of repeat-purchase item occurrences and zero discovery occurrences. Item-item CF recovers 3.88% of eligible discovery occurrences but loses substantial overall ranking quality. This specific experiment supports retaining the simpler restocking baseline.

## Limits

These are validation results. Final `eval_set == train` baskets remain reserved, and no final-test performance is claimed. Bootstrap intervals use the same validation customers involved in tuning; they do not remove model-selection uncertainty. The candidate rule prevents recommending unseen products, and personalized repeat rules cannot discover new-to-customer products. The item-item result applies to the tested fixed settings, not every collaborative-filtering method. No production or causal claim is made.

## Inspect or run

Read `analysis.ipynb` for saved outputs. To rerun, place the five exact authorized CSV files in `data/`, install the packages in `requirements.txt`, launch Jupyter from this directory, and run the notebook top to bottom. Setup cells were adapted from Colab Drive paths to relative paths; numerical analysis was preserved. The portfolio copy has not been rerun.
