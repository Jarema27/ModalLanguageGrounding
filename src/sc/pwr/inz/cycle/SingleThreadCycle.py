from src.sc.pwr.inz.language.components.State import State
from src.sc.pwr.inz.memory.episodic.Observations import Observation
from src.sc.pwr.inz.memory.semantic.KnowledgeBoosters.CSVReader import CSVReader
from src.sc.pwr.inz.memory.semantic.IndividualModel import IndividualModel
from src.sc.pwr.inz.memory.semantic.KnowledgeBoosters.XMLReader import XMLReader
from src.sc.pwr.inz.memory.semantic.ObjectType import ObjectType
import itertools


class SingleThreadCycle:

    def main(self):
        pass

    def __init__(self):
        self.state_dict = {1: State.IS, 2: State.IS_NOT,3: State.MAYHAPS}
        self.object_type = ObjectType.get_object_types()
        self.traits = list((x.get_traits() for x in self.object_type))
        self.identifiers = XMLReader.read_ids()
        self.ims = self.set_ims()

        self.observations = self.extract_observations()
        print(self.observations)
        #Obserwacje++
        #Formowanie bpekow w reakcji na nadchodzace obserwacje
        #Tworzenie holonow co 10 sekund
        #Tworzenie Holonow na zapytanie
        #Powiazanie z working memory

    def extract_observations(self):
        scope = CSVReader.get_some_observations()
        out = []
        for x in scope:
            traitsNstates = []
            for tuplecik in x[1]:
                trait = self.get_object_type(x[0])[0].get_object_type().get_traits()[int(tuplecik[0])]
                state = self.state_dict.get(tuplecik[1])
                traitsNstates.append((trait, state))
            out.append(Observation(x[0], traitsNstates, x[2]))
        return out

    def get_object_type(self, a):
        return list((x for x in self.ims if a == x.get_identifier()))

    def set_ims(self):
        out = []
        for i in range(0, min(len(self.identifiers), len(self.object_type))):
            out.append(IndividualModel(self.identifiers[i], self.object_type[i]))
        return out

if __name__ == "__main__":
    a = SingleThreadCycle()
    a.main()
