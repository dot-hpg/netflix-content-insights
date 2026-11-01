#!/usr/bin/env bash
# Re-run the notebook end to end and export HTML + PDF into reports/.
# The PDF can also be made from the HTML with Chrome: File > Print > Save as PDF.
set -euo pipefail
cd "$(dirname "$0")/.."
jupyter nbconvert --to notebook --execute --inplace notebooks/Netflix_EDA_Case_Study.ipynb
jupyter nbconvert --to html notebooks/Netflix_EDA_Case_Study.ipynb --output-dir reports
jupyter nbconvert --to webpdf notebooks/Netflix_EDA_Case_Study.ipynb --output-dir reports 2>/dev/null \
  || echo "webpdf needs 'pip install nbconvert[webpdf]'; otherwise print reports/Netflix_EDA_Case_Study.html to PDF from Chrome."
