from time import time

from src.sc.pwr.inz.memory.LongTermMemory.semantic.language.components.Formula import TypeOfFormula

"""
Distributed knowledge is approximately what "a wise man knows" or what someone who has complete knowledge of what each 
member of the community knows knows. For now DK focuses on own observations.
Distributed Knowledge module serves us to create Holon's later on, it contains formula, list of BProfiles and episode
"""


class DistributedKnowledge:

    def __init__(self, formula, bpset, episode=None):
        """
        formula and BProfile list are mandatory, episode will be current time if not set manually
        :param formula (Formula): Formula of this Distributed Knowledge
        :param bpset list(BaseProfile): List containing all BProfiles later used to establish tao in Holon
        :param episode (int): episode serves us to connect DK with a moment in time
        """
        self.formula = formula
        self.bpset = bpset
        self.groundingsets = {}
        if episode is None:
            self.episode = int(time())
        else:
            self.episode = episode
        if formula.get_type() == TypeOfFormula.OT:
            for bp in self.bpset:
                for sub in formula.get_subjects():
                    if sub in bp.give_subjects_involved():
                        self.groundingsets[sub] = bp
        else:
            for bp in self.bpset:
                for trr in self.formula.get_traits():
                    if trr in bp.give_all_traits_involved():
                        self.groundingsets[trr] = bp

    def get_formula(self):
        """
        :return Formula: formula of this DK
        """
        return self.formula

    def get_grounding_sets(self):
        """
        :return dict{Trait:BaseProfile}
        """
        return self.groundingsets

    def get_episode(self):
        """
        :return int: episode
        """
        return self.episode

    def get_bpset(self):
        """
        :return list(BaseProfile)
        """
        return self.bpset

    def get_grounding_set(self, formula):
        """
        :param formula: Formula which grounding sets we wish to get
        :return list(BaseProfile): List of BP which include given formula
        """
        if formula in self.groundingsets.keys():
            out = []
            for trait in formula.get_traits():
                if trait in self.groundingsets.keys():
                    out.append(trait)
            return out
        else:
            return []

    def get_complementary_formulas(self):
        """
        Gives set of complementary formulas, for full explanation visit Formula
        :return list(Formula)
        """
        return self.formula.get_complementary_formulas()

    def __eq__(self, other):
        return self.formula == other.formula and self.groundingsets == other.groundingsets and \
               self.episode == other.episode
