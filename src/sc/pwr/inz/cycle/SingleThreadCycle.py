from sc.pwr.inz.language.constructs.Interrogative import Interrogative
from sc.pwr.inz.memory.WokeMemory import WokeMemory
from src.sc.pwr.inz.cycle.Preparations import Preparations


class SingleThreadCycle:
    def main(self):
        #       while True:
        time = 1
        print("Receiving observations")
        obs = self.preparations.get_observations_with_timestamp(time)
        if len(obs) == 0:
            print("No observations at " + str(time))
        else:
            self.is_busy = True
            print("Captured " + str(len(obs)) + " observations")
            bp = self.preparations.prepare_bps(time, obs)
            self.memory.add_bp(bp)
            print("Observations have been transformed into properly built base profiles")
            self.is_busy = False
        if time % 5 == 0 and not self.is_busy:
            self.memory.update_em_all(time)

        #   Not complementary segment of asking questions
        question = Interrogative(None, None, None, None, "is RJ45 Bloody and is Twisted ?",
                                 self.memory, time)
        print(question.ask())

    def __init__(self):
        self.preparations = Preparations()
        self.memory = WokeMemory(None, None, self.preparations.ims)
        self.is_busy = False
        # Tworzenie Holonow na zapytanie
        # Powiazanie z working memor

if __name__ == "__main__":
    a = SingleThreadCycle()
    a.main()
