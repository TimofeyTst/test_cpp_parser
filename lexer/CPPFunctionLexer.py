# Generated from CPPFunction.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\22")
        buf.write("d\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\3\2\3\2\3\3\3\3\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3")
        buf.write("\16\3\16\3\17\3\17\7\17T\n\17\f\17\16\17W\13\17\3\20\6")
        buf.write("\20Z\n\20\r\20\16\20[\3\21\6\21_\n\21\r\21\16\21`\3\21")
        buf.write("\3\21\2\2\22\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13")
        buf.write("\25\f\27\r\31\16\33\17\35\20\37\21!\22\3\2\6\5\2C\\aa")
        buf.write("c|\6\2\62;C\\aac|\3\2\62;\5\2\13\f\17\17\"\"\2f\2\3\3")
        buf.write("\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2")
        buf.write("\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2")
        buf.write("\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2")
        buf.write("\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\3#\3\2\2\2\5%\3\2")
        buf.write("\2\2\7\'\3\2\2\2\t,\3\2\2\2\13\60\3\2\2\2\r\65\3\2\2\2")
        buf.write("\17;\3\2\2\2\21B\3\2\2\2\23G\3\2\2\2\25I\3\2\2\2\27K\3")
        buf.write("\2\2\2\31M\3\2\2\2\33O\3\2\2\2\35Q\3\2\2\2\37Y\3\2\2\2")
        buf.write("!^\3\2\2\2#$\7*\2\2$\4\3\2\2\2%&\7+\2\2&\6\3\2\2\2\'(")
        buf.write("\7x\2\2()\7q\2\2)*\7k\2\2*+\7f\2\2+\b\3\2\2\2,-\7k\2\2")
        buf.write("-.\7p\2\2./\7v\2\2/\n\3\2\2\2\60\61\7e\2\2\61\62\7j\2")
        buf.write("\2\62\63\7c\2\2\63\64\7t\2\2\64\f\3\2\2\2\65\66\7h\2\2")
        buf.write("\66\67\7n\2\2\678\7q\2\289\7c\2\29:\7v\2\2:\16\3\2\2\2")
        buf.write(";<\7f\2\2<=\7q\2\2=>\7w\2\2>?\7d\2\2?@\7n\2\2@A\7g\2\2")
        buf.write("A\20\3\2\2\2BC\7d\2\2CD\7q\2\2DE\7q\2\2EF\7n\2\2F\22\3")
        buf.write("\2\2\2GH\7.\2\2H\24\3\2\2\2IJ\7}\2\2J\26\3\2\2\2KL\7\177")
        buf.write("\2\2L\30\3\2\2\2MN\7=\2\2N\32\3\2\2\2OP\7?\2\2P\34\3\2")
        buf.write("\2\2QU\t\2\2\2RT\t\3\2\2SR\3\2\2\2TW\3\2\2\2US\3\2\2\2")
        buf.write("UV\3\2\2\2V\36\3\2\2\2WU\3\2\2\2XZ\t\4\2\2YX\3\2\2\2Z")
        buf.write("[\3\2\2\2[Y\3\2\2\2[\\\3\2\2\2\\ \3\2\2\2]_\t\5\2\2^]")
        buf.write("\3\2\2\2_`\3\2\2\2`^\3\2\2\2`a\3\2\2\2ab\3\2\2\2bc\b\21")
        buf.write("\2\2c\"\3\2\2\2\6\2U[`\3\b\2\2")
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
    T__12 = 13
    ID = 14
    INT_CONST = 15
    WS = 16

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'void'", "'int'", "'char'", "'float'", "'double'", 
            "'bool'", "','", "'{'", "'}'", "';'", "'='" ]

    symbolicNames = [ "<INVALID>",
            "ID", "INT_CONST", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "ID", 
                  "INT_CONST", "WS" ]

    grammarFileName = "CPPFunction.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


