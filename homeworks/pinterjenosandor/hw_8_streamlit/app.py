import pandas as pd
#import plotly.express as px
import plotly.graph_objects as go
import requests
import streamlit as st

#Use URL's
URL = "https://geocoding-api.open-meteo.com/v1/search?"
OPEN_WEATHER_FORECAST_URL = "https://api.open-meteo.com/v1/forecast"

# Page config
st.set_page_config(page_title="Meteo Dash", layout="wide")
st.title("Meteo Dashboard 🌤")


# Cache setting and location data
@st.cache_data(ttl=1800)
def get_coordinates(city_name: str):
  url = f"{URL}name={city_name}&count=1&language=hu&format=json"
  try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    data = response.json()

    if "results" in data and len(data["results"]) > 0:
      result = data["results"][0]
      return {
          "name": result.get("name", city_name),
          "country": result.get("country", ""),
          "latitude": result.get("latitude"),
          "longitude": result.get("longitude"),
      }
    else:
      return None
  except Exception as e:
    return None


# Cache setting and get weather date
@st.cache_data(ttl=600)
def get_weather_data(lat: float, lon: float):
  url = (
      f"{OPEN_WEATHER_FORECAST_URL}?"
      f"latitude={lat}&longitude={lon}"
      f"&current=temperature_2m,relative_humidity_2m,wind_speed_10m"
      f"&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
      f"&daily=temperature_2m_max,temperature_2m_min"
      f"&timezone=auto"
  )
  try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()
  except Exception as e:
    return None


#Sidebar
st.sidebar.header("Search") # search text
city_input = st.sidebar.text_input("City:", value="Budapest") #search box

if not city_input.strip():
  st.warning("Please add a city name on the sidebar.") # if has
else:
  location = get_coordinates(city_input.strip())

  if not location:
    st.warning(f"Not found that city: '{city_input}'. Please check it!")
  else:
    city_name = location["name"]
    country = location["country"]
    full_location = f"{city_name}, {country}" if country else city_name

    weather_data = get_weather_data(location["latitude"], location["longitude"])

    if not weather_data or "current" not in weather_data:
      st.warning("Error occured when loading data")
    else:
      current = weather_data["current"]
      temp = current.get("temperature_2m")
      humidity = current.get("relative_humidity_2m")
      wind = current.get("wind_speed_10m")

      units = weather_data.get("current_units", {})
      t_unit = units.get("temperature_2m", "°C")
      h_unit = units.get("relative_humidity_2m", "%")
      w_unit = units.get("wind_speed_10m", "km/h")

      # Header
      st.subheader(f"Actual weather in {full_location}")

      #Actual weather info
      col1, col2, col3 = st.columns(3)
      col1.metric("Temperature", f"🌡 {temp} {t_unit}") #show temp
      col2.metric("Humidity", f"💧 {humidity} {h_unit}") #show hum
      col3.metric("Wind speed", f"💨 {wind} {w_unit}") #show wind

      #Combinated forecast trend and diagram for daily min max and hourly
      if "hourly" in weather_data and "daily" in weather_data:
        st.markdown("---")
        st.subheader(f"Weather forecast of {full_location}")

        hourly_data = weather_data["hourly"]
        daily_data = weather_data["daily"]

        df_hourly = pd.DataFrame({
            "Time": pd.to_datetime(hourly_data["time"]),
            "Temperature (Hourly)": hourly_data["temperature_2m"],
        })

        df_daily = pd.DataFrame({
            "Date": pd.to_datetime(daily_data["time"]).strftime("%Y-%m-%d"),
            "Minimum Temperature": daily_data["temperature_2m_min"],
            "Maximum Temperature": daily_data["temperature_2m_max"],
        })

        fig = go.Figure()

        fig.add_trace(
            go.Bar(
                x=df_daily["Date"],
                y=df_daily["Maximum Temperature"],
                name="Daily Maximum (°C)",
                marker_color="#B69B96",
            )
        )

        fig.add_trace(
            go.Bar(
                x=df_daily["Date"],
                y=df_daily["Minimum Temperature"],
                name="Daily Minimum (°C)",
                marker_color="#90B2C8",
            )
        )

        fig.add_trace(
            go.Scatter(
                x=df_hourly["Time"],
                y=df_hourly["Temperature (Hourly)"],
                mode="lines+markers",
                name="HourlyTemp (°C)",
                line=dict(color="#7B8B87", width=1.5),
            )
        )

        fig.update_layout(
            barmode="group",
            title="Daily (Min/Max) - Horly temp",
            xaxis_title="Date/Time",
            yaxis_title=f"Temperature ({t_unit})",
            template="plotly_white",
            legend=dict(
                orientation="h", yanchor="bottom", y=1.00, xanchor="right", x=1
            ),
        )

        st.plotly_chart(fig, use_container_width=True)

      #map
      st.subheader(f"Location of {full_location}")

      lat = location.get("latitude")
      lon = location.get("longitude")

      if lat is not None and lon is not None:
        df_map = pd.DataFrame({"lat": [lat], "lon": [lon]})
        st.map(df_map, zoom=10, use_container_width=True)
      else:
        st.warning("Not find coordinates to this city for map")