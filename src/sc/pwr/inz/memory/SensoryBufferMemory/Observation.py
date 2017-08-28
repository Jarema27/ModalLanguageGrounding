import time
"""
Observation module is responsible for holding observations made by agent.
As example 'Carpet is Red' -> Identifier, Trait, Trait.State
"""


class Observation:

    def __init__(self, identifier=None, observed=None, episode=None):
        """
        :param identifier: (Identifier): Identifier such as QRCode or UniqueName, if None agent will
         try to establish one based on traits
        :param observed: list(Tuple(Trait,State)): list of observed traits in context of given Identifier if None
         agent will try to deduce traits based on IndividualModel
        :param episode (int): episode
        """
        if identifier is not None:
            self.identifier = identifier
        if observed is not None:
            self.observed = observed
        if episode is None:
            self.episode = int(time.time())
        else:
            self.episode = episode

    def get_identifier(self):
        """
        :return observation's identifier
        """
        return self.identifier

    def get_observed(self):
        """
        :return list(Trait): List of observed traits
        """
        return self.observed

    def get_episode(self):
        """
        :return int : episode
        """
        return self.episode

    def set_identifier(self, identifier):
        """
        :param identifier: QRCode,UniqueName etc.
        """
        self.identifier = identifier

    def set_observed(self, traits):
        """
        :param traits: traits you wish to establish for this specific observation
        """
        self.observed = traits

    def __str__(self):
        return "{" + str(self.identifier) + " " + str(list((str(x[0]) + " " + str(x[1]) for x in self.observed))) +\
               " observed: " + str(self.episode) + "}"

    def __eq__(self, other):
        return self.identifier == other.identifier and len(list((x for x in other.get_observed() if x in
                                                                 self.get_observed()))) == len(other.get_observed())

    def __hash__(self):
        return sum(hash(x) for x in self.observed) ^ hash(self.identifier)
