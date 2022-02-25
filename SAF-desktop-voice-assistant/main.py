import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Good Morning!')

    elif hour>=12 and hour<18:
        speak('Good Afternoon!')   

    else:
        speak('Good Evening!')  

    speak('I am Saf Sir. Please tell me how may I help you')       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        if query == 'close' or 'close the program':
            print('It was good helping you, Thank you!!')

    except Exception as e:
        # print(e)    
        print('Unable to recognize, please say that again sir...')  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    print('welcome')
    print ("You could close this program by saying 'close' or 'close the program'")
    working = True
    while working == True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'who are you'in query:
            speak("I'am SAF, sir")
            print("I'am SAF, sir")

        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            speak('According to Wikipedia')
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak('Opening youtube')
            print('Opening youtube')
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak('Opening google')
            print('Opening google')
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            speak('Opening stackoverflow')
            print('Opening stackoverflow')
            webbrowser.open("stackoverflow.com")   

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print('Time is : ', strTime)
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = 'C:\\Program Files\\Microsoft VS Code\\Code.exe'
            print('Opening VsCode')
            speak('Opening VsCode')
            os.startfile(codePath)

        elif 'open media' in query:
            mediaPath = 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\VideoLAN'
            print('Opening VLC Media')
            speak('Opening VLC Media')
            os.startfile(mediaPath)

        elif 'send email' in query:
            try:
                speak('What should I say?')
                content = takeCommand()
                to = "_______@gmail.com" 
                sendEmail(to, content)
                speak('Email has been sent!')
            except Exception as e:
                print(e)
                speak('Sorry my friend. I am not able to send this email')
        elif 'close'in query:
            working = False
