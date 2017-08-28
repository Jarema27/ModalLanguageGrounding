from enum import Enum

"""
Enum represents possible state of object, IS - when we can certainly tell that something was observed,
IS_NOT when we're certain that we didn't observe such trait
MAYHAPS - When we're not sure whether thing we observed was or was not
"""


class State(Enum):
    IS = 1
    IS_NOT = 2
    MAYHAPS = 0

    def andS(self, fst, sec):
        possible_answers = {(State.IS, State.IS): State.IS,
                            (State.IS, State.IS_NOT): State.MAYHAPS,
                            (State.IS, State.MAYHAPS): State.MAYHAPS,
                            (State.IS_NOT, State.IS_NOT): State.IS_NOT,
                            (State.MAYHAPS, State.MAYHAPS): State.MAYHAPS,
                            (State.IS_NOT, State.MAYHAPS): State.MAYHAPS}
        return possible_answers.get((fst, sec)) if not possible_answers.get((fst, sec)) is None else \
            possible_answers.get((sec, fst))

    def orS(self, fst, sec):
        possible_answers = {(State.IS, State.IS): State.IS,
                            (State.IS, State.IS_NOT): State.IS,
                            (State.IS, State.MAYHAPS): State.IS,
                            (State.IS_NOT, State.IS_NOT): State.IS_NOT,
                            (State.MAYHAPS, State.MAYHAPS): State.MAYHAPS,
                            (State.IS_NOT, State.MAYHAPS): State.IS_NOT}
        return possible_answers.get((fst, sec)) if not possible_answers.get((fst, sec)) is None else \
            possible_answers.get((sec, fst))

    def notS(self, giv):
        if giv == State.IS:
            return State.IS_NOT
        if giv == State.IS_NOT:
            return State.IS
        if giv == State.MAYHAPS:
            return State.MAYHAPS

    def __str__(self, other):
        if other == State.IS:
            return " is "
        if other == State.IS_NOT:
            return " is_not "
        if other == State.MAYHAPS:
            return " might_be "
