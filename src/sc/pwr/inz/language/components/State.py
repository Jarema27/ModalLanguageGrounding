from enum import Enum


class State(Enum):
    IS = 1
    IS_NOT = 2
    MAYHAPS = 0

    def andS(fst, sec):
        possible_answers = {(State.IS, State.IS): State.IS,
                            (State.IS, State.IS_NOT): State.MAYHAPS,
                            (State.IS, State.MAYHAPS): State.MAYHAPS,
                            (State.IS_NOT, State.IS_NOT): State.IS_NOT,
                            (State.MAYHAPS, State.MAYHAPS): State.MAYHAPS,
                            (State.IS_NOT, State.MAYHAPS): State.MAYHAPS}
        return possible_answers.get((fst, sec)) if not possible_answers.get((fst, sec)) is None else \
            possible_answers.get((sec, fst))

    def orS(fst,sec):
        possible_answers = {(State.IS, State.IS): State.IS,
                            (State.IS, State.IS_NOT): State.MAYHAPS,
                            (State.IS, State.MAYHAPS): State.IS,
                            (State.IS_NOT, State.IS_NOT): State.IS_NOT,
                            (State.MAYHAPS, State.MAYHAPS): State.MAYHAPS,
                            (State.IS_NOT, State.MAYHAPS): State.IS_NOT}
        return possible_answers.get((fst, sec)) if not possible_answers.get((fst, sec)) is None else \
            possible_answers.get((sec, fst))

    def notS(giv):
        if giv == State.IS:
            return State.IS_NOT
        if giv == State.IS_NOT:
            return State.IS
        if giv == State.MAYHAPS:
            return State.MAYHAPS

    def __str__(giv):
        if giv == State.IS:
            return " is "
        if giv == State.IS_NOT:
            return " is_not "
        if giv == State.MAYHAPS:
            return " might_be "
