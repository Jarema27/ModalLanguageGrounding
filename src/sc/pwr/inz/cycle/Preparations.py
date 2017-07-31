from src.sc.pwr.inz.memory.semantic.identifiers.UniqueName import UniqueName
from src.sc.pwr.inz.memory.episodic.BaseProfile import BaseProfile
from src.sc.pwr.inz.language.components.State import State
from src.sc.pwr.inz.memory.episodic.Observations import Observation
from src.sc.pwr.inz.memory.semantic.KnowledgeBoosters.CSVReader import CSVReader
from src.sc.pwr.inz.memory.semantic.IndividualModel import IndividualModel
from src.sc.pwr.inz.memory.semantic.KnowledgeBoosters.XMLReader import XMLReader
from src.sc.pwr.inz.memory.semantic.ObjectType import ObjectType


class Preparations:

    def __init__(self):
        self.state_dict = {'1': State.IS, '2': State.IS_NOT, '3': State.MAYHAPS}
        self.object_type = ObjectType.get_object_types()
        self.traits = list((x.get_traits() for x in self.object_type))
        self.identifiers = self.properly_prepare_identifiers()
        self.ims = self.set_ims()

        self.observations = self.extract_observations()

    def extract_observations(self):
        scope = CSVReader.get_some_observations()
        out = []
        for x in scope:
            traitsnstates = []
            for tuplecik in x[1]:
                trait = self.get_object_type(x[0])[0].get_object_type().get_traits()[int(tuplecik[0])]
                state = self.state_dict.get(tuplecik[1])
                traitsnstates.append((trait, state))
            out.append(Observation(x[0], traitsnstates, x[2]))
        return out

    def get_object_type(self, a):
        return list((x for x in self.ims if a == x.get_identifier()))

    def set_ims(self):
        out = []
        for i in range(0, min(len(self.identifiers), len(self.object_type))):
            out.append(IndividualModel(self.identifiers[i], self.object_type[i]))
        return out

    def get_observations_with_timestamp(self, timestamp):
        return list(x for x in self.observations if int(x.get_timestamp()) == timestamp)

    def properly_prepare_identifiers(self):
        unique_names = XMLReader.read_ids()
        out = []
        for name in unique_names:
            out.append(UniqueName(name))
        return out

    @staticmethod
    def prepare_bps(timestamp, observations):
        return BaseProfile(timestamp, observations)
