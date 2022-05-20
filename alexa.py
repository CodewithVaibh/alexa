import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pywhatkit
import pyjokes


engine = pyttsx3.init('sapi5')
voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_11.0"
engine.setProperty('voice', voice_id)


def speak(audio):
   engine.say(audio)
   engine.runAndWait()
   
def wishme():
    hour = int(datetime.datetime.now().hour)
    
    if hour>=4 and hour<=12:
        speak("Good Morning Vaibhav!")
    
    elif hour>12 and hour<=16:
        speak("Good afternoon Vaibhav!")
        
    elif hour>16 and hour<=20:
        speak("Good Evening Vaibhav!")
        
    else:
        speak("Good Night Vaibhav!")
    
    speak("My name is Jarvis. I am your assistant and will be at your service anytime.")

def hear():
    import speech_recognition as sr
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        audio = r.listen(source)
        try:
              print("Recognizing...")    
              query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
              print(f"User said: {query}\n")  #User query will be printed.

        except:
            print("Say that again please")
            return "None"
        return query
    


if __name__== "__main__":
    wishme()
    while True:
        query = hear().lower()
        
        if 'wikipedia' in query:
            speak("Searching Wikipedia....please wait")
            query=query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences = 3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            
        
        elif 'youtube' in query:
            speak("Opening youtube")
            webbrowser.open("youtube.com")
        
        elif 'google' in query:
            speak("Opening google")
            webbrowser.open("google.com")
            
        elif 'bluestacks' in query:
            speak("opening bluestacks")
            path="C:\\Program Files\\BlueStacks_nxt\\HD-Player.exe"
            os.startfile(path)
            
        elif 'discord' in query:
            speak("opening discord")
            path="C:\\Users\\Vaibh\\OneDrive\\Desktop\\Discord.lnk"
            os.startfile(path)
            
        elif 'teams' in query:
            speak("opening ms teams")
            path="C:\\Users\\Vaibh\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Teams (work or school).lnk"
            os.startfile(path)
        
        elif 'the time' in query:
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Vaibhav, the time is {strtime}")
        
        elif 'your name' in query:
            speak("My name is Jarvis. I am ur assistant")
            
        elif 'my name' in query:
            speak("Your name is Vaibhav and you are my owner.")
        
        elif 'play' in query:
            song=query.replace("play","")
            speak("playing"+ song)
            pywhatkit.playonyt(song)
            
        elif 'joke' in query:
            speak(pyjokes.get_joke())
            
            
            
        
            
            