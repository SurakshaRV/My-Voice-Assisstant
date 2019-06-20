import pyttsx3 #to convert text to speech
import speech_recognition as sr
import datetime
import webbrowser
import wikipedia
import os
import smtplib  #to send mail

tts = pyttsx3.init()
voices = tts.getProperty('voices')
tts.setProperty('voice', voices[0].id) #female voice
# use voices[1].id for male voice

# to make voice assisstant speak
def speak(audio):
    tts.say(audio)
    tts.runAndWait()

#greets everytime this program is run
def Greet():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am RV, your personal voice assisstant. how may I help you")

#takes user's command
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        speak("Say that again please...")
        return "None"
    return query

def sendEmail(to, msg):
    host ="smtp.gmail.com"
    port=587
    username="meskillpy@gmail.com"
    password= "im1atpyp"
    conn = smtplib.SMTP(host,port)
    conn.ehlo()
    conn.starttls()
    conn.login(username,password)
    conn.sendmail(username, to, msg)
    conn.close()

if __name__ == "__main__":
    Greet()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'google' in query:
            webbrowser.open("google.com/"+ query)
        #elif 'open stackoverflow' in query:
        #    webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
            music_dir = 'C:\\Users\\user\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[1]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif 'open atom' in query:
            codePath = "C:\\Users\\user\\AppData\\Local\\atom\\atom.exe"
            os.startfile(codePath)
        elif 'open whatsapp' in query:
            codePath = "C:\\Users\\user\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            os.startfile(codePath)
        elif 'open pictures' in query:
            codePath = "C:\\Users\\user\\Pictures"
            os.startfile(codePath)
        elif 'send an email' in query:
            try:
                speak("Reciever mail ID please")
                to=takeCommand()
                speak("What should I say?")
                msg = takeCommand()
                sendEmail(to, msg)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Oops! Sorry. I am not able to send this email")
        elif  'exit'  in query:
            exit()
