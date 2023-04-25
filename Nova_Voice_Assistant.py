# pyttsx3 is a test-to-speach conversion library in python
# Unlike alternative libraries, it works offline, and is compatible with both python 2 and python 3.

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

def Yourself():
    speak("Hi i am Nova")
    #print("Hi i am Nova")
    speak("I am your personal Assistant")
    #print("I am your personal Assistant")
    speak("I was Developed in Python Programming language")
    #print("I was Developed in Python Programming language")
    speak("I was Developed by Mr.Rohan Biturwar as a major project for final year, Batch 2020-2023")
    #print("I was Developed by Mr.Rohan Biturwar as a major project for final year, Batch 2020-2023")
    speak("I am currently in my developing stage")
    #print("I am currently in my developing stage")
    speak("Soon my first version will be released")
    #print("Soon my first version will be released")
    speak("There are many various work that i can do")
    #print("There are many various work that i can do")
    speak("Some of which include p y t t s x 3 , speach recognition , pygame , and many more")
    #print("Some of which include p y t t s x 3 , speach recognition , pygame , and many more")
    speak("Soon i willbe at my 100% to help you")
    #print("Soon i willbe at my 100% to help you")

def what_can_you_do():

    speak("I can give top 10 daily international headlines as and when requested")
    speak("I am able to capture your entire screen that is screen shot")
    speak("I can search all the image that you want from google")
    speak("I can get you all the weather Updates of any place you want")
    speak("When you are upset i can put a smile on your face with the help of some jokes")
    speak("I am also capable of conerting values from one unit to another unit")
    speak("Thank you this is all that i can do, My next version will have some new aditional features as well")

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

def weather(text):
    try:
        api_key_weather = "23917b44d9e7de5e3fe0876778777519"
        main_url = "http://api.openweathermap.org/data/2.5/weather?q="+text+",in&appid="+api_key_weather
        open_page = requests.get(main_url).json

        condition = open_page['weather'][0]['description'] # weather codition in string 
        temp = str(round(open_page['main']['temp'] - 273.165)) + 'degree celsius' # Tempprature in celsius
        pressure = str(open_page['main']['pressure']) + 'milli bar'# pressure in mili bar
        humidity = str(open_page['main']['hummidity']) + 'precent' # Humidity in precentage %
        wind_speed = str(open_page['wind']['speed']) + 'meter per second' # wind speed in meter per second
        wind_angle = str(open_page['main']['deg']) + 'degree of attack' # angle of wind

        print(f"weather at {text.capatalize()} is as follows")
        speak(f"weather at {text} is as follows")

        print(f"Condition    {condition}")
        speak(f"Condition    {condition}")

        print(f"Temprature   {temp}")
        speak(f"Temprature   {temp}")

        print(f"Pressure     {pressure}")
        speak(f"Pressure     {pressure}")

        print(f"hummidity    {humidity}")
        speak(f"hummidity    {humidity}")

        print(f"wind speed    {wind_speed}")
        speak(f"wind speed    {wind_speed}")

        print(f"wind angle    {wind_angle}")
        speak(f"wind angle    {wind_angle}")


        
        database_weather(condition, temp, pressure, humidity, wind_speed, wind_angle, text)



    except Exception as e:
            print("Sorry! Connection Failed -Please try again")
            speak("Sorry")
            speak("Connection Failed Please try again")

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
        

        elif 'wikipedia' in query:
            speak('Searching wekipedia ..........')
            query = query.replace('wikipedia', "")
            result = wikipedia.summary(query, sentences=2)
            speak('according to wikipedia')
            speak(result)


        elif 'play music' in query:
            speak("Be ready to rock and roll")
            music_dir = 'D:\\Song'
            songs = os.listdir(music_dir) # It will list all the songs in our music directory
            print(songs)
            speak("Dj play music")
            os.startfile(os.path.join(music_dir, songs[0])) # It will play the first song we can use random number technique to play any random song
            
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

        elif 'exit' in query:
            exit()
