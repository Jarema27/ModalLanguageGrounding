from abc import ABC, abstractmethod
from enum import Enum

"""
Superclass of Formula. Represents formula present in natural language.
"""


class Formula(ABC):

    @abstractmethod
    def get_traits(self):
        pass

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_model(self):
        pass

    @abstractmethod
    def get_type(self):
        pass

    @abstractmethod
    def get_states(self):
        pass

    @abstractmethod
    def get_complementary_formulas(self):
        pass

    @abstractmethod
    def __eq__(self, other):
        pass

"""
Enum made in order to distinguish types of formulas from each other
"""


class TypeOfFormula(Enum):
    SF = 'Simple formula'
    CF = 'Complex Formula'
