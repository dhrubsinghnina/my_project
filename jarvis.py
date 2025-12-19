import speech_recognition as sr
import pyttsx3
import win32com.client as wincl
import webbrowser
import musiclibrary
import requests
from openai import OpenAI

speaker = wincl.Dispatch("SAPI.SpVoice")
speaker.Rate=1
def speak_fast(text):
    speaker.Speak(text)

engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()

def aiprocess(command):
    client = OpenAI(
    api_key="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"
    )

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a virtual assistent names jarvis, skilled in generl task like Alexa and Google cloud"},
            {"role": "user", "content": command}
        ]
    )

    return completion.choices[0].message.content

    
def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open github" in c.lower():
        webbrowser.open("https://github.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com")
    elif "open chess" in c.lower():
        webbrowser.open("https://www.chess.com/play")
    elif "open hotstar" in c.lower():
        webbrowser.open("https://www.hotstar.com/in/home")
    elif "open mangaclash" in c.lower():
        webbrowser.open("https://wwww.toonclash.com")
    elif "play" in c.lower():
        song=c.lower().split(" ")[1]
        link=musiclibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r=requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=4610374b7ddf460a8e1f6ff8a1fcae73")
        if r.status_code == 200:
            data = r.json()
    
        # Check if articles exist
        articles = data.get("articles", [])
        
        # Grab top 5 headlines
        top_5 = articles[:5]
        
        for i, article in enumerate(top_5, start=1):
            headline = article.get("title")
            print(f"{i}. {headline}")
        else:
            print(f"Request failed with status code: {r.status_code}")
    else:
        output = aiprocess(c)
        speak_fast(output)
        
if __name__=="__main__":
    speak("Initializing Jarvis .......")
    while True:
        
        r = sr.Recognizer()
        
        try:
            # listen for the wake word Jarvis:
            with sr.Microphone() as source:
                print("Listening.....")
                r.adjust_for_ambient_noise(source, duration=1)
                audio = r.listen(source,timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            print(word)
            if "jarvis" in word.lower():
                speak_fast("Yessir how can i help you")
                # listen for command
                with sr.Microphone() as source:
                    r.adjust_for_ambient_noise(source, duration=1)
                    audio=r.listen(source,timeout=5,phrase_time_limit=4)
                command=r.recognize_google(audio)
                print(command) 
                processCommand(command)
                    
        except Exception as e:
            print("error; {0}".format(e))
            
            