import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import time

engine = pyttsx3.init()
r = sr.Recognizer()


def speak(text):
    engine.say(text)
    engine.runAndWait()


def greet():
    x = datetime.datetime.now().hour
    if 0 <= x < 12:
        print("Good morning")
        speak("Good morning")
    elif 12 <= x < 18:
        print("Good afternoon")
        speak("Good afternoon")
    else:
        print("Good evening")
        speak("Good evening")


def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        return text.lower()
    except sr.UnknownValueError:
        print("Could not understand audio")

    except sr.RequestError as e:
        print("Error fetching results; {0}".format(e))


def execute_command(com):
    s = "Searching for:"+ com
    print(s)
    speak(s)
    url = "https://www.google.com/search?q=" + com.replace(" ", "+")
    webbrowser.open(url)


def get_time():
    t = "Current time is " + str(datetime.datetime.now().replace(microsecond=0))
    print(t)
    speak(t)


if __name__ == "__main__":
    greet()
    print("How can i help you today?")
    speak("How can i help you today")
    while True:
        command = listen()
        if command == "exit":
            break
        if command == "what is the time":
            get_time()
        elif command:
            execute_command(command)