import time


class Observation:

    def __init__(self, identifier, observed, timestamp=None):
        self.identifier = identifier
        self.observed = observed
        if timestamp is None:
            self.timestamp = int(time.time())
        else:
            self.timestamp = timestamp

    def get_identifier(self):
        return self.identifier

    def get_observed(self):
        return self.observed

    def get_timestamp(self):
        return self.timestamp

    def set_identifier(self, identifier):
        self.identifier = identifier

    def set_observed(self, traits):
        self.observed = traits

    def __str__(self):
        return "{" + str(self.identifier) + " " + str(list((str(x[0]) + " " + str(x[1]) for x in self.observed))) +\
               " observed: " + str(self.timestamp) + "}"

    def __eq__(self, other):
        return self.identifier == other.identifier and len(list((x for x in other.get_observed() if x in
                                                                 self.get_observed()))) == len(other.get_observed())
