from time import time

from src.sc.pwr.inz.memory.holons.NonBinaryHolon import NonBinaryHolon
from src.sc.pwr.inz.memory.episodic.DistributedKnowledge import DistributedKnowledge
from src.sc.pwr.inz.memory.holons.BinaryHolon import BinaryHolon
from src.sc.pwr.inz.language.components.Formula import TypeOfFormula


class WokeMemory:

    def __init__(self, holons, bpcollective, individuals):
        self.holons = holons
        self.bpcollective = bpcollective
        self.individuals = individuals

    def get_holon_by_formula(self, formula):
        for holon in self.holons:
            if holon.is_applicable(formula):
                return holon
        if formula.get_type == TypeOfFormula.SF:
            dk = self.get_distributed_knowledge(self.formula)
            new_holon = BinaryHolon(dk)
            self.holons.append(new_holon)
            return new_holon
        else:
            dk = self.get_distributed_knowledge(self.formula)
            new_holon = NonBinaryHolon(dk)
            self.holons.append(new_holon)
            return new_holon

    def get_distributed_knowledge(self, formula):
        return DistributedKnowledge(formula, self.bpcollective, time.now())

    def add_bp(self, bp):
        self.bpcollective.append(bp)

    def add_individual(self, im):
        self.individuals.append(im)
