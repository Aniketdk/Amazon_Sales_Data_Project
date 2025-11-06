"""amazon_sales_etl.py
Performs local cleaning with pandas and uploads cleaned data to Snowflake RAW table.
Requires: pandas, snowflake-connector-python
"""
import pandas as pd
import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas
from pathlib import Path

CSV_PATH = Path(__file__).parent.parent / 'data' / 'amazon_sales_data.csv'
SNOWFLAKE_CONFIG = {
    "user": "YOUR_USER",
    "password": "YOUR_PASSWORD",
    "account": "YOUR_ACCOUNT",
    "warehouse": "SALES_WH",
    "database": "AMAZON_SALES_DB",
    "schema": "SALES_SCHEMA"
}

def main():
    df = pd.read_csv(CSV_PATH)
    # drop exact duplicate rows
    df = df.drop_duplicates()
    # handle missing columns gracefully
    for col in ['product','category','sub_category','region','country']:
        if col in df.columns:
            df[col] = df[col].fillna('Unknown')
    for col in ['quantity','unit_price','discount','profit']:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)
    df['total_sales'] = df.get('quantity',0) * df.get('unit_price',0)
    df['net_sales'] = df['total_sales'] - df.get('discount',0)
    conn = snowflake.connector.connect(
        user=SNOWFLAKE_CONFIG['user'],
        password=SNOWFLAKE_CONFIG['password'],
        account=SNOWFLAKE_CONFIG['account'],
        warehouse=SNOWFLAKE_CONFIG['warehouse'],
        database=SNOWFLAKE_CONFIG['database'],
        schema=SNOWFLAKE_CONFIG['schema']
    )
    try:
        success, nchunks, nrows, _ = write_pandas(conn, df, 'RAW_AMAZON_SALES')
        print(f'Uploaded {nrows} rows to RAW_AMAZON_SALES (success={success})')
    finally:
        conn.close()

if __name__ == '__main__':
    main()
