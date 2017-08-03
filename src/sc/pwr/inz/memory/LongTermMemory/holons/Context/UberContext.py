from abc import abstractmethod, ABC

"""
Abstract module which allows us to build and use numerous contextsS
"""


class UberContext(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_judgement_method(self):
        pass

    @abstractmethod
    def get_bpset(self):
        pass

    @abstractmethod
    def get_contextualized_bpset(self):
        pass
