"""Homework 8 – Weather Map & Data Visualization App (Streamlit).

Apple "Liquid Glass" inspired design: frosted glass cards over an animated sky gradient.

Run:
    streamlit run app.py
"""

import sqlite3
from datetime import datetime
from pathlib import Path

import pandas as pd
import plotly.graph_objects as go
import requests
import streamlit as st
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
FORECAST_URL = "https://api.open-meteo.com/v1/forecast"
DB_PATH = Path(__file__).parent / "weather_log.db"
TIMEOUT = (5, 30)  # (connect, read) timeout in seconds


@st.cache_resource
def get_http_session() -> requests.Session:
    """HTTP session that retries slow or failed API calls automatically."""
    retry = Retry(
        total=3,                                      # up to 3 retries
        backoff_factor=1,                             # wait 1s, 2s, 4s between tries
        status_forcelist=[429, 500, 502, 503, 504],   # retry on these HTTP errors
        allowed_methods=["GET"],
    )
    session = requests.Session()
    session.mount("https://", HTTPAdapter(max_retries=retry))
    return session

# WMO weather codes -> (description, emoji)
WEATHER_CODES = {
    0: ("Clear sky", "☀️"), 1: ("Mainly clear", "🌤️"), 2: ("Partly cloudy", "⛅"),
    3: ("Overcast", "☁️"), 45: ("Fog", "🌫️"), 48: ("Rime fog", "🌫️"),
    51: ("Light drizzle", "🌦️"), 53: ("Drizzle", "🌦️"), 55: ("Dense drizzle", "🌧️"),
    56: ("Freezing drizzle", "🌧️"), 57: ("Freezing drizzle", "🌧️"),
    61: ("Light rain", "🌦️"), 63: ("Rain", "🌧️"), 65: ("Heavy rain", "🌧️"),
    66: ("Freezing rain", "🌧️"), 67: ("Freezing rain", "🌧️"),
    71: ("Light snow", "🌨️"), 73: ("Snow", "🌨️"), 75: ("Heavy snow", "❄️"),
    77: ("Snow grains", "🌨️"), 80: ("Rain showers", "🌦️"), 81: ("Rain showers", "🌧️"),
    82: ("Violent showers", "⛈️"), 85: ("Snow showers", "🌨️"), 86: ("Snow showers", "❄️"),
    95: ("Thunderstorm", "⛈️"), 96: ("Thunderstorm, hail", "⛈️"), 99: ("Thunderstorm, hail", "⛈️"),
}


def describe(code: int) -> tuple[str, str]:
    return WEATHER_CODES.get(code, ("Unknown", "🌡️"))


# ---------- API calls ----------

@st.cache_data(ttl=600)
def get_coordinates(city: str) -> dict | None:
    """Geocoding API: city name -> lat, lon, country."""
    params = {"name": city, "count": 1, "language": "en", "format": "json"}
    response = get_http_session().get(GEOCODING_URL, params=params, timeout=TIMEOUT)
    response.raise_for_status()
    results = response.json().get("results")
    if not results:
        return None
    r = results[0]
    return {
        "name": r["name"],
        "country": r.get("country", ""),
        "lat": r["latitude"],
        "lon": r["longitude"],
    }


@st.cache_data(ttl=600)
def get_weather(lat: float, lon: float) -> dict:
    """Forecast API: current weather + 5-day hourly and daily forecast."""
    params = {
        "latitude": lat,
        "longitude": lon,
        "current": "temperature_2m,relative_humidity_2m,wind_speed_10m,weather_code,is_day",
        "hourly": "temperature_2m",
        "daily": "weather_code,temperature_2m_max,temperature_2m_min",
        "forecast_days": 5,
        "timezone": "auto",
    }
    response = get_http_session().get(FORECAST_URL, params=params, timeout=TIMEOUT)
    response.raise_for_status()
    return response.json()


# ---------- SQLite logging (extra 2) ----------

