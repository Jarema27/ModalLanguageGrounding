from src.sc.pwr.inz.memory.LongTermMemory.semantic.identifiers.Identifier import Identifier

"""
QRCode as identificator
"""


class QRCode(Identifier):

    typeId = ""

    def __init__(self, code):
        """
        :param name (int): unique code of certain identificator
        """
        self.typeId = code

    def get_code(self):
        """
        :return (str) unique code
        """
        return self.typeId

    def set_code(self, typeId):
        """
        :param typeId: new unique code
        """
        self.typeId = typeId

    def is_id_member_of(self):
        """
        Not implemented method,might be used in future
        :return:
        """
        return True

    def __str__(self):
        return "QRCode{id=" + self.typeId + "}"

    def __eq__(self, other):
        return self.typeId == other.typeId

    def __hash__(self):
        return hash(self.typeId)
