import streamlit as st
import plotly.express as px
import pandas as pd
import requests
from db_connector import SqliteDb
from datetime import datetime
from pathlib import Path

#--------------------------------------------------------------------------

BASE_DIR = Path(__file__).parent.resolve()

# -----------------get_data_from_openmeteo -------------------

@st.cache_data(ttl=3600, show_spinner="Weather data downloading...")
def get_data_from_openmeteo(lat, lon):

    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "hourly": "temperature_2m,relative_humidity_2m,wind_speed_10m",
        "current": "temperature_2m,relative_humidity_2m,wind_speed_10m",
        "timezone": "auto"
    }
    try:
        response = requests.get(url, params = params, timeout = 10)
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        st.warning(f"Error when try to get the weather {e}")
        return None
    except requests.exceptions.RequestException as e:
        st.warning(f"Network error {e}")
        return None
    return response.json()

#---------------- get_location_by_city_name --------------------------------------------

def get_location_by_city_name(city_name):
    url = "https://geocoding-api.open-meteo.com/v1/search"
    params = {
          "name": city_name,
          "count": 1
    }
    
    try:
        response = requests.get(url, params=params, timeout = 10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        st.warning(f"Error when searching for a city {e}")
        return None

    result = response.json()
    if result.get("error"):
        st.warning(f"Problem with the geolocation module: {result.get('reason')}")
        return None

    weather_result = result.get("results")
    if not weather_result:
        st.warning(f"City not found: {city_name}")
        return None

    return weather_result[0]

#------------ show map --------------------------

def show_map(location):
    lat = location["latitude"]
    lon = location["longitude"]
    city = location["name"]
    
    map_df = pd.DataFrame({
        "lat": [lat],
        "lon": [lon],
        "city": [city],
    })

    fig_map = px.scatter_map(
        map_df,
        lat="lat",
        lon="lon",
        hover_name="city",
        center={"lat": lat, "lon": lon},
        zoom=11,
        height=350,
    )
    fig_map.update_traces(marker=dict(size=14))
    fig_map.update_layout(
        map_style="open-street-map",
        margin=dict(l=0, r=0, t=0, b=0),
    )

    st.plotly_chart(fig_map,
                    config = {
                        "editable": False,
                        "displayModeBar": False,
                        "staticPlot": True
                    },
                    use_container_width=True
                    )

#---------- draw chart ----------------------------

def draw_chart(location, weather_data):
        
        variables = {
            "temperature_2m": "Temp",
            "relative_humidity_2m": "Humidity",
            "wind_speed_10m": "Wind"
            }

        # KPI
        kpi_cols = st.columns(len(variables))

        for col, (key, name) in zip(kpi_cols, variables.items()):
            current_unit = weather_data["current_units"][key]
            with col:
                st.metric(name, f'{weather_data["current"][key]} {current_unit}')

        # chart
        df = pd.DataFrame(weather_data["hourly"])

        for column, name in variables.items():
            hourly_unit = weather_data["hourly_units"][column]

            fig = px.line(
                        df,
                        x="time",
                        y=column,
                        title=f"{location['name']}, {location['country']} - {name }",
                        labels={column: f"{name} ({hourly_unit})", "time":"Time"},
                        height=150
                        )
            fig.update_layout(hovermode="x unified", dragmode=False, margin=dict(b=1, t=50))
            st.plotly_chart(
                fig, 
                config = {
                    "scrollZoom": False,
                    "displayModeBar": False,
                    "doubleClick": False
                },
                use_container_width=True)

# ------------------- main -----------------------
def main():
    st.set_page_config(initial_sidebar_state="expanded")

        #--- cut the space after, before
    st.markdown(
        """
        <style>
            [data-testid="stMainBlockContainer"] {
            padding-top: 1rem;
            }
            h1 {
                padding-top: 0;
            }
            [data-testid="stSidebarHeader"] {
                height: 2rem;
                padding: 0;
                display: none;
            }
            [data-testid="stSidebarUserContent"] {
                padding-top: 0rem;
            }   
        </style>
        """,
        unsafe_allow_html=True,
    )

    # sidebar (header, edit field, button)
    st.sidebar.header("Weather forecast configuration")
    with st.sidebar.form("city_form"):
            city = st.text_input("City", "Budapest")
            submitted = st.form_submit_button("Submit")

    if submitted: # ha megnyomták a gombot

        # lekeri a lat, lon adatokat a varosnev alapjan
        location = get_location_by_city_name(city)
        if location is None:
            st.stop()

        # lekeri az idojarasi adatokat a lat, lon alapjan
        weather_data = get_data_from_openmeteo(location["latitude"], location["longitude"])
        if weather_data is None:
            st.stop()

        # session eltarolas
        st.session_state.city = city
        st.session_state.location = location
        st.session_state.weather_data = weather_data

        # SQLite naplozas
        with SqliteDb(BASE_DIR/"log.sqlite") as db:
            db.write_single_record("log", {
                                            "city": location["name"],
                                            "temp": weather_data["current"]["temperature_2m"],
                                            "humidity": weather_data["current"]["relative_humidity_2m"],
                                            "wind_speed": weather_data["current"]["wind_speed_10m"],
                                            "datetime": datetime.now()
                                            })
    elif "weather_data" not in st.session_state:
        # Automatikus induló lekérdezés
        location = get_location_by_city_name("Budapest")

        if location is not None:
            weather_data = get_data_from_openmeteo(
                location["latitude"],
                location["longitude"]
            )

            if weather_data is not None:
                st.session_state.city = "Budapest"
                st.session_state.location = location
                st.session_state.weather_data = weather_data
    
    # session visszatoltes
    if "weather_data" in st.session_state:
        city = st.session_state.city
        location = st.session_state.location
        weather_data = st.session_state.weather_data

        # stat drawing
        title=f"{location['name']}, {location['country']} weather"
        st.title(title)
        show_map(location)
        draw_chart(location, weather_data)

        # sidebar City reszletek kiirasa (a markdown-ban kevesebb a terkoz a szoveket alatt/felett)
        st.sidebar.subheader("City details:")
        skip = {"id", "feature_code", "country_id", "admin1_id", "admin2_id", "admin3_id", "admin4_id"}
        city_details = [f"**{key}:** {values}" for key, values in location.items() if key not in skip]
        st.sidebar.markdown("  \n".join(city_details))

#------------------------------------------------------------------

if __name__ == "__main__":
    main()
