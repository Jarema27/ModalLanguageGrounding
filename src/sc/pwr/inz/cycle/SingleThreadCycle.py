from src.sc.pwr.inz.memory.LongTermMemory.WokeMemory import WokeMemory
from src.sc.pwr.inz.cycle.Preparations import Preparations
from src.sc.pwr.inz.memory.LongTermMemory.semantic.language.constructs.Interrogative import Interrogative

"""
Module being a cycle in which agent will work, simple way of presenting functionality of agent
"""


class SingleThreadCycle:
    def main(self):
        """
        Method in which we initialize time,capturing observations and asking questions along with computing them
        """
        time = 0
        while time < 11:

            self.capture_observations(time)
            #   Not complementary segment of asking questions
            time += 1

        question = Interrogative(None, None, None, None, "was Stado Kompletne ?",
                                 self.memory, time)
        print("Proceeding with question: ")
        print(question)
        print(question.ask())

        question = Interrogative(None, None, None, None, "was Partyzant Uzbrojony ?",
                                 self.memory, time)
        print("Proceeding with question: ")
        print(question)
        print(question.ask())

        question = Interrogative(None, None, None, None, "was Bron Mauser_M1905 ?",
                                 self.memory, time)
        print("Proceeding with question: ")
        print(question)
        print(question.ask())
        print('m')

    def __init__(self):
        self.preparations = Preparations()
        self.memory = WokeMemory(None, None, self.preparations.ims)
        self.memory.toggle_contextualised()
        self.is_busy = False

    def capture_observations(self, timer):
        """
        :param timer: int: point in time
        :return: Observations with given episode
        """
        print("Receiving observations")
        obs = self.preparations.get_observations_with_episode(timer)
        if len(obs) == 0:
            print("No observations at " + str(timer))
        else:
            self.is_busy = True
            print("Captured " + str(len(obs)) + " observations")
            bp = self.preparations.prepare_bps(timer, obs)
            self.memory.add_bp(bp)
            print("Observations have been transformed into properly built base profiles")
            self.is_busy = False
        if timer % 5 == 0 and not self.is_busy:
            self.memory.update_em_all(timer)

if __name__ == "__main__":
    a = SingleThreadCycle()
    a.main()
