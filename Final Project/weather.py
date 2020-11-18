"""
Import PyOWM and modules into program
"""

from pyowm import OWM
owm = OWM('b4422cd2b94310f148af2aa9a9649490')
mgr = owm.weather_manager()

'''seattle coordinates'''
one_call = mgr.one_call(lat=47.608013, lon=-122.335167)
print(one_call.forecast_daily[0].temperature('fahrenheit').get('feels_like_morn', None))

