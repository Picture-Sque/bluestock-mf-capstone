# 📈 Bluestock Mutual Fund Analytics Platform

## 🚀 Project Overview

The **Bluestock Mutual Fund Analytics Platform** is an end-to-end fintech analytics solution developed as part of the **Bluestock Data Analyst Internship Capstone Project**.

The platform ingests, cleans, validates, stores, analyzes, and visualizes mutual fund industry data to help investors, analysts, and financial institutions make data-driven investment decisions.

The project combines **Data Engineering**, **SQL Analytics**, **Financial Risk Analysis**, **Business Intelligence**, and **Advanced Analytics** into a single integrated workflow.

---

## 🎯 Business Problem

The Indian Mutual Fund industry has witnessed significant growth, with increasing investor participation, rising SIP inflows, and expanding Assets Under Management (AUM).

However, investors often face challenges such as:

* Fragmented fund data across multiple sources
* Difficulty comparing fund performance
* Limited visibility into risk-adjusted returns
* Lack of investor behavior analytics
* Absence of unified dashboards for decision-making

This project addresses these challenges by creating a centralized analytics platform for mutual fund data.

---

## 📊 Project Objectives

### Data Engineering

* Build a robust ETL pipeline
* Clean and validate financial datasets
* Create a structured analytics database

### Financial Analytics

* Calculate CAGR
* Compute Sharpe Ratio
* Compute Sortino Ratio
* Calculate Alpha and Beta
* Measure Maximum Drawdown
* Benchmark funds against market indices

### Investor Analytics

* Analyze investor demographics
* Study transaction behavior
* Evaluate SIP participation trends
* Perform cohort analysis

### Business Intelligence

* Build an interactive Power BI dashboard
* Enable fund-level filtering and exploration
* Generate actionable insights for stakeholders

---

## 🏗️ System Architecture

Raw Data Sources
↓
Data Ingestion
↓
Data Cleaning & Validation
↓
SQLite Data Warehouse
↓
Performance & Risk Analytics
↓
Advanced Analytics
↓
Power BI Dashboard
↓
Investor Insights & Reporting

---

## 📂 Project Structure

```text
bluestock-mf-capstone/

├── dashboard/
│   ├── bluestock_mf_dashboard.pbix
│   ├── Dashboard.pdf
│   └── screenshots/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── 01_data_ingestion.ipynb
│   ├── 03_EDA_Analysis.ipynb
│   ├── 04_performance_analytics.ipynb
│   └── 05_advanced_analytics.ipynb
│
├── outputs/
│
├── reports/
│
├── scripts/
│
├── sql/
│   ├── schema.sql
│   └── queries.sql
│
├── data_dictionary.md
├── requirements.txt
└── README.md
```

---

## 📚 Datasets Used

| Dataset               | Description                              |
| --------------------- | ---------------------------------------- |
| Fund Master           | Mutual fund metadata and classifications |
| NAV History           | Historical Net Asset Value records       |
| AUM Data              | Assets Under Management by fund house    |
| SIP Inflows           | Monthly SIP statistics                   |
| Category Inflows      | Fund category-wise inflows               |
| Folio Counts          | Industry investor participation          |
| Scheme Performance    | Risk and return metrics                  |
| Investor Transactions | Investor transaction history             |
| Portfolio Holdings    | Equity holdings of schemes               |
| Benchmark Indices     | Market benchmark performance             |

### Project Scale

* 40 Mutual Fund Schemes
* 46,000+ NAV Records
* 32,000+ Investor Transactions
* 4+ Years of Historical Data
* 10 Integrated Datasets

---

## ⚙️ ETL Pipeline

### Data Ingestion

* Imported all project datasets
* Retrieved live NAV data using APIs
* Validated AMFI scheme codes

### Data Cleaning

* Date standardization
* Missing value treatment
* Duplicate removal
* Transaction validation
* NAV consistency checks
* Performance metric validation

### Database Loading

* SQLite star-schema architecture
* Fact and dimension tables
* Analytical SQL querying support

---

## 🗄️ Database Design

### Dimension Tables

* dim_fund
* dim_date

### Fact Tables

* fact_nav
* fact_transactions
* fact_performance
* fact_aum
* fact_sip

---

## 📈 Exploratory Data Analysis

The project includes extensive EDA with 15+ visualizations.

### Key Analysis Areas

* NAV trend analysis
* AUM growth trends
* SIP inflow trends
* Category-wise inflows
* Investor demographics
* Geographic investment patterns
* Folio growth analysis
* Sector allocation analysis
* Correlation analysis among funds

---

## 📉 Performance & Risk Analytics

### Return Metrics

* Daily Returns
* Annualized Returns
* CAGR (1Y / 3Y)

### Risk Metrics

* Sharpe Ratio
* Sortino Ratio
* Alpha
* Beta
* Maximum Drawdown
* Tracking Error

### Fund Ranking Model

Composite Fund Score:

* 30% Return Ranking
* 25% Sharpe Ranking
* 20% Alpha Ranking
* 15% Expense Ratio Ranking
* 10% Drawdown Ranking

---

## 🔬 Advanced Analytics

### Value at Risk (VaR)

Calculated historical 95% VaR for each scheme.

### Conditional VaR (CVaR)

Measured expected losses beyond the VaR threshold.

### Cohort Analysis

Investor behavior segmented by investment cohorts.

### SIP Continuity Analysis

Identified investors at risk of SIP discontinuation.

### Fund Recommendation Engine

Generated fund recommendations based on investor risk appetite.

### Sector Concentration Analysis

Calculated Herfindahl-Hirschman Index (HHI) for portfolio concentration assessment.

---

## 📊 Interactive Power BI Dashboard

The dashboard contains four fully interactive pages.

### Page 1 — Industry Overview

* Industry AUM trends
* SIP growth trends
* Fund house comparison
* Key industry KPIs

### Page 2 — Fund Performance

* Risk vs Return analysis
* Fund scorecard
* Performance benchmarking

### Page 3 — Investor Analytics

* State-wise investment patterns
* Age-group analysis
* Transaction type distribution
* Investor behavior insights

### Page 4 — SIP & Market Trends

* SIP growth analysis
* Category inflows
* Market trend monitoring

---

## 🏆 Key Insights

* SBI Mutual Fund emerged as the largest AMC by AUM.
* Equity-oriented funds generated stronger long-term returns than debt-oriented funds.
* The 26–35 age group contributed the highest investment volume.
* SIP inflows showed consistent growth throughout the analysis period.
* Several schemes delivered superior risk-adjusted returns despite moderate absolute returns.
* Fund performance varied significantly across categories and risk profiles.

---

## 🛠️ Technologies Used

### Programming & Analytics

* Python
* Pandas
* NumPy

### Database

* SQLite
* SQLAlchemy
* SQL

### Visualization

* Power BI
* Matplotlib
* Seaborn

### Development

* Jupyter Notebook
* VS Code
* Git & GitHub

---

## ▶️ How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Run data processing scripts:

```bash
python scripts/data_ingestion.py
python scripts/load_database.py
```

Open:

```text
dashboard/bluestock_mf_dashboard.pbix
```

to explore the interactive dashboard.

---

## 👨‍💻 Author

**Krishnadas PS**

Data Analyst Intern Candidate

Bluestock Fintech Capstone Project

---

## Disclaimer

This project was created for educational and internship evaluation purposes. Mutual fund data used in the project is sourced from publicly available datasets and APIs. The platform is intended for analytics and learning purposes only and does not constitute financial advice.