def init_db() -> None:
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS searches (
                city TEXT,
                temperature REAL,
                humidity REAL,
                wind_speed REAL,
                searched_at TEXT
            )
            """
        )


def log_search(city: str, temperature: float, humidity: float, wind_speed: float) -> None:
    row = pd.DataFrame([{
        "city": city,
        "temperature": temperature,
        "humidity": humidity,
        "wind_speed": wind_speed,
        "searched_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }])
    with sqlite3.connect(DB_PATH) as conn:
        row.to_sql("searches", conn, if_exists="append", index=False)


def read_log() -> pd.DataFrame:
    with sqlite3.connect(DB_PATH) as conn:
        return pd.read_sql("SELECT * FROM searches ORDER BY searched_at DESC", conn)


# ---------- Styling ----------

# Sky gradients: (background gradient, blob color 1, blob color 2)
DAY_SKY = ("linear-gradient(160deg, #1d4e89 0%, #3a7bd5 45%, #6fb1fc 100%)", "#7f5af0", "#2cb1ff")
NIGHT_SKY = ("linear-gradient(160deg, #0b1026 0%, #1b1f4b 50%, #2b2d6e 100%)", "#6a3cff", "#ff4fa3")

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@200;300;400;500;600&display=swap');

html, body, [class*="st-"], .stApp {
    font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", "Inter", "Segoe UI", sans-serif;
}

/* Animated sky background with soft colour blobs */
.stApp { background: __BG__; background-attachment: fixed; }
.stApp::before, .stApp::after {
    content: ""; position: fixed; width: 520px; height: 520px; border-radius: 50%;
    filter: blur(110px); opacity: .55; z-index: 0; pointer-events: none;
    animation: float 18s ease-in-out infinite alternate;
}
.stApp::before { background: __BLOB1__; top: -120px; left: -80px; }
.stApp::after  { background: __BLOB2__; bottom: -160px; right: -100px; animation-delay: -9s; }
@keyframes float {
    0%   { transform: translate(0, 0) scale(1); }
    50%  { transform: translate(120px, 80px) scale(1.15); }
    100% { transform: translate(-60px, 140px) scale(.95); }
}
[data-testid="stAppViewContainer"], [data-testid="stMain"], [data-testid="stHeader"] {
    background: transparent !important; position: relative; z-index: 1;
}
[data-testid="stDecoration"], footer { display: none !important; }
.block-container { max-width: 1100px; padding-top: 2.5rem; }

/* Liquid glass surface, shared by all cards */
.glass, [data-testid="stMetric"], [data-testid="stPlotlyChart"], [data-testid="stDeckGlJsonChart"] {
    position: relative;
    background: linear-gradient(135deg, rgba(255,255,255,.20) 0%, rgba(255,255,255,.06) 100%);
    backdrop-filter: blur(28px) saturate(180%);
    -webkit-backdrop-filter: blur(28px) saturate(180%);
    border: 1px solid rgba(255,255,255,.28);
    border-radius: 28px;
    box-sizing: border-box;
    box-shadow: inset 0 1px 0 rgba(255,255,255,.45),
                inset 0 -1px 0 rgba(255,255,255,.08),
                0 10px 40px rgba(0,0,0,.25);
    overflow: hidden;
}
/* Specular highlight on top of the glass */
.glass::before, [data-testid="stMetric"]::before {
    content: ""; position: absolute; inset: 0; pointer-events: none;
    background: radial-gradient(120% 60% at 20% 0%, rgba(255,255,255,.28), transparent 60%);
}

/* Title */
.app-title { text-align: center; color: rgba(255,255,255,.75); font-size: .95rem;
    font-weight: 500; letter-spacing: .08em; text-transform: uppercase; margin-bottom: 1rem; }

/* Search field (selectors for both older and newer Streamlit versions) */
[data-testid="stTextInputRootElement"],
[data-testid="stTextInput"] div[data-baseweb="input"] {
    background: rgba(255,255,255,.14) !important;
    backdrop-filter: blur(24px) saturate(180%); -webkit-backdrop-filter: blur(24px) saturate(180%);
    border: 1px solid rgba(255,255,255,.3) !important; border-radius: 999px !important;
    box-shadow: inset 0 1px 0 rgba(255,255,255,.35), 0 6px 24px rgba(0,0,0,.18);
    height: auto !important;
}
[data-testid="stTextInput"] div[data-baseweb="base-input"] { background: transparent !important; }
[data-testid="stTextInput"] input {
    background: transparent !important; color: #fff !important; font-size: 1.05rem;
    padding: .8rem 1.3rem !important; text-align: center;
}
[data-testid="stTextInput"] input::placeholder { color: rgba(255,255,255,.6); }

/* Hero card (Apple Weather style) */
.hero { text-align: center; padding: 2.2rem 1rem 2rem; margin: 1.4rem 0 1.2rem; color: #fff; }
.hero .city { font-size: 2.1rem; font-weight: 500; letter-spacing: -.01em; }
.hero .country { font-size: .95rem; color: rgba(255,255,255,.7); margin-top: .1rem; }
.hero .temp { font-size: 6.5rem; font-weight: 200; line-height: 1; margin: .6rem 0 .3rem;
    letter-spacing: -.04em; text-shadow: 0 4px 30px rgba(0,0,0,.15); }
.hero .cond { font-size: 1.25rem; font-weight: 500; }
.hero .hilo { font-size: 1.05rem; color: rgba(255,255,255,.85); margin-top: .2rem; }

/* KPI metrics */
[data-testid="stMetric"] { padding: 1.1rem 1.4rem; }
[data-testid="stMetricLabel"] p { color: rgba(255,255,255,.7) !important; font-size: .78rem !important;
    font-weight: 600; text-transform: uppercase; letter-spacing: .06em; }
[data-testid="stMetricValue"] div { color: #fff; font-weight: 300; font-size: 2.3rem; }

/* Tabs as a glass segmented control (older and newer Streamlit versions) */
[data-testid="stTabs"] [role="tablist"] {
    display: flex; gap: 4px; padding: 5px; width: fit-content; margin: 1.6rem auto 1.2rem;
    background: rgba(255,255,255,.12); border: 1px solid rgba(255,255,255,.25) !important;
    border-radius: 999px; overflow: visible;
    backdrop-filter: blur(24px) saturate(180%); -webkit-backdrop-filter: blur(24px) saturate(180%);
    box-shadow: inset 0 1px 0 rgba(255,255,255,.35);
}
[data-testid="stTabs"] [role="tab"] {
    height: auto; padding: .5rem 1.4rem !important; margin: 0 !important; border-radius: 999px;
    background: transparent; border: none !important; color: rgba(255,255,255,.75);
    transition: all .25s ease;
}
[data-testid="stTabs"] [role="tab"] p { font-weight: 500; font-size: .92rem; }
[data-testid="stTabs"] [role="tab"][aria-selected="true"] {
    background: rgba(255,255,255,.28); color: #fff;
    box-shadow: inset 0 1px 0 rgba(255,255,255,.5), 0 4px 14px rgba(0,0,0,.15);
}
[data-testid="stTabs"] [data-baseweb="tab-highlight"],
[data-testid="stTabs"] [data-baseweb="tab-border"],
[data-testid="stTabs"] .react-aria-SelectionIndicator { display: none !important; }
[data-testid="stTabs"] [role="tablist"]::after,
[data-testid="stTabs"] [role="tablist"]::before { display: none !important; }

/* Section headings */
.section { color: rgba(255,255,255,.7); font-size: .78rem; font-weight: 600; letter-spacing: .06em;
    text-transform: uppercase; margin: 1.4rem 0 .6rem .4rem; }

/* Daily forecast list */
.daily { padding: .4rem 1.4rem; color: #fff; }
.day-row { display: grid; grid-template-columns: 90px 40px 50px 1fr 50px; align-items: center;
    gap: 12px; padding: .85rem 0; border-bottom: 1px solid rgba(255,255,255,.15); }
.day-row:last-child { border-bottom: none; }
.day-name { font-weight: 500; font-size: 1.05rem; }
.day-icon { font-size: 1.5rem; text-align: center; }
.day-min { color: rgba(255,255,255,.6); text-align: right; }
.day-max { text-align: left; font-weight: 500; }
.bar { position: relative; height: 6px; border-radius: 999px; background: rgba(255,255,255,.18); }
.bar span { position: absolute; top: 0; bottom: 0; border-radius: 999px;
    background: linear-gradient(90deg, #5ac8fa, #a3e635, #fcd34d, #fb923c); }

/* Search log table */
.log { padding: .6rem 1.2rem; overflow-x: auto; }
.log-table { width: 100%; border-collapse: collapse; color: #fff; font-size: .95rem; }
.log-table th { text-align: left; font-size: .75rem; font-weight: 600; letter-spacing: .06em;
    text-transform: uppercase; color: rgba(255,255,255,.65); padding: .8rem .6rem;
    border-bottom: 1px solid rgba(255,255,255,.2); }
.log-table td { padding: .75rem .6rem; border-bottom: 1px solid rgba(255,255,255,.1); }
.log-table tr:last-child td { border-bottom: none !important; }
.log-table, .log-table th, .log-table td {
    border-top: none !important; border-left: none !important; border-right: none !important; }
.log-table { border: none !important; }
.log-table tbody tr:hover { background: rgba(255,255,255,.08); }

/* Alerts as glass too */
[data-testid="stAlert"] { border-radius: 20px; backdrop-filter: blur(20px); }
</style>
"""


