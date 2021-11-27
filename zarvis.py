import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

print("initializing Jarvis")

MASTER = "Pintu"
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


# speak function will speak pronounce the string
def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():
     hour = datetime.datetime.now().hour

     if hour>=0 and hour <12:
        speak("Good morning" + MASTER)
     
     elif hour>=12 and hour <18:
         speak("Good afternoon" + MASTER)

     else:
        speak("Good evening" + MASTER)

     #speak("I am jarvis. How may I help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        
        try :
            print("Recognizing...")
            query = r.recognize_google(audio)
            print(f"user said: {query}\n")

        except Exception as e:     
            print("Say that again please")
            query = None

        return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmial.com','password')
    server.sendmail("harry@codewithharry.com",to,content)
    server.close();

def main():
    #main program
    #speak("initiallizing jarvis...")
    wishMe()
    query = takeCommand()


    #executing task
    if 'wikipedia' in query.lower():
        speak('Searching wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query,sentences =2)
        print(results)
        speak(results)

    elif 'open google' in query.lower():
            url="google.com"

            chrome_path ='C:/program files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)    

    elif 'open youtube' in query.lower():
            url="youtube.com"

            chrome_path ='C:/program files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)

    elif 'open reddit' in query.lower():
            url="reddit.com"

            chrome_path ='C:/program files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url) 

    elif 'play music' in query.lower():
        song_dir="C:\\Users\\Dell\\Music"
        song = os.listdir(song_dir)
        print(song)
        os.startfile(os.path.join(song_dir,song[0]))

    elif 'the time' in query.lower():
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"{MASTER} the time is {strTime}")

    elif 'open code' in query.lower():
        codePath = "C:\\Users\\Dell\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath)

    elif 'email to pintu' in query.lower():
        try :
            speak("What should I send")
            content =takeCommand()
            to = "pintu@gmail.com"
            sendEmail(to,content)
            speak("Email has sent sucessfully")
        except Exception as e:
            print(e)

main()          