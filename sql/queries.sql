-- =====================================================
-- BLUESTOCK DAY 2 ANALYTICAL QUERIES
-- =====================================================

-- =====================================================
-- 1. TOP 5 FUNDS BY AUM
-- =====================================================

SELECT
    scheme_name,
    aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;


-- =====================================================
-- 2. AVERAGE NAV PER MONTH
-- =====================================================

SELECT
    SUBSTR(date,1,7) AS month,
    ROUND(AVG(nav),2) AS avg_nav
FROM fact_nav
GROUP BY month
ORDER BY month;


-- =====================================================
-- 3. SIP YOY GROWTH
-- =====================================================

SELECT
    month,
    sip_inflow_crore,
    yoy_growth_pct
FROM fact_sip
ORDER BY month;


-- =====================================================
-- 4. TRANSACTIONS BY STATE
-- =====================================================

SELECT
    state,
    COUNT(*) AS total_transactions,
    SUM(amount_inr) AS total_amount
FROM fact_transactions
GROUP BY state
ORDER BY total_amount DESC;


-- =====================================================
-- 5. FUNDS WITH EXPENSE RATIO < 1%
-- =====================================================

SELECT
    scheme_name,
    expense_ratio_pct
FROM dim_fund
WHERE expense_ratio_pct < 1
ORDER BY expense_ratio_pct;


-- =====================================================
-- 6. TOP 10 FUNDS BY SHARPE RATIO
-- =====================================================

SELECT
    scheme_name,
    sharpe_ratio
FROM fact_performance
ORDER BY sharpe_ratio DESC
LIMIT 10;


-- =====================================================
-- 7. TOP FUNDS BY 3 YEAR RETURN
-- =====================================================

SELECT
    scheme_name,
    return_3yr_pct
FROM fact_performance
ORDER BY return_3yr_pct DESC
LIMIT 10;


-- =====================================================
-- 8. AVERAGE INVESTMENT BY AGE GROUP
-- =====================================================

SELECT
    age_group,
    ROUND(AVG(amount_inr),2) AS avg_investment
FROM fact_transactions
GROUP BY age_group
ORDER BY avg_investment DESC;


-- =====================================================
-- 9. KYC STATUS DISTRIBUTION
-- =====================================================

SELECT
    kyc_status,
    COUNT(*) AS investor_count
FROM fact_transactions
GROUP BY kyc_status;


-- =====================================================
-- 10. TRANSACTION TYPE DISTRIBUTION
-- =====================================================

SELECT
    transaction_type,
    COUNT(*) AS transaction_count,
    SUM(amount_inr) AS total_amount
FROM fact_transactions
GROUP BY transaction_type
ORDER BY total_amount DESC;