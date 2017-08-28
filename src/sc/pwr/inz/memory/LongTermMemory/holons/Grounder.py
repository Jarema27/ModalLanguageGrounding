from src.sc.pwr.inz.memory.LongTermMemory.semantic.language.components.State import State
from src.sc.pwr.inz.memory.LongTermMemory.semantic.language.components.LogicalOperator import LogicalOperator

"""
Module involves methods essential for establishing tao in Holons.
As it seems this old 500loc module wasn't so necessary after all.
"""


class Grounder:
    @staticmethod
    def determine_fulfilment(dk, formula, context=None):
        """
        Method determines fulfilment for SimpleFormula it basically counts appearances of Observations in which
        formula was fulfilled a.e when carpet indeed was red.
        :param dk : DistributedKnowledge: contains most of data which we will seek truth in
        :param context: Context : Context under which we take BP into consideration
        :param formula: Formula : Given formula we'd want to find answer for
        :return int : Number of times given formula was observed
        """
        if (dk.get_formula().get_type() == formula.get_type()) and (formula in dk.get_complementary_formulas()):
            count = 0
            if context is not None and len(context) != 0:
                bloop = context
            else:
                bloop = dk.get_bpset()
            for bp in bloop:
                if bp.check_if_observed(formula.get_model().get_identifier(),
                                        formula.get_traits()[0], formula.get_states()[0]):
                    count += 1
            return count
        else:
            raise AttributeError("Either you gave me wrong formula,or Distributed Knowledge which doesn't belong to it")

    @staticmethod
    def determine_fulfilment_ident(dk, formula, context=None):
        if (dk.get_formula().get_type() == formula.get_type()) and (formula in dk.get_complementary_formulas()):
            count = 0
            if context is not None and len(context) != 0:
                bloop = context
            else:
                bloop = dk.get_bpset()
            is1 = None
            is2 = None
            if formula.get_states()[0] == State.IS:
                is1 = True
            else:
                is1 = False
            if formula.get_states()[1] == State.IS:
                is2 = True
            else:
                is2 = False
            for bp in bloop:
                if formula.get_logical_operator() == LogicalOperator.AND:
                    if ((formula.get_subjects()[0] in bp.give_subjects_involved()) == is1) and \
                            ((formula.get_subjects()[1] in bp.give_subjects_involved()) == is2):
                        count += 1
                if formula.get_logical_operator() == LogicalOperator.OR:
                    if ((formula.get_subjects()[0] in bp.give_subjects_involved()) == is1) or\
                            ((formula.get_subjects()[1] in bp.give_subjects_involved()) == is2):
                        count += 1
            return count

    @staticmethod
    def determine_fulfilment_cf(dk, formula, context=None):
        """
        Method determines fulfilment for ComplexFormula it basically counts appearances of Observations in which
        formula was fulfilled a.e when carpet indeed was red and fluffy.
        :param dk:  DistributedKnowledge: contains most of data which we will seek truth in
        :param formula: Formula : Given formula we'd want to find answer for
        :param context: Context : Context under which we take BP into consideration
        :return int : Number of times given formula was observed
        """
        if (dk.get_formula().get_type() == formula.get_type()) and (formula in dk.get_complementary_formulas()):
            count = 0
            if context is not None and len(context) != 0:
                bloop = context
            else:
                bloop = dk.get_bpset()
            for bp in bloop:
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
