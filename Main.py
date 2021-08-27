# Creator Pranaveshvar

import datetime
import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import pyjokes
import robloxpy
import youtube3

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
command = "placeholder"


def talk(text):
    engine.say('Hello Boss, I am Friday, An Artificial Intelligence')
    engine.say('Boss, What can I do for you?')
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'Friday' in command:
                command = command.replace('Friday', '')
                talk(command)
    except:
        pass
    return command


def run_Friday():
    command = 'take_command()'
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'Roblox' in command:
        talk(robloxpy.Game())
        talk(robloxpy.User())
        talk(robloxpy.Group())
        talk(robloxpy.Market())
    elif 'youtube' in command:
        talk(youtube3.YoutubeClient())
    else:
        talk('Boss please repeat the command again.')


while True:
    run_Friday()
