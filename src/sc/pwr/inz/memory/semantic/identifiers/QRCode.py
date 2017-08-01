from src.sc.pwr.inz.memory.semantic.identifiers.Identifier import Identifier

"""
QRCode as identificator
"""


class QRCode(Identifier):

    code = ""

    def __init__(self, code):
        """
        :param name (int): unique code of certain identificator
        """
        self.code = code

    def get_code(self):
        """
        :return: unique code
        """
        return self.code

    def set_code(self, code):
        """
        :param code: new unique code
        """
        self.code = code

    def is_id_member_of(self):
        """
        Not implemented method,might be used in future
        :return:
        """
        return True

    def __str__(self):
        return "QRCode{id=" + self.code + "}"

    def __eq__(self, other):
        return self.code == other.code

    def __hash__(self):
        return hash(self.code)