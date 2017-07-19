from src.sc.pwr.inz.memory.semantic.identifiers.Identifier import Identifier


class QRCode(Identifier):

    code = ""

    def __init__(self, code):
        self.code = code

    def get_code(self):
        return self.code

    def set_code(self,code):
        self.code = code

    def is_id_member_of(self):
        return True

    def __str__(self):
        return "QRCode{id=" + self.code + "}"

    def __eq__(self, other):
        return self.code == other.code

    def __hash__(self):
        return hash(self.code)