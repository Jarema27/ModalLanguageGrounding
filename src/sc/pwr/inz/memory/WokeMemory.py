from src.sc.pwr.inz.memory.holons.NonBinaryHolon import NonBinaryHolon
from src.sc.pwr.inz.memory.episodic.DistributedKnowledge import DistributedKnowledge
from src.sc.pwr.inz.memory.holons.BinaryHolon import BinaryHolon
from src.sc.pwr.inz.language.components.Formula import TypeOfFormula


class WokeMemory:

    def __init__(self, holons=None, bpcollective=None, imodels=None):
        if holons is None:
            self.holons = []
        else:
            self.holons = holons
        if bpcollective is None:
            self.bpcollective = []
        else:
            self.bpcollective = bpcollective
        if imodels is None:
            self.indiv = []
        else:
            self.indiv = imodels
        self.point_of_no_return = 0
        self.timestamp = 0

    def get_holon_by_formula(self, formula, timestamp):
        self.timestamp = timestamp
        for holon in self.holons:
            if holon.is_applicable(formula) and timestamp == holon.get_timestamp():
                return holon
            elif holon.is_applicable(formula):
                holon.update(self.get_distributed_knowledge(holon.get_formula(), timestamp, holon.get_timestamp()))
                return holon
        if formula.get_type() == TypeOfFormula.SF:
            dk = self.get_distributed_knowledge(formula, timestamp, self.point_of_no_return)
            new_holon = BinaryHolon(dk)
            self.holons.append(new_holon)
            return new_holon
        else:
            dk = self.get_distributed_knowledge(formula, timestamp, self.point_of_no_return)
            new_holon = NonBinaryHolon(dk)
            self.holons.append(new_holon)
            return new_holon

    def get_distributed_knowledge(self, formula, timestamp, point):
        return DistributedKnowledge(formula, self.get_bp_with_timestamp(point, timestamp), timestamp)

    def add_bp(self, bp):
        self.bpcollective.append(bp)

    def get_holons(self):
        return self.holons

    def get_bpcollective(self):
        return self.bpcollective

    def get_indivmodels(self):
        return self.indiv

    def get_timestamp(self):
        return self.timestamp

    def update_em_all(self, timestamp):
        for h in self.holons:
            h.update(self.get_distributed_knowledge(h.get_formula(), timestamp, self.point_of_no_return))

    def get_bp_with_timestamp(self, point, timestamp):
        return list(x for x in self.bpcollective if timestamp >= int(x.get_timestamp()) >= point)

    def set_point_of_no_return(self, other):
        self.point_of_no_return = other
