from src.sc.pwr.inz.memory.LongTermMemory.semantic.language.components.Formula import Formula, TypeOfFormula
from src.sc.pwr.inz.memory.LongTermMemory.semantic.language.components.State import State

from src.sc.pwr.inz.memory.LongTermMemory.semantic.language.components.Trait import Trait

"""
    Module representing Simple Formula ,which is widely present in natural speech. Simple formula contains one trait and
     state of this trait, example : 'Is this plant blue?'
"""


class SimpleFormula(Formula):

    def get_states(self):
        """
        :return list(State) : one member list of State used in formula
        """
        return [self.state]

    def get_model(self):
        """
        :return (IndividualModel): returns IM used to build this Formula
        """
        return self.indiv_model

    def get_type(self):
        """
        :return (TypeOfFormula.SF): Returns Type of Formula,Simple one in this case
        """
        return TypeOfFormula.SF

    def get_complementary_formulas(self):
        """
        Complementary formulas are all formulas which could be acquired from given set of IM and traits
        :return list(Formula): list of two formulas,mind the order.
        """
        temp1 = SimpleFormula(self.indiv_model, self.trait, State.IS)
        temp2 = SimpleFormula(self.indiv_model, self.trait, State.IS_NOT)
        return [temp1, temp2]

    def __eq__(self, other):
        return self.state == other.state and self.indiv_model == other.indiv_model and self.trait == other.trait

    def __init__(self, im, trait, state, tense=None):
        if not isinstance(trait, Trait):
            raise TypeError("Given trait ain't instance of Trait")
        if im is not None and trait is not None:
            if trait in im.get_object_type().get_traits():
                self.indiv_model = im
                self.tense = tense
                self.trait = trait
                if state is None:
                    self.state = State.IS_NOT
                else:
                    self.state = state
        else:
            raise Exception("Obligatory fields include variables with None value")

    def get_traits(self):
        """
        :return list(Trait): One member list of Trait
        """
        return [self.trait]

    def __hash__(self):
        return hash(self.indiv_model) ^ hash(self.trait)
