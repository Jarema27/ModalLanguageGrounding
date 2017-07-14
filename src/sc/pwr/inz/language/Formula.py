from abc import ABC,abstractmethod


class Formula(ABC):

    @abstractmethod
    def foo(self):
        pass

print("a")