import requests 
from dotenv import load_dotenv
import os 

city = input("Enter the city you want weather for: ").strip().lower()

load_dotenv()
API_KEY = os.environ.get('WEATHER_API_KEY')

if not API_KEY:
    print("Please enter your API key in a .env file in the project root folder.")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    output = data['main']['temp']
    print(f"{output} degree celsius")
else:
    print(f"Please enter a valid city name.")
