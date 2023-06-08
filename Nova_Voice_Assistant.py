# PYTTSX3 is a text-to-speach connversion libraary in python
# unlike alternative libraries, it works offline, and is compatible with both python 2 and python 3

import pyttsx3
import datetime 
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import requests 
import json
import time
import pyautogui
import pymysql
import pygame as py
import random
import math
from auigui import *
from pred import *

obj1 = gui()
obj1.start()

engine = pyttsx3.init('sapi5')              # object creation, The Speech Application Programming Interface or SAPI is an API developed
                                            # by Microsoft to allow the use of speech recognition and speech synthesis within Windows applications.

voices = engine.getProperty("voices")       # getting deatils of current speaking voices                                             #print(voices[0].id) It will all voices available in syste, We only have female voice Zira
engine.setProperty('voice' , voices[1].id)  # setting up a new voice voices[0]

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour <= 16:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("Nova at your service")
    speak("How may i help you")

def speak(audio):
    gui.wave = False
    gui.circle = True
    engine.say(audio)
    engine.runAndWait()

def takecommand():
    '''
    It takes microphone input from user and returns string output and for converting speech to text it requires internet
    '''

    gui.wave = True
    gui.circle = False
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 0.8    # kitna tej bole yaha se control hoga
        r.adjust_for_ambient_noise(source , duration=1)
        r.non_speaking_duration = 0.3
        audio = r.listen(source)  # It listens what ever we say


    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print("User Said : ", query)

    except Exception as e:
        print(e)
        print("Say that Again Please....")
        speak("Say that Again Please....")
        return "None"
    return query

def newsfromBBC():
    # BBC news api
    main_url = "https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=a05cf53c56bf4c0882db52aed506e3bc"

    # Fetching Data in Json format
    open_page = requests.get(main_url).json()

    # Getting all article in a string article 
    article = open_page["articles"]

    # Empty list which will contain all ternding news
    results = []

    for ar in article:
        results.append(ar["title"])
    speak("The headlines are")

    for i in range(len(results)):

        # Print all trending news
        print(i+1, results[i])
        speak(results[i])
t = time.localtime()
timestamp = time.strftime('%b-%d-%Y_%H%M', t).lower()
filename = 'Screenshot' + timestamp + '.jpeg'

def imgsearch(text):
    urlp = "https://www.google.com/search?hl=en&tbm=isch&source=hp&biw=1745&bih=861&ei=bVgwXcSvKMzUvASsvr24BQ&q="+text
    urlm = urlp+"&oq="+text+"&gs_l=img.3..0l10.6121.7120..7308...0.0..0.242.1136.2j5j1......0....1..gws-wiz-img.....0..35i39.IvSjTlBizUM&ved=0ahUKEwiEmr2Kr77jAhVMKo8KHSxfD1cQ4dUDCAU&uact=5"
    webbrowser.open(urlm)

def say_joke():
    # main_url = "http://api.icndb.com/jokes/random"
    main_url =  "https://api.chucknorris.io/jokes/random"  # "https://hindi-jokes-api.onrender.com"
    open_page = requests.get(main_url).json()
    # joke = open_page["value"]["joke"]
    joke = open_page["value"]
    print(f"Joke : {joke}")
    speak(joke)

def capture():
    # Takes screenshot
    img = pyautogui.screenshot()

    # Save the image
    img.save("D:\\Nova Voice assistant\\ScreenShot\\" + filename)

    # Show the image
    # img.show()
    
def weather(text):
 
    try:
        api_key_weather = "23917b44d9e7de5e3fe0876778777519"
        main_url = "http://api.openweathermap.org/data/2.5/weather?q="+text+",in&appid="+api_key_weather
        open_page = requests.get(main_url).json()

        condition = open_page['weather'][0]['description']  # weather condition in string
        temp = str(round(open_page['main']['temp'] - 273.165)) + 'degree celsius'  # temp in C
        pressure = str(open_page['main']['pressure']) + 'mili Bar'  # pressure in mBar
        humidity = str(open_page['main']['humidity']) + 'percent'  # humidity in percentage %
        wind_speed = str(open_page['wind']['speed']) + 'meter per second'  # wind speed in m/s
        wind_angle = str(open_page['wind']['deg']) + 'degree'  # angle of wind

        print(f"Weather at {text.capitalize()} is as follows")
        speak(f"Weather at   {text} is as follows")

        print(f"Condition       {condition}")
        speak(f"condition       {condition}")

        print(f"Temperature     {temp}")
        speak(f"Temperature     {temp}")

        print(f"Pressure        {pressure}")
        speak(f"Pressure        {pressure}")

        print(f"Humidity        {humidity}")
        speak(f"Humidity        {humidity}")

        print(f"Wind Speed      {wind_speed}")
        speak(f"Wind Speed      {wind_speed}")

        print(f"At an Angle of  {wind_angle}")
        speak(f"At an Angle of  {wind_angle}")

        database_weather(condition, temp, pressure, humidity, wind_speed, wind_angle, text)



    except Exception as e:
        print("Sorry! Connection Failed - Please try again ", e)
        speak("Sorry ")
        speak("connection Failed Please try again")


