# Weather dashboard (homework 8)

This Streamlit app looks up a city with Open-Meteo's geocoding API, then uses its
coordinates to fetch current conditions and five days of hourly temperatures.
It shows three metrics, a map, and a temperature chart. Successful searches are
also logged to a local SQLite database.

## Run locally

From the `python_hu5` repository root:

```powershell
python -m pip install -r homeworks/bakacsygabor/hw_08_streamlit/requirements.txt
python -m streamlit run homeworks/bakacsygabor/hw_08_streamlit/weather_app.py
```

Open the local URL shown by Streamlit, enter a city, and select **Show weather**.
For ambiguous names, add the country, for example `Paris, France`.

## Deployment note

Streamlit Community Cloud can use `weather_app.py` as the entrypoint and the
`requirements.txt` beside it. The SQLite database is created at runtime and is
not committed. Community Cloud's local storage is temporary, so the search log
may be lost after a restart or redeployment.
