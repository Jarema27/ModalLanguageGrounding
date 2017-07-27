from src.sc.pwr.inz.speech.Phonograph import Phonograph


class RiseAndShine:

    def __init__(self):
        self.phonograph = Phonograph()

    @staticmethod
    def main():
        print('a')

    def read_it_out(self, sentence):
        self.phonograph.read_something_up(sentence)


if __name__ == "__main__":
    a = RiseAndShine()
    a.main()
