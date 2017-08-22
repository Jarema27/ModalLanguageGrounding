"""
Don't want to destroy ComplexFormula,which was done exclusively for two traits sentences ,which after some time seems to
be overly precise thing to do,this class will focus on two Object Types/Individual Models questions, this time will
attempt to make it more flexible for future usage.
"""
from src.sc.pwr.inz.memory.LongTermMemory.semantic.language.components.State import State
from src.sc.pwr.inz.memory.LongTermMemory.semantic.language.components.Formula import Formula, TypeOfFormula


class ComplexFormulaOT(Formula):

    def get_traits(self):
        pass

    def get_model(self):
        pass

    def __init__(self, subjects, states, lo, tense=None):
        """
        :param subjects list(IndividualModel): or list(Object Type): as subjects
        :param states list(State):  list of two states,in order in which we want to form formula
        :param log (LogicalOperator): LO used to connect two parts of Formula
        :param tense:
        """
        if not all(isinstance(elem, State) for elem in states):
            raise TypeError("Given states aren't instance of State List")
        if subjects is not None and lo is not None:
            self.subjects = subjects
            self.state = states
            self.LO = lo
            self.tense = tense
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

    def get_subjects(self):
        """
        :return (IndividualModel): IM used to form formula
        """
        return self.subjects

    def get_tense(self):
        """
        :return (Tense): Tense in which the formula has been created
        """
        return self.tense

    def get_complementary_formulas(self):
        """
        Complementary formulas are all formulas which could be acquired from given set of IM,traits and Logical operator
        :return list(Formula): mind the order
        """
        return [ComplexFormulaOT(self.subjects, [State.IS, State.IS], self.LO, self.tense),
                ComplexFormulaOT(self.subjects, [State.IS, State.IS_NOT], self.LO, self.tense),
                ComplexFormulaOT(self.subjects, [State.IS_NOT, State.IS], self.LO), self.tense,
                ComplexFormulaOT(self.subjects, [State.IS_NOT, State.IS_NOT], self.LO, self.tense)]

    @staticmethod
    def get_type():
        """
        :return (TypeOfFormula): Returns type of formula, Complex Formula at this point.
        """
        return TypeOfFormula.OT

    def __eq__(self, other):
        return self.get_states() == other.get_states() and self.get_logical_operator() == other.get_logical_operator() \
            and self.get_subjects() == other.get_subjects() and self.get_tense() == other.get_tense()

    def __hash__(self):
        return hash(self.state[0]) * sum(list((hash(x) for x in self.subjects)))