def inject_css(is_day: bool) -> None:
    bg, blob1, blob2 = DAY_SKY if is_day else NIGHT_SKY
    css = CSS.replace("__BG__", bg).replace("__BLOB1__", blob1).replace("__BLOB2__", blob2)
    st.markdown(css, unsafe_allow_html=True)


def hero_html(place_name: str, country: str, temp: float, unit: str,
              condition: str, emoji: str, t_max: float, t_min: float) -> str:
    # Kept on single lines: indented HTML would be rendered as a Markdown code block
    return (
        '<div class="glass hero">'
        f'<div class="city">{place_name}</div>'
        f'<div class="country">{country}</div>'
        f'<div class="temp">{round(temp)}°</div>'
        f'<div class="cond">{emoji} {condition}</div>'
        f'<div class="hilo">H: {round(t_max)}°&nbsp;&nbsp;L: {round(t_min)}°</div>'
        '</div>'
    )


def daily_html(daily: dict) -> str:
    lows, highs = daily["temperature_2m_min"], daily["temperature_2m_max"]
    week_min, week_max = min(lows), max(highs)
    span = (week_max - week_min) or 1
    rows = []
    for i, day in enumerate(daily["time"]):
        name = "Today" if i == 0 else datetime.fromisoformat(day).strftime("%a")
        _, emoji = describe(daily["weather_code"][i])
        left = (lows[i] - week_min) / span * 100
        width = (highs[i] - lows[i]) / span * 100
        rows.append(
            '<div class="day-row">'
            f'<div class="day-name">{name}</div>'
            f'<div class="day-icon">{emoji}</div>'
            f'<div class="day-min">{round(lows[i])}°</div>'
            f'<div class="bar"><span style="left:{left:.1f}%;width:{max(width, 4):.1f}%"></span></div>'
            f'<div class="day-max">{round(highs[i])}°</div>'
            '</div>'
        )
    return '<div class="glass daily">' + "".join(rows) + '</div>'


