# Generated from CPPFunction.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\21")
        buf.write("P\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\5\7\5\'\n\5\f\5")
        buf.write("\16\5*\13\5\3\6\3\6\3\6\3\7\3\7\3\7\7\7\62\n\7\f\7\16")
        buf.write("\7\65\13\7\3\7\3\7\3\b\3\b\3\b\3\b\3\t\3\t\3\t\7\t@\n")
        buf.write("\t\f\t\16\tC\13\t\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\f")
        buf.write("\3\f\5\fN\n\f\3\f\2\2\r\2\4\6\b\n\f\16\20\22\24\26\2\3")
        buf.write("\3\2\5\t\2I\2\30\3\2\2\2\4\37\3\2\2\2\6!\3\2\2\2\b#\3")
        buf.write("\2\2\2\n+\3\2\2\2\f.\3\2\2\2\168\3\2\2\2\20<\3\2\2\2\22")
        buf.write("D\3\2\2\2\24G\3\2\2\2\26M\3\2\2\2\30\31\5\4\3\2\31\32")
        buf.write("\5\6\4\2\32\33\7\3\2\2\33\34\5\b\5\2\34\35\7\4\2\2\35")
        buf.write("\36\5\f\7\2\36\3\3\2\2\2\37 \t\2\2\2 \5\3\2\2\2!\"\7\17")
        buf.write("\2\2\"\7\3\2\2\2#(\5\n\6\2$%\7\n\2\2%\'\5\n\6\2&$\3\2")
        buf.write("\2\2\'*\3\2\2\2(&\3\2\2\2()\3\2\2\2)\t\3\2\2\2*(\3\2\2")
        buf.write("\2+,\5\4\3\2,-\5\6\4\2-\13\3\2\2\2.\63\7\13\2\2/\62\5")
        buf.write("\16\b\2\60\62\5\22\n\2\61/\3\2\2\2\61\60\3\2\2\2\62\65")
        buf.write("\3\2\2\2\63\61\3\2\2\2\63\64\3\2\2\2\64\66\3\2\2\2\65")
        buf.write("\63\3\2\2\2\66\67\7\f\2\2\67\r\3\2\2\289\5\4\3\29:\5\20")
        buf.write("\t\2:;\7\r\2\2;\17\3\2\2\2<A\5\6\4\2=>\7\n\2\2>@\5\6\4")
        buf.write("\2?=\3\2\2\2@C\3\2\2\2A?\3\2\2\2AB\3\2\2\2B\21\3\2\2\2")
        buf.write("CA\3\2\2\2DE\5\24\13\2EF\7\r\2\2F\23\3\2\2\2GH\5\6\4\2")
        buf.write("HI\7\16\2\2IJ\5\26\f\2J\25\3\2\2\2KN\5\6\4\2LN\7\20\2")
        buf.write("\2MK\3\2\2\2ML\3\2\2\2N\27\3\2\2\2\7(\61\63AM")
        return buf.getvalue()


