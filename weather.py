# from flask import Flask, render_template
import requests
from dataclasses import dataclass

apikey = "884bb2ed14133d87eba976001186a192"

@dataclass
class WeatherData:
    main: str
    description: str
    icon: str
    temperature: int


def get_lat_lon(city_name, state_code, country_code, API_KEY):
    resp = requests.get(
        f"http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={API_KEY}"
    ).json()
    data = resp[0]
    lat, lon = data.get("lat"), data.get("lon")
    return lat, lon


def get_current_weather(lat,lon,API_KEY):
    resp = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric').json()
    data = WeatherData(main=resp.get('weather')[0].get('main'),
                       description = resp.get('weather')[0].get('description'),
                       icon = resp.get('weather')[0].get('icon'),
                       temperature=int(resp.get('main').get('temp')))
    return data

def main(city_name, state_name, country_name):
    try:
        lat,lon=get_lat_lon(city_name, state_name, country_name, apikey)
        weather_data = get_current_weather(lat,lon,apikey)
        return weather_data
    except Exception as e:
        return "Please enter valid Location!!!"
if __name__ == "__main__":
    lat,lon = get_lat_lon('Vadodara','GJ', 'India', apikey)
    get_current_weather(lat,lon,apikey)
# app = Flask(__name__)


# @app.route("/")
# def index():
#     return render_template("index.html")



# if __name__ == "__main__":
#     app.run(debug=True)
