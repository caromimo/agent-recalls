import duckdb
import os

# Initialize DuckDB
connection = duckdb.connect()

# Define tool to count recalls from April 2026
def count_April_2026_recalls() -> int:
    """
    Filter and count all recalls from April 2026
    """
    # The data file is one directory up from the tools directory
    base_dir = os.path.dirname(os.path.dirname(__file__))
    data_path = os.path.join(base_dir, 'data', 'HCRSAMOpenData.csv')
    return connection.execute(
        f"""
        SELECT COUNT(*) as "Total Recalls in April 2026" FROM '{data_path}'
        WHERE "Last updated" >= '2026-04-01'
        AND "Last updated" < '2026-05-01'
        """).fetchone()[0]
