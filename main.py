import pyttsx3  # This is module is contvert simple text to speech.s
from time import *
import pyjokes
import random
import os
import webbrowser
import wikipedia
import speech_recognition as sr  # speech recognition that allows the machine to catch the words, phrases and sentences we speak.
import datetime

import requests
from bs4 import BeautifulSoup


from tkinter import *
import tkinter as tk
root = tk.Tk()
root.minsize(1210, 650)
root.maxsize(1210, 650)
root.title("JARVIS")

label = Label(root, text="Jarvis", font="Gill 30 bold",bg="black", fg="white")
label.pack(fill=X,ipady=10)

from PIL import Image, ImageTk
image = Image.open("D:\\My python_materials\\Project-Jarvis\\Jarvis - Desktop_Voice_Assistant\\bg_edited.jpg")
photo = ImageTk.PhotoImage(image)
photo_label = Label(image=photo)
photo_label.pack()


root.config(bg="black")

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty("rate", 180)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

scvalue = StringVar()
screen = Entry(root, textvar=scvalue, font="lucide 20 bold italic",fg="white",bg="black",justify='center')
screen.pack(fill=X, ipadx=500,ipady=2, padx=200, pady=20)
scvalue.set("CLICK ON RUN")

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        scvalue.set("Good Morning...")
        screen.update()
        speak("Good Morning")
        

    elif hour >= 12 and hour < 18:
        scvalue.set("Good Afternoon...")
        screen.update()
        speak("Good Afternoon ")
       

    else:
        scvalue.set("Good Evening...")
        screen.update()
        speak("Good Evening")
      
    
    speak("I am Jarvis sir. Please tell me how may i help you.")

def takeCommand():
    # It takes microphone input from the user and returns string output.
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # print("Listening...")
        scvalue.set("Listening...")
        screen.update()
        # seconds of non-speaking audio before a phrase is considered complete.
        r.pause_threshold = 0.5
        audio = r.listen(source)
    try:
        print("Recognizing...")
        scvalue.set("Recognizing...")
        screen.update()
        query = r.recognize_google(audio, language='en-in')
        # print(f"User said : {query}\n")
        scvalue.set(f"User said : {query}\n")
        screen.update()
    except Exception as e:
        # print(e)
        scvalue.set(f"{e}")
        screen.update()
        # print("Say that again please...!")
        scvalue.set("Say that again please...!")
        screen.update()
        return "None"
    return query


