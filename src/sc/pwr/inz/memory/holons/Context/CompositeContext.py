from src.sc.pwr.inz.memory.holons.Context.UberContext import UberContext


class CompositeContext(UberContext):

    def __init__(self, estimator, bpset, maxthreshold, taken_into_consideration=3):
        super(CompositeContext, self).__init__()
        self.estimator = estimator
        self.bpset = bpset
        if len(bpset) < taken_into_consideration:
            raise AttributeError("You should give me nuff Base Profiles for building Context you moron")
        else:
            self.benchmarks = self.bpset[:3]
        self.taken_into_consideration = taken_into_consideration
        self.maxthreshold = maxthreshold
        self.benchtraits = self.get_common_traits(self.benchmarks)

    def get_judgement_method(self):
        return self.estimator

    def get_bpset(self):
        return self.bpset

    def set_maxthreshold(self, other):
        self.maxthreshold = other

    def get_contextualized_bpset(self):
        return list(x for x in self.bpset if self.estimator.get_estimated_value(x, self.benchtraits) > self.maxthreshold)

#   todo
    @staticmethod
    def get_common_traits(bpset):
        trait_is = list(list(x.get_observations_is().keys()) for x in bpset)
        trait_is_not = list(list(x.get_observations_is_not().keys()) for x in bpset)
        out = ([], [])
        for t in trait_is:
            for bp in bpset:
                for trait in t:
                    if trait in bp.get_observations_is().keys():
                        out[0].append(trait)
        for t in trait_is_not:
            for bp in bpset:
                for trait in t:
                    if trait not in  bp.get_observations_is_not().keys():
                        out[1].append(out)
        print(out)
        return trait_is, trait_is_not
