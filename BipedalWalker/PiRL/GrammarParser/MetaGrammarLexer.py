# Generated from MetaGrammar.g4 by ANTLR 4.9.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\b")
        buf.write("9\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\3\2\3\2\3\3\3\3\3\3\3\4\3\4\3\5\3\5\6\5\31\n\5\r\5\16")
        buf.write("\5\32\3\5\3\5\3\6\5\6 \n\6\3\6\6\6#\n\6\r\6\16\6$\3\6")
        buf.write("\6\6(\n\6\r\6\16\6)\3\6\6\6-\n\6\r\6\16\6.\5\6\61\n\6")
        buf.write("\3\7\6\7\64\n\7\r\7\16\7\65\3\7\3\7\2\2\b\3\3\5\4\7\5")
        buf.write("\t\6\13\7\r\b\3\2\7\5\2\62;C\\c|\6\2\60\60\62;C\\c|\5")
        buf.write("\2,-//??\5\2*+..@@\4\2\13\f\"\"\2@\2\3\3\2\2\2\2\5\3\2")
        buf.write("\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2")
        buf.write("\3\17\3\2\2\2\5\21\3\2\2\2\7\24\3\2\2\2\t\26\3\2\2\2\13")
        buf.write("\60\3\2\2\2\r\63\3\2\2\2\17\20\7=\2\2\20\4\3\2\2\2\21")
        buf.write("\22\7/\2\2\22\23\7@\2\2\23\6\3\2\2\2\24\25\7~\2\2\25\b")
        buf.write("\3\2\2\2\26\30\7>\2\2\27\31\t\2\2\2\30\27\3\2\2\2\31\32")
        buf.write("\3\2\2\2\32\30\3\2\2\2\32\33\3\2\2\2\33\34\3\2\2\2\34")
        buf.write("\35\7@\2\2\35\n\3\2\2\2\36 \7/\2\2\37\36\3\2\2\2\37 \3")
        buf.write("\2\2\2 \"\3\2\2\2!#\t\3\2\2\"!\3\2\2\2#$\3\2\2\2$\"\3")
        buf.write("\2\2\2$%\3\2\2\2%\61\3\2\2\2&(\t\4\2\2\'&\3\2\2\2()\3")
        buf.write("\2\2\2)\'\3\2\2\2)*\3\2\2\2*\61\3\2\2\2+-\t\5\2\2,+\3")
        buf.write("\2\2\2-.\3\2\2\2.,\3\2\2\2./\3\2\2\2/\61\3\2\2\2\60\37")
        buf.write("\3\2\2\2\60\'\3\2\2\2\60,\3\2\2\2\61\f\3\2\2\2\62\64\t")
        buf.write("\6\2\2\63\62\3\2\2\2\64\65\3\2\2\2\65\63\3\2\2\2\65\66")
        buf.write("\3\2\2\2\66\67\3\2\2\2\678\b\7\2\28\16\3\2\2\2\n\2\32")
        buf.write("\37$).\60\65\3\b\2\2")
        return buf.getvalue()


class MetaGrammarLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    NON_TERMINAL = 4
    TERMINAL = 5
    NS = 6

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "';'", "'->'", "'|'" ]

    symbolicNames = [ "<INVALID>",
            "NON_TERMINAL", "TERMINAL", "NS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "NON_TERMINAL", "TERMINAL", "NS" ]

    grammarFileName = "MetaGrammar.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


