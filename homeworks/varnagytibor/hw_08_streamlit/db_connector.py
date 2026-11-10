import sqlite3
import pandas as pd

#az órai (lesson_15/db_connector.py) SqliteDb osztály, a házihoz szükséges részekkel:
#context manager (with), tábla létrehozása, egy rekord beszúrása, lekérdezés DataFrame-be


class SqliteDb:

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

    def create_table(self, query):
        with self.conn:
            self.conn.execute(query)

    def write_single_record(self, table, record):
        #pl. INSERT INTO searches (city, temperature, ...) VALUES (?, ?, ...)
        columns = ", ".join(record.keys())
        placeholders = ", ".join(['?' for _ in record])
        query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
        with self.conn:
            self.conn.execute(query, tuple(record.values()))

    def select_records(self, query):
        df = pd.read_sql(query, self.conn)
        return df
