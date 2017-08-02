from src.sc.pwr.inz.language.components.Formula import Formula, TypeOfFormula
from src.sc.pwr.inz.language.components.State import State

from src.sc.pwr.inz.language.components.Trait import Trait

"""
    Module representing Complex Formula ,which is widely present in natural speech. Complex Formula contains two traits
    and two states of those traits, example : 'Is this life pointless or is it pointful ?'
"""


class ComplexFormula(Formula):

    def __init__(self, im, traits, states, log):
        """
        :param im (IndividualModel): IM which is subject of out formula
        :param traits list(Trait): list of two traits, in order in which we want to form formula
        :param states list(State):  list of two states,in order in which we want to form formula
        :param log (LogicalOperator): LO used to connect two parts of Formula
        """
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
        """
        :return list(State): list of states of formula
        """
        return self.state

    def get_logical_operator(self):
        """
        :return (LogicalOperator): used to form the formula
        """
        return self.LO

    def get_model(self):
        """
        :return (IndividualModel): IM used to form formula
        """
        return self.indiv_model

    def get_complementary_formulas(self):
        """
        Complementary formulas are all formulas which could be acquired from given set of IM,traits and Logical operator
        :return list(Formula): mind the order
        """
        return [ComplexFormula(self.indiv_model, self.traits, [State.IS, State.IS], self.LO),
                ComplexFormula(self.indiv_model, self.traits, [State.IS, State.IS_NOT], self.LO),
                ComplexFormula(self.indiv_model, self.traits, [State.IS_NOT, State.IS], self.LO),
                ComplexFormula(self.indiv_model, self.traits, [State.IS_NOT, State.IS_NOT], self.LO)]

    def get_type(self):
        """
        :return (TypeOfFormula): Returns type of formula, Complex Formula at this point.
        """
        return TypeOfFormula.CF

    def get_traits(self):
        """
        :return list(traits): List of traits used to form formula
        """
        return self.traits

    def __eq__(self, other):
        return self.indiv_model == other.get_model() and((self.traits[0], self.state[0]) == (other.traits[0],
                                                                                             other.state[0]) and
                                                         self.traits[1], self.state[1]) == (other.traits[1],
                                                                                            other.state[1])

    def __hash__(self):
        return hash(self.indiv_model) * sum(list((hash(x) for x in self.traits)))