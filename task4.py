import speech_recognition as sr
import pyttsx3
import datetime

# Initialize the recognizer and engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen to user commands
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)
        command = ""

        try:
            command = recognizer.recognize_google(audio)
            print(f"User said: {command}")
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand what you said.")
        except sr.RequestError:
            print("I'm sorry, but I couldn't request results.")

        return command

# Function to execute commands
def execute_command(command):
    if "what's the time" in command:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The current time is {current_time}")
    elif "hello" in command:
        speak("Hello! How can I help you today?")
    elif "what is your name?" in command:
        speak("my name is siri.")
    elif "what is the weather today" in command:
        speak("today's weather is too cold.")
    else:
        speak("I'm sorry, I don't understand that command.")

# Main loop to continuously listen and respond
while True:
    command = listen().lower()
    execute_command(command)
