# Bay Area Boba EDA — What Makes a 5★ Cup?

> Exploring pricing, ratings, and location patterns across Bay Area boba shops.

![sample](assets/hero.png)

## 📌 TL;DR
- **Dataset**: `data/bayarea_boba_spots.csv` (place your CSV there)
- **Goal**: Find patterns in price, rating, and location
- **Tools**: Python (Pandas, Seaborn, Matplotlib, Folium), Jupyter
- **Highlights**: Fill in after you export 3–5 hero charts

## 🗺️ Key Questions
1. Which cities/clusters have the most shops?
2. Does higher price correlate with better ratings?
3. When do reviews/traffic spike during the week?
4. Do shops near campuses rate higher?

## 🛠️ Methods
- Cleaning: dedupe, date parsing (if available), missing value handling
- Features: `price_bucket`, `weekday/weekend`, `chain_flag`, `campus_radius_km` (optional)
- Viz: sorted bars with labels, rolling means, geospatial density map

## 📂 Repo
```
boba-eda/
  ├─ data/                 # raw & processed (gitignored by default)
  ├─ notebooks/            # Jupyter notebooks
  ├─ src/                  # clean.py, viz.py
  ├─ assets/               # exported plots
  ├─ README.md
  ├─ requirements.txt
```
*(Export 6–8 hero charts to /assets and reference them here.)*

## 🚀 Quickstart
```bash
python -m venv .venv && source .venv/bin/activate  # or use conda
pip install -r requirements.txt
jupyter lab
```
Open `notebooks/eda.ipynb` and run it.

## 📸 Sample Visuals
Add PNGs here after you generate them.

## ✅ Next Steps
- [ ] Add TL;DR bullets with numbers
- [ ] Export plots to `assets/` and embed
- [ ] Move helpers to `src/` for clean diffs
- [ ] (Optional) Streamlit dashboard
