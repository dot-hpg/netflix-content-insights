# Interactive dashboard

A static, filterable web dashboard of the Netflix catalogue (8,807 titles, to Sep 2021): growth, countries, genres, ratings, durations, launch timing, top actors/directors, a searchable title table, and the case study's insights and recommendations.

- `index.html`: the dashboard (no build step; Chart.js 4.4.1 is vendored as `chart.umd.min.js`)
- `data.json`: compact data built from `data/processed/netflix_cleaned.csv`
- `build_data.py`: regenerates `data.json`: `python dashboard/build_data.py data/processed/netflix_cleaned.csv dashboard/data.json`

## Deploy on Vercel

Import this repository at https://vercel.com/new, set **Root Directory** to `dashboard`, Framework Preset **Other**, leave build/output settings empty, and deploy.

Run locally: `python -m http.server -d dashboard 8000`, then open http://localhost:8000.
