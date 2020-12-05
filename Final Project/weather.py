"""
Import PyOWM and modules into program
"""

from pyowm import OWM
owm = OWM('b4422cd2b94310f148af2aa9a9649490')
weather_mgr = owm.weather_manager()


observation = weather_mgr.weather_at_place('Boston,US')  # the observation object is a box containing a weather object
weather = observation.weather
weather.status
weather.detailed_status


weather = weather_mgr.weather_at_place('Boston,US').weather
temp_dict_fahrenheit = weather.temperature('fahrenheit')
temp_dict_fahrenheit['temp_min']
temp_dict_fahrenheit['temp_max']




print(f"Today there will be a low of", temp_dict_fahrenheit['temp_min'], "F, with a high of", temp_dict_fahrenheit['temp_max'], "F.")
print(f"Right now there are", weather.detailed_status, "and feels like", temp_dict_fahrenheit['feels_like'], "F")

