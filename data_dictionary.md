# Bluestock Mutual Fund Analytics Platform - Data Dictionary

## 1. Fund Master Dataset

Source: 01_fund_master.csv

| Column             | Data Type | Description                                |
| ------------------ | --------- | ------------------------------------------ |
| amfi_code          | INTEGER   | Unique identifier for mutual fund scheme   |
| fund_house         | TEXT      | Mutual fund company name                   |
| scheme_name        | TEXT      | Name of the mutual fund scheme             |
| category           | TEXT      | Fund category (Equity, Debt, Hybrid)       |
| sub_category       | TEXT      | Specific scheme classification             |
| plan               | TEXT      | Direct or Regular plan                     |
| launch_date        | DATE      | Fund launch date                           |
| benchmark          | TEXT      | Benchmark index used for comparison        |
| expense_ratio_pct  | REAL      | Annual expense ratio percentage            |
| exit_load_pct      | REAL      | Exit load percentage charged on redemption |
| min_sip_amount     | INTEGER   | Minimum SIP investment amount              |
| min_lumpsum_amount | INTEGER   | Minimum lump sum investment amount         |
| fund_manager       | TEXT      | Fund manager name                          |
| risk_category      | TEXT      | Risk classification                        |
| sebi_category_code | TEXT      | SEBI category code                         |

---

## 2. NAV History Dataset

Source: 02_nav_history.csv

| Column    | Data Type | Description            |
| --------- | --------- | ---------------------- |
| amfi_code | INTEGER   | Mutual fund identifier |
| date      | DATE      | NAV date               |
| nav       | REAL      | Net Asset Value        |

---

## 3. Investor Transactions Dataset

Source: 08_investor_transactions.csv

| Column             | Data Type | Description                |
| ------------------ | --------- | -------------------------- |
| investor_id        | TEXT      | Unique investor identifier |
| transaction_date   | DATE      | Transaction date           |
| amfi_code          | INTEGER   | Mutual fund identifier     |
| transaction_type   | TEXT      | SIP, Lumpsum, Redemption   |
| amount_inr         | INTEGER   | Transaction amount in INR  |
| state              | TEXT      | Investor state             |
| city               | TEXT      | Investor city              |
| city_tier          | TEXT      | T30 or B30 classification  |
| age_group          | TEXT      | Investor age category      |
| gender             | TEXT      | Investor gender            |
| annual_income_lakh | REAL      | Annual income in lakhs     |
| payment_mode       | TEXT      | Payment method used        |
| kyc_status         | TEXT      | KYC verification status    |

---

## 4. Scheme Performance Dataset

Source: 07_scheme_performance.csv

| Column             | Data Type | Description                   |
| ------------------ | --------- | ----------------------------- |
| return_1yr_pct     | REAL      | One-year return percentage    |
| return_3yr_pct     | REAL      | Three-year return percentage  |
| return_5yr_pct     | REAL      | Five-year return percentage   |
| benchmark_3yr_pct  | REAL      | Benchmark return percentage   |
| alpha              | REAL      | Excess return over benchmark  |
| beta               | REAL      | Volatility relative to market |
| sharpe_ratio       | REAL      | Risk-adjusted return metric   |
| sortino_ratio      | REAL      | Downside-risk-adjusted return |
| std_dev_ann_pct    | REAL      | Annualized standard deviation |
| max_drawdown_pct   | REAL      | Maximum observed loss         |
| aum_crore          | INTEGER   | Assets under management       |
| expense_ratio_pct  | REAL      | Expense ratio percentage      |
| morningstar_rating | INTEGER   | Morningstar fund rating       |
| risk_grade         | TEXT      | Risk category                 |

---

## 5. AUM Dataset

Source: 03_aum_by_fund_house.csv

| Column         | Data Type | Description               |
| -------------- | --------- | ------------------------- |
| date           | DATE      | Reporting date            |
| fund_house     | TEXT      | Fund house name           |
| aum_lakh_crore | REAL      | AUM in lakh crores        |
| aum_crore      | INTEGER   | AUM in crores             |
| num_schemes    | INTEGER   | Number of schemes managed |
