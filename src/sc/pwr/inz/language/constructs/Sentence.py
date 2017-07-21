from abc import ABC, abstractmethod
from enum import Enum


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
