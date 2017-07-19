from src.sc.pwr.inz.language.Formula import Formula,TypeOfFormula
from src.sc.pwr.inz.language.Trait import Trait
from src.sc.pwr.inz.language.State import State


class SimpleFormula(Formula):

    def get_states(self):
        return self.state

    def get_model(self):
        return self.indiv_model

    def get_type(self):
        return TypeOfFormula.SF

    def get_complementary_formulas(self):
        temp2 = SimpleFormula(self.indiv_model, self.trait, self.state.notS())
        return [self, temp2]

    def __eq__(self, other):
        return self.state == other.state and self.indiv_model == other.indiv_model and self.trait == other.trait

    def __init__(self, im, trait, state):
        super().__init__()
        if not isinstance(trait, Trait):
            raise TypeError("Given trait ain't instance of Trait")
        if im is not None and trait is not None:
            if trait in im.get_object_type().get_traits():
                self.indiv_model = im
                self.trait = trait
                if state is None:
                    self.state = State.IS_NOT
                else:
                    self.state = state
        else:
            raise Exception("Obligatory fields include variables with None value")

    def get_traits(self):
        return [self.trait]

    def __hash__(self):
        return hash(self.indiv_model) ^ hash(self.trait)
