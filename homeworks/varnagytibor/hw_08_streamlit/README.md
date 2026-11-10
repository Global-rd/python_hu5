# hw_08_streamlit — Weather Map & Data Visualization App

Streamlit app: városnév → Open-Meteo geocoding (lat/lon) → Open-Meteo forecast
→ KPI-ok (hőmérséklet, páratartalom, szélsebesség), térkép, 5 napos óránkénti
előrejelzés (extra 1), és minden keresés naplózása sqlite-ba (extra 2).

Deployed app: <IDE JÖN A COMMUNITY CLOUD LINK>

## Futtatás helyben

```bash
pip install -r requirements.txt
streamlit run weather_app.py
```

## Fájlok

- `weather_app.py` — maga az app
- `db_connector.py` — az órai SqliteDb osztály (tábla létrehozás, beszúrás, lekérdezés)
- `requirements.txt` — a Community Cloud ebből telepíti a csomagokat