def forecast_chart(hourly: pd.DataFrame, unit: str) -> go.Figure:
    fig = go.Figure(go.Scatter(
        x=hourly["time"], y=hourly["temperature"], mode="lines",
        line=dict(color="#ffffff", width=3, shape="spline"),
        fill="tozeroy", fillcolor="rgba(255,255,255,0.12)",
        hovertemplate="%{x|%a %H:%M}<br><b>%{y:.1f} " + unit + "</b><extra></extra>",
    ))
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="rgba(255,255,255,0.8)", family="-apple-system, Inter, sans-serif"),
        margin=dict(l=24, r=24, t=24, b=40), height=380,
        hoverlabel=dict(bgcolor="rgba(30,40,70,0.85)", bordercolor="rgba(255,255,255,0.3)",
                        font=dict(color="#fff")),
    )
    fig.update_xaxes(showgrid=False, tickformat="%a %H:%M", dtick=12 * 3600 * 1000, tickangle=0)
    fig.update_yaxes(gridcolor="rgba(255,255,255,0.12)", zeroline=False, ticksuffix="°")
    return fig


# ---------- Page ----------

st.set_page_config(page_title="Weather", page_icon="🌤️", layout="wide")
init_db()

# Default (day) style first, so the page looks right even before / without a result
inject_css(is_day=True)

