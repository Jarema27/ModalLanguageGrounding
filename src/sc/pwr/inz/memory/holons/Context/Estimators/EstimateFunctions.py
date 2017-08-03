from abc import abstractmethod, ABC
from enum import Enum

"""
Abstract module which allows us to build various ways of estimating context
"""


class EstimateFunctions(ABC):

    @abstractmethod
    def get_kind_of_estimator(self):
        pass

    @abstractmethod
    def get_estimated_value(self):
        pass


class EstimatorKind(Enum):
    """
    Enum showing us kind of estimator, allowing us to vary our estimation modules
    """
    DF = 'DistanceFunction'
