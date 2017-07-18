from abc import ABC, abstractmethod
from enum import Enum


class Formula(ABC):

    @abstractmethod
    def get_traits(self):
        pass

    @abstractmethod
    def __init__(self, im, traits, states):
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


class TypeOfFormula(Enum):
    SF = 'Simple formula'
    CF = 'Complex Formula'
