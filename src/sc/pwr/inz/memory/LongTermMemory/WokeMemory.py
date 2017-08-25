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
        self.episode = 0

    def get_holon_by_formula(self, formula, episode):
        """
        Method checks if holon is in our memory,if it is and episode is valid (holon doesn't require update)
        it will return holon,otherwise it will update holon, otherwise it will create new holon for given formula and
        episode.
        :param formula : Formula, for which we want to find or create holon.
        :param episode: int, measure of time, used to specify which BPs and Observations we use
        :return    Holon, with freshly created tao
        """
        self.episode = episode
        for holon in self.holons:
            if holon.is_applicable(formula) and episode == holon.get_episode():
                return holon
            elif holon.is_applicable(formula):
                holon.update(self.get_distributed_knowledge(holon.get_formula(), episode, holon.get_episode()))
                return holon
        if formula.get_type() == TypeOfFormula.SF:
            dk = self.get_distributed_knowledge(formula, episode, self.point_of_no_return)
            new_holon = BinaryHolon(dk)
            self.holons.append(new_holon)
            return new_holon
        else:
            dk = self.get_distributed_knowledge(formula, episode, self.point_of_no_return)
            new_holon = NonBinaryHolon(dk)
            self.holons.append(new_holon)
            return new_holon

    def get_distributed_knowledge(self, formula, episode, point):
        """
        Builds DistributedKnowledge based on formula and two points in time,point which is minimal value in range
        we take into consideration and episode which is maximal value in mentioned range.
        :param formula:  Formula, around which we build DistributedKnowledge
        :param episode: Integer, maximal value in range of time
        :param point:   Integer, minimal value in range of time
        :return DistributedKnowledge
        """
        return DistributedKnowledge(formula, self.get_bp_with_episode(point, episode), episode)

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

    def get_episode(self):
        """
        Returns episode of WokeMemory which is last time it was used
        :return int: episode
        """
        return self.episode

    def update_em_all(self, episode):
        """
        Updates all stored holons based on new episode
        :param episode: int: episode used to determine moment of time we take into consideration
        """
        for h in self.holons:
            h.update(self.get_distributed_knowledge(h.get_formula(), episode, self.point_of_no_return))

    def get_bp_with_episode(self, point, episode):
        """
        Method collecting all bp which episodes are in range(point, episode)
        :param point: int: minimal value of time we take into consideration
        :param episode: int: maximal value of time we take into consideration
        :return list(BProfiles): BProfiles with episode in range (point, episode)
        """
        return list(x for x in self.bpcollective if episode >= int(x.get_episode()) >= point)

    def set_point_of_no_return(self, other):
        """
        Sets minimal value which we'll take into consideration when looking for BProfiles
        :param other: new value of point
        """
        self.point_of_no_return = other

    def deduce_possible_appearance(self, subject, state_uno, state_dos):
        """
        Given subject (identifier for now ), will try to deduce other identifier,which might appear under condition of
        subject being in state_uno and the other one being in state_dos. Method is equivalent of thought process of
        asking self 'Well I can see that USA is being overrun by commies, what else can be present in there?' We got
        subject of communism with state is,and we look for most probable outcome for another thing that might be, in
        case above, hunger or massive downfall of western civilization might be the case.
        :param subject : (Identifier) : Subject that state we know and want to find out what it might imply
        :param state_uno: (State) : State of given subject
        :param state_dos: (State) : State which we look for in the deduced subject
        :return: Most likely outcome ,might be better to include top 5 so agent appears to be smartass
        """
        out = 0
        indie = None
        for holon in self.holons:
            if subject in holon.get_formula().get_subjects():
                temp = holon.get_tao_for_state(state_uno, state_dos)
                if temp > out:
                    out = temp
                    indie = holon.get_formula().get_subjects().remove(subject)[0]
        return indie
