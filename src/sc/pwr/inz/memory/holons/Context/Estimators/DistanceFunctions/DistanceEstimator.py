from src.sc.pwr.inz.memory.holons.Context.Estimators.EstimateFunctions import EstimateFunctions, EstimatorKind

"""
Module counting Distance from one BaseProfile to set of traits,which is usually extracted from numerous BaseProfiles 
called root
"""


class DistanceEstimator(EstimateFunctions):

    @staticmethod
    def get_estimated_value(bp, traits):
        """
        :param bp: (BaseProfile): BaseProfile which distance we wish to know
        :param traits: list(Trait): List of traits considered as benchmark
        :return (int): Value describing how 'far' bp is from root
        """
        return len(list(x for x in bp.get_observations_is().keys() if x in traits[0])) + \
               len(list(x for x in bp.get_observations_is_not().keys() if x in traits[1]))

    @staticmethod
    def get_kind_of_estimator():
        """
        :return (EstimatorKind): Kind of Estimator which this module represents.
        """
        return EstimatorKind.DF
