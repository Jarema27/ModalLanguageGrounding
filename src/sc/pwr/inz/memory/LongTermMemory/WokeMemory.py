from src.sc.pwr.inz.memory.LongTermMemory.holons.NonBinaryHolon import NonBinaryHolon
from src.sc.pwr.inz.memory.ShortTermMemory.episodic.DistributedKnowledge import DistributedKnowledge
from src.sc.pwr.inz.memory.LongTermMemory.holons.BinaryHolon import BinaryHolon
from src.sc.pwr.inz.memory.LongTermMemory.semantic.language.components.Formula import TypeOfFormula

"""
Module representing memory of agent. It's woke memory,which means that agent is conscious of processes going in here.
"""


class WokeMemory:

    def __init__(self, holons=None, bpcollective=None, imodels=None):
        """
        :param holons (list(Holon)):List of holons which will be established as initial list ,used later in using memory.
            Might be none,in that case, default empty list will be created.
        :param bpcollective (list(BProfile)):list of BaseProfiles which will be used later. Might be none, in that case
            empty list will be provided, is used to create DistributedKnowledge and Holons later on.
        :param imodels (list(IndividualModel)):list of IndividualModels ,used later (I recall),if None, empty list will
            be provided

        """
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
        """
        Method checks if holon is in our memory,if it is and episode is valid (holon doesn't require update)
        it will return holon,otherwise it will update holon, otherwise it will create new holon for given formula and
        episode.
        :param formula : Formula, for which we want to find or create holon.
        :param timestamp: int, measure of time, used to specify which BPs and Observations we use
        :return    Holon, with freshly created tao
        """
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
        """
        Builds DistributedKnowledge based on formula and two points in time,point which is minimal value in range
        we take into consideration and episode which is maximal value in mentioned range.
        :param formula:  Formula, around which we build DistributedKnowledge
        :param timestamp: Integer, maximal value in range of time
        :param point:   Integer, minimal value in range of time
        :return DistributedKnowledge
        """
        return DistributedKnowledge(formula, self.get_bp_with_timestamp(point, timestamp), timestamp)

    def add_bp(self, bp):
        """
        Adds BaseProfile to collection of base profiles
        :param bp: BaseProfile, which we want to add
        """
        self.bpcollective.append(bp)

    def get_holons(self):
        """
        Returns list of Holons from memory
        :return list(Holon): list of Holons stored in memory
        """
        return self.holons

    def get_bpcollective(self):
        """
        Returns list of base profiles
        :return list(BaseProfile): list of base profiles stored in memory
        """
        return self.bpcollective

    def get_indivmodels(self):
        """
        Returns list of individual models
        :return list(IndividualModel): list of individual models stored in memory
        """
        return self.indiv

    def get_timestamp(self):
        """
        Returns episode of WokeMemory which is last time it was used
        :return int: episode
        """
        return self.timestamp

    def update_em_all(self, timestamp):
        """
        Updates all stored holons based on new episode
        :param timestamp: int: episode used to determine moment of time we take into consideration
        """
        for h in self.holons:
            h.update(self.get_distributed_knowledge(h.get_formula(), timestamp, self.point_of_no_return))

    def get_bp_with_timestamp(self, point, timestamp):
        """
        Method collecting all bp which timestamps are in range(point, episode)
        :param point: int: minimal value of time we take into consideration
        :param timestamp: int: maximal value of time we take into consideration
        :return list(BProfiles): BProfiles with episode in range (point, episode)
        """
        return list(x for x in self.bpcollective if timestamp >= int(x.get_timestamp()) >= point)

    def set_point_of_no_return(self, other):
        """
        Sets minimal value which we'll take into consideration when looking for BProfiles
        :param other: new value of point
        """
        self.point_of_no_return = other
