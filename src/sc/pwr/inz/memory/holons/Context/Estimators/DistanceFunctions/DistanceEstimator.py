from src.sc.pwr.inz.memory.holons.Context.Estimators.EstimateFunctions import EstimateFunctions, EstimatorKind


class DistanceEstimator(EstimateFunctions):

    def __init__(self):
        super(EstimateFunctions, self).__init__()
        pass

    def get_estimated_value(self, bp, traits):
        return sum(list(x for x in bp.get_observations_is().keys() if x in traits[0])) + \
               sum(list(x for x in bp.get_observations_is_not().keys() if x in traits[1]))

    def get_kind_of_estimator(self):
        return EstimatorKind.DF
