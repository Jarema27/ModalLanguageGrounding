from time import time

from src.sc.pwr.inz.memory.episodic.Observations import Observation
from src.sc.pwr.inz.language.State import State


class BaseProfile:

    def __init__(self, timestamp = None, observations = None):
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

    def get_em_observations(self, observation):
        for obs in observation:
            for tupl in obs.get_observed():
                if tupl[1] == State.IS:
                    self.observationsIS[tupl[0]] = obs
                elif tupl[1] == State.IS_NOT:
                    self.observationsIS_NOT[tupl[0]] = obs
                else:
                    self.observationsMAYHAPS[tupl[0]] = obs

    def get_observations_is(self):
        return self.observationsIS

    def get_observations_is_not(self):
        return self.observationsIS_NOT

    def get_observations_mayhaps(self):
        return self.observationsMAYHAPS

    def get_timestamp(self):
        return self.timestamp

    def add_observations_is(self, other):
        self.observationsIS = other
        self.observations.append(other)

    def add_observations_is_not(self, other):
        self.observationsIS_NOT = other
        self.observations.append(other)

    def add_observations_mayhaps(self, other):
        self.observationsMAYHAPS = other
        self.observations.append(other)

    def get_observed_ims(self):
        return list(set([x.identifier for x in self.observations]))

    def check_if_observed(self, im, trait_state_in_proper_order):
        return Observation(im, trait_state_in_proper_order) in self.observations

    def add_observation_which_state_you_know_not(self, obs):
        self.observations.append(obs)
        self.get_em_observations([obs])

    def give_all_traits_involved(self):
        out = []
        for obs in self.observations:
            for tuptup in obs.get_observed():
                out.append(tuptup[0])
        print(set(out))
        return list(set(out))

    def __eq__(self, other):
        return self.timestamp == other.timestamp and self.observationsIS == other.observationsIS and \
               self.observationsIS_NOT == other.observationsIS_NOT and self.observationsMAYHAPS == \
               other.observationsMAYHAPS
