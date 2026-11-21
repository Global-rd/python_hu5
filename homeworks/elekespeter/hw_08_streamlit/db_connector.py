import sqlite3

import pandas as pd


class SqliteDb:
    """
    SQLite kapcsolatkezelő - a lesson_15/db_connector.py órai osztálya.
    Context managerként használjuk:  with SqliteDb("fajl.db") as db: ...

    Változások az órai verzióhoz képest:
      - új create_table() metódus a tábla létrehozásához
      - a fájl végéről kimaradt az órai kipróbáló kód, mert az importáláskor lefutna
      - a delete_records / update_records itt nem kell, ezért kimaradt
    """

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

    def create_table(self, create_query):
        """Lefuttat egy CREATE TABLE IF NOT EXISTS ... lekérdezést."""
        with self.conn:
            self.conn.execute(create_query)

    def write_single_record(self, table, record):
        # {"city": "Budapest, Hungary", "temperature": 9.8, ...}
        # -> INSERT INTO table (city, temperature, ...) VALUES (?, ?, ...)
        columns = ", ".join(record.keys())
        placeholders = ", ".join(['?' for _ in record])
        query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
        with self.conn:
            self.conn.execute(query, tuple(record.values()))

    def select_records(self, query):
        df = pd.read_sql(query, self.conn)
        return df
