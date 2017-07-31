from time import time

from src.sc.pwr.inz.language.components.Formula import TypeOfFormula
from src.sc.pwr.inz.language.constructs.Declarative import Declarative
from src.sc.pwr.inz.language.components.LogicalOperator import LogicalOperator
from src.sc.pwr.inz.language.components.State import State
from src.sc.pwr.inz.memory.semantic.KnowledgeBoosters.XMLReader import XMLReader
from src.sc.pwr.inz.language.components.SimpleFormula import SimpleFormula
from src.sc.pwr.inz.language.components.ComplexFormula import ComplexFormula
from src.sc.pwr.inz.language.constructs.Sentence import Sentence, SentenceType
from src.sc.pwr.inz.language.components.ModalOperator import ModalOperator


class Interrogative(Sentence):

    def __init__(self, subject=None, traits=None, states=None, logicaloperator=None, plaintext=None, memory=None,
                 timestamp=None):
        self.dict = {'is': State.IS, 'is_not': State.IS_NOT, 'might_be': State.MAYHAPS,
                     'and': LogicalOperator.AND, 'or': LogicalOperator.OR}
        if timestamp is None:
            self.timestamp = time()
        else:
            self.timestamp = timestamp
        if subject is not None and traits is not None:
            self.subject = subject
            self.traits = traits
            self.states = states
            self.memory = memory
            if len(traits) > 1:
                self.LO = logicaloperator
        else:
            self.memory = memory
            acquired = self.build_from_scraps(plaintext)
            self.subject = acquired[0]
            self.traits = acquired[1]
            self.states = acquired[2]
            if len(self.traits) > 1:
                self.LO = acquired[3]
        if self.subject is None or self.traits is None or self.states is None:
            raise ValueError("What are you on about ? Can't really understand you mate")
        if len(self.traits) > 0:
            if len(self.traits) == 1:
                self.formula = SimpleFormula(self.subject, self.traits[0], self.states[0])
            elif len(self.traits) == 2:
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
                   + str(self.LO) + "" + str(self.states[1]) + "" + str(self.traits[1]) + "?"

    def ask(self):
        epistemic_values = self.memory.get_holon_by_formula(self.formula, self.timestamp)
        pass_responsibility = self.get_epistemic_conclusion(epistemic_values)
        if hasattr(self, 'LO'):
            return Declarative(self.subject, self.traits, self.states, self.LO, pass_responsibility[0])
        else:
            return Declarative(self.subject, self.traits[0], self.states[0], None, pass_responsibility[0])

    def build_from_scraps(self, plaintext):
        shattered = plaintext.split(" ")
        imfound = None
        traitfound = None
        if len(shattered) == 4:
            for im in self.memory.get_indivmodels():
                if shattered[1] == str(im.get_identifier()):
                    imfound = im
            for trait in imfound.get_object_type().get_traits():
                if shattered[2] == trait.name:
                    traitfound = trait

            return [imfound, [traitfound], [self.dict.get(shattered[0])]]
        elif len(shattered) == 7:
            imfound = None
            trait1 = None
            trait2 = None
            for im in self.memory.get_indivmodels():
                if shattered[1] == str(im.get_identifier()):
                    imfound = im
            for trait in imfound.get_object_type().get_traits():
                if shattered[2] == trait.name:
                    trait1 = trait
                if shattered[5] == trait.name:
                    trait2 = trait
            return [imfound, [trait1, trait2], [self.dict.get(shattered[0]), self.dict.get(shattered[4])],
                    self.dict.get(shattered[3])]
        else:
            raise ValueError(" Question ain't properly built ")

    def get_epistemic_conclusion(self, holon):
        if holon.get_formula().get_type() == TypeOfFormula.SF:
            values = holon.get_tao_for_state(self.formula.get_states()[0])
        elif holon.get_formula().get_type() == TypeOfFormula.CF:
            if len(self.formula.get_states()) > 1:
                values = holon.get_tao_for_state(self.formula.get_states()[0], self.formula.get_states()[1])
            else:
                values = holon.get_tao_for_state(self.formula.get_states()[0], self.formula.get_states()[0])
        return self.check_epistemic_scope([values])

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
            else:
                out.append(ModalOperator.NOIDEA)
        return out
