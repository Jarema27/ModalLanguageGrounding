from src.sc.pwr.inz.memory.LongTermMemory.semantic.IdentifyingMetaCognition.IndividualModel import IndividualModel
from src.sc.pwr.inz.memory.LongTermMemory.semantic.IdentifyingMetaCognition.ObjectType import ObjectType
from src.sc.pwr.inz.memory.LongTermMemory.semantic.KnowledgeBoosters.CSVReader import CSVReader
from src.sc.pwr.inz.memory.LongTermMemory.semantic.KnowledgeBoosters.XMLReader import XMLReader
from src.sc.pwr.inz.memory.LongTermMemory.semantic.identifiers.UniqueName import UniqueName
from src.sc.pwr.inz.memory.LongTermMemory.semantic.language.components.State import State
from src.sc.pwr.inz.memory.SensoryBufferMemory.Observation import Observation
from src.sc.pwr.inz.memory.ShortTermMemory.episodic.BaseProfile import BaseProfile
from src.sc.pwr.inz.speech.Phonograph import Phonograph

"""
Module responsible for setting data up and preparing it to fire agent up.
Metaphoric 5 minutes after waking up.
"""


class Preparations:

    def __init__(self):
        self.state_dict = {'1': State.IS, '2': State.IS_NOT, '3': State.MAYHAPS}
        self.object_type = ObjectType.get_object_types()
        self.traits = list((x.get_traits() for x in self.object_type))
        self.identifiers = self.properly_prepare_identifiers()
        self.ims = self.set_ims()
        self.phonograph = Phonograph()
        self.observations = self.extract_observations()

    def extract_observations(self):
        """
        Gets observation data extracted from csv file and turns them into actual objects
        :return: list(Observation): list of observations
        """
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
        """
        :param a: Identifier : which OT we desire to find
        :return:  ObjectType: with a as identifier
        """
        return list((x for x in self.ims if a == x.get_identifier()))

    def set_ims(self):
        """
        :return: list(IndividualModel): based on Identifiers and OT we read
        """
        out = []
        for i in range(0, min(len(self.identifiers), len(self.object_type))):
            for j in self.object_type:
                if int(j.get_type_id()) - 1 == i:
                    out.append(IndividualModel(self.identifiers[i], j))
        return out

    def get_observations_with_episode(self, episode):
        """

        :param episode: Point in time
        :return: list(Observation): with given episode or empty list
        """
        return list(x for x in self.observations if int(x.get_episode()) == episode)

    @staticmethod
    def properly_prepare_identifiers():
        """
        :return: list(Identifier): list of identifiers read from xml
        """
        unique_names = XMLReader.read_ids()
        out = []
        for name in unique_names:
            out.append(UniqueName(name))
        return out

    @staticmethod
    def prepare_bps(episode, observations):
        """
        :param episode: point in time
        :param observations: observations from x=csv
        :return: BaseProfile : made from given episode and observations
        """
        return BaseProfile(episode, observations)
