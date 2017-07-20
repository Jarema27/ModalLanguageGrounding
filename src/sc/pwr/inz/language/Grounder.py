
class Grounder:

    @staticmethod
    def determine_fulfilment(dk, formula):
        if dk.get_formula().get_type() == formula.get_type() and formula in dk.get_complementary_formulas():
            count = 0
            for bp in dk.get_bpset():
                if bp.check_if_observed(formula.get_model().get_identifier(), formula.get_traits(), formula.get_states()):
                    count += 1
            return count/len(dk.get_bpset())
        else:
            raise AttributeError("Either you gave me wrong formula,or Distributed Knowledge which doesn't belong to it")
        return 0
