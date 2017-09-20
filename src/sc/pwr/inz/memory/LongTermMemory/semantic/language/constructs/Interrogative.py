from time import time

from src.sc.pwr.inz.memory.LongTermMemory.semantic.language.components.ComplexFormulaOT import ComplexFormulaOT
from src.sc.pwr.inz.memory.LongTermMemory.semantic.language.components.Tense import Tense
from src.sc.pwr.inz.memory.LongTermMemory.semantic.language.components.Formula import TypeOfFormula
from src.sc.pwr.inz.memory.LongTermMemory.semantic.language.constructs.Declarative import Declarative
from src.sc.pwr.inz.memory.LongTermMemory.semantic.language.components.LogicalOperator import LogicalOperator
from src.sc.pwr.inz.memory.LongTermMemory.semantic.language.components.State import State
from src.sc.pwr.inz.memory.LongTermMemory.semantic.KnowledgeBoosters.XMLReader import XMLReader
from src.sc.pwr.inz.memory.LongTermMemory.semantic.language.components.SimpleFormula import SimpleFormula
from src.sc.pwr.inz.memory.LongTermMemory.semantic.language.components.ComplexFormula import ComplexFormula
from src.sc.pwr.inz.memory.LongTermMemory.semantic.language.constructs.Sentence import Sentence, SentenceType
from src.sc.pwr.inz.memory.LongTermMemory.semantic.language.components.ModalOperator import ModalOperator
"""
Sentence ,which serves purpose of acquiring data, usually ends up with ? and high pitched voice.
"""


class Interrogative(Sentence):

    def __init__(self, subject=None, traits=None, states=None, logicaloperator=None, plaintext=None, memory=None,
                 episode=None, tense=None):
        """
        Again, names of attributes are pretty self explanatory
        :param subject (IndividualModel): subject
        :param traits (list(Trait) or Trait): traits
        :param states (list(State) or State): states
        :param logicaloperator (LogicalOperator): LO
        :param plaintext (str): Interesting option to build question from plain text, must follow strict rules.
        a.e ' is QRCode{id=1} Sowiecki ?' or 'is QRCode{id=2} Konieczny and is_not Bolszoj ?'
        :param memory (WokeMemory): memory we associate this question with
        :param episode (int): Moment in time when question was asked
        """
        if traits is not None or plaintext is not None:
            self.tense = tense
            self.dict = {'is': State.IS, 'is_not': State.IS_NOT, 'might_be': State.MAYHAPS,
                         'and': LogicalOperator.AND, 'or': LogicalOperator.OR}
            self.traditional = True
            if episode is None:
                self.episode = time()
            else:
                self.episode = episode
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
        elif isinstance(subject, list):
            self.traditional = False
            self.traits = None
            if episode is None:
                self.episode = time()
            else:
                self.episode = episode
            self.subject = subject
            self.states = states
            self.memory = memory
            self.formula = ComplexFormulaOT(subject, states, logicaloperator, tense)
            self.tense = tense
            self.LO = logicaloperator

    def get_kind(self):
        """
        :return (SentenceType): Type of sentence, Interrogative in this kind
        """
        return SentenceType.Int

    def get_subject(self):
        """
        :return (IndividualModel): subject
        """
        return self.subject

    def get_episode(self):
        """
        :return (int): episode
        """
        return self.episode

    def set_episode(self, other):
        """
        set episode
        :param other : int: other episode
        """
        self.episode = other

    def __str__(self):
        if self.traits is not None:
            if len(self.traits) == 1:
                return str(self.states[0]) + " " + str(self.subject) + " " + str(self.traits[0]) + "?"
            else:
                return str(self.states[0]) + " " + str(self.subject) + " " + str(self.traits[0]) + " " \
                       + str(self.LO) + "" + str(self.states[1]) + "" + str(self.traits[1]) + "?"
        else:
            if self.tense == Tense.PRESENT:
                return "Do you see that " + str(self.subject[0]) + "" + str(self.states[0]) + "" + str(self.LO) + " " \
                       + str(self.subject[1]) + "" + str(self.states[1]) + "?"
            elif self.tense == Tense.PAST:
                return "Have you ever seen " + str(self.subject[0]) + "" + str(self.states[0]) + "" + \
                       str(self.LO) + " " + str(self.subject[1]) + "" + str(self.states[1]) + "?"
            elif self.tense == Tense.FUTURE:
                return "Do think you will see that " + str(self.subject[0]) + "" + str(self.states[0]) +\
                 "" + str(self.LO) + " " + str(self.subject[1]) + "" + str(self.states[1]) + "?"

    def ask(self):
        """
        Method 'asks' question which means it finds or builds holon, then checks epistemic ranges and gets proper
        modal operator and in the end builds Declarative based on acquired data
        :return (Declarative): as answer to asked question
        """
        epistemic_values = self.memory.get_holon_by_formula(self.formula, self.episode)
        pass_responsibility = self.get_epistemic_conclusion(epistemic_values)
        if isinstance(self.subject, list):
            return Declarative(self.subject, None, self.states, self.LO, pass_responsibility[0], self.tense)
        elif hasattr(self, 'LO'):
            return Declarative(self.subject, self.traits, self.states, self.LO, pass_responsibility[0], self.tense)
        else:
            return Declarative(self.subject, self.traits[0], self.states[0], None, pass_responsibility[0], self.tense)

    def build_from_scraps(self, plaintext):
        """
        builds Interrogative object from string
        :param plaintext: str: which will be turned into meaningful question
        :raises ValueError: in case you didn't build your question properly
        :return: self(Interrogative)
        """
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
            #   todo usunac workaround na temat modeli indywidualnych
            for im in self.memory.get_indivmodels():
                if shattered[1] == str(im.get_identifier()):
                    imfound = im
            for im in self.memory.get_indivmodels():
                for trait in im.get_object_type().get_traits():
                    if shattered[2] == trait.name:
                        trait1 = trait
                    if shattered[5] == trait.name:
                        trait2 = trait
            return [imfound, [trait1, trait2], [self.dict.get(shattered[0]), self.dict.get(shattered[4])],
                    self.dict.get(shattered[3])]
        else:
            raise ValueError(" Question ain't properly built ")

    def get_epistemic_conclusion(self, holon):
        """
        Acquires proper piece of tao and acquires Modal Operator for it.
        :param holon: Holon which contains values we're interested in
        :return: list(ModalOperator)
        """
        values = 0
        if holon.get_formula().get_type() == TypeOfFormula.SF:
            values = holon.get_tao_for_state(self.formula.get_states()[0])
        elif holon.get_formula().get_type() == TypeOfFormula.CF or holon.get_formula().get_type() == TypeOfFormula.OT:
            if len(self.formula.get_states()) > 1:
                values = holon.get_tao_for_state(self.formula.get_states()[0], self.formula.get_states()[1])
            else:
                values = holon.get_tao_for_state(self.formula.get_states()[0], self.formula.get_states()[0])
        return self.check_epistemic_scope([values])

    @staticmethod
    def check_epistemic_scope(vallist):
        """
        Gets ranges of each modal operator and returns proper ModalOperator
        :param vallist: list(int): to which we want to obtain Modal Operators
        :return list(ModalOperator)
        """
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
