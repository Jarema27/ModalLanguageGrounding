from abc import abstractmethod, ABC
from enum import Enum


class Holon(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_tao(self):
        pass

    @abstractmethod
    def get_complementary_formulas(self):
        pass

    @abstractmethod
    def is_applicable(self, formula):
        pass

    @abstractmethod
    def update(self, dk):
        pass

    @abstractmethod
    def get_tao_for_state(self, state1, state2=None):
        pass

    @abstractmethod
    def get_kind(self):
        pass

    @abstractmethod
    def get_formula(self):
        pass

    @abstractmethod
    def get_timestamp(self):
        pass


class HolonKind(Enum):
    BH = 'BinaryHolon'
    NBH = 'NonBinaryHolon'
