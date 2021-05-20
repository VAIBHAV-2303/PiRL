from antlr4.CommonTokenStream import CommonTokenStream
from antlr4.StdinStream import StdinStream
from treelib import Node, Tree
import random

import PiRL
from PiRL import rule_table
from PiRL.ProgramGen.SketchBuilderVisitor import SketchBuilderVisitor
from PiRL.GrammarParser import MetaGrammarLexer, MetaGrammarVisitor
from PiRL.GrammarParser.MetaGrammarParser import MetaGrammarParser
from PiRL.ProgramGen.ParseTreeGenerator import getProgTree

def generatePool(N,  maxDepth, tree, rule_table, debug=False):

	# Collecting all non-terminal nodes
	nodeIDs = []
	for nodeID in tree.expand_tree(mode=Tree.DEPTH):
		nodeType = tree[nodeID].data
		if isinstance(nodeType, PiRL.DataStructures.Token.NonTerminal):
			nodeIDs.append(nodeID) 

	neighbours = []
	for _ in range(N):
		# Making a deep copy
		newTree = Tree(tree=tree, deep=True)

		# Selecting a random non-terminal to be replaced
		nodeToReplaceID = random.choice(nodeIDs)
		
		# Generating a new subtree
		newSubTree = getProgTree(newTree[nodeToReplaceID].data, maxDepth - newTree.depth(nodeToReplaceID))

		# Replacing subtree
		try:
			newTree.replace_node(newTree[nodeToReplaceID].predecessor(newTree.identifier), nodeToReplaceID, newSubTree, deep=False)
		except Exception as e:
			# traceback.print_exc()
			if debug:
				print("Root node replaced") 
			newTree = newSubTree

		if debug:
			print("Generated neighbour:", end=' ')
			# newTree.show(data_property='str')
			for leaf in newTree.leaves():
			    print(leaf.data.name, end=' ')
			print("\n")		

		neighbours.append(newTree)

	return neighbours


if __name__ == "__main__":

	# Generating rule table
	lexer = MetaGrammarLexer.MetaGrammarLexer(StdinStream())
	token_stream = CommonTokenStream(lexer)
	parser = MetaGrammarParser(token_stream)
	tree = parser.sketch()
	tree.accept(SketchBuilderVisitor())

	# Generating random program
	tree = getProgTree(rule_table.start, 7)

	print("Given program:", end=' ')
	for leaf in tree.leaves():
	    print(leaf.data.name, end=' ')
	print("\n")

	generatePool(N=5, maxDepth=4, tree=tree, rule_table=rule_table, debug=True)