def run():  
    wishMe()
    while True:
        query = takeCommand().lower()
        # Logic for executing tasks based on query.

        if 'wikipedia' in query:
            scvalue.set("Please wait we are searching wikipedia")
            screen.update()
            speak("Please wait we are searching wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=4)
            scvalue.set("According to wikipedia..")
            screen.update()
            speak("According to wikipedia..")
            # print(results)
            speak(results)

        elif "who are you" in query:
            scvalue.set("i am jarvis sir. Please tell me how may i help you.")
            screen.update()
            speak("i am jarvis sir. Please tell me how may i help you.")


        elif "how are you" in query:
            # print("i am fine sir. Please tell me how may i help you.")
            scvalue.set("i am fine sir. Please tell me how may i help you.")
            screen.update()
            speak("i am fine sir. Please tell me how may i help you.")

        elif 'open youtube' in query:
            scvalue.set("Please wait sir, opening youtube...")
            screen.update()
            speak("Please wait sir, opening youtube...")
            webbrowser.open("https://youtube.com")

        elif 'open amazon' in query:
            scvalue.set("Please wait sir, opening amazon...")
            screen.update()
            speak("Please wait sir, opening amazon...")
            webbrowser.open("https://www.amazon.in/?&ext_vrnc=hi&tag=googhydrabk1-21&ref=pd_sl_drjtlom86_e&adgrpid=54397910370&hvpone=&hvptwo=&hvadid=486382063653&hvpos=&hvnetw=g&hvrand=17821143910699793947&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1007805&hvtargid=kwd-31596400&hydadcr=5623_2175702&gclid=CjwKCAiA78aNBhAlEiwA7B76p_E_hMP3svvHDeWZaNRa6ZtHyMWwwpdUqa0BrJQqrs34cgApPNqsDBoCkvAQAvD_BwE")

        
            
        elif 'open google' in query:
            scvalue.set("Please wait sir, opening google...")
            screen.update()
            speak("Please wait sir, opening google...")
            webbrowser.open("https://google.com")

        elif 'open stackoverflow' in query:
            scvalue.set("Please wait sir, opening stackoverflow...")
            screen.update()
            speak("Please wait sir, opening stackoverflow...")
            webbrowser.open("https://stackoverflow.com")

        elif 'open instagram' in query:
            scvalue.set("Please wait sir, opening instagram...")
            screen.update()
            speak("Please wait sir, opening instagram...")
            webbrowser.open("https://instagram.com")

        elif 'open facebook' in query:
            scvalue.set("Please wait sir, opening facebook...")
            screen.update()
            speak("Please wait sir, opening facebook...")

            webbrowser.open("https://facebook.com")

        elif 'open linkedin' in query:
            scvalue.set("Please wait sir, linkedin...")
            screen.update()
            speak("Please wait sir, opening linkedin...")
            webbrowser.open("https://linkedin.com")

        elif 'open twitter' in query:
            scvalue.set("Please wait sir, twitter...")
            screen.update()
            speak("Please wait sir, opening twitter...")
            webbrowser.open("https://twitter.com")

        # Play music
        elif 'music' in query:
            music_dir = 'D:\\my python_materials\\Project-Jarvis\music'
            songs = os.listdir(music_dir)
            # print(songs)
            song_num = random.randint(0, 8)
            os.startfile(os.path.join(music_dir, songs[song_num]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            # print(strTime)
            scvalue.set(f"The time is {strTime}")
            screen.update()
            speak(f"The time is {strTime}")
 
        elif 'temperature' in query:
            scvalue.set("Please wait sir, we searching temperature...")
            screen.update()
            speak("Please wait sir, we searching temperature...")
            search = "temperature in udaipur"
            url = f"http://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div",class_="BNeawe").text
            scvalue.set(f"Current {search} is {temp}")
            screen.update()
            speak(f"Current {search} is {temp}")
            

        elif 'open vs code' in query:
            scvalue.set("Please wait sir, opening vs code...")
            screen.update()
            speak("Please wait sir, opening vs code...")
            Codepath = "C:\\Users\\91800\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(Codepath)

        elif 'close vs code' in query:
            scvalue.set("ok sir, closing vs code...")
            screen.update()
            speak("ok sir, closing vs code...")
            os.system("taskkill /f /im Code.exe")

        elif 'hide' in query:
            os.system("attrib +h /s /d")
            speak("Sir, all file in this folder are now hidden.")

        elif 'visible for everyone' in query:
            os.system("attrib -h /s /d")
            speak("Sir, all file in this folder are now visible for everyone.")

        elif 'open notepad' in query:
            scvalue.set("Please wait sir, opening notepad...")
            screen.update()
            speak("Please wait sir, opening notepad...")
            Notepadpath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Notepad"
            os.startfile(Notepadpath)

        elif 'close notepad' in query:
            scvalue.set("ok sir, closing notepad...")
            screen.update()
            speak("ok sir, closing notepad...")
            os.system("taskkill /f /im Notepad.exe")

        elif 'open command prompt' in query:
            speak("sir, opening command prompt please wait...")
            cmdPath = (
                "C:\\Users\\91800\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Command_Prompt")
            os.startfile(cmdPath)

        elif 'tell me a joke' in query:
            my_joke = pyjokes.get_joke(language='en', category='all')
            print(my_joke)
            speak(my_joke)

        elif 'sleep' in query:
            scvalue.set("Thanks for using me sir. have a good day.")
            screen.update()
            speak("Thanks for using me sir. have a good day.")
            exit()


def myExit():
    exit()


btn_run = Button(root, text="RUN", bg="green", fg="black",font="Arial 20 bold", command=run)
btn_run.place(x=490, y=580, height=50, width=110)

btn_exit = Button(root, text="EXIT", bg="red", fg="black",font="Arial 20 bold", command=myExit)
btn_exit.place(x=620, y=580, height=50, width=110)



root.mainloop()
