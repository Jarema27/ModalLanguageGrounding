from src.sc.pwr.inz.memory.holons.Holon import Holon, HolonKind
from src.sc.pwr.inz.language.Formula import TypeOfFormula
from src.sc.pwr.inz.language.Grounder import Grounder
from src.sc.pwr.inz.language.State import State


class BinaryHolon(Holon):

    def __init__(self, dk):
        super().__init__()
        self.formula = dk.get_formula()
        self.timestamp = dk.get_timestamp()
        self.dk = dk
        self.tao = ()
        self.update(dk)

    def update(self, dk):
        if dk.get_formula.get_type() is not TypeOfFormula.SF:
            raise TypeError("Wrong type of formula has been provided, I only take simple ones")
        else:
            if dk.get_complementary_formulas[0].get_states == State.IS:
                self.tao = (Grounder.determine_fullfilment(dk, dk.get_complementary_formulas[0]),
                            Grounder.determine_fullfilment(dk, dk.get_complementary_formulas[1]))
            else:
                self.tao = (Grounder.determine_fullfilment(dk, dk.get_complementary_formulas[1]),
                            Grounder.determine_fullfilment(dk, dk.get_complementary_formulas[0]))

    def get_kind(self):
        return HolonKind.BH

    def get_formula(self):
        pass

    def get_complementary_formulas(self):
        pass

    def get_tao(self):
        pass

    def get_context(self):
        pass

    def is_applicable(self, formula):
        pass

