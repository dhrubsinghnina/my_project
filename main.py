import speech_recognition as sr
import pyttsx3
import win32com.client as wincl
import webbrowser

speaker = wincl.Dispatch("SAPI.SpVoice")
speaker.Rate=1
def speak_fast(text):
    speaker.Speak(text)

engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()
    
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
        
    else:
        speak_fast("Mujhe iski anumati nahi hai ")
        
if __name__=="__main__":
    speak("Initializing Jarvis .......")
    while True:
        
        r = sr.Recognizer()
        
        try:
            # listen for the wake word Jarvis:
            with sr.Microphone() as source:
                print("Listening.....")
                r.adjust_for_ambient_noise(source, duration=0.5)
                audio = r.listen(source,timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            print(word)
            if "jarvis" in word.lower():
                speak_fast("Yessir how can i help you")
                # listen for command
                with sr.Microphone() as source:
                    r.adjust_for_ambient_noise(source, duration=0.5)
                    audio=r.listen(source,timeout=5,phrase_time_limit=4)
                command=r.recognize_google(audio)
                print(command) 
                processCommand(command)
                    
        except Exception as e:
            print("error; {0}".format(e))
      