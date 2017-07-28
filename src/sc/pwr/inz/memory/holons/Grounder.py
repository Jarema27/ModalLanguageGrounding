from src.sc.pwr.inz.language.components.LogicalOperator import LogicalOperator


class Grounder:
    @staticmethod
    def determine_fulfilment(dk, formula):
        if (dk.get_formula().get_type() == formula.get_type()) and (formula == dk.get_formula()):
            count = 0
            for bp in dk.get_bpset():
                if bp.check_if_observed(formula.get_model().get_identifier(),
                                        formula.get_traits()[0], formula.get_states()[0]):
                    count += 1
            return count
        else:
            raise AttributeError("Either you gave me wrong formula,or Distributed Knowledge which doesn't belong to it")

    @staticmethod
    def determine_fulfilment_cf(dk, formula):
        if (dk.get_formula().get_type() == formula.get_type()) and (formula == dk.get_formula()):
            count = 0
            for bp in dk.get_bpset():
                if formula.get_logical_operator() == LogicalOperator.AND:
                    if bp.check_if_observed(formula.get_model().get_identifier(), formula.get_traits()[0],
                                            formula.get_states()[0]) and \
                            bp.check_if_observed(formula.get_model().get_identifier(), formula.get_traits()[1],
                                                 formula.get_states()[1]):
                        count += 1
                if formula.get_logical_operator() == LogicalOperator.OR:
                    if bp.check_if_observed(formula.get_model().get_identifier(), formula.get_traits()[0],
                                            formula.get_states()[0]) or \
                            bp.check_if_observed(formula.get_model().get_identifier(), formula.get_traits()[1],
                                                 formula.get_states()[1]):
                        count += 1
                if formula.get_logical_operator() == LogicalOperator.XOR:
                    if (bp.check_if_observed(formula.get_model().get_identifier(), formula.get_traits()[0],
                                             formula.get_states()[0]) and not
                        bp.check_if_observed(formula.get_model().get_identifier(), formula.get_traits()[1],
                                             formula.get_states()[1])) or (not
                                                                    bp.check_if_observed(
                                                                           formula.get_model().get_identifier(),
                                                                           formula.get_traits()[0],
                                                                           formula.get_states()[0]) and
                                                                           bp.check_if_observed(
                                                                               formula.get_model().get_identifier(),
                                                                               formula.get_traits()[1],
                                                                               formula.get_states()[1])):
                        count += 1
                    return count
            return count
        else:
            raise AttributeError("Either you gave me wrong formula,or Distributed Knowledge "
                                 "which doesn't belong to it")
