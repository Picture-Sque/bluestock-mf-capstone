# Mutual Fund Analytics Platform 📊
### Bluestock Fintech Pvt. [cite_start]Ltd. — Data Analyst Internship Capstone Project [cite: 122]

## 📌 Project Overview
[cite_start]This repository hosts the end-to-end data engineering architecture, ETL pipeline, and interactive dashboard ecosystem developed during my Data Analyst Internship at Bluestock Fintech[cite: 121, 122]. [cite_start]The platform automates the ingestion of public mutual fund data from AMFI India, validates and cleans historical time-series blocks, constructs a relational Star Schema database, and surfaces high-density financial analytics for executive-level fund selection[cite: 139, 150].

---

## 👨‍💻 Project Metadata
* **Intern Name:** Krishnadas P S
* **GitHub Profile:** [@Picture-Sque](https://github.com/Picture-Sque)
* [cite_start]**Domain:** Mutual Fund / Fintech Domain Analytics [cite: 122]
* [cite_start]**Project Type:** Individual Capstone Project [cite: 122]
* **Project Manager:** Yash Kale (yashkale@bluestock.in)
* **Final Evaluation Deadline:** June 12, 2026

---

## 🛠️ Technical Stack
* **Language:** Python 3.10+ [cite: 345]
* **Data Manipulation & Processing:** Pandas, NumPy [cite: 345]
* **Statistical Computation:** SciPy [cite: 345]
* **Relational Storage Engine:** SQLite3 via SQLAlchemy ORM layer [cite: 345]
* **Exploratory Workspace:** Jupyter Lab / Notebooks [cite: 345]
* **Data Visualization Canvas:** Power BI Desktop / Matplotlib, Seaborn, Plotly [cite: 345]
* **Network Client Operations:** Requests (HTTP client hitting public REST endpoints) [cite: 345]

---

## 📂 Repository Architecture
[cite_start]The workspace strictly mirrors production-level modular patterns [cite: 346-359]:

```text
bluestock_mf_capstone/
├── data/
│   ├── raw/           ← Original immutable source files & live API text outputs [cite: 349]
│   ├── processed/     ← Cleaned, type-converted, and forward-filled datasets [cite: 354]
│   └── db/            ← Local bluestock_mf.db relational binary (Git ignored) [cite: 348, 349]
├── notebooks/
│   ├── 01_data_ingestion.ipynb    ← Initial validation, exploration, and profiling [cite: 351]
│   ├── 02_data_cleaning.ipynb     ← Data filtering, normalization, and type casting [cite: 350]
│   ├── 03_eda_analysis.ipynb      ← Visual pattern recognition & trend identification [cite: 350]
│   ├── 04_performance_analytics.py ← Quantitative calculation of risk-return profiles [cite: 351]
│   └── 05_advanced_analytics.ipynb ← Predictive modeling & portfolio risk simulations [cite: 350]
├── scripts/
│   ├── data_ingestion.py          ← System flat-file evaluation script
│   ├── live_nav_fetch.py          ← Target REST API ingestion tool [cite: 352]
│   ├── compute_metrics.py         ← Mathematical metric derivation script [cite: 351]
│   └── recommender.py             ← Risk-appetite mapping engine [cite: 353]
├── sql/
│   ├── schema.sql     ← DDL structure script detailing table constraints [cite: 355]
│   └── queries.sql    ← 10 analytical business verification queries [cite: 355]
├── dashboard/
│   └── bluestock_mf.pbix          ← Comprehensive Power BI analytical workbook [cite: 356]
├── reports/
│   ├── Final_Report.pdf           ← Executive-level narrative portfolio documentation [cite: 357]
│   └── Presentation.pptx          ← 12-slide stakeholder delivery deck [cite: 356]
├── requirements.txt   ← Python environment deployment locks
└── README.md          ← Project tracking master document
