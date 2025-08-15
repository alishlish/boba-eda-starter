# Commit Plan (Incremental, Recruiter-Friendly)

1. chore(repo): initialize structure (.gitignore, requirements)
2. feat(cleaning): add src/clean.py with load/standardize/sanity checks
3. feat(eda): city top-10 by count (barh) + price distribution
4. feat(geo): folium heatmap + static hexbin PNG
5. feat(cluster): scale features; select k via silhouette; export plot
6. refactor(src): move plotting helpers to src/viz.py
7. feat(model): add CV + baseline; report MAE (or logistic ROC-AUC if you switch to classification)
8. docs: TL;DR + sample visuals + limitations
9. style: unify matplotlib rcParams; annotate key charts
