import streamlit as st
import plotly.express as px
import pandas as pd
import requests
import numpy as np
import sqlite3
import datetime


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

    def write_single_record(self, table, record): 
        columns = ", ".join(record.keys())
        placeholders = ", ".join(['?' for _ in record])
        query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
        with self.conn:
            self.conn.execute(query, tuple(record.values()))


def get_location_coordinates(city):
    
    url=f"https://geocoding-api.open-meteo.com/v1/search?name={city}"
    
    coordinate_response = requests.get(url)

    if coordinate_response.status_code == 200:
        coordinate_response = coordinate_response.json()

        coordinate_df = pd.DataFrame(coordinate_response["results"])

        if len(coordinate_df) == 1:
            coordinates = []
            coordinates.extend([coordinate_df["latitude"].loc[0], 
                                coordinate_df["longitude"].loc[0], 
                                coordinate_df["name"].loc[0],
                                coordinate_df["admin1"].loc[0], 
                                coordinate_df["country"].loc[0]])                        
        else:
            cities = [
            f"{name} ({admin1}), {country}" for name, admin1, country in coordinate_df[["name", "admin1", "country"]].values]
            selection = st.selectbox(f"There are more than one locations available for {city}, select the proper one:", cities, index=0)
            selected_index = cities.index(selection)
            coordinates = []
            coordinates.extend([coordinate_df["latitude"].loc[selected_index], 
                                coordinate_df["longitude"].loc[selected_index], 
                                coordinate_df["name"].loc[selected_index],
                                coordinate_df["admin1"].loc[selected_index], 
                                coordinate_df["country"].loc[selected_index]])
        
        return coordinates
    else:
        st.warning(f"Failed to fetch data for {city}: {coordinate_response.status_code} - {coordinate_response.text}")


def fetch_location_data(latitude, longitude, city):
    print(f"Fetch data for {city}")

    url="https://api.open-meteo.com/v1/forecast"

    parameters = {"latitude": {latitude},
                    "longitude": {longitude},
                    "current": "temperature_2m,relative_humidity_2m,wind_speed_10m,precipitation",
                    "hourly": "temperature_2m,relative_humidity_2m,wind_speed_10m,precipitation",
                    "forecast_days": 7}
    
    meteo_response = requests.get(url=url, params=parameters)

    if meteo_response.status_code == 200:
        return meteo_response.json()
    else:
        st.error(f"Failed to fetch data: {meteo_response.status_code} - {meteo_response.text}")



def process_data(data):
    current_df = pd.DataFrame([data["current"]])
    current_df.rename(columns={"temperature_2m" : "Temperature (°C)",
                                "wind_speed_10m" : "Wind speed (km/h)", 
                                "relative_humidity_2m" : "Humidity (%)", 
                                "precipitation" : "Precipitation (mm)"}, inplace=True)

    forecast_df = pd.DataFrame(data["hourly"])
    forecast_df.rename(columns={"temperature_2m" : "Temperature (°C)", 
                                "wind_speed_10m" : "Wind speed (km/h)", 
                                "relative_humidity_2m" : "Humidity (%)", 
                                "precipitation" : "Precipitation (mm)", 
                                "time" : "days"}, inplace=True)
    forecast_df["days"] = pd.to_datetime(forecast_df["days"], format="%Y-%m-%dT%H:%M")
    forecast_df.set_index("days", inplace=True)

    weather_metrics = [
    "Temperature (°C)",
    "Humidity (%)",
    "Wind speed (km/h)",
    "Precipitation (mm)"]

    for col in weather_metrics:
        forecast_df[f"bar_color_{col}"] = np.where(forecast_df[col] == forecast_df[col].max(), "Maximum", "")
    
    return current_df, forecast_df


