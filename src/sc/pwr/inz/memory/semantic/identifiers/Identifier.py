from abc import ABC,abstractmethod


class Identifier(ABC):

    @abstractmethod
    def is_id_member_of(self):
        pass
