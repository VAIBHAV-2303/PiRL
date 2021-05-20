# Generated from MetaGrammar.g4 by ANTLR 4.9.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MetaGrammarParser import MetaGrammarParser
else:
    from MetaGrammarParser import MetaGrammarParser

# This class defines a complete generic visitor for a parse tree produced by MetaGrammarParser.

class MetaGrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MetaGrammarParser#sketch.
    def visitSketch(self, ctx:MetaGrammarParser.SketchContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MetaGrammarParser#start.
    def visitStart(self, ctx:MetaGrammarParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MetaGrammarParser#production.
    def visitProduction(self, ctx:MetaGrammarParser.ProductionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MetaGrammarParser#rhs.
    def visitRhs(self, ctx:MetaGrammarParser.RhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MetaGrammarParser#expansion.
    def visitExpansion(self, ctx:MetaGrammarParser.ExpansionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MetaGrammarParser#terminal_group.
    def visitTerminal_group(self, ctx:MetaGrammarParser.Terminal_groupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MetaGrammarParser#non_terminal_group.
    def visitNon_terminal_group(self, ctx:MetaGrammarParser.Non_terminal_groupContext):
        return self.visitChildren(ctx)



del MetaGrammarParser