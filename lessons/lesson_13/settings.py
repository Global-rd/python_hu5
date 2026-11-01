import os
from dotenv import load_dotenv
load_dotenv()

OPENWEATHERMAP_API_KEY=os.environ.get("OPENWEATHERMAP_API_KEY")
BUDAPEST = {"lat":47.4979, "lon":19.0402}