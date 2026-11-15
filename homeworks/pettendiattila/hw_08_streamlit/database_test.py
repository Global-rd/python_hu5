import sqlite3

conn = sqlite3.connect("weather.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM weather_logs")
rows = cursor.fetchall()

print("Saved weather records:")
for row in rows:
    print(row)

conn.close()