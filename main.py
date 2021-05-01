import requests
import json
import inspect
import os
from datetime import datetime

from util import FormateTime,FormateCardinalDirection,mps_to_kmph


API_URL = "http://api.openweathermap.org/data/2.5/weather?q=" + os.environ["WEATHERPY_CITY_NAME"] + "," + os.environ["WEATHERPY_COUNTRY_CODE"]+ "&units=" + os.environ["WEATHERPY_UNITS"] + "&appid=" + os.environ["WEATHERPY_API_KEY"]


weatherResponseRaw = requests.get(API_URL)
weatherResponse = weatherResponseRaw.json()


class Weather:
    def __init__(self):
        self.weather = weatherResponse["weather"][0]
        self.main = weatherResponse["main"]
        self.wind = weatherResponse["wind"]
        self.sys = weatherResponse["sys"]
        self.coord = weatherResponse["coord"]

    def getCoord(self, option: str):
        if option in ["lat", "lon"]:
            return self.coord[option]
        else:
            return "INVALID OPTION"

    def getWeather(self, option: str):
        if option in ["id", "main", "description", "icon"]:
            return self.weather[option]
        else:
            return "INVALID OPTION"

    def getMain(self, option: str):
        if option in ["temp", "feels_like", "temp_min", "temp_max", "pressure", "humidity", "sea_level", "grnd_level"]:
            return self.main[option]
        else:
            return "INVALID OPTION"

    def getVisibility(self):
        return weatherResponse["visibility"]

    def getWind(self, option: str):
        if option in ["speed", "deg"]:
            return self.wind[option]
        else:
            return "INVALID OPTION"

    def getSys(self, option: str):
        if option in ["country", "sunrise", "sunset"]:
            return self.sys[option]
        else:
            return "INVALID OPTION"



w = Weather()

info = inspect.cleandoc(f'''
        Current Temperature : {w.getMain("temp")}{chr(176)}C
        Feels like : {w.getMain("feels_like")}{chr(176)}C
        Max temperature : {w.getMain("temp_max")}{chr(176)}C
        Min temperature : {w.getMain("temp_min")}{chr(176)}C
        Humidity : {w.getMain("humidity")}%
        Wind : {mps_to_kmph(w.getWind("speed"))}kmph {w.getMain("pressure")}atm {w.getWind("deg")}{chr(176)} {FormateCardinalDirection(w.getWind("deg"))}
        Visibility : {w.getVisibility()}m
        Sunrise : {FormateTime(w.getSys("sunrise"))}
        Sunset : {FormateTime(w.getSys("sunset"))}
'''
                        )


def main():
    if weatherResponse["cod"] == 200:
        print(info)


if __name__ == "__main__":
    main()
