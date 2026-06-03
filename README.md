# Bluestock Mutual Fund Analytics Platform

## Overview

This project was developed as part of the Bluestock Data Analyst Internship assessment.

The objective is to build a complete Mutual Fund Analytics Platform by performing:

* Data ingestion
* Data cleaning and validation
* SQLite database design
* ETL pipeline development
* SQL analytics
* Data documentation

The project uses mutual fund datasets containing fund information, NAV history, investor transactions, scheme performance metrics, SIP inflows, and AUM statistics.

---

## Project Structure

```text
BLUESTOCK_MF_CAPSTONE/

├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│
├── reports/
│
├── scripts/
│   ├── clean_nav_history.py
│   ├── clean_transactions.py
│   ├── clean_performance.py
│   ├── load_database.py
│   └── update_database.py
│
├── sql/
│   ├── schema.sql
│   └── queries.sql
│
├── data_dictionary.md
├── README.md
├── requirements.txt
└── bluestock_mf.db
```

---

## Datasets Used

| Dataset                      | Description                    |
| ---------------------------- | ------------------------------ |
| 01_fund_master.csv           | Mutual fund master information |
| 02_nav_history.csv           | Historical NAV records         |
| 03_aum_by_fund_house.csv     | Assets under Management data   |
| 04_monthly_sip_inflows.csv   | SIP inflow statistics          |
| 05_category_inflows.csv      | Category-wise inflows          |
| 06_industry_folio_count.csv  | Industry folio statistics      |
| 07_scheme_performance.csv    | Performance and risk metrics   |
| 08_investor_transactions.csv | Investor transaction records   |
| 09_portfolio_holdings.csv    | Portfolio holdings             |
| 10_benchmark_indices.csv     | Benchmark index history        |

---

## Data Cleaning Performed

### NAV History

* Converted date column to datetime
* Sorted by AMFI code and date
* Applied forward-fill logic
* Removed duplicate records
* Validated NAV values

### Investor Transactions

* Standardized transaction types
* Validated transaction amounts
* Converted dates
* Validated KYC status values

### Scheme Performance

* Validated numeric performance metrics
* Checked expense ratio ranges
* Flagged Sharpe ratio anomalies
* Removed duplicate records

---

## Database Design

A star schema was implemented using SQLite.

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

## Key Analytical Queries

1. Top 5 funds by AUM
2. Average NAV per month
3. SIP Year-over-Year growth
4. Transactions by state
5. Funds with expense ratio below 1%
6. Top funds by Sharpe ratio
7. Top funds by 3-year return
8. Average investment by age group
9. KYC status distribution
10. Transaction type distribution

---

## Technologies Used

* Python
* Pandas
* SQLite
* SQLAlchemy
* SQL
* Git
* VS Code

---

## Author

Krishnadas PS

Bluestock Data Analyst Internship Project
