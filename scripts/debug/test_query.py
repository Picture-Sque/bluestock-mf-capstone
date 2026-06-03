import sqlite3
import pandas as pd

conn = sqlite3.connect("bluestock_mf.db")

query = """
SELECT
    scheme_name,
    aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;
"""

result = pd.read_sql(query, conn)

print(result)

conn.close()