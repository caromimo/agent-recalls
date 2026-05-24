import duckdb
import os
import datetime

# Initialize DuckDB
connection = duckdb.connect()

# Create a class of tools that accepts the data path as an argument to use in unit tests
class Tool():
    def __init__(self, data_path="recall_agent/data/HCRSAMOpenData.csv"):
        self.data_path = data_path
        
    def count_recalls_by_month_and_year(self, year: int, month_name: str) -> int:
        """
        Filter and count all recalls for a specific month and year.
        
        Args:
            year: The year to query (e.g., 2026)
            month_name: The name of the month to query (e.g., "May", "January")
        """
        month_map = {
            "january": 1, "february": 2, "march": 3, "april": 4,
            "may": 5, "june": 6, "july": 7, "august": 8,
            "september": 9, "october": 10, "november": 11, "december": 12
        }
        
        month_num = month_map.get(month_name.lower().strip())
        if not month_num:
            raise ValueError("Invalid month name provided.")

        return connection.execute(
            f"""
            SELECT COUNT(*) as "Total Recalls in Period" FROM '{self.data_path}'
            WHERE EXTRACT(year FROM CAST("Last updated" AS DATE)) = $year
            AND EXTRACT(month FROM CAST("Last updated" AS DATE)) = $month
            """,
            {"year": year, "month": month_num}
        ).fetchone()[0]
        
    def search_recalls_by_keyword(self, keyword: str) -> list[dict]:
        """
        Search for recalls containing a specific keyword.
        
        Args:
            keyword: The keyword to search for (e.g., "peptides")
        """
        # Drop a trailing 's' if it exists (but not 'ss' like "glass")
        # This allows a search for 'peptides' to become '%peptide%', which matches both.
        base_keyword = keyword.strip()
        if base_keyword.lower().endswith('s') and not base_keyword.lower().endswith('ss'):
            base_keyword = base_keyword[:-1]
            
        result = connection.execute(
            f"""
            SELECT * FROM read_csv_auto('{self.data_path}')
            WHERE Title ILIKE $keyword 
            OR Product ILIKE $keyword 
            OR Issue ILIKE $keyword
            """,
            {
            "keyword": f"%{base_keyword}%"
            }
        )
        
        columns = [col[0] for col in result.description]
        rows = []
        for row in result.fetchall():
            row_dict = {}
            for i, val in enumerate(row):
                if isinstance(val, (datetime.date, datetime.datetime)):
                    row_dict[columns[i]] = val.isoformat()
                else:
                    row_dict[columns[i]] = val
            rows.append(row_dict)
        return rows