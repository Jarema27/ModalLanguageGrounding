from src.sc.pwr.inz.memory.LongTermMemory.holons.Grounder import Grounder
from src.sc.pwr.inz.memory.LongTermMemory.semantic.language.components.Formula import TypeOfFormula
from src.sc.pwr.inz.memory.LongTermMemory.semantic.language.components.State import State
from src.sc.pwr.inz.memory.LongTermMemory.holons.Holon import Holon, HolonKind

"""
Holon, specific case of dealing with SimpleFormula
"""


class BinaryHolon(Holon):

    def get_episode(self):
        """
        :return int: episode
        """
        return self.episode

    def __init__(self, dk, context=None):
        """
        :param dk (DistributedKnowledge) : Nicely packed data which is needed to properly establish holon.
        """
        super().__init__()
        self.formula = dk.get_formula()
        self.episode = dk.get_episode()
        self.dk = dk
        self.context = context
        self.tao = [0, 0]
        self.update(dk)

    def update(self, dk):
        """
        To be accurate ,holon needs to be updated with valid data
        :param  dk :(DistributedKnowledge) : Nicely packed data which is needed to properly establish holon.
        """
        self.episode = dk.get_episode()
        self.dk = dk
        if dk.get_formula().get_type() is not TypeOfFormula.SF:
            raise TypeError("Wrong type of formula has been provided, I only take simple ones")
        else:
            self.tao[0] += Grounder.determine_fulfilment(self.dk, self.dk.get_complementary_formulas()[0], self.context)
            self.tao[1] += Grounder.determine_fulfilment(self.dk, self.dk.get_complementary_formulas()[1], self.context)
            suma = sum(self.tao)
            if suma > 0:
                self.tao = [self.tao[0]/suma, self.tao[1]/suma]

    def get_tao_for_state(self, state1, state2=None):
        """
        :param state1: State : which we want to know,either IS or IS_NOT
        :param state2: State : Not used here
        :return int: Returns value of tao for given state
        """
        dicdic = {State.IS: 0, State.IS_NOT: 1}
        return self.tao[dicdic.get(state1)]

    def get_kind(self):
        """
        :return HolonKind:  Returns information that it's Binary Holon
        """
        return HolonKind.BH

    def get_formula(self):
        """
        :return Formula: formula of this holon
        """
        return self.formula

    def get_complementary_formulas(self):
        """
        For more info goto Formula
        :return list(Formula) Complementary Formulas
        """
        return self.formula.get_complementary_formulas()

    def get_tao(self):
        """
        :return list(int): Two element list containing two sides of tao
        """
        return self.tao

    def get_context(self):
        """
        :return (UberContext):
        """
        return self.context

    def is_applicable(self, formula):
        """
        :param formula: Formula : which we want to check if can be applied to this specific Holon
        :return Boolean: Depending if formula is applicable or not
        """
        if formula.get_type() is TypeOfFormula.SF:
            return formula in self.formula.get_complementary_formulas()
        else:
            return False

    def __eq__(self, other):
        return self.formula == other.formula and self.episode == other.get_episode and self.dk == other.dk