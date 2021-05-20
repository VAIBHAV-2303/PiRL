# Generated from MetaGrammar.g4 by ANTLR 4.9.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\b")
        buf.write(";\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\3\2\3\2\6\2\23\n\2\r\2\16\2\24\3\3\3\3\3\3\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\5\3\5\3\5\6\5\"\n\5\r\5\16\5#\7\5&\n")
        buf.write("\5\f\5\16\5)\13\5\3\6\3\6\6\6-\n\6\r\6\16\6.\3\7\6\7\62")
        buf.write("\n\7\r\7\16\7\63\3\b\6\b\67\n\b\r\b\16\b8\3\b\2\2\t\2")
        buf.write("\4\6\b\n\f\16\2\2\2:\2\20\3\2\2\2\4\26\3\2\2\2\6\31\3")
        buf.write("\2\2\2\b\36\3\2\2\2\n,\3\2\2\2\f\61\3\2\2\2\16\66\3\2")
        buf.write("\2\2\20\22\5\4\3\2\21\23\5\6\4\2\22\21\3\2\2\2\23\24\3")
        buf.write("\2\2\2\24\22\3\2\2\2\24\25\3\2\2\2\25\3\3\2\2\2\26\27")
        buf.write("\5\16\b\2\27\30\7\3\2\2\30\5\3\2\2\2\31\32\5\16\b\2\32")
        buf.write("\33\7\4\2\2\33\34\5\b\5\2\34\35\7\3\2\2\35\7\3\2\2\2\36")
        buf.write("\'\5\n\6\2\37!\7\5\2\2 \"\5\n\6\2! \3\2\2\2\"#\3\2\2\2")
        buf.write("#!\3\2\2\2#$\3\2\2\2$&\3\2\2\2%\37\3\2\2\2&)\3\2\2\2\'")
        buf.write("%\3\2\2\2\'(\3\2\2\2(\t\3\2\2\2)\'\3\2\2\2*-\5\16\b\2")
        buf.write("+-\5\f\7\2,*\3\2\2\2,+\3\2\2\2-.\3\2\2\2.,\3\2\2\2./\3")
        buf.write("\2\2\2/\13\3\2\2\2\60\62\7\7\2\2\61\60\3\2\2\2\62\63\3")
        buf.write("\2\2\2\63\61\3\2\2\2\63\64\3\2\2\2\64\r\3\2\2\2\65\67")
        buf.write("\7\6\2\2\66\65\3\2\2\2\678\3\2\2\28\66\3\2\2\289\3\2\2")
        buf.write("\29\17\3\2\2\2\t\24#\',.\638")
        return buf.getvalue()


