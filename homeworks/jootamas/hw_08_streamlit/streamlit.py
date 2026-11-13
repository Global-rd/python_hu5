"""
https://api.open-meteo.com/v1/forecast
https://geocoding-api.open-meteo.com/v1/search

A felhasználónak képesnek kell lennie megadni egy létező város nevét.
Az, hogy hol kéred be az inputot, rád van bízva (pl egy sidebaron, vagy ahogy a screenshoton látod).
Ha az API hívás hibát dob, tudasd egy warning használatával. Minden városnévvel kapcsolatos text az oldalon dinamikusan változzon (országot is beleértve).
A https://api.open-meteo.com/v1/forecast endpoint-ról húzd le a megadott település jelenlegi hőmérsékletét, páratartalmát és a szél sebességét.
Jelenítsd meg KPI-okként/key metric-enként ezeket az adatokat.
Ez az API lat és lon paraméterek alapján azonosítja be a várost, így először a geocoding api-ra lesz szükséged: https://geocoding-api.open-meteo.com/v1/search

Lépések:
1. Felhasználó megadja a városnevet
2. Geocoding api visszaadja az ehhez tartozó lat és lon értéket
3. Forecast endpoint visszaadja a lat/lon-hoz tartozó hőmérsékleti adatokat
4. Megjelenik az adat a streamlit dashboardon

Használd a dokumentációt a feladat további értelmezéséhez:
https://open-meteo.com/en/docs

Deployold az app-ot a Community Cloud–ra, és a PR-odnak legyen része a link.
A deployment-hez létre kell hoznod egy saját public repository-t, mivel csak admin joggal rendelkező felhasználó deployolhat.
Ettől függetlenül a robot_dreams repo-ba PR-ként be kell adni a házi kódját a megszokott módon.

Extra:
1.Készíts egy előrejelzést a /forecast-ból szerzett adatokból a mintán látható módon.
2.Logolj minden keresést (városnév, temperature, humidity, wind speed, és a jelenlegi idő (datetime.now()) egy sqlite adatbázisba.
Ehhez hozd létre az adatbázist és egy táblát a fent említett 5 oszloppal (használd az órán tanult metódusokat a betöltéshez)
"""

import streamlit as st
import pandas as pd
import requests

st.title("Robot Dreams Python - Weather Map & Data Visualization App")

# varos bekerese es koordinatak lekerese

city = st.text_input(
  "Enter City name",
  "Szeged"
)

# IDE hisztizett a try utani ellenorzesnel, hogy coordinates can be undefined
coordinates = None

try:
  req = requests.get(
    "https://geocoding-api.open-meteo.com/v1/search",
    params={
      "name": city
    }
  )
  req.raise_for_status()
  coordinates = req.json()
except requests.exceptions.RequestException as e:
  st.warning(e)
  st.stop()

# legyen egy kis ellenorzes is

if not(isinstance(coordinates, dict)) or not(coordinates.get("results")) or len(coordinates["results"]) == 0:
  st.warning("City not found or it is not a Hungarian city")
  st.stop()

# szurunk egy kicsit, mert pl. Budapest-re keresve sorolja, hogy Ujbuda meg a keruleteket, meg USA New York Allamban is van egy Budapest
# talaltam count parametert az API-nal, de attol meg marad a szuro, az a biztos

coordinates = next((c for c in coordinates["results"] if c["country_code"] == "HU" and c["name"] == city), None)

if not(isinstance(coordinates, dict)):
  st.warning("City not found or it is not a Hungarian city")
  st.stop()

# szinten IDE warning miatt
weather = None

try:
  req = requests.get(
    "https://api.open-meteo.com/v1/forecast",
    params={
      "latitude": coordinates["latitude"],
      "longitude": coordinates["longitude"],
      "current": (
        "temperature_2m,",
        "relative_humidity_2m,",
        "wind_speed_10m"
      ),
      "temperature_unit": "celsius",
      "wind_speed_unit": "kmh",
      "timezone": "Europe/Budapest",
      "forecast_hours": 120,
      "hourly": "temperature_2m"
    }
  )
  req.raise_for_status()
  weather = req.json()
except requests.exceptions.RequestException as e:
  st.warning(e)
  st.stop()

kpi_temperature, kpi_humidity, kpi_wind_speed = st.columns(3)

with kpi_temperature:
  st.metric(
    label="Temperature (°C)",
    value=weather["current"]["temperature_2m"]
  )
with kpi_humidity:
  st.metric(
    label="Humidity (%)",
    value=weather["current"]["relative_humidity_2m"]
  )
with kpi_wind_speed:
  st.metric(
    label="Wind Speed (km/h)",
    value=weather["current"]["wind_speed_10m"]
  )

st.header("Weather Map")

map_center = {
  "lat": [coordinates["latitude"]],
  "lon": [coordinates["longitude"]]
}

st.map(map_center, zoom=12)

st.header("Hourly Temperature Forecast (Next 5 Days)")

# extra 1

hourly = weather["hourly"]

df = pd.DataFrame({
    "Időpont": pd.to_datetime(hourly["time"][::4]),
    "Hőmérséklet (°C)": hourly["temperature_2m"][::4],
})

# enelkul az X-en csak a datumok jelennek meg, nem 4 orankent, mint a mintan
df["Időpont"] = df["Időpont"].dt.strftime("%m.%d. %H:%M")

st.line_chart(df, x="Időpont", y="Hőmérséklet (°C)")
