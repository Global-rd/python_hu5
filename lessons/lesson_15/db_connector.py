import sqlite3
import pandas as pd

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

    def write_single_record(self, table, record): # {"department_name": "TEST", "is_active": 0}
        #INSERT INTO department (department_name, is_active) VALUES (?, ?)

        columns = ", ".join(record.keys())
        placeholders = ", ".join(['?' for _ in record])
        query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
        with self.conn:
            self.conn.execute(query, tuple(record.values()))

    def write_multiple_records(self, table, df):
        if df.empty:
            return
        df.to_sql(table, self.conn, if_exists="append", index=False)

    def select_records(self, query): # fetch(), fetchall()
        df = pd.read_sql(query, self.conn)
        return df

    def delete_records(self, table, where_clause):
        query = f"DELETE from {table} WHERE {where_clause}"
        with self.conn:
            cursor = self.conn.execute(query)
            return cursor.rowcount

    def update_records(self, table, updates, where_clause):
        # {"department_name": "Research_2", "is_active": 1}

        update_clause = ", ".join(f"{k} = ?" for k in updates.keys())
        query = f"UPDATE {table} SET {update_clause} WHERE {where_clause}"
        values = tuple(updates.values())

        with self.conn:
            cursor = self.conn.execute(query, values)
            return cursor.rowcount



with SqliteDb("lessons/lesson_15/department-db") as db:
    #db.write_single_record("department", {"department_name": "TEST", "is_active": 0})

    df = pd.DataFrame([{"department_name": "TEST1", "is_active": 0},
                       {"department_name": "TEST2", "is_active": 1}])
    print(df)
    db.write_multiple_records("department", df)

    df = db.select_records("SELECT * FROM department")
    print(df)

    db.delete_records("department", "department_id > 6")

    print(db.update_records("department", {"department_name": "Updated_record"}, "department_id=6"))
