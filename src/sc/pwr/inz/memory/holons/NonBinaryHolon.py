from sc.pwr.inz.language.components.Formula import TypeOfFormula
from src.sc.pwr.inz.memory.episodic.Grounder import Grounder
from src.sc.pwr.inz.memory.holons.Holon import HolonKind, Holon


class NonBinaryHolon(Holon):

    def __init__(self, dk):
        super().__init__()
        self.formula = dk.get_formula()
        self.timestamp = dk.get_timestamp()
        self.dk = dk
        self.tao = [0, 0, 0, 0]
        self.update(dk)

    def get_complementary_formulas(self):
        return self.formula.get_complementary_formulas()

    def update(self, dk):
        if dk.get_formula().get_type() is not TypeOfFormula.CF:
            raise TypeError("Wrong type of formula has been provided, I only take simple ones")
        else:
            self.tao[0] += Grounder.determine_fulfilment_cf(self.dk, self.dk.get_complementary_formulas()[0])
            self.tao[1] += Grounder.determine_fulfilment_cf(self.dk, self.dk.get_complementary_formulas()[1])
            self.tao[2] += Grounder.determine_fulfilment_cf(self.dk, self.dk.get_complementary_formulas()[2])
            self.tao[3] += Grounder.determine_fulfilment_cf(self.dk, self.dk.get_complementary_formulas()[3])
            suma = sum(self.tao)
            if suma > 0:
                self.tao = [self.tao[0]/suma, self.tao[1]/suma, self.tao[2]/suma, self.tao[3]/suma]

    def get_kind(self):
        return HolonKind.NBH

    def get_tao(self):
        return self.tao

    def is_applicable(self, formula):
        return formula in self.formula.get_complementary_formulas()

    def get_formula(self):
        return self.formula
