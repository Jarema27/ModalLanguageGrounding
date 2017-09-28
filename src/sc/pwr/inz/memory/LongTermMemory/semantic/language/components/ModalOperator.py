from enum import Enum

""""
Enum Modal Operator made in order to picture human's understatement of epistemic values
"""


class ModalOperator(Enum):
    BEL = 'BEL'
    POS = 'POS'
    KNOW = 'KNOW'
    KNOWNOT = 'Know it is not'

    def __str__(self):
        if self.KNOW:
            return "Know"
        if self.BEL:
            return "Believe"
        if self.POS:
            return "Possible"
        if self.KNOWNOT:
            return "I know it is not"
