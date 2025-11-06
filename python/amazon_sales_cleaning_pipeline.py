"""amazon_sales_cleaning_pipeline.py
Runner to:
 - upload local CSV to Snowflake RAW table using write_pandas
 - execute SQL pipeline (reads sql file and runs statements)
Requires: snowflake-connector-python, pandas
Fill in SNOWFLAKE_CONFIG before running.
"""
import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas
import pandas as pd
from pathlib import Path

SNOWFLAKE_CONFIG = {
    "user": "YOUR_USER",
    "password": "YOUR_PASSWORD",
    "account": "YOUR_ACCOUNT",
    "warehouse": "SALES_WH",
    "database": "AMAZON_SALES_DB",
    "schema": "SALES_SCHEMA"
}

BASE = Path(__file__).parent.parent
CSV_PATH = BASE / "data" / "amazon_sales_data.csv"
SQL_PATH = BASE / "sql" / "amazon_sales_cleaning_pipeline.sql"

def upload_csv(conn):
    df = pd.read_csv(CSV_PATH)
    # basic cleaning before upload
    df = df.drop_duplicates()
    # ensure numeric columns
    for col in ['quantity','unit_price','discount','profit']:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)
    success, nchunks, nrows, _ = write_pandas(conn, df, 'RAW_AMAZON_SALES')
    print(f'Uploaded {nrows} rows to RAW_AMAZON_SALES (success={success})')

def run_sql_file(conn):
    sql = SQL_PATH.read_text()
    # naive split by ';' — works for this pipeline
    stmts = [s.strip() for s in sql.split(';') if s.strip()]
    cur = conn.cursor()
    try:
        for stmt in stmts:
            cur.execute(stmt)
        print('Executed pipeline SQL successfully.')
    finally:
        cur.close()

def main():
    conn = snowflake.connector.connect(
        user=SNOWFLAKE_CONFIG['user'],
        password=SNOWFLAKE_CONFIG['password'],
        account=SNOWFLAKE_CONFIG['account'],
        warehouse=SNOWFLAKE_CONFIG['warehouse'],
        database=SNOWFLAKE_CONFIG['database'],
        schema=SNOWFLAKE_CONFIG['schema']
    )
    try:
        upload_csv(conn)
        run_sql_file(conn)
    finally:
        conn.close()

if __name__ == '__main__':
    main()
