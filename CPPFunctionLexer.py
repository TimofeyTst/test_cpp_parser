# Generated from CPPFunction.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\20")
        buf.write("V\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\3\2\3\2\3\3\3\3\3\4\3\4\3\4\3\4\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f")
        buf.write("\3\r\3\r\7\rF\n\r\f\r\16\rI\13\r\3\16\6\16L\n\16\r\16")
        buf.write("\16\16M\3\17\6\17Q\n\17\r\17\16\17R\3\17\3\17\2\2\20\3")
        buf.write("\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16")
        buf.write("\33\17\35\20\3\2\6\5\2C\\aac|\6\2\62;C\\aac|\3\2\62;\5")
        buf.write("\2\13\f\17\17\"\"\2X\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2")
        buf.write("\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2")
        buf.write("\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31")
        buf.write("\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\3\37\3\2\2\2\5!\3\2")
        buf.write("\2\2\7#\3\2\2\2\t\'\3\2\2\2\13,\3\2\2\2\r\62\3\2\2\2\17")
        buf.write("9\3\2\2\2\21;\3\2\2\2\23=\3\2\2\2\25?\3\2\2\2\27A\3\2")
        buf.write("\2\2\31C\3\2\2\2\33K\3\2\2\2\35P\3\2\2\2\37 \7*\2\2 \4")
        buf.write("\3\2\2\2!\"\7+\2\2\"\6\3\2\2\2#$\7k\2\2$%\7p\2\2%&\7v")
        buf.write("\2\2&\b\3\2\2\2\'(\7e\2\2()\7j\2\2)*\7c\2\2*+\7t\2\2+")
        buf.write("\n\3\2\2\2,-\7h\2\2-.\7n\2\2./\7q\2\2/\60\7c\2\2\60\61")
        buf.write("\7v\2\2\61\f\3\2\2\2\62\63\7f\2\2\63\64\7q\2\2\64\65\7")
        buf.write("w\2\2\65\66\7d\2\2\66\67\7n\2\2\678\7g\2\28\16\3\2\2\2")
        buf.write("9:\7.\2\2:\20\3\2\2\2;<\7}\2\2<\22\3\2\2\2=>\7\177\2\2")
        buf.write(">\24\3\2\2\2?@\7=\2\2@\26\3\2\2\2AB\7?\2\2B\30\3\2\2\2")
        buf.write("CG\t\2\2\2DF\t\3\2\2ED\3\2\2\2FI\3\2\2\2GE\3\2\2\2GH\3")
        buf.write("\2\2\2H\32\3\2\2\2IG\3\2\2\2JL\t\4\2\2KJ\3\2\2\2LM\3\2")
        buf.write("\2\2MK\3\2\2\2MN\3\2\2\2N\34\3\2\2\2OQ\t\5\2\2PO\3\2\2")
        buf.write("\2QR\3\2\2\2RP\3\2\2\2RS\3\2\2\2ST\3\2\2\2TU\b\17\2\2")
        buf.write("U\36\3\2\2\2\6\2GMR\3\b\2\2")
        return buf.getvalue()


class CPPFunctionLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    ID = 12
    INT_CONST = 13
    WS = 14

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'int'", "'char'", "'float'", "'double'", "','", 
            "'{'", "'}'", "';'", "'='" ]

    symbolicNames = [ "<INVALID>",
            "ID", "INT_CONST", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "ID", "INT_CONST", "WS" ]

    grammarFileName = "CPPFunction.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