st.markdown('<div class="app-title">Robot Dreams Python · Weather Map & Data Visualization</div>',
            unsafe_allow_html=True)

_, search_col, _ = st.columns([1, 2, 1])
with search_col:
    city_input = st.text_input("Enter city name", value="Dabas",
                               placeholder="🔍  Search for a city", label_visibility="collapsed")

if not city_input.strip():
    st.info("Enter a city name to search.")
    st.stop()

# Steps 1–2: city name -> coordinates
try:
    location = get_coordinates(city_input.strip())
except requests.RequestException as e:
    st.warning(f"Error calling the geocoding API: {e}")
    st.stop()

if location is None:
    st.warning(f"City not found: '{city_input}'")
    st.stop()

place = f"{location['name']}, {location['country']}" if location["country"] else location["name"]

# Step 3: coordinates -> weather data
try:
    weather = get_weather(location["lat"], location["lon"])
except requests.RequestException as e:
    st.warning(f"Error calling the forecast API: {e}")
    st.stop()

current = weather["current"]
units = weather["current_units"]
temperature = current["temperature_2m"]
humidity = current["relative_humidity_2m"]
wind_speed = current["wind_speed_10m"]
condition, emoji = describe(current.get("weather_code", -1))

# Switch to the night sky after sunset in the searched city
if not current.get("is_day", 1):
    inject_css(is_day=False)

# Log only when a new search happens (not on every rerun of the script)
if st.session_state.get("last_logged") != place:
    log_search(place, temperature, humidity, wind_speed)
    st.session_state["last_logged"] = place

# Step 4: display the data
daily = weather["daily"]
st.markdown(
    hero_html(location["name"], location["country"], temperature, units["temperature_2m"],
              condition, emoji, daily["temperature_2m_max"][0], daily["temperature_2m_min"][0]),
    unsafe_allow_html=True,
)

# KPIs / key metrics
st.markdown(f'<div class="section">Current weather in {place}</div>', unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)
c1.metric(f"🌡️ Temperature ({units['temperature_2m']})", f"{temperature} {units['temperature_2m']}")
c2.metric(f"💧 Humidity ({units['relative_humidity_2m']})", f"{humidity} {units['relative_humidity_2m']}")
c3.metric(f"💨 Wind Speed ({units['wind_speed_10m']})", f"{wind_speed} {units['wind_speed_10m']}")

tab_forecast, tab_map, tab_log = st.tabs(["Forecast", "Map", "Search log"])

with tab_forecast:
    # Extra 1: forecast from the /forecast data
    st.markdown(f'<div class="section">5-day forecast · {place}</div>', unsafe_allow_html=True)
    st.markdown(daily_html(daily), unsafe_allow_html=True)

    st.markdown(f'<div class="section">Hourly temperature (next 5 days) · {place}</div>',
                unsafe_allow_html=True)
    hourly = pd.DataFrame({
        "time": pd.to_datetime(weather["hourly"]["time"]),
        "temperature": weather["hourly"]["temperature_2m"],
    })
    st.plotly_chart(forecast_chart(hourly, units["temperature_2m"]), width="stretch",
                    config={"displayModeBar": False})

with tab_map:
    st.markdown(f'<div class="section">Weather map · {place}</div>', unsafe_allow_html=True)
    st.map(pd.DataFrame({"lat": [location["lat"]], "lon": [location["lon"]]}),
           zoom=10, color="#5ac8fa", size=600)

with tab_log:
    st.markdown('<div class="section">Search log (SQLite)</div>', unsafe_allow_html=True)
    log = read_log().rename(columns={
        "city": "City", "temperature": "Temperature (°C)", "humidity": "Humidity (%)",
        "wind_speed": "Wind speed (km/h)", "searched_at": "Searched at",
    })
    if log.empty:
        st.info("No searches logged yet.")
    else:
        # Render as a glass HTML table; lines are stripped so Markdown doesn't treat them as code
        table = log.head(50).to_html(index=False, classes="log-table", border=0)
        table = "".join(line.strip() for line in table.splitlines())
        st.markdown(f'<div class="glass log">{table}</div>', unsafe_allow_html=True)