class CPPFunctionParser ( Parser ):

    grammarFileName = "CPPFunction.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'int'", "'char'", "'float'", 
                     "'double'", "'bool'", "','", "'{'", "'}'", "';'", "'='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "ID", "INT_CONST", "WS" ]

    RULE_function = 0
    RULE_type_specifier = 1
    RULE_identifier = 2
    RULE_parameter_list = 3
    RULE_parameter = 4
    RULE_compound_statement = 5
    RULE_declaration = 6
    RULE_identifier_list = 7
    RULE_statement = 8
    RULE_assignment_statement = 9
    RULE_expression = 10

    ruleNames =  [ "function", "type_specifier", "identifier", "parameter_list", 
                   "parameter", "compound_statement", "declaration", "identifier_list", 
                   "statement", "assignment_statement", "expression" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    ID=13
    INT_CONST=14
    WS=15

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class FunctionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_specifier(self):
            return self.getTypedRuleContext(CPPFunctionParser.Type_specifierContext,0)


        def identifier(self):
            return self.getTypedRuleContext(CPPFunctionParser.IdentifierContext,0)


        def parameter_list(self):
            return self.getTypedRuleContext(CPPFunctionParser.Parameter_listContext,0)


        def compound_statement(self):
            return self.getTypedRuleContext(CPPFunctionParser.Compound_statementContext,0)


        def getRuleIndex(self):
            return CPPFunctionParser.RULE_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction" ):
                listener.enterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction" ):
                listener.exitFunction(self)




    def function(self):

        localctx = CPPFunctionParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_function)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.type_specifier()
            self.state = 23
            self.identifier()
            self.state = 24
            self.match(CPPFunctionParser.T__0)
            self.state = 25
            self.parameter_list()
            self.state = 26
            self.match(CPPFunctionParser.T__1)
            self.state = 27
            self.compound_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Type_specifierContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CPPFunctionParser.RULE_type_specifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType_specifier" ):
                listener.enterType_specifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType_specifier" ):
                listener.exitType_specifier(self)




    def type_specifier(self):

        localctx = CPPFunctionParser.Type_specifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_type_specifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CPPFunctionParser.T__2) | (1 << CPPFunctionParser.T__3) | (1 << CPPFunctionParser.T__4) | (1 << CPPFunctionParser.T__5) | (1 << CPPFunctionParser.T__6))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IdentifierContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CPPFunctionParser.ID, 0)

        def getRuleIndex(self):
            return CPPFunctionParser.RULE_identifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifier" ):
                listener.enterIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifier" ):
                listener.exitIdentifier(self)




    def identifier(self):

        localctx = CPPFunctionParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.match(CPPFunctionParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Parameter_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CPPFunctionParser.ParameterContext)
            else:
                return self.getTypedRuleContext(CPPFunctionParser.ParameterContext,i)


        def getRuleIndex(self):
            return CPPFunctionParser.RULE_parameter_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameter_list" ):
                listener.enterParameter_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameter_list" ):
                listener.exitParameter_list(self)




    def parameter_list(self):

        localctx = CPPFunctionParser.Parameter_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_parameter_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self.parameter()
            self.state = 38
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CPPFunctionParser.T__7:
                self.state = 34
                self.match(CPPFunctionParser.T__7)
                self.state = 35
                self.parameter()
                self.state = 40
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ParameterContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_specifier(self):
            return self.getTypedRuleContext(CPPFunctionParser.Type_specifierContext,0)


        def identifier(self):
            return self.getTypedRuleContext(CPPFunctionParser.IdentifierContext,0)


        def getRuleIndex(self):
            return CPPFunctionParser.RULE_parameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameter" ):
                listener.enterParameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameter" ):
                listener.exitParameter(self)




    def parameter(self):

        localctx = CPPFunctionParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.type_specifier()
            self.state = 42
            self.identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Compound_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CPPFunctionParser.DeclarationContext)
            else:
                return self.getTypedRuleContext(CPPFunctionParser.DeclarationContext,i)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CPPFunctionParser.StatementContext)
            else:
                return self.getTypedRuleContext(CPPFunctionParser.StatementContext,i)


        def getRuleIndex(self):
            return CPPFunctionParser.RULE_compound_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompound_statement" ):
                listener.enterCompound_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompound_statement" ):
                listener.exitCompound_statement(self)




    def compound_statement(self):

        localctx = CPPFunctionParser.Compound_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_compound_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(CPPFunctionParser.T__8)
            self.state = 49
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CPPFunctionParser.T__2) | (1 << CPPFunctionParser.T__3) | (1 << CPPFunctionParser.T__4) | (1 << CPPFunctionParser.T__5) | (1 << CPPFunctionParser.T__6) | (1 << CPPFunctionParser.ID))) != 0):
                self.state = 47
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [CPPFunctionParser.T__2, CPPFunctionParser.T__3, CPPFunctionParser.T__4, CPPFunctionParser.T__5, CPPFunctionParser.T__6]:
                    self.state = 45
                    self.declaration()
                    pass
                elif token in [CPPFunctionParser.ID]:
                    self.state = 46
                    self.statement()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 51
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 52
            self.match(CPPFunctionParser.T__9)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_specifier(self):
            return self.getTypedRuleContext(CPPFunctionParser.Type_specifierContext,0)


        def identifier_list(self):
            return self.getTypedRuleContext(CPPFunctionParser.Identifier_listContext,0)


        def getRuleIndex(self):
            return CPPFunctionParser.RULE_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration" ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration" ):
                listener.exitDeclaration(self)




    def declaration(self):

        localctx = CPPFunctionParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.type_specifier()
            self.state = 55
            self.identifier_list()
            self.state = 56
            self.match(CPPFunctionParser.T__10)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Identifier_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CPPFunctionParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(CPPFunctionParser.IdentifierContext,i)


        def getRuleIndex(self):
            return CPPFunctionParser.RULE_identifier_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifier_list" ):
                listener.enterIdentifier_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifier_list" ):
                listener.exitIdentifier_list(self)




    def identifier_list(self):

        localctx = CPPFunctionParser.Identifier_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_identifier_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.identifier()
            self.state = 63
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CPPFunctionParser.T__7:
                self.state = 59
                self.match(CPPFunctionParser.T__7)
                self.state = 60
                self.identifier()
                self.state = 65
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment_statement(self):
            return self.getTypedRuleContext(CPPFunctionParser.Assignment_statementContext,0)


        def getRuleIndex(self):
            return CPPFunctionParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = CPPFunctionParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.assignment_statement()
            self.state = 67
            self.match(CPPFunctionParser.T__10)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Assignment_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(CPPFunctionParser.IdentifierContext,0)


        def expression(self):
            return self.getTypedRuleContext(CPPFunctionParser.ExpressionContext,0)


        def getRuleIndex(self):
            return CPPFunctionParser.RULE_assignment_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment_statement" ):
                listener.enterAssignment_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment_statement" ):
                listener.exitAssignment_statement(self)




    def assignment_statement(self):

        localctx = CPPFunctionParser.Assignment_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_assignment_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.identifier()
            self.state = 70
            self.match(CPPFunctionParser.T__11)
            self.state = 71
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(CPPFunctionParser.IdentifierContext,0)


        def INT_CONST(self):
            return self.getToken(CPPFunctionParser.INT_CONST, 0)

        def getRuleIndex(self):
            return CPPFunctionParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = CPPFunctionParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_expression)
        try:
            self.state = 75
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CPPFunctionParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 73
                self.identifier()
                pass
            elif token in [CPPFunctionParser.INT_CONST]:
                self.enterOuterAlt(localctx, 2)
                self.state = 74
                self.match(CPPFunctionParser.INT_CONST)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





