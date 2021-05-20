from PiRL.Utils import TreeUtils
from PiRL.DataStructures.Token import NonTerminal, Token
from typing import List


class Rule:
    def __init__(self, NT : NonTerminal, rhs : List[Token]):
        self.NT = NT
        self.rhs = rhs

    def __eq__(self, o):
        return self.NT == o.NT and self.rhs == o.rhs

    def __str__(self):
        return f"Rule({self.NT} -> {self.rhs})" 
    
    def __repr__(self) -> str:
        return str(self)

    def __hash__(self) -> int:
        return hash(str(self))
    @property
    def str(self):
        return str(self)

    @property
    def tree(self):
        if hasattr(self, '_tree'):
            return self._tree

        self._tree = TreeUtils.newTree()
        root = TreeUtils.createNode(self._tree, data=self.NT)
        for token in self.rhs:
            TreeUtils.createNode(self._tree, data=token, parent=root)

        return self._tree

        
class RuleTable:
    def __init__(self):
        self.table : List[Rule] = []

    def addRule(self, NT:NonTerminal, rhs: List[Token]):
        new_rule = Rule(NT, rhs)

        for rule in self.table:
            if rule == new_rule:
                return rule
        
        self.table.append(new_rule)
        new_rule.id = len(self.table)
        return new_rule

    def getAllRules(self, NT:NonTerminal = None):
        if NT is None:
            return self.table
        else:
            return [rule for rule in self.table if rule.NT == NT]

    @property
    def start(self):
        return self._start

    @start.setter
    def start(self, value : NonTerminal):
        self._start = value
