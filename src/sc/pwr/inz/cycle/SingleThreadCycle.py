
import itertools

from src.sc.pwr.inz.cycle.Preparations import Preparations


class SingleThreadCycle:

    def main(self):
        while True:
            print(self.preparations.observations)

    def __init__(self):
        self.preparations = Preparations()
        #Formowanie bpekow w reakcji na nadchodzace obserwacje
        #Tworzenie holonow co 10 sekund
        #Tworzenie Holonow na zapytanie
        #Powiazanie z working memor

if __name__ == "__main__":
    a = SingleThreadCycle()
    a.main()