def database_weather(condition, temp, pressure, humidity, wind_speed, wind_angle, place):
    # print("db wether")
   # return

    try:

        conn = pymysql.connect(host="127.0.0.1", user="root", passwd='', db='my_python')  # creates connection object
        mycursor = conn.cursor()  # It will allow to fire SQL Query

        date = datetime.datetime.now()
        date = str(date)

        url2 = "INSERT INTO weather (conditions, temperature, pressure, humidity, speed, angle, datetime, place) VALUES('"+condition+"','"+temp+"','"+pressure+"','"+humidity+"','"+wind_speed+"','"+wind_angle+"','"+date+"','"+place+"')"
        mycursor.execute(url2)
        print()
        # Fires Query

        conn.commit()  # Save changes in Mysql
    except Exception as e:
        print(e)
    finally:
        conn.close()

def database(name, age, gender, hobbies, qualification, favfood):
   # print("db")
   # return

    try:
        conn = pymysql.connect(host="127.0.0.1", user="root", passwd='', db='my_python') # creates connection object

        mycursor = conn.cursor()  # It will allow to fire SQL Query

        url = "INSERT INTO information (Name, Age, Gender, Hobbies, Qualification, Favfood) VALUES('"+name+"','"+age+"','"+gender+"','"+hobbies+"','"+qualification+"','"+favfood+"')"
        mycursor.execute(url)
        print()
        # Fires Query

        conn.commit()  # Save changes in Mysql
    except Exception as e:
        print(e)
    finally:
        speak("Thankyou for the co-operation")
        conn.close()


if __name__ == '__main__':

    wish()

    while True:
        query = takecommand().lower() # wee are converting the query in lower while searching any word we pass it in lower case
        #Logic to execute tast  based query
        if 'yourself' in query:
            Yourself()
        elif 'what can you do' in query:
            speak("Sure sir I would be happy shairing details about me with you")
            what_can_you_do()
        elif 'headlines' in query:
            newsfromBBC()
        
        elif 'jokes' in query:
            speak("Get Ready you won't be able to control your laughter")
            say_joke()
            say_joke()
            say_joke()
            say_joke()
            say_joke()


        elif'search' in query:
                speak("Sure sir tell what do you want to search")
                img = takecommand()
                imgsearch(img) 
        
        elif 'surfing' in query:
            speak("Sure but please tell me want you want to search")
            text = takecommand().lower()
            if "youtube" in text:
                text = text.replace('search', "")
                text = text.replace("youtube", "")
                text = text.split(" ")
                text = "+".join(text[4:])
                url = 'https://www.youtube.com/results?search_query='
                url = url + text
                print(url)
                webbrowser.open(url)

            elif "search" in text:
                text = text.replace('search', "").split(" ")
                text = "+".join(text[1:])
                urlp = 'https://www.google.com/search?source=hp&ei=txgvXfO1Cov_vAT_9oq4Dg&q='
                urlm = '&oq='
                urls = '&gs_l=psy-ab.3..0j0i22i30l9.1636.9226..9363...2.0..0.395.4581.0j11j5j4....2..0....1..gws-wiz.....10..35i39j0i67j0i131j0i20i263.GsXvyMxzL-0'
                url = urlp + text + urlm + text + urls
                print(url)
                webbrowser.open(url)

        elif 'play music' in query:
            speak("Be ready to rock and roll")
            music_dir = 'D:\\Song'
            songs = os.listdir(music_dir) # It will list all the songs in our music directory
            print(songs)
            speak("Dj play music")
            os.startfile(os.path.join(music_dir, songs[0])) # It will play the first song we can use random number technique to play any random song
        
        elif 'party' in query:
            speak("Be ready to rock and roll")
            music_dir = 'D:\\EDM'
            songs = os.listdir(music_dir) # It will list all the songs in our music directory
            print(songs)
            speak("Dj play music")
            os.startfile(os.path.join(music_dir, songs[0])) # It will play the first song we can use random number technique to play any random song
        
        elif 'Screenshot' in query:
            capture()
            print("Sir your image has been captured successfully")
            speak("Sir your image has been captured successfully")
            speak("Do you want to see it")
            query = takecommand()
            if 'yes' in query:
                path = "D:\\Nova Voice assistant\\ScreenShot\\" + filename
                os.startfile(path)
            
        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")
        
        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S") # Gives the current time in given format in form of a string
            speak(f"Sir,the time is {strtime}")
        
        elif 'C drive' in query:
            path = "C:\\"
            os.startfile(path)
        
        elif 'D drive' in query:
            path = "D:\\"
            os.startfile(path)

        elif 'weather' in query:
            speak("Tell me the place whose weather report you want")
            place = takecommand()
            weather(place)

        elif 'my friend' in query:
            speak("Welcome friend How Are you?")
            speak("Could you help me with your name please...")
            name = 'None'
            age = 'None'
            gender = 'None'
            hobbies = 'None'
            qualification = 'None'
            favfood = 'None'

            speak("What is Your Name")
            print("Name")
            while name == 'None':
                name = takecommand()


            speak("I also keen to know you gender...")
            while gender == 'None':
                gender = takecommand()

            speak('What is your age')
            while age == 'None':
                age = takecommand()


            speak("I am also interested in knowing your hobbies")
            while hobbies == 'None':
                hobbies = takecommand()

            speak("Can you tell me something about your Qualifications..")
            while qualification == 'None':
                qualification = takecommand()

            speak("Lastly tell me something which food item you love to eat")
            while favfood == 'None':
                favfood = takecommand()
            print(name, age, gender, hobbies, qualification, favfood)

            database(name, age, gender, hobbies, qualification, favfood)


        elif 'exit' in query:
            exit()
