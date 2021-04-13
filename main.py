import requests
import json
import inspect
from datetime import datetime

from API import APIinfo


API_URL = "http://api.openweathermap.org/data/2.5/weather?q=" + APIinfo["query"]["city_name"] + "," + APIinfo["query"]["country_code"] + "&units=" + APIinfo["units"] + "&appid=" + APIinfo["API_KEY"]


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
            return "INVALID OPTON"

    def getWeather(self, option: str):
        '''
        returns the main weather information
        @param option type str
        options can be main,description,icon,id
        '''

        if option in ["id", "main", "description", "ison"]:
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
            return "INVALID OPTON"

    def getFormatedTime(self,UNIX_TIMESTAMP:str):
        ts = int(UNIX_TIMESTAMP)
        return datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')


w = Weather()

# :TODO: Convert wind speed from m/s to kmph

info = inspect.cleandoc(f'''
        Current Temparature : {w.getMain("temp")}C
        Feels like : {w.getMain("feels_like")}C
        Max temparature : {w.getMain("temp_max")}C
        Min temparature : {w.getMain("temp_min")}C
        Wind : {w.getWind("speed")} m/s {w.getWind("deg")} degree 
        Visibility : {w.getVisibility()}m
        Sunrise : {w.getFormatedTime(w.getSys("sunrise"))}
        Sunset : {w.getFormatedTime(w.getSys("sunset"))}
'''
                        )


def main():
    if weatherResponse["cod"] == 200:
        print(info)


if __name__ == "__main__":
    main()
