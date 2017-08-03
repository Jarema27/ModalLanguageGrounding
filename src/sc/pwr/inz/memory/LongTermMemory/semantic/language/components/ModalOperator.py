from enum import Enum

""""
Enum Modal Operator made in order to picture human's understatement of epistemic values
"""


class ModalOperator(Enum):
    BEL = 'BEL'
    POS = 'POS'
    KNOW = 'KNOW'
    NOIDEA = 'XD'

    def __str__(self):
        if self.KNOW:
            return "Know"
        if self.BEL:
            return "Believe"
        if self.POS:
            return "Possible"
        if self.NOIDEA:
            return "I don't know, really"

