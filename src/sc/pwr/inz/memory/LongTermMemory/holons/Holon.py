from abc import abstractmethod, ABC
from enum import Enum

"""
Holon is mind representation of some knowledge. For centuries we learned how to transform simple Observations into 
amazing mind creations called Holons. Holons contain knowledge about Formula, a.e Orange is orange. In time with every
observation belief in the fact that Orange is orange is strengthened , until we see red orange. When we do,we update our
belief, we don't start to believe that oranges are red, but we do know that not all oranges are orange,that bit of 
uncertainty will remain in our minds forever. That's exactly what makes us human. Holon is represented by Tao.
https://upload.wikimedia.org/wikipedia/commons/thumb/b/b1/Tao_symbol.svg/463px-Tao_symbol.svg.png

Tao is used for two main reasons. First is that it's accurate representation of idea that each formula we can think of
might be fulfilled or not ,which is nicely presented in such metaphor.
Secondly 'It pleases chinks' , I believe Chinese people like to imagine that people more coherent than
third wave hippies are interested in their culture.
"""


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
    def get_episode(self):
        pass


class HolonKind(Enum):
    """
    Enum showing us weather we deal with Binary or NonBinaryHolon
    """
    BH = 'BinaryHolon'
    NBH = 'NonBinaryHolon'
