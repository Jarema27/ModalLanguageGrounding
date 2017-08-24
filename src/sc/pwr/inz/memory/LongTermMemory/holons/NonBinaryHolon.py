from src.sc.pwr.inz.memory.LongTermMemory.holons.Grounder import Grounder
from src.sc.pwr.inz.memory.LongTermMemory.semantic.language.components.Formula import TypeOfFormula
from src.sc.pwr.inz.memory.LongTermMemory.semantic.language.components.State import State
from src.sc.pwr.inz.memory.LongTermMemory.holons.Holon import HolonKind, Holon

"""
Holon, specific case of dealing with ComplexFormula
"""


class NonBinaryHolon(Holon):

    def get_timestamp(self):
        """
        :return int: timestamp
        """
        return self.timestamp

    def __init__(self, dk=None, context=None):
        """
        :param dk (DistributedKnowledge) : Nicely packed data which is needed to properly establish holon.
        """
        super().__init__()
        self.formula = dk.get_formula()
        self.timestamp = dk.get_timestamp()
        self.dk = dk
        self.context = context
        self.suma = 0
        self.tao = [0, 0, 0, 0]
        self.update(dk)

    def get_complementary_formulas(self):
        """
        For more info goto Formula
        :return list(Formula) Complementary Formulas
        """
        return self.formula.get_complementary_formulas()

    def update(self, dk):
        """
        To be accurate ,holon needs to be updated with valid data
        :param  dk :(DistributedKnowledge) : Nicely packed data which is needed to properly establish holon.
        """
        self.timestamp = dk.get_timestamp()
        self.dk = dk
        if dk.get_formula().get_type() is not TypeOfFormula.CF:
            if dk.get_formula().get_type() is TypeOfFormula.OT:
                self.tao[0] += Grounder.determine_fulfilment_ident(self.dk, self.dk.get_complementary_formulas()[0],
                                                                   self.context)
                self.tao[1] += Grounder.determine_fulfilment_ident(self.dk, self.dk.get_complementary_formulas()[1],
                                                                   self.context)
                self.tao[2] += Grounder.determine_fulfilment_ident(self.dk, self.dk.get_complementary_formulas()[2],
                                                                   self.context)
                self.tao[3] += Grounder.determine_fulfilment_ident(self.dk, self.dk.get_complementary_formulas()[3],
                                                                   self.context)
                self.suma = sum(self.tao)
                if self.suma > 0:
                    self.tao = [self.tao[0]/self.suma, self.tao[1]/self.suma, self.tao[2]/self.suma,
                                self.tao[3]/self.suma]
            else:
                raise TypeError("Wrong type of formula has been provided, I only take complex ones")
        else:
            self.tao[0] += Grounder.determine_fulfilment_cf(self.dk, self.dk.get_complementary_formulas()[0],
                                                            self.context)
            self.tao[1] += Grounder.determine_fulfilment_cf(self.dk, self.dk.get_complementary_formulas()[1],
                                                            self.context)
            self.tao[2] += Grounder.determine_fulfilment_cf(self.dk, self.dk.get_complementary_formulas()[2],
                                                            self.context)
            self.tao[3] += Grounder.determine_fulfilment_cf(self.dk, self.dk.get_complementary_formulas()[3],
                                                            self.context)
            self.suma = sum(self.tao)
            if self.suma > 0:
                self.tao = [self.tao[0]/self.suma, self.tao[1]/self.suma, self.tao[2]/self.suma, self.tao[3]/self.suma]

    def get_tao_for_state(self, state1, state2=None):
        """
        :param state1: State : which we want to know,either IS or IS_NOT
        :param state2: State : which we want to know,either IS or IS_NOT
        :return int: Returns value of tao for given state
        """
        dicdic = {(State.IS, State.IS): 0, (State.IS, State.IS_NOT): 1, (State.IS_NOT, State.IS): 2,
                  (State.IS_NOT, State.IS_NOT): 3}
        return self.tao[dicdic.get((state1, state2))]

    def get_kind(self):
        """
        :return HolonKind:  Returns information that it's Binary Holon
        """
        return HolonKind.NBH

    def get_tao(self):
        """
        :return list(int): Four element list containing four sides of tao
        """
        return self.tao

    def is_applicable(self, formula):
        """
        :param formula: Formula : which we want to check if can be applied to this specific Holon
        :return Boolean: Depending if formula is applicable or not
        """
        return formula in self.formula.get_complementary_formulas()

    def get_formula(self):
        """
        :return Formula: formula of this holon
        """
        return self.formula

    def __eq__(self, other):
        return self.formula == other.formula and self.timestamp == other.timestamp and self.dk == other.dk
