from time import time

from src.sc.pwr.inz.language.parts.State import State


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

    def get_em_observations(self, observations):
        for obs in observations:
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

    def add_observations_is(self, o):
        self.get_em_observations(o)
        self.observations.append(o)

    def add_observations_is_not(self, o):
        self.get_em_observations(o)
        self.observations.append(o)

    def add_observations_mayhaps(self, o):
        self.get_em_observations(o)
        self.observations.append(o)

    def get_observed_ims(self):
        return list(set([x.identifier for x in self.observations]))

    def check_if_observed(self, im, trait, state):
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
            else:
                return False

    def add_observation_which_state_you_know_not(self, obs):
        self.observations.append(obs)
        self.get_em_observations([obs])

    def give_all_traits_involved(self):
        out = []
        for obs in self.observations:
            for tuptup in obs.get_observed():
                out.append(tuptup[0])
        return list(set(out))

    def __eq__(self, other):
        return self.timestamp == other.timestamp and self.observationsIS == other.observationsIS and \
               self.observationsIS_NOT == other.observationsIS_NOT and self.observationsMAYHAPS == \
               other.observationsMAYHAPS

""""for obs in self.observations:
            if obs.get_identifier() == im.get_identifier():
                k = 0
                for i in range(0,len(traits)):
                    if (traits[i], state[i]) in obs.get_observed():
                        k += 1
                if k == len(traits):
                    return True
        return False"""