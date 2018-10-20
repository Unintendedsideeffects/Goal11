import openweather
import datetime
import requests
#import pyowm

#owm = pyowm.OWM("1de8930ec5d19e8b86bf6561b6f9bb74")

#station = owm.weather_at_coords(32.1736,36.1940)._location._name

#print(station)

import requests
import datetime
import calendar

def weather(coordinates=[31.90,36.58], date = datetime.datetime.now(), allMonth = False):
    URL = "http://climateapi.scottpinkelman.com/api/v1/location/"+ str(coordinates[0]) + "/" + str(coordinates[1])
    r = requests.get(url = URL)
    data = r.json()
    climate = data["return_values"][0]["zone_description"]
    climateId = data["return_values"][0]["koppen_geiger_zone"] #Not used now

    URL = "https://www.metaweather.com/api/location/search/?lattlong="+ str(coordinates[0]) + "," + str(coordinates[1])
    r = requests.get(url = URL) 
    idCity = r.json()[0]["woeid"]

    if not allMonth:
        URL = "https://www.metaweather.com/api/location/" + str(idCity) + "/" + str(date.year) + "/" +  str(date.month) +"/" + str(date.day) + "/"
        r = requests.get(url = URL) 
        data = r.json()[0]
    else:
        maxDays = calendar.monthrange(date.year, date.month)
        for d in range(1, maxDays):
            
    
    min_temp = data["min_temp"]
    max_temp = data["max_temp"]
    weather_name = data["weather_state_name"]

    return [climate, weather_name, min_temp, max_temp]

weather()


