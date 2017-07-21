from src.sc.pwr.inz.language.components.SimpleFormula import SimpleFormula
from src.sc.pwr.inz.language.components.ComplexFormula import ComplexFormula
from src.sc.pwr.inz.language.constructs.Sentence import Sentence, SentenceType


class Interrogative(Sentence):

    def __init__(self, subject=None, traits=None, states=None, logicaloperator=None, plaintext=None):
        if subject is not None and traits is not None:
            self.subject = subject
            self.traits = traits
            self.states = states
            if len(traits > 1):
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
                self.formula = SimpleFormula(self.subject, self.traits, self.states)
            elif len(traits) == 2:
                self.formula = ComplexFormula(self.subject, self.traits, self.states, self.LO)

    def get_kind(self):
        return SentenceType.Int

    def get_subject(self):
        return self.subject

    def __str__(self):
        if len(self.traits) == 1:
            return "Is " + self.subject + " " + self.states[0] + " " + self.traits[0] + "?"
        else:
            return "Is " + self.subject + " " + self.states[0] + " " + self.traits[0] + " " + self.LO + " "
            + self.states[0] + " " + self.traits[0] + "?"

    def answer(self):
        return #todo

    @staticmethod
    def build_from_scraps(plaintext):
        shattered = plaintext.split(" ")
        if len(shattered) == 4:
            return [shattered[1], shattered[3], shattered[2]]
        elif len(shattered) == 7:
            return [shattered[1], [shattered[3], shattered[6]], [shattered[2], shattered[5]], shattered[4]]
        else:
            raise ValueError(" Question ain't properly built ")
