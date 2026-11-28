import sqlite3
import pandas as pd


class SqliteDB:

    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = None

    def __enter__(self):
        try:
            self.conn = sqlite3.connect(self.db_name)
            return self
        except Exception as e:
            raise RuntimeError(
                f"Failed to open database {self.db_name}"
            ) from e

    def __exit__(self, *args):
        if self.conn:
            try:
                self.conn.close()
            except Exception as close_err:
                print(
                    f"Error: failed to close database connection: {close_err}"
                )

    def create_log_table(self):
       query = """
        CREATE TABLE IF NOT EXISTS search_log (
            city TEXT,
            temperature REAL,
            humidity REAL,
            wind_speed REAL,
            search_time TEXT
        )
        """  

       with self.conn:
                self.conn.execute(query)
     

    def write_single_record(self, table, record):
        columns = ", ".join(record.keys())
        placeholders = ", ".join(['?' for _ in record])
        query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
        with self.conn:
            self.conn.execute(query, tuple(record.values()))

    def write_multiple_records(self, table, df):
        if df.empty:
            return
        df.to_sql(table, self.conn, if_exists="append", index=False)

    def select_records(self, query):
        df = pd.read_sql(query, self.conn)
        return df
