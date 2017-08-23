from time import time

from src.sc.pwr.inz.memory.LongTermMemory.semantic.language.components.State import State

"""
Base Profile represents a point in time, single frame in time ,containing observations.
Photo is good metaphor of Base Profile ,let's take
https://funalive.com/uploads/files/article/images/funny-interesting-pictures_24sep16-4.jpg
Observations - Shark is close to human, human is calm, human has black suit, human's feet are funny
Base Profile contains all of those observations, the most important fact is the time they share.
"""


class BaseProfile:

    def __init__(self, timestamp=None, observations=None):
        """
        Initial method, creates dictionaries for observations depending on states it contains and trait it involves.
        :param timestamp (int): Value describing time, might or might not be provided, if not, system time will be set
        :param observations list(observations):list of observations associated with this specific BP, might be None,
            if so, default empty list shall be provided.
        """
        if timestamp is None:
            self.timestamp = time()
        else:
            self.timestamp = timestamp
        if observations is None:
            self.observations = []
            self.observationsIS = {}
            self.observationsIS_NOT = {}
            self.observationsMAYHAPS = {}
        else:
            self.observations = observations
            self.observationsIS = {}
            self.observationsIS_NOT = {}
            self.observationsMAYHAPS = {}
            self.get_em_observations(self.observations)

    def get_em_observations(self, observations):
        """
        Method used to split observations into proper dictionaries
        :param observations: list(Observation): list of observations we desire to split
        """
        for obs in observations:
            for tupl in obs.get_observed():
                if tupl[1] == State.IS:
                    self.observationsIS[tupl[0]] = obs
                elif tupl[1] == State.IS_NOT:
                    self.observationsIS_NOT[tupl[0]] = obs
                else:
                    self.observationsMAYHAPS[tupl[0]] = obs

    def get_observations_is(self):
        """
        :return dict(Trait:Observation): Dictionary of Observations with State IS
        """
        return self.observationsIS

    def get_observations_is_not(self):
        """
        :return dict(Trait:Observation): Dictionary of Observations with State IS_NOT
        """
        return self.observationsIS_NOT

    def get_observations_mayhaps(self):
        """
        :return dict(Trait:Observation): Dictionary of Observations with State MAYHAPS
        """
        return self.observationsMAYHAPS

    def get_timestamp(self):
        """
        :return int : timestamp
        """
        return self.timestamp

    def add_observations_is(self, o):
        """
        Add observation which state is both known and is IS
        :param o: Observation : itself
        """
        self.get_em_observations(o)
        self.observations.append(o)

    def add_observations_is_not(self, o):
        """
        Add observation which state is both known and is IS_NOT
        :param o: Observation : itself
        """
        self.get_em_observations(o)
        self.observations.append(o)

    def add_observations_mayhaps(self, o):
        """
        Add observation which state is both known and is MAYHAPS
        :param o: Observation : itself
        """
        self.get_em_observations(o)
        self.observations.append(o)

    def get_observed_ims(self):
        """
        Method giving all IMs which appeared in observations
        :return list(IndividualModel)
        """
        return list(set([x.identifier for x in self.observations]))

    def check_if_observed(self, im, trait, state):
            """
            Method indicates if individual model had trait in such state
            :param im: IndividualModel
            :param trait: Trait
            :param state: State
            :return Boolean : depending weather such im had given trait in given state
            """
            if state == State.IS:
                if trait in self.observationsIS.keys():
                    if self.observationsIS.get(trait).get_identifier() == im:
                        return True
                return False
            elif state == State.IS_NOT:
                if trait in self.observationsIS_NOT.keys():
                    if self.observationsIS_NOT.get(trait).get_identifier() == im:
                        return True
                return False
            elif state == State.MAYHAPS:
                if trait in self.observationsMAYHAPS.keys():
                    if self.observationsMAYHAPS.get(trait).get_identifier() == im:
                        return True
                return False

    def add_observation_which_state_you_know_not(self, obs):
        """
        Add single observation which state you know not
        :param obs: Observation
        """
        self.observations.append(obs)
        self.get_em_observations([obs])

    def give_all_traits_involved(self):
        """
        :return list(Trait): list of traits which were observed
        """
        out = []
        for obs in self.observations:
            for tuptup in obs.get_observed():
                out.append(tuptup[0])
        return list(set(out))

    def give_subjects_involved(self):
        """
        :return list(Trait): list of traits which were observed
        """
        out = []
        for obs in self.observations:
            out.append(obs.get_identifier())
        return list(set(out))

    def __eq__(self, other):
        return self.timestamp == other.timestamp and self.observationsIS == other.observationsIS and \
               self.observationsIS_NOT == other.observationsIS_NOT and self.observationsMAYHAPS == \
               other.observationsMAYHAPS
