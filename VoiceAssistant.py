import pyttsx3 # Text-to-speech library, pip install pyttsx3
import speech_recognition as sr # Speech recognition library, pip install speechRecognition
import datetime
import wikipedia # Wikipedia API, pip install wikipedia
import webbrowser
import os
import smtplib
import pyaudio

# Initialize the text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    """Function to convert text to speech"""
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    """Function to greet the user based on the time of the day"""
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("Hello  Imama Kainat.I am Bob. Please tell me how may I help you")

def takeCommand():
    """Function to capture audio input and perform speech recognition"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query.lower()

def sendEmail(to, content):
    """Function to send an email using the Gmail SMTP server"""
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('mamainataki@gmail.com', 'mamainataki@gmail.com')  # Use your email and password
    server.sendmail('imamakainat9@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    # Greet the user
    wishMe()

    # Continuously listen for commands
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on the user's command
        if 'wikipedia' in query:
            # Search and speak about the topic from Wikipedia
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            # Open YouTube in the default web browser
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            # Open Google in the default web browser
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            # Open Stack Overflow in the default web browser
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            # Play the first music file in the specified directory
            music_dir = 'C:\\Users\\Mamai Nataki\\Desktop\\music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            # Speak the current time
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Imama, the time is {strTime}")

        elif 'open code' in query:
            # Open Visual Studio Code
            codePath = "C:\\Users\\Mamai Nataki\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to imama' in query:
            try:
                # Send an email to Imama
                speak("What should I say?")
                content = takeCommand()
                to = "imamakainat9@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend Imama dear, I am not able to send this email")
