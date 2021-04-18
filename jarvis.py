# Jarvis is you're virtual assistant like cortona. You can add some codes for you comfortable like you can add some more websites.

import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

    
# For wish function 

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("good morning sir")

    elif hour >= 12 and hour < 18:
        speak("good afternoon sir")
    else:
        speak(" good evening sir")

    speak(" i am Jarvis. please tell me how may i help you")

# For listening and recognize the voice(command by user)
    
def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said, {query}\n")
    except Exception as e:
        print(e)
        print("say that again please...")
        return "None"
    return query

# for sending Email
# NOTE :- You have to write you're own email and password


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('nkrider27@gmail.com','XXXX')
    server.sendmail('nkrider27@gmail.com', to, content)
    server.close()


if __name__ == '__main__':
    wishMe()
    while True:

        query = takeCommand().lower()

        if 'wikipedia' in query:                                         # Code for open wikipedia 
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:                                    # Code for open Youtube
            webbrowser.open("youtube.com")

        elif 'open google' in query:                                     # Code for google search engine
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:                              # Code for Stackoverflow
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:                                      #code for Songs 
            music_dir = 'E:\\whats app audio'                            # location of musics
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[2]))

        elif 'the time' in query:                                       # For time 
            srtTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {srtTime}")

        elif 'email to nikhil' in query:                               # For sending the Email
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "nkrider27@gmail.com"                            # add you're own Email
                sendEmail(to, content)
                speak("Email has been send!")
            except Exception as e:                                    # If email is not sent becaue of some reasons like internet issues 
                print(e)
                speak("Sorry Nikhil sir. I am not able to send this email")

        elif 'quit' in query:                                         # speak quite to stop the program 
            exit()

