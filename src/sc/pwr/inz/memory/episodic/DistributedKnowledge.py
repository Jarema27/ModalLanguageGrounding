from time import time


class DistributedKnowledge:

    def __init__(self, formula, bpset, timestamp=None):
        self.formula = formula
        self.bpset = bpset
        self.groundingsets = {}
        if timestamp is None:
            self.timestamp = int(time())
        else:
            self.timestamp = timestamp
        for bp in self.bpset:
            for trr in self.formula.get_traits():
                if trr in bp.give_all_traits_involved():
                    self.groundingsets[trr] = bp

    def get_formula(self):
        return self.formula

    def get_grounding_sets(self):
        return self.groundingsets

    def get_timestamp(self):
        return self.timestamp

    def get_bpset(self):
        return self.bpset

    def get_grounding_set(self, formula):
        if formula in self.groundingsets.keys():
            out = []
            for trait in formula.get_traits():
                if trait in self.groundingsets.keys():
                    out.append(trait)
            return out
        else:
            return []

    def get_complementary_formulas(self):
        return self.formula.get_complementary_formulas()
