from src.sc.pwr.inz.language.components.ModalOperator import ModalOperator
from src.sc.pwr.inz.language.components.Trait import Trait
from src.sc.pwr.inz.language.components.ComplexFormula import ComplexFormula
from src.sc.pwr.inz.language.components.SimpleFormula import SimpleFormula
from src.sc.pwr.inz.language.components.Formula import TypeOfFormula
from src.sc.pwr.inz.language.constructs.Sentence import Sentence,SentenceType


class Declarative(Sentence):

    def __init__(self, subject=None, traits=None, states=None, logicaloperator=None, modal_operator=None):
        self.subject = subject
        self.gentleman_dict = {ModalOperator.NOIDEA: 'I cannot tell if ',
                               ModalOperator.POS: 'I think its absolutely possible that ',
                               ModalOperator.BEL: 'I deeply and truthfully believe that ',
                               ModalOperator.KNOW: 'I definitely know that'}
        self.traits = traits
        self.states = states
        if isinstance(traits, Trait):
            self.formula = SimpleFormula(subject, traits, states)
        elif len(traits) > 1:
            self.logicaloperator = logicaloperator
            self.formula = ComplexFormula(subject, traits, states, logicaloperator)
        if modal_operator is not None:
            self.modaloperator = modal_operator

    def get_kind(self):
        return SentenceType.Dec

    def get_subject(self):
        return self.subject

    def __str__(self):
        if self.formula.get_type() == TypeOfFormula.SF:
            return self.gentleman_dict.get(self.modaloperator) + " " + str(self.subject) + " " + \
                   str(self.states) + " " + str(self.traits)

        elif self.formula.get_type() == TypeOfFormula.CF:
            return self.gentleman_dict.get(self.modaloperator) + " " + str(self.subject) + " " + str(self.states[0]) + "" + str(self.traits[0]) + " " + str(self.logicaloperator) + " " + str(self.states[1]) + str(self.traits[1]) + "."
