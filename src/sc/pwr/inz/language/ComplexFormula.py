from sc.pwr.inz.language.Trait import Trait
from src.sc.pwr.inz.language.Formula import Formula, TypeOfFormula
from src.sc.pwr.inz.language.State import State


class ComplexFormula(Formula):

    def __init__(self, im, traits, states):
        if not isinstance(traits, [Trait]):
            raise TypeError("Given traits aren't instance of Trait List")
        if not isinstance(states,[State]):
            raise TypeError("Given states aren't instance of State List")
        if im is not None and traits is not None and states is not None:
            if traits in im.get_object_type().get_traits():
                self.indiv_model = im
                self.traits = traits
                self.state = states
        else:
            raise Exception("Obligatory fields include variables with None value")

    def get_states(self):
        return self.state

    def get_model(self):
        return self.indiv_model

    def get_complementary_formulas(self):
        """"todo"""

    def get_type(self):
        return TypeOfFormula.CF

    def get_traits(self):
        return self.traits

    def __eq__(self, other):
        pass
