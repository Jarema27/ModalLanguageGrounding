from src.sc.pwr.inz.memory.LongTermMemory.semantic.language.components.ComplexFormulaOT import ComplexFormulaOT
from src.sc.pwr.inz.memory.LongTermMemory.semantic.language.components.ModalOperator import ModalOperator
from src.sc.pwr.inz.memory.LongTermMemory.semantic.language.components.Trait import Trait
from src.sc.pwr.inz.memory.LongTermMemory.semantic.language.components.ComplexFormula import ComplexFormula
from src.sc.pwr.inz.memory.LongTermMemory.semantic.language.components.SimpleFormula import SimpleFormula
from src.sc.pwr.inz.memory.LongTermMemory.semantic.language.components.Formula import TypeOfFormula
from src.sc.pwr.inz.memory.LongTermMemory.semantic.language.constructs.Sentence import Sentence, SentenceType

"""
Declarative is one of types of Sentence. As example 'Carl indeed was white' or 'She might have been stoked and broke'
"""


class Declarative(Sentence):

    def __init__(self, subject=None, traits=None, states=None, logicaloperator=None, modal_operator=None, tense=None):
        """
        I really don't have any desire in explaining basic english
        :param subject (IndividualModel): subject
        :param traits (Trait or list(Traits)) : traits
        :param states (State or list(State)) : states
        :param logicaloperator (LogicalOperator): Logical operator
        :param modal_operator (ModalOperator): Modal Operator
        """
        self.subject = subject
        self.gentleman_dict = {ModalOperator.NOIDEA: 'I cannot tell if ',
                               ModalOperator.POS: 'I think its absolutely possible that ',
                               ModalOperator.BEL: 'I deeply and truthfully believe that ',
                               ModalOperator.KNOW: 'I definitely know that'}
        self.traits = traits
        self.states = states
        if traits is not None:
            if isinstance(traits, Trait):
                self.formula = SimpleFormula(subject, traits, states)
            elif len(traits) > 1:
                self.logicaloperator = logicaloperator
                self.formula = ComplexFormula(subject, traits, states, logicaloperator)
        elif tense is not None:
            self.formula = ComplexFormulaOT(subject, states, logicaloperator, tense)
            self.tense = tense
            self.logicaloperator = logicaloperator
        if modal_operator is not None:
            self.modaloperator = modal_operator

    def get_kind(self):
        """
        :return (SentenceType): Type of sentence,in this one Declarative
        """
        return SentenceType.Dec

    def get_subject(self):
        """
        :return IndividualModel: IM of this sentence
        """
        return self.subject

    def __str__(self):
        if self.formula.get_type() == TypeOfFormula.SF:
            return self.gentleman_dict.get(self.modaloperator) + " " + str(self.subject) + " " + \
                   str(self.states) + " " + str(self.traits)

        elif self.formula.get_type() == TypeOfFormula.CF:
            return self.gentleman_dict.get(self.modaloperator) + " " + str(self.subject) + " " + str(self.states[0]) +\
                   "" + str(self.traits[0]) + " " + str(self.logicaloperator) + " " + \
                   str(self.states[1]) + str(self.traits[1]) + "."
        elif self.formula.get_type() == TypeOfFormula.OT:
            return self.gentleman_dict.get(self.modaloperator) + " " + str(self.subject[0]) + "" + \
                   str(self.states[0]) + " " + str(self.logicaloperator) + " " + \
                   str(self.subject[1]) + "" + str(self.states[1])
