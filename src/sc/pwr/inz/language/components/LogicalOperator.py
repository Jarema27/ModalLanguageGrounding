from enum import Enum

"""
Logical Operator Enum represents logical operators present in common speech
"""


class LogicalOperator(Enum):
    OR = 'OR'
    AND = 'AND'
    XOR = 'XOR'

    def __str__(self):
        if self.AND:
            return 'and'
        if self.OR:
            return 'or'
        if self.XOR:
            return 'either of em'
