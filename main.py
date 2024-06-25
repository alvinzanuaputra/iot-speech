import pyttsx3 
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('rate', 200)  # Speed of speech
engine.setProperty('volume', 1)  # Volume (0.0 to 1.0)
engine.setProperty('voice', voices[0].id)  # Selecting the desired voice

def speak(text):
    engine.say(text)
    engine.runAndWait()
speak("Sistem is Ready for use, Alvin Zanua Putra Im so proud of you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening........")
        audio = r.listen(source)
        try:
            print("Recognizing.................")
            # speak("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
        except Exception as e:
            print("Try Again......")
            return "None"
        return query

if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if 'turn on' in query:
            print("Light On.......")
            speak("ouuupiii.")
        elif 'turn off' in query:
            print ("turn Off......")
            speak("The render is complete, sir........")
        elif 'close program' in query:
            print ("All Right Sir......")
            speak("All Right Sir........")
            break
