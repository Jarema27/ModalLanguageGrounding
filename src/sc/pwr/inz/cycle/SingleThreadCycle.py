from sc.pwr.inz.language.constructs.Interrogative import Interrogative
from sc.pwr.inz.memory.WokeMemory import WokeMemory
from src.sc.pwr.inz.cycle.Preparations import Preparations


class SingleThreadCycle:
    def main(self):
        #       while True:
        time = 1
        self.capture_observations(time)
        #   Not complementary segment of asking questions
        question = Interrogative(None, None, None, None, "is RJ45 Bloody and is Twisted ?",
                                 self.memory, time)
        print("Proceeding with question: ")
        print(question)
        print(question.ask())
        time += 1
        self.capture_observations(time)
        question = Interrogative(None, None, None, None, "is RJ45 Bloody and is Twisted ?",
                                 self.memory, time)
        print("Proceeding with question: ")
        print(question)
        print(question.ask())
        time += 2
        self.capture_observations(time)
        question = Interrogative(None, None, None, None, "is RJ45 Bloody and is Twisted ?",
                                 self.memory, time)
        print("Proceeding with question: ")
        print(question)
        print(question.ask())
        time += 2
        self.capture_observations(time)
        question = Interrogative(None, None, None, None, "is RJ45 Bloody and is Twisted ?",
                                 self.memory, time)
        print("Proceeding with question: ")
        print(question)
        print(question.ask())
        time += 1
        self.capture_observations(time)
        question = Interrogative(None, None, None, None, "is RJ45 Bloody and is Twisted ?",
                                 self.memory, time)
        print("Proceeding with question: ")
        print(question)
        print(question.ask())
        print("Agent has regained his sureness in object's state through continuously positive observations")

        question2 = Interrogative(None, None, None, None, "is Gun Juicy ?",
                                  self.memory, time)
        print("Proceeding with question: ")
        print(question2)
        print(question2.ask())

    def __init__(self):
        self.preparations = Preparations()
        self.memory = WokeMemory(None, None, self.preparations.ims)
        self.is_busy = False
        # Tworzenie Holonow na zapytanie
        # Powiazanie z working memor

    def capture_observations(self, time):
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

if __name__ == "__main__":
    a = SingleThreadCycle()
    a.main()
