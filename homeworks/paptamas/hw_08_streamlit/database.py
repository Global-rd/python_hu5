import sqlite3

DB_NAME = "weather_history.db"


def init_db():

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS weather_searches (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            city TEXT,
            temperature REAL,
            humidity REAL,
            wind_speed REAL,
            search_time TEXT
        )
    """)

    conn.commit()
    conn.close()


def save_search(
    city,
    temperature,
    humidity,
    wind_speed,
    search_time
):

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO weather_searches
        (
            city,
            temperature,
            humidity,
            wind_speed,
            search_time
        )
        VALUES (?, ?, ?, ?, ?)
    """, (
        city,
        temperature,
        humidity,
        wind_speed,
        search_time
    ))

    conn.commit()
    conn.close()