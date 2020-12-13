"""
Import PyOWM and modules into program
"""

from pyowm import OWM
owm = OWM('b4422cd2b94310f148af2aa9a9649490')
weather_mgr = owm.weather_manager()

"""
Weather Questionnaire

This is a quiz that sets the user's weather preferences

the higher the score the warmer someone tends to dress
"""

score = 0

question1 = input("Do you tend to run "
                  "A) warm "
                  "B) cold? ")
while question1 != "A" and question1 != "B":
    print("Please answer either 'A' or 'B.")
    question1 = input("Do you tend to run "
                      "A) warm "
                      "B) cold? ")
if question1 == "A":
    score = score + 1
elif question1 == "B":
    score = score + 2

question2 = input("Are you from a "
                  "A) colder climate "
                  "B) warmer climate? ")
while question2 != "A" and question2 != "B":
    print("Please answer either 'A' or 'B.")
    question2 = input("Are you from a "
                      "A) colder climate "
                      "B) warmer climate? ")
if question2 == "A":
    score = score + 1
elif question2 == "B":
    score = score + 2

question3 = input("It's 60 degrees out and sunny. Are you wearing "
                  "A) a t-shirt "
                  "B) a light jacket "
                  "C) a heavy sweater? "
                  )
while question3 != "A" and question3 != "B" and question3 != "C":
    print("Please answer either 'A' 'B' or 'C'.")
    question3 = input("It's 60 degrees out and sunny. Are you wearing "
                      "A) a t-shirt "
                      "B) a light jacket "
                      "C) a heavy sweater? ")
if question3 == "A":
    score = score + 1
elif question3 == "B":
    score = score + 2
elif question3 == "C":
    score = score + 3

question4 = input("At what temperature do you start wearing shorts instead of pants? "
                  "A) 60F "
                  "B) 70F "
                  "C) 80F ")
while question4 != "A" and question4 != "B" and question4 != "C":
    print("Please answer either 'A' 'B' or 'C'.")
    question4 = input("At what temperature do you start wearing shorts instead of pants? "
                      "A) 60F "
                      "B) 70F "
                      "C) 80F ")
if question4 == "A":
    score = score + 1
elif question4 == "B":
    score = score + 2
elif question4 == "C":
    score = score + 3

question5 = input("It’s pouring rain out, what do you do? "
                  "A) Nothing, I don't mind rain "
                  "B) A hood will do just fine "
                  "C) Bring an umbrella "
                  "D) I'm not going outside today ")
while question5 != "A" and question5 != "B" and question5 != "C" and question5 != "D":
    print("Please answer either 'A' 'B' or 'C'.")
    question5 = input("It’s pouring rain out, what do you do? "
                      "A) Nothing, I don't mind rain "
                      "B) A hood will do just fine "
                      "C) Bring an umbrella "
                      "D) I'm not going outside today ")
if question5 == "A":
    score = score + 1
elif question5 == "B":
    score = score + 2
elif question5 == "C":
    score = score + 3
elif question5 == "D":
    score = score + 4

"""
Getting the weather
"""

location = input("Location City,Country (ex. seattle,US) : ")
observation = weather_mgr.weather_at_place(location)  # the observation object is a box containing a weather object
weather = observation.weather
weather.status
weather.detailed_status


weather = weather_mgr.weather_at_place(location).weather
temp_dict_fahrenheit = weather.temperature('fahrenheit')
temp_dict_fahrenheit['temp_min']
temp_dict_fahrenheit['temp_max']
temp_dict_fahrenheit["feels_like"]

print("")
print("Here's what you should wear:")
if 5 <= score <= 7:
    if temp_dict_fahrenheit['feels_like'] >= 68:
        print("Shorts and a t-shirt for you today")
    if 68 > temp_dict_fahrenheit['feels_like'] >= 50:
        print("A light jacket will be good for today")
    if temp_dict_fahrenheit["feels_like"] < 50:
        print("Dress in layers because it's chilly out right now!")
    if "sunny" in weather.detailed_status:
        print("You may need sunglasses today")
    if "rain" in weather.detailed_status:
        print("It's going to rain today, bring a light jacket!")
    if "snow" in weather.detailed_status:
        print("Time for snow pants!")
elif 8 >= score <= 11:
    if temp_dict_fahrenheit['feels_like'] >= 68:
        print("Shorts would be good with a t-shirt, but don't forget a light jacket!")
    if 68 > temp_dict_fahrenheit["feels_like"] >= 50:
        print("Long sleeves and a jacket, maybe a hat would be good today!")
    if temp_dict_fahrenheit["feels_like"] < 50:
        print("Time to bust out the winter jacket!")
    if "sunny" in weather.detailed_status:
        print("You may need sunglasses today")
    if "rain" in weather.detailed_status:
        print("It's going to rain today, bring an umbrella!")
    if "snow" in weather.detailed_status:
        print("Time for snow pants!")
else:
    if temp_dict_fahrenheit['feels_like'] >= 68:
        print("Light pants would be good with a t-shirt, but don't forget a light jacket!")
    if 68 > temp_dict_fahrenheit["feels_like"] >= 50:
        print("Long sleeves, long pants, and a jacket. Maybe a hat would be good today!")
    if temp_dict_fahrenheit["feels_like"] < 50:
        print("Time to bust out the winter jacket and LAYERS!")
    if "sunny" in weather.detailed_status:
        print("You may need sunglasses today")
    if "rain" in weather.detailed_status:
        print("It's going to rain today, are you sure you want to go out?")
    if "snow" in weather.detailed_status:
        print("It's snowing today, if you are going out wear ALL the layers")

print(" ")
print("Here's your weather report:")
print(f"Today there will be a low of", temp_dict_fahrenheit['temp_min'], "F, with a high of", temp_dict_fahrenheit['temp_max'], "F.")
print(f"Right now there are", weather.detailed_status, "and feels like", temp_dict_fahrenheit['feels_like'], "F")
