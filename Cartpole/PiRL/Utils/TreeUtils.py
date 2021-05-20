from typing import Union
from treelib import Tree, Node

def newTree(id=None, copy_from : Tree = None, deep_copy : bool = False) -> Tree:
    return Tree(tree=copy_from, deep = deep_copy, identifier=id)

def addNode(tree : Tree, node : Node, parent : Node = None):
    """add existing node to a tree

    Args:
        tree (Tree): [description]
        node (Node): [description]
        parent (Node, optional): Defaults to Root.
    """
    if parent is None:
        parent = tree.root

    tree.add_node(node, parent)

def createNode(tree : Tree, tag = None, id = None, parent : Union[str, Node] = None, data = None):
    return tree.create_node(tag = tag, identifier=id, parent=parent, data=data)