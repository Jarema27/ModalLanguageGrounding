import time
"""
Observation module is responsible for holding observations made by agent.
As example 'Carpet is Red' -> Identifier, Trait, Trait.State
"""


class Observation:

    def __init__(self, identifier=None, observed=None, timestamp=None):
        """
        :param identifier: (Identifier): Identifier such as QRCode or UniqueName, if None agent will
         try to establish one based on traits
        :param observed: list(Trait): list of observed traits in context of given Identifier if None agent will try
         to deduce traits based on IndividualModel
        :param episode (int): episode
        """
        if identifier is not None:
            self.identifier = identifier
        else:
            self.identifier = self.establish_identifier()
        if observed is not None:
            self.observed = observed
        else:
            self.observed = self.deduce_traits()
        if timestamp is None:
            self.timestamp = int(time.time())
        else:
            self.timestamp = timestamp

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

    def get_timestamp(self):
        """
        :return int : episode
        """
        return self.timestamp

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

    def establish_identifier(self):
        """
        Method tries to find individual model with similar traits and alike object_type
        those we observed,if it finds nothing like that,it
         creates brand new IndividualModel
        :return (IndividualModel):
        """
        #   todo Implement
        return self.identifier + None

    def establish_object_type(self):
        """
        Method tries to establish object type by it's traits
        :return:
        """
        #   todo Implement
        return self.identifier + None

    def deduce_traits(self):
        """
        Having object type or/and Individual model we're able to deduce proper traits of model.
        :return:
        """
        #   todo Implement
        return self.identifier + None

    def __str__(self):
        return "{" + str(self.identifier) + " " + str(list((str(x[0]) + " " + str(x[1]) for x in self.observed))) +\
               " observed: " + str(self.timestamp) + "}"

    def __eq__(self, other):
        return self.identifier == other.identifier and len(list((x for x in other.get_observed() if x in
                                                                 self.get_observed()))) == len(other.get_observed())

    def __hash__(self):
        return sum(hash(x) for x in self.observed) ^ hash(self.identifier)
