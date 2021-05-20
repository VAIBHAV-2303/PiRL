
from PiRL.DataStructures.Token import Terminal, NonTerminal
from PiRL.GrammarParser import MetaGrammarVisitor
from PiRL.GrammarParser.MetaGrammarParser import MetaGrammarParser

from PiRL import rule_table

from functools import reduce

class SketchBuilderVisitor(MetaGrammarVisitor.MetaGrammarVisitor):
    def __init__(self) -> None:
        super().__init__()

    def visitTerminal_group(self, ctx: MetaGrammarParser.Terminal_groupContext):
        return [Terminal(str(item)) for item in ctx.TERMINAL()]

    def visitNon_terminal_group(self, ctx: MetaGrammarParser.Non_terminal_groupContext):
        return [NonTerminal(str(item).strip("<>")) for item in ctx.NON_TERMINAL()]

    def visitExpansion(self, ctx: MetaGrammarParser.ExpansionContext):
        result = self.visitChildren(ctx)
        return list(reduce(lambda agg, item: agg + item, result, []))
    
    def visitRhs(self, ctx: MetaGrammarParser.RhsContext):
        result = self.defaultResult()
        for expansion_ctx in ctx.expansion():
            child = expansion_ctx.accept(self)
            result = self.aggregateResult(result, child)

        return result

    def visitStart(self, ctx: MetaGrammarParser.StartContext):
        result = ctx.non_terminal_group().accept(self)
        assert len(result) == 1 , f"only 1 start symbol allowed; found {result}"
        rule_table.start = result[0]

    def visitProduction(self, ctx: MetaGrammarParser.ProductionContext):
        lhs = ctx.non_terminal_group().accept(self)
        rhs = ctx.rhs().accept(self)

        assert len(lhs) == 1, "only 1 non terminal lhs allowed in a prod"
        lhs = lhs[0]

        for expansion in rhs:
            rule_table.addRule(lhs, expansion)
            
    #region aggregation
    def defaultResult(self):
        return []

    def aggregateResult(self, aggregate, nextResult):
        aggregate.append(nextResult)
        return aggregate

    #endregion
