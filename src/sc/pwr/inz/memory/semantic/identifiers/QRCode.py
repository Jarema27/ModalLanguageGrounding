from src.sc.pwr.inz.memory.semantic.identifiers.Identifier import Identifier


class QRCode(Identifier):

    def __init__(self):
        pass

    def is_id_member_of(self):
        return True

    def __str__(self):
        return "QRCode{id=" + self.get_id_number() + "\" + ""}"
