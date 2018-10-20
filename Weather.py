import openweather
import datetime
import requests
import time
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
        try:
            data = r.json()[0]
            min_temp = data["min_temp"]
            max_temp = data["max_temp"]
            weather_name = data["weather_state_name"]
        except:
            min_temp = None
            max_temp = None
            weather_name = None
            
        return [climate, weather_name, min_temp, max_temp]
        
    else:
        maxDays = calendar.monthrange(date.year, date.month)[1]
        min_temp = 0
        max_temp = 0
        areNone = 0

        for d in range(1, maxDays+1):
            URL = "https://www.metaweather.com/api/location/" + str(idCity) + "/" + str(date.year) + "/" +  str(date.month) +"/" + str(d) + "/"
            r = requests.get(url = URL)
            try:
                data = r.json()[0]
                min_temp += data["min_temp"]
                max_temp += data["max_temp"]
            except:
                areNone += 1

            time.sleep(0.25)

        if areNone<maxDays:
            min_temp /= (maxDays-areNone)
            max_temp /= (maxDays-areNone)
        else:
            min_temp = None
            max_temp = None
    
        return [climate, min_temp, max_temp]

#date = datetime.datetime(2019,2,1)

#w = weather(date=date,allMonth=True)

#print(w)