class MetaGrammarParser ( Parser ):

    grammarFileName = "MetaGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'->'", "'|'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "NON_TERMINAL", "TERMINAL", "NS" ]

    RULE_sketch = 0
    RULE_start = 1
    RULE_production = 2
    RULE_rhs = 3
    RULE_expansion = 4
    RULE_terminal_group = 5
    RULE_non_terminal_group = 6

    ruleNames =  [ "sketch", "start", "production", "rhs", "expansion", 
                   "terminal_group", "non_terminal_group" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    NON_TERMINAL=4
    TERMINAL=5
    NS=6

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class SketchContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def start(self):
            return self.getTypedRuleContext(MetaGrammarParser.StartContext,0)


        def production(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MetaGrammarParser.ProductionContext)
            else:
                return self.getTypedRuleContext(MetaGrammarParser.ProductionContext,i)


        def getRuleIndex(self):
            return MetaGrammarParser.RULE_sketch

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSketch" ):
                return visitor.visitSketch(self)
            else:
                return visitor.visitChildren(self)




    def sketch(self):

        localctx = MetaGrammarParser.SketchContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_sketch)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.start()
            self.state = 16 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 15
                self.production()
                self.state = 18 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MetaGrammarParser.NON_TERMINAL):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def non_terminal_group(self):
            return self.getTypedRuleContext(MetaGrammarParser.Non_terminal_groupContext,0)


        def getRuleIndex(self):
            return MetaGrammarParser.RULE_start

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStart" ):
                return visitor.visitStart(self)
            else:
                return visitor.visitChildren(self)




    def start(self):

        localctx = MetaGrammarParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self.non_terminal_group()
            self.state = 21
            self.match(MetaGrammarParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProductionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def non_terminal_group(self):
            return self.getTypedRuleContext(MetaGrammarParser.Non_terminal_groupContext,0)


        def rhs(self):
            return self.getTypedRuleContext(MetaGrammarParser.RhsContext,0)


        def getRuleIndex(self):
            return MetaGrammarParser.RULE_production

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProduction" ):
                return visitor.visitProduction(self)
            else:
                return visitor.visitChildren(self)




    def production(self):

        localctx = MetaGrammarParser.ProductionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_production)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self.non_terminal_group()
            self.state = 24
            self.match(MetaGrammarParser.T__1)
            self.state = 25
            self.rhs()
            self.state = 26
            self.match(MetaGrammarParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expansion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MetaGrammarParser.ExpansionContext)
            else:
                return self.getTypedRuleContext(MetaGrammarParser.ExpansionContext,i)


        def getRuleIndex(self):
            return MetaGrammarParser.RULE_rhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRhs" ):
                return visitor.visitRhs(self)
            else:
                return visitor.visitChildren(self)




    def rhs(self):

        localctx = MetaGrammarParser.RhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_rhs)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.expansion()
            self.state = 37
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MetaGrammarParser.T__2:
                self.state = 29
                self.match(MetaGrammarParser.T__2)
                self.state = 31 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 30
                    self.expansion()
                    self.state = 33 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==MetaGrammarParser.NON_TERMINAL or _la==MetaGrammarParser.TERMINAL):
                        break

                self.state = 39
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpansionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def non_terminal_group(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MetaGrammarParser.Non_terminal_groupContext)
            else:
                return self.getTypedRuleContext(MetaGrammarParser.Non_terminal_groupContext,i)


        def terminal_group(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MetaGrammarParser.Terminal_groupContext)
            else:
                return self.getTypedRuleContext(MetaGrammarParser.Terminal_groupContext,i)


        def getRuleIndex(self):
            return MetaGrammarParser.RULE_expansion

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpansion" ):
                return visitor.visitExpansion(self)
            else:
                return visitor.visitChildren(self)




    def expansion(self):

        localctx = MetaGrammarParser.ExpansionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_expansion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 42
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [MetaGrammarParser.NON_TERMINAL]:
                        self.state = 40
                        self.non_terminal_group()
                        pass
                    elif token in [MetaGrammarParser.TERMINAL]:
                        self.state = 41
                        self.terminal_group()
                        pass
                    else:
                        raise NoViableAltException(self)


                else:
                    raise NoViableAltException(self)
                self.state = 44 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Terminal_groupContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TERMINAL(self, i:int=None):
            if i is None:
                return self.getTokens(MetaGrammarParser.TERMINAL)
            else:
                return self.getToken(MetaGrammarParser.TERMINAL, i)

        def getRuleIndex(self):
            return MetaGrammarParser.RULE_terminal_group

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerminal_group" ):
                return visitor.visitTerminal_group(self)
            else:
                return visitor.visitChildren(self)




    def terminal_group(self):

        localctx = MetaGrammarParser.Terminal_groupContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_terminal_group)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 46
                    self.match(MetaGrammarParser.TERMINAL)

                else:
                    raise NoViableAltException(self)
                self.state = 49 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Non_terminal_groupContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NON_TERMINAL(self, i:int=None):
            if i is None:
                return self.getTokens(MetaGrammarParser.NON_TERMINAL)
            else:
                return self.getToken(MetaGrammarParser.NON_TERMINAL, i)

        def getRuleIndex(self):
            return MetaGrammarParser.RULE_non_terminal_group

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNon_terminal_group" ):
                return visitor.visitNon_terminal_group(self)
            else:
                return visitor.visitChildren(self)




    def non_terminal_group(self):

        localctx = MetaGrammarParser.Non_terminal_groupContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_non_terminal_group)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 51
                    self.match(MetaGrammarParser.NON_TERMINAL)

                else:
                    raise NoViableAltException(self)
                self.state = 54 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





