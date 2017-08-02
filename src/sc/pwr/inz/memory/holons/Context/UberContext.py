from abc import abstractmethod, ABC


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
