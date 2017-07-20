from src.sc.pwr.inz.language.Formula import TypeOfFormula

class Grounder():

    def __init__(self):
        pass

    @staticmethod
    def determine_fulfilment(dk, formula):
        if dk.get_formula().get_type() == formula.get_type() and  dk.get_formula() == formula:
            count = 0
            for bp in dk.get_bpset():
                if bp.check_if_observed(formula.get_model().get_identifier(), formula.get_traits(), formula.get_states()):
                    count += 1
            return count
        else:
            raise AttributeError("Either you gave me wrong formula,or Distributed Knowledge which doesn't belong to it")
        return 0
