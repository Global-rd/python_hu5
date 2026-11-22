import sqlite3
from pathlib import Path

db_path = Path(__file__).with_name("inventory.db")

connection = sqlite3.connect(db_path)
connection.execute("""
    CREATE TABLE IF NOT EXISTS items (
        id TEXT NOT NULL PRIMARY KEY,
        item_name TEXT NOT NULL,
        quantity INTEGER NOT NULL,
        price INTEGER NOT NULL,
        category TEXT
    )
""")
connection.commit()
connection.close()