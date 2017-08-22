"""
Module which reflects idea of time. As human being you can probably put yourself in flow of time, recognizing at least 3
territories of time - Past (Things which for current ego already happened), Present (Concept of 'now' which is actually
not too easy to explain) , Future (Things that might or will happen in future)
"""
from enum import Enum


class Tense(Enum):
    PAST = 'Past'
    PRESENT = 'Present'
    FUTURE = 'Future'
