import logging
import threading
import time

from src.sc.pwr.inz.memory.LongTermMemory.WokeMemory import WokeMemory
from src.sc.pwr.inz.cycle.Preparations import Preparations
from src.sc.pwr.inz.memory.LongTermMemory.semantic.language.constructs.Interrogative import Interrogative

"""
Module being a cycle in which agent will work, it's way more precise than SingleThread, also allows for a 
few interesting behaviors
"""


class MultiThreadCycle:

    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s (%(threadName)-2s) %(message)s',
                        )

    def main(self):
        """
        Main method managing threads and initializing new questions,in real life ,questions should be initialized in
        listening_service
        """
        self.thread_listening.start()
        self.thread_answering.start()
        self.thread_mind.start()
        self.thread_capturing.start()

        self.semaphore[3] = 1
        self.semaphore[0] = 1

        if self.episoder % 5 == 0:
            self.semaphore[2] = 1
        question = Interrogative(None, None, None, None, "is RJ45 Bloody and is Twisted ?",
                                 self.memory, self.episoder)
        self.active_questions.append(question)

        time.sleep(2)

        question = Interrogative(None, None, None, None, "is RJ45 Bloody and is Twisted ?",
                                 self.memory, self.episoder)
        self.active_questions.append(question)

    def listening_service(self):
        """
        Thread of agent which is always active, it waits for questions and even after receiving one,is still active.
        Whenever question appears it changes answering_service's semaphore to 1 which allows it to work.
        """
        logging.debug(" I'm able to listen")
        while True:
            logging.debug(" I'm listening ")
            if self.semaphore[0] == 1:
                if len(self.active_questions) > 0:
                    for question in self.active_questions:
                        print(question)
                        question.set_timestamp(self.episoder)
                    self.semaphore[2] = 1
            else:
                time.sleep(3)
            time.sleep(1)
        #    logging.debug(" Cannot listen anymore ")

    def answering_service(self):
        """
        Answering thread ,focused on answering questions delivered by listening thread and processed by mind thread
        Puts itself to sleep after it answers the question.
        """
        while True:
            logging.debug(" I'm able to answer")
            if self.semaphore[1] == 1:
                if len(self.answers) == 0:
                    self.semaphore[1] = 0
                else:
                    for answer in self.answers:
                        print("Based on observations taken in moment of " + str(self.memory.get_episode()) + " "
                              + answer)
                        self.answers.remove(answer)
                    self.semaphore[1] = 0
            else:
                time.sleep(3)
        #   logging.debug(" Exiting ")

    def mind(self):
        """
        Thread responsible for processing data either acquired by other threads or the one in memory in order
         to process them and perfect it's cognitive abilities
        """
        logging.debug(" Mind is present ")
        while True:
            logging.debug(" thinking... ")
            if self.semaphore[2] == 1:
                if self.new_observations_flag:
                    bp = self.preparations.prepare_bps(self.episoder, self.obs)
                    self.memory.add_bp(bp)
                    self.new_observations_flag = False
                    print("Observations have been transformed into properly built base profiles")
                self.semaphore[2] = 0
                if self.episoder % 5 == 0:
                    self.memory.update_em_all(self.episoder)

                if len(self.active_questions) == 0:
                    self.semaphore[2] = 0
                else:
                    for question in self.active_questions:
                        self.answers.append(str(question.ask()))
                        self.active_questions.remove(question)
                    self.semaphore[1] = 1
                    self.semaphore[2] = 0

            else:
                time.sleep(2)
                self.episoder += 1
        #    logging.debug(" Falling asleep ")

    def capture(self):
        """
        Thread responsible for capturing new observations,whenever it does,it sets mind semaphore to awake
        thread to process them. It's always active.
        """
        inner_timer = 0
        while True:
            logging.debug(" Watching ")
            if self.semaphore[3] == 1:
                if inner_timer < self.episoder:
                    self.capture_observations(self.episoder)
                    time.sleep(1)
                    self.new_observations_flag = True
            #       self.semaphore[3] = 0
                    self.semaphore[2] = 1
                    inner_timer += 1
                else:
                    time.sleep(2)
            else:
                time.sleep(2)
        #    logging.debug(" I'm done ")

    def __init__(self):
        self.preparations = Preparations()
        self.memory = WokeMemory(None, None, self.preparations.ims)
        self.is_busy = False
        self.thread_listening = threading.Thread(name='Questions_go_here ', target=self.listening_service)
        self.thread_answering = threading.Thread(name=' Answers_derive_from_here',
                                                 target=self.answering_service)
        self.thread_mind = threading.Thread(name='Processing_data_happens_here', target=self.mind)
        self.thread_capturing = threading.Thread(name=' Gathering data for collective', target=self.capture)
        self.obs = []
        self.active_questions = []
        self.episoder = 0
        self.new_observations_flag = False
        self.answers = []
        self.semaphore = [0, 0, 0, 0]
        #        threads [listening, answering, mind, capturing]

    def capture_observations(self, timer):
        """
        Captures observations in given moment
        :param timer: episode which we use to acquire observations from
        """
        print("Receiving observations")
        self.obs = self.preparations.get_observations_with_episode(timer)
        if len(self.obs) == 0:
            print("No observations at " + str(timer))
        else:
            self.is_busy = True
            print("Captured " + str(len(self.obs)) + " observations at " + str(self.episoder))
            self.is_busy = False
            self.new_observations_flag = True

if __name__ == "__main__":
    a = MultiThreadCycle()
    a.main()


