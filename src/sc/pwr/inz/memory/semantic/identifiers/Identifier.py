from abc import ABC, abstractmethod

"""
Identifier module serves us to be able to differ one object from another.
"""


class Identifier(ABC):

    @abstractmethod
    def is_id_member_of(self):
        pass
