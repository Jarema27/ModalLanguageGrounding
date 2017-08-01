import pyttsx3

"""
This module serves a purpose of converting strings to sound.
"""


class Phonograph:

    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.runAndWait()

    def read_something_up(self, string):
        """
        Method called whenever you want something converted to sound.
        Mind that pyttsx3 library provides really fast speaker.
        Args:
            :param string: string which will be spoken
        """

        self.engine.say(string)
        self.engine.runAndWait()

Phonograph()
