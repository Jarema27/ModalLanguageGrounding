from sc.pwr.inz.memory.WokeMemory import WokeMemory
from src.sc.pwr.inz.cycle.Preparations import Preparations
import logging
import time
import threading


class MultiThreadCycle:

    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s (%(threadName)-2s) %(message)s',
                        )

    def main(self):
        self.thread_listening.start()
        self.thread_answering.start()
        self.thread_mind.start()
        self.thread_capturing.start()

        self.semaphore[3] = 1
        self.semaphore[0] = 1

        if self.time % 5 == 0:
            self.semaphore[2] = 1

    def listening_service(self):
        logging.debug(" I'm able to listen")
        while True:
            logging.debug(" I'm listening ")
            if self.semaphore[0] == 1:
                pass
            else:
                time.sleep(3)
            time.sleep(1)
        #    logging.debug(" Cannot listen anymore ")

    def answering_service(self):
        while True:
            logging.debug(" I'm able to answer")
            if self.semaphore[1] == 1:
                pass
            else:
                time.sleep(3)
        #   logging.debug(" Exiting ")

    def mind(self):
        logging.debug(" Mind is present ")
        while True:
            logging.debug(" thinking... ")
            if self.semaphore[2] == 1:
                if self.new_observations_flag:
                    bp = self.preparations.prepare_bps(self.time, self.obs)
                    self.memory.add_bp(bp)
                    print("Observations have been transformed into properly built base profiles")
                self.semaphore[2] = 0
                if self.time % 5 == 0:
                    self.memory.update_em_all(self.time)
            else:
                time.sleep(3)
        #    logging.debug(" Falling asleep ")

    def capture(self):

        while True:
            logging.debug(" Watching ")
            if self.semaphore[3] == 1:
                self.capture_observations(self.time)
                time.sleep(1)
                self.semaphore[3] = 0
                self.semaphore[2] = 1
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
        self.time = 0
        self.new_observations_flag = False
        self.semaphore = [0, 0, 0, 0]
        #        threads [listening, answering, mind, capturing]

    def capture_observations(self, timer):
        print("Receiving observations")
        self.obs = self.preparations.get_observations_with_timestamp(timer)
        if len(self.obs) == 0:
            print("No observations at " + str(timer))
        else:
            self.is_busy = True
            print("Captured " + str(len(self.obs)) + " observations")
            self.is_busy = False
            self.new_observations_flag = True

if __name__ == "__main__":
    a = MultiThreadCycle()
    a.main()
