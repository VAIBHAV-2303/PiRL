from collections import defaultdict

import tensorflow as tf
from PiRL.DataStructures.Token import NonTerminal, Terminal
from treelib.node import Node
from treelib.tree import Tree
from .CodegenFns import function_lookup, input_map


def TFCodegen(node : Node, tree : Tree):
    children = list(map(lambda nid: tree.get_node(nid), node.successors(tree.identifier)))

    child_codes = []
    for child_code in list(map(lambda child: TFCodegen(child, tree), children)):
        if isinstance(child_code, list):
            for item in child_code:
                child_codes.append(item)
        else:
            child_codes.append(child_code)

    if isinstance(node.data, NonTerminal):
        fn = function_lookup[node.data.name]
        return fn(node, tree, child_codes)

    if isinstance(node.data, Terminal):
        return None

def callGraph(graph_fn, inputs : dict):
    input_map.update(inputs)
    return graph_fn()