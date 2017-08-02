from src.sc.pwr.inz.memory.holons.Context.Estimators.EstimateFunctions import EstimateFunctions, EstimatorKind


class DistanceEstimator(EstimateFunctions):

    @staticmethod
    def get_estimated_value(bp, traits):
        return len(list(x for x in bp.get_observations_is().keys() if x in traits[0])) + \
               len(list(x for x in bp.get_observations_is_not().keys() if x in traits[1]))

    @staticmethod
    def get_kind_of_estimator():
        return EstimatorKind.DF
