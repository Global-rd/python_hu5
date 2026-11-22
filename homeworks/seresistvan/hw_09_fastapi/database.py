import sqlite3
from pathlib import Path

db_path = Path(__file__).with_name("inventory.db")  # A ddatabase file helye

# Kapcsolódás a DB-hez
# Létrehozzuk az items táblát, ha még nincs
connection = sqlite3.connect(db_path)
connection.execute("""
    CREATE TABLE IF NOT EXISTS items (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        item_name TEXT NOT NULL,
        quantity INTEGER NOT NULL,
        price INTEGER NOT NULL,
        category TEXT
    )
""")




connection.commit()
connection.close()