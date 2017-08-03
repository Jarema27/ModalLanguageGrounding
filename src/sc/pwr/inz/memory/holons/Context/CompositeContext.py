from src.sc.pwr.inz.memory.holons.Context.UberContext import UberContext

"""
All observations are taken in certain context, maintaining such context is valid in understanding and 
building knowledge about the world. As example object Tree will be different in winter than in spring.
"""


class CompositeContext(UberContext):

    def __init__(self, estimator, bpset, maxthreshold, taken_into_consideration=3):
        """

        :param estimator (EstimateFunctions): Instance of module extending abstract class EstimateFunctions
        :param bpset (list(BaseProfile)): list of BaseProfiles which we want to build context around
        :param maxthreshold (int): is a variable making contextualisation stronger or weaker
        :param taken_into_consideration (int): How many BProfiles we will consider a root of context, root of context is
         set of BaseProfiles from which we extract traits and compare other BProfiles to
        """
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
        """
        :return (EstimateFunctions):
        """
        return self.estimator

    def get_bpset(self):
        """
        :return list(BaseProfile):
        """
        return self.bpset

    def set_maxthreshold(self, other):
        """
        Allows to set new value of threshold
        :param other :(int):
        """
        self.maxthreshold = other

    def get_contextualized_bpset(self):
        """
        :return list(BaseProfile): list of BProfiles which are considered context from now on,estimated by function
        and root of context
        """
        return list(x for x in self.bpset if self.estimator.get_estimated_value(x, self.benchtraits)
                    >= self.maxthreshold)

    @staticmethod
    def get_common_traits(bpset):
        """
        Really ugly method, would totally need to be simplified, most of this redundant coding is done to maintain
        staticness
        :param bpset:list(BaseProfile):
        :return Tuple(list(Trait), list[Trait]):
        """
        trait_is = []
        trait_is_not = []
        for bp in bpset:
            for trait in bp.get_observations_is():
                trait_is.append(trait)
            for trait in bp.get_observations_is_not():
                trait_is_not.append(trait)
        trait_is_2 = []
        trait_is_not_2 = []
        for i in trait_is:
            if i not in trait_is_2:
                trait_is_2.append(i)
        for i in trait_is_not:
            if i not in trait_is_not_2:
                trait_is_not_2.append(i)
        out = [list(x for x in trait_is_2 if trait_is.count(x) == len(bpset)),
               list(x for x in trait_is_not_2 if trait_is_not.count(x) == len(bpset))]
        return out[0], out[1]
