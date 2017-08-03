from abc import ABC, abstractmethod
from enum import Enum

"""
Module containing superclass Sentence, subclasses are Imperative, Declarative, Interrogative and Exclamatory.
Based on english language.
"""


class Sentence(ABC):

    @abstractmethod
    def __init__(self, ):
        pass

    @abstractmethod
    def get_subject(self):
        pass

    @abstractmethod
    def get_kind(self):
        pass

"""
Enum showing us what kind of Sentence we deal with
"""


class SentenceType(Enum):
    #   Command, Order, Request
    Imp = 'Imperative'
    #   Statement
    Dec = 'Declarative'
    #   Asks a Question
    Int = 'Interrogative'
    #   Expresses a sudden emotion
    #   todo: implement emotions
    Exc = 'Exclamatory'
