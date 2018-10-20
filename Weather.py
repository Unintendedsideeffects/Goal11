import openweather
import datetime
import pyowm

owm = pyowm.OWM("1de8930ec5d19e8b86bf6561b6f9bb74")

station = owm.weather_at_coords(32.1736,36.1940)._location._name

print(station)
