from src.sc.pwr.inz.language.Trait import Trait
from src.sc.pwr.inz.language.Formula import Formula, TypeOfFormula
from src.sc.pwr.inz.language.State import State


class ComplexFormula(Formula):

    def __init__(self, im, traits, states,log):
        if not all(isinstance(elem, Trait) for elem in traits):
            raise TypeError("Given traits aren't instance of Trait List")
        if not all(isinstance(elem, State) for elem in states):
            raise TypeError("Given states aren't instance of State List")
        if im is not None and traits is not None and states is not None:
            if all(elem in im.get_object_type().get_traits() for elem in traits):
                self.indiv_model = im
                self.traits = traits
                self.state = states
                self.LO = log
        else:
            raise Exception("Obligatory fields include variables with None value")

    def get_states(self):
        return self.state

    def get_logical_operator(self):
        return self.LO

    def get_model(self):
        return self.indiv_model

    def get_complementary_formulas(self):
        return [ComplexFormula(self.indiv_model, self.traits, [State.IS, State.IS], self.LO),
                ComplexFormula(self.indiv_model, self.traits, [State.IS, State.IS_NOT], self.LO),
                ComplexFormula(self.indiv_model, self.traits, [State.IS_NOT, State.IS], self.LO),
                ComplexFormula(self.indiv_model, self.traits, [State.IS_NOT, State.IS_NOT], self.LO)]

    def get_type(self):
        return TypeOfFormula.CF

    def get_traits(self):
        return self.traits

    def __eq__(self, other):
        return self.indiv_model == other.get_model() and((self.traits[0], self.state[0]) == (other.traits[0],
                                                                                             other.state[0]) and
                                                         self.traits[1], self.state[1]) == (other.traits[1],
                                                                                            other.state[1])

    def __hash__(self):
        return hash(self.indiv_model) * sum(list((hash(x) for x in self.traits)))
