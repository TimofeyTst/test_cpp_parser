# Generated from CPPFunction.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\21")
        buf.write("]\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\3\2\3\2\3\3\3\3\3\4\3\4\3\4")
        buf.write("\3\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\n")
        buf.write("\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\7\16M\n\16\f")
        buf.write("\16\16\16P\13\16\3\17\6\17S\n\17\r\17\16\17T\3\20\6\20")
        buf.write("X\n\20\r\20\16\20Y\3\20\3\20\2\2\21\3\3\5\4\7\5\t\6\13")
        buf.write("\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37")
        buf.write("\21\3\2\6\5\2C\\aac|\6\2\62;C\\aac|\3\2\62;\5\2\13\f\17")
        buf.write("\17\"\"\2_\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2")
        buf.write("\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2")
        buf.write("\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2")
        buf.write("\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\3!\3\2\2\2\5#")
        buf.write("\3\2\2\2\7%\3\2\2\2\t)\3\2\2\2\13.\3\2\2\2\r\64\3\2\2")
        buf.write("\2\17;\3\2\2\2\21@\3\2\2\2\23B\3\2\2\2\25D\3\2\2\2\27")
        buf.write("F\3\2\2\2\31H\3\2\2\2\33J\3\2\2\2\35R\3\2\2\2\37W\3\2")
        buf.write("\2\2!\"\7*\2\2\"\4\3\2\2\2#$\7+\2\2$\6\3\2\2\2%&\7k\2")
        buf.write("\2&\'\7p\2\2\'(\7v\2\2(\b\3\2\2\2)*\7e\2\2*+\7j\2\2+,")
        buf.write("\7c\2\2,-\7t\2\2-\n\3\2\2\2./\7h\2\2/\60\7n\2\2\60\61")
        buf.write("\7q\2\2\61\62\7c\2\2\62\63\7v\2\2\63\f\3\2\2\2\64\65\7")
        buf.write("f\2\2\65\66\7q\2\2\66\67\7w\2\2\678\7d\2\289\7n\2\29:")
        buf.write("\7g\2\2:\16\3\2\2\2;<\7d\2\2<=\7q\2\2=>\7q\2\2>?\7n\2")
        buf.write("\2?\20\3\2\2\2@A\7.\2\2A\22\3\2\2\2BC\7}\2\2C\24\3\2\2")
        buf.write("\2DE\7\177\2\2E\26\3\2\2\2FG\7=\2\2G\30\3\2\2\2HI\7?\2")
        buf.write("\2I\32\3\2\2\2JN\t\2\2\2KM\t\3\2\2LK\3\2\2\2MP\3\2\2\2")
        buf.write("NL\3\2\2\2NO\3\2\2\2O\34\3\2\2\2PN\3\2\2\2QS\t\4\2\2R")
        buf.write("Q\3\2\2\2ST\3\2\2\2TR\3\2\2\2TU\3\2\2\2U\36\3\2\2\2VX")
        buf.write("\t\5\2\2WV\3\2\2\2XY\3\2\2\2YW\3\2\2\2YZ\3\2\2\2Z[\3\2")
        buf.write("\2\2[\\\b\20\2\2\\ \3\2\2\2\6\2NTY\3\b\2\2")
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
    T__11 = 12
    ID = 13
    INT_CONST = 14
    WS = 15

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'int'", "'char'", "'float'", "'double'", "'bool'", 
            "','", "'{'", "'}'", "';'", "'='" ]

    symbolicNames = [ "<INVALID>",
            "ID", "INT_CONST", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "ID", "INT_CONST", 
                  "WS" ]

    grammarFileName = "CPPFunction.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


