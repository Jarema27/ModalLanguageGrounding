from src.sc.pwr.inz.memory.holons.Holon import Holon, HolonKind
from src.sc.pwr.inz.language.Formula import TypeOfFormula
from src.sc.pwr.inz.language.Grounder import Grounder


class BinaryHolon(Holon):

    def __init__(self, dk):
        super().__init__()
        self.formula = dk.get_formula()
        self.timestamp = dk.get_timestamp()
        self.dk = dk
        self.tao = ()
        self.update(dk)

    def update(self, dk):
        if dk.get_formula().get_type() is not TypeOfFormula.SF:
            raise TypeError("Wrong type of formula has been provided, I only take simple ones")
        else:
            pos = Grounder.determine_fulfilment(dk, dk.get_complementary_formulas[0])
            neg = Grounder.determine_fulfilment(dk, dk.get_complementary_formulas[1])
            self.tao = (pos, neg)

    def get_kind(self):
        return HolonKind.BH

    def get_formula(self):
        return self.formula

    def get_complementary_formulas(self):
        return self.formula.get_complementary_formulas()

    def get_tao(self):
        return self.tao

    def is_applicable(self, formula):
        return formula in self.formula.get_complementary_formulas()

"""else:
            pos = Grounder.determine_fulfilment(dk, dk.get_complementary_formulas[0])
            neg = Grounder.determine_fulfilment(dk, dk.get_complementary_formulas[1])
            self.tao = (pos, neg)"""