"""
Import PyOWM and modules into program
"""

from pyowm import OWM
owm = OWM('b4422cd2b94310f148af2aa9a9649490')
mgr = owm.weather_manager()
reg = owm.city_id_registry()

city = input("City Name: ")

country = input("Country Abbreviation: ")

list_of_locations = reg.locations_for('moscow', country='RU')
moscow = list_of_locations[0]
lat = moscow.lat
lon = moscow.lon


#takes the coordinates and finds the weather

one_call = mgr.one_call(lat=moscow.lat, lon= moscow.lon)
temp = one_call.forecast_daily[0].temperature('fahrenheit').get('feels_like_morn', None)

print(f"It is {temp} degrees Fahrenheit in {city}, {country}.")

if temp <= 40:
    print("You better be wearing layers. Do NOT forget a hat, scarf, and gloves!")
elif 40 < temp <= 70:
    print("I'd bring a sweatshirt wherever you go.")
elif temp > 70:
    print("SWIMSUIT WEATHER")
