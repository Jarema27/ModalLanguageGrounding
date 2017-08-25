import speech_recognition as sr

from src.sc.pwr.inz.memory.LongTermMemory.semantic.language.constructs.Interrogative import Interrogative


class VoiceRecognizerGoogle:

    @staticmethod
    def listen():
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

        Interrogative(r.recognize_google(audio)).ask()
#   VoiceRecognizerGoogle.listen()
