from abc import ABC,abstractmethod
from src.sc.pwr.inz.memory.semantic.ObjectType import ObjectType


class Identifier(ABC):

    idNumber = ""

    def set_idn(self, idn):
        self.idNumber = idn

    def get_id_number(self):
        return self.idNumber

    @abstractmethod
    def is_id_member_of(self):
        pass

    def __eq__(self, other):
        return self.idNumber == other.IdNumber

    def get_type(self):
        for idk in ObjectType.get_object_types():
            if idk.__eq__(self.get_id_number()[:2]):
                return idk
