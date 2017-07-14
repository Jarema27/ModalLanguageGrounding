from enum import Enum

class State(Enum):
    IS = 1
    IS_NOT = 2
    MAYHAPS = 0

    def andS(self, first, second):
        possible_answers = {(State.IS, State.IS): State.IS,
                            (State.IS, State.IS_NOT): State.MAYHAPS,
                            (State.IS, State.MAYHAPS): State.MAYHAPS,
                            (State.IS_NOT, State.IS_NOT): State.IS_NOT,
                            (State.MAYHAPS, State.MAYHAPS): State.MAYHAPS,
                            (State.IS_NOT, State.MAYHAPS): State.MAYHAPS}
        return possible_answers.get((first, second)) if not None else possible_answers.get((second,first))