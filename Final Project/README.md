# Weather the Weather!
*How did I do this?*

## **Original Proposal:**

It's 5am and you're running late to work. It's still pitch black outside so it's hard to tell what the weather will be like much less what to wear. Thank God for the handy-dandy weather widget on your iPhone that tells you it's going to be 64 degrees with 15mph winds and some showers towards the end of the day. Unfortunately you don't know what heck that actually feels like to you and you're stuck picking a quick outfit and praying it won't fail you.

Well, what if there was a personalized program that tells you exactly what YOU should wear based on the weather? Soon there will be because that's my Final Project. This program will be useful for anyone who lives where there is weather.

---

## **Resources Used:**

- I used [Dress for the Weather](https://projects.raspberrypi.org/en/projects/dress-for-the-weather) instructions from Raspberrypi, but then found it to be outdated.
- [PyOWM](https://pyowm.readthedocs.io/en/latest/): a client Python wrapper library for OpenWeatherMap web APIs. It allows quick and easy consumption of OWM data from Python applications via a simple object model and in a human-friendly fashion.
- [Code Recipes](https://pyowm.readthedocs.io/en/latest/v3/code-recipes.html#library_init): shows how to use PyOWM and make it your own.
- [This Github](https://github.com/csparpa/pyowm) that describes how to use PyOWM
- [OpenWeatherMap](openweathermap.org): This open source weather map gives you an API for free to link to your Program

---

## **Problems Faced:**

- Wrapping my head around what the heck I was doing was hard. Coding is relatively new to me and I didn't know where to start. Once I found "Dress for the Weather" I had a clearer path on how to create this program.
- After figuring out how to use OpenWeatherMap, I ran into a serious problem... I could only grab the weather from Moscow, Russia! I could *not* figure out what was wrong and then sidelined this project for a week to do further investigating. Eventually (and I mean *eventually*), I found that instead of writing "seattle,WA" I had to write "seattle,US". I felt so dumb, but hey at least I figured it out!
- Creating questions that are specific enough to capture if a person tends to dress warmer or not was difficult. Also, making sure that the questions were universally understood was important. Once I came up with a set of questions that I was comfortable with I was good to do.
- I couldn't figure out how to "call" the weather.questionnaire into the weather program so I ended up copying and pasting the questionnaire in the official weather program.

---

## __*The Future*__

I could see this program being used in an app and even as a widget on a phone. When people are getting ready for the day they are more likely to check the weather on a smartphone than the computer. Also, this app could eventually *partner* with clothing companies.

*Hey, today's going to be raining, you should wear a jacket*

*Oh, you don't have a jacket?*

*Well __here's__ a great store to buy one online!*

Here's an example of what the app User Interface could look like:

![alt text](https://github.com/talizhaky/LMSC261/blob/master/Final%20Project/Weather_the_Weather_App.png)
