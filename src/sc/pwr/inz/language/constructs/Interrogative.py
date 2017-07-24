from src.sc.pwr.inz.memory.semantic.KnowledgeBoosters.XMLReader import XMLReader
from src.sc.pwr.inz.language.components.SimpleFormula import SimpleFormula
from src.sc.pwr.inz.language.components.ComplexFormula import ComplexFormula
from src.sc.pwr.inz.language.constructs.Sentence import Sentence, SentenceType
from src.sc.pwr.inz.language.components.ModalOperator import ModalOperator


class Interrogative(Sentence):

    def __init__(self, subject=None, traits=None, states=None, logicaloperator=None, plaintext=None, memory=None):
        if subject is not None and traits is not None:
            self.subject = subject
            self.traits = traits
            self.states = states
            self.memory = memory
            if len(traits) > 1:
                self.LO = logicaloperator
        else:
            acquired = self.build_from_scraps(plaintext)
            self.subject = acquired[0]
            self.traits = acquired[1]
            self.states = acquired[2]
            if len(traits > 1):
                self.LO = acquired[3]
        if self.subject is None or self.traits is None or self.states is None:
            raise ValueError("What are you on about ? Can't really understand you mate")
        if len(traits) > 0:
            if len(traits) == 1:
                self.formula = SimpleFormula(self.subject, self.traits[0], self.states[0])
            elif len(traits) == 2:
                self.formula = ComplexFormula(self.subject, self.traits, self.states, self.LO)

    def get_kind(self):
        return SentenceType.Int

    def get_subject(self):
        return self.subject

    def __str__(self):
        if len(self.traits) == 1:
            return str(self.states[0]) + " " + str(self.subject) + " " + str(self.traits[0]) + "?"
        else:
            return str(self.states[0]) + " " + str(self.subject) + " " + str(self.traits[0]) + " " \
                   + str(self.LO) + " " + str(self.states[1]) + "" + str(self.traits[1]) + "?"

    def answer(self):
        epistemic_values = self.memory.get_holon_by_formula(self.formula)
        pass_responsibility = self.get_epistemic_conclusion(epistemic_values)
#       return Declarative(self.subject, self.traits, pass_responsibility, self.LO)

    @staticmethod
    def build_from_scraps(plaintext):
        shattered = plaintext.split(" ")
        if len(shattered) == 4:
            return [shattered[1], shattered[3], shattered[2]]
        elif len(shattered) == 7:
            return [shattered[1], [shattered[3], shattered[6]], [shattered[2], shattered[5]], shattered[4]]
        else:
            raise ValueError(" Question ain't properly built ")

    def get_epistemic_conclusion(self, holon):
        values = holon.get_tao()
        return self.check_epistemic_scope(values)

    @staticmethod
    def check_epistemic_scope(vallist):
        ranges = XMLReader.read_agent_variables()
        out = []
        for val in vallist:
            if float(ranges[0]) <= val <= float(ranges[1]):
                out.append(ModalOperator.NOIDEA)
            elif float(ranges[2]) <= val <= float(ranges[3]):
                out.append(ModalOperator.POS)
            elif float(ranges[4]) <= val <= float(ranges[5]):
                out.append(ModalOperator.BEL)
            elif float(ranges[6]) <= val <= float(ranges[7]):
                out.append(ModalOperator.KNOW)
        return out
