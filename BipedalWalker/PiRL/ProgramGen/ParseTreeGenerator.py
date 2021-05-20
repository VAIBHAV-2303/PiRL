from PiRL.Utils.TreeUtils import newTree
from PiRL.DataStructures.Token import NonTerminal, Terminal, Token
from PiRL.DataStructures.RuleTable import Rule
from PiRL import rule_table

from treelib import Tree, Node

import random

__isValidDepth = {}

def checkRuleDepth(rule : Rule, depth : int):
    if (rule, depth) in __isValidDepth:
        return __isValidDepth[(rule, depth)]

    if depth == 1:
        non_terminals = list(filter(lambda x : isinstance(x, NonTerminal), rule.rhs))
        return len(non_terminals) == 0

    for token in rule.rhs:
        if isinstance(token, NonTerminal):
            valid_rules = list(filter(
                            lambda rule: checkRuleDepth(rule, depth-1), 
                            rule_table.getAllRules(token)
                        ))
            if len(valid_rules) == 0:
                print(rule, depth, token)
                __isValidDepth[(rule, depth)] = False
                break
    
    __isValidDepth[(rule, depth)] = True
    return __isValidDepth[(rule, depth)]

def generate(tree : Tree, parent : Node, token : Token, depth : int):
    node = tree.create_node(parent = parent, data = token)
    if isinstance(token, Terminal):
        return

    valid_rules = list(filter(
                    lambda rule : checkRuleDepth(rule, depth), 
                    rule_table.getAllRules(token)
                ))
    
    # print(token, valid_rules)
    rule = random.choice(valid_rules)
    list(map(lambda next_token: generate(tree, node, next_token, depth-1), rule.rhs))

    node.data.text = ' '.join(list(map(lambda leaf: leaf.data.name, tree.leaves(node.identifier))))

def getProgTree(start_token, depth):
    tree = newTree()
    generate(tree, parent=None, token=start_token, depth=depth)

    return tree