def main():

    st.title("Weather Forecast Dashboard")

    city = st.text_input("Enter a city: (e.g.: Budapest, Casablanca, Tijuana)")

    if city:
        coordinate_data = get_location_coordinates(city)

        meteo_data = fetch_location_data(coordinate_data[0], coordinate_data[1], coordinate_data[2])

        if meteo_data:
            current_df, forecast_df = process_data(meteo_data)

            st.header(f"Current weather metrics for {coordinate_data[2]} ({coordinate_data[3]}), {coordinate_data[4]}")

            if current_df is not None:
                with SqliteDb("homeworks/krimerdaniel/hw_08_streamlit/weather_db") as db:
                    db.write_single_record("weather", {"location": f"{coordinate_data[2]}-{coordinate_data[3]}-{coordinate_data[4]}",
                                                        "temperature": current_df["Temperature (°C)"].loc[0],
                                                        "wind_speed": current_df["Wind speed (km/h)"].loc[0],
                                                        "humidity": int(current_df["Humidity (%)"].loc[0]),
                                                        "precipitation": current_df["Precipitation (mm)"].loc[0],
                                                        "time" : datetime.datetime.now()
                                                        })


                kpi_temp, kpi_wind, kpi_humidity, kpi_precipitation = st.columns(4)

                with kpi_temp:
                    st.metric(label="Current temperature", 
                              value=f"{current_df['Temperature (°C)'].iloc[0]:.1f} °C", 
                              icon=":material/thermometer:")

                with kpi_wind:
                    st.metric(label="Current wind speed", 
                              value=f"{current_df['Wind speed (km/h)'].iloc[0]:.1f} km/h", 
                              icon=":material/air:")

                with kpi_humidity:
                    st.metric(label="Current humidity", 
                              value=f"{current_df['Humidity (%)'].iloc[0]} %", 
                              icon=":material/humidity_percentage:")

                with kpi_precipitation:
                    st.metric(label="Current precipitation", 
                              value=f"{current_df['Precipitation (mm)'].iloc[0]:.2f} mm", 
                              icon=":material/rainy:")


                map_df = pd.DataFrame({"latitude": [coordinate_data[0]],
                                        "longitude": [coordinate_data[1]]})

                st.map(map_df, zoom=11)

            if forecast_df is not None:

                st.header("Forecast for the next 7 days")
                
                options = ["Temperature (°C)", "Wind speed (km/h)", "Humidity (%)", "Precipitation (mm)"]
                to_forecast = st.multiselect("Select weather metrics to forecast:", options)
          
                if "Temperature (°C)" in to_forecast:                    
                    fig_fore_temp = px.bar(
                        forecast_df,
                        x=forecast_df.index,
                        y="Temperature (°C)",
                        title=f"Temperature (°C)",
                        color="bar_color_Temperature (°C)",
                        color_discrete_map={"Maximum": "#DD0F0F", "": "#9A9A9A"}
                    )
                    fig_fore_temp.update_layout(showlegend=False)
                    st.plotly_chart(fig_fore_temp)

                if "Wind speed (km/h)" in to_forecast:                   
                    fig_fore_wind = px.bar(
                        forecast_df,
                        x=forecast_df.index,
                        y="Wind speed (km/h)",
                        title=f"Wind speed (km/h)",
                        color="bar_color_Wind speed (km/h)",
                        color_discrete_map={"Maximum": "#DD0F0F", "": "#9A9A9A"}
                    )
                    fig_fore_wind.update_layout(showlegend=False)
                    st.plotly_chart(fig_fore_wind)

                if "Humidity (%)" in to_forecast:
                    fig_fore_humidity = px.bar(
                        forecast_df,
                        x=forecast_df.index,
                        y="Humidity (%)",
                        title=f"Humidity (%)",
                        color="bar_color_Humidity (%)",
                        color_discrete_map={"Maximum": "#DD0F0F", "": "#9A9A9A"}
                    )
                    fig_fore_humidity.update_layout(showlegend=False)
                    st.plotly_chart(fig_fore_humidity)

                if "Precipitation (mm)" in to_forecast:
                    fig_fore_rain = px.bar(
                        forecast_df,
                        x=forecast_df.index,
                        y="Precipitation (mm)",
                        title=f"Precipitation (mm)",
                        color="bar_color_Precipitation (mm)",
                        color_discrete_map={"Maximum": "#DD0F0F", "": "#9A9A9A"}
                    )
                    fig_fore_rain.update_layout(showlegend=False)
                    st.plotly_chart(fig_fore_rain)


if __name__ == "__main__":
    main()