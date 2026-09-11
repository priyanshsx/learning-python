import requests 
from dotenv import load_dotenv
import os 

city = input("City you want to check the weather for: ").strip().lower()

load_dotenv()
API_KEY=os.environ.get('WEATHER_API_KEY')

if not API_KEY:
    raise RuntimeError("Weather API key not set. Please add it to the .env file in the root folder.")

