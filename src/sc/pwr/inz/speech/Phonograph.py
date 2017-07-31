import pyttsx3


class Phonograph:

    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.runAndWait()

    def read_something_up(self, string):
        self.engine.say(string)
        self.engine.runAndWait()

Phonograph()
