import speech_recognition as sr
import os
import time
import webbrowser
import playsound
import sys
from time import ctime
from gtts import gTTS

r = sr.Recognizer()

def clear() :
    if os.name == 'nt' :
        os.system('cls')
    else :
        pass

def speak(text) : 
    tts = gTTS(text = text, lang = 'en')
    filename = 'voice.mp3'
    tts.save(filename)
    playsound.playsound(filename)
    if os.name == 'nt' :
        os.system('del voice.mp3')
    else : 
        os.system('rm voice.mp3')

time.sleep(1)
speak('Starting voice recognition services, Please Wait')
time.sleep(2)
speak('what should I call you ?')
masterName = input(' What should I Call You ? ')
greet = 'Hello Master ' + masterName
speak(greet)
time.sleep(1)
speak('Identifying System, Please wait')
time.sleep(2)
if os.name == 'nt' : 
    speak('Detected System as Microsoft Windows')
else : 
    speak('Linux System detected, some commands may not work properly')

clear()
speak('you can now leave me running in the background and i will keep responding to your voice commands.')

def record_audio(ask = False) : 
    with sr.Microphone() as source : 
        if ask : 
            print(ask)
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        voice_data = ''
        try : 
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError : 
            speak('Sorry I did not understand')
        except sr.RequestError : 
            speak('Speech service down')
        return voice_data
    if os.name == 'nt' :
        os.system('del voice.mp3')
    else : 
        os.system('rm voice.mp3')

def respond(voice_data) : 
    if 'who are you' in voice_data :
        speak('I am the only assistant to Master Grady')

    if 'programmer' in voice_data : 
        speak('Master Grady is my real programmer\n')

    if 'what time is it' in voice_data : 
        speak(ctime())

    if 'what is the weather' in voice_data : 
        speak('Fetching weather details')
        webbrowser.get().open('https://www.google.com/search?q=current+weather')

    #internet queries
    if 'find' in voice_data :
        speak('What do you wanna find ?')
        search = record_audio()
        url = 'https://google.com/search?q=' + search
        speak("Searching " + search)
        webbrowser.get().open(url)

    if 'news' in voice_data : 
        speak('Fetching News')
        webbrowser.get().open('https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN:en')

    if 'open exploit database' in voice_data : 
        speak("Opening Exploit Database")
        webbrowser.get().open("https://exploit-db.com")

    if 'locate' in voice_data : 
        speak('What do you wanna locate ?')
        location = record_audio()
        url = 'https://google.com/maps/place/' + location + '/&amp;'
        speak('Locating ' + location)
        webbrowser.get().open(url)

    if 'WhatsApp' in voice_data : 
        speak('Opening Whatsapp')
        webbrowser.get().open('https://web.whatsapp.com')

    if 'Instagram' in voice_data : 
        speak('Opening Instagram')
        webbrowser.get().open('https://instagram.com')
    
    if 'Facebook' in voice_data : 
        speak('Opening Faceebook')
        webbrowser.get().open('https://facebook.com')

    if 'drive' in voice_data : 
        speak('Opening Google Drive')
        webbrowser.get().open('https://drive.google.com')

    if 'one drive' in voice_data : 
        speak('Opening Microsoft One Drive')
        webbrowser.get().open('https://onedrive.live.com/')

    if 'meet' in voice_data : 
        speak('Opening Google Meet')
        webbrowser.get().open('https://meet.google.com')

    if 'open command' in voice_data :
        if os.name == 'nt' : 
            speak('Spawning Command Shell') 
            os.system("start cmd.exe")
        else : 
            speak("I cannot access the linux command system at the moment")

    if 'get videos' in voice_data : 
        speak('What video topic you want ? ')
        videos = record_audio()
        speak('Getiing Videos for ' + videos)
        url = 'https://youtube.com/search?q=' + videos
        webbrowser.get().open(url)

    if 'upload code' in voice_data :
        speak('Opening Github')
        webbrowser.get().open('https://github.com/')

    #misc queries
    if 'take notes' in voice_data : 
        speak('Taking Notes')
        if os.name == 'nt' : 
            os.system('start notepad.exe')
        else : 
            speak('I cannot access the Linux file system at the moment')

    if 'exit' in voice_data : 
        speak('Bye and thanks for choosing me')
        time.sleep(1)
        sys.exit()

time.sleep(1)
while(1) : 
    speak('Waiting for your command ...')
    voice_data = record_audio()
    respond(voice_data)

input()