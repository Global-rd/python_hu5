import sqlite3

class SqliteDb:

    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = None

    def __enter__(self):
        try:
            self.conn = sqlite3.connect(self.db_name)
            self.conn.execute("""CREATE TABLE IF NOT EXISTS log
                                    (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    city TEXT NOT NULL,
                                    temp REAL,
                                    humidity REAL,
                                    wind_speed REAL,
                                    datetime TEXT
                                )
            """)   
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
    def write_single_record(self, table, record): # {"department_name": "TEST", "is_active": 0}
        #INSERT INTO department (department_name, is_active) VALUES (?, ?)

        columns = ", ".join(record.keys())
        placeholders = ", ".join(['?' for _ in record])
        query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
        with self.conn:
            self.conn.execute(query, tuple(record.values()))
            