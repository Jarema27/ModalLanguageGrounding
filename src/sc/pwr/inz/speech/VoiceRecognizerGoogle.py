import speech_recognition as sr

"""
This module serves purpose of converting speech to strings,which could be further used in agent's processes.

Todo:
    Make class out of it
    Test the shit out of it
"""

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

try:
    print("You said: " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
