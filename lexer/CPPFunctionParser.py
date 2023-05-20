# Generated from CPPFunction.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\22")
        buf.write("S\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\3\2\3\2\3\2")
        buf.write("\5\2\35\n\2\3\2\3\2\5\2!\n\2\3\3\3\3\3\4\3\4\3\5\3\5\3")
        buf.write("\5\7\5*\n\5\f\5\16\5-\13\5\3\6\3\6\3\6\3\7\3\7\3\7\7\7")
        buf.write("\65\n\7\f\7\16\78\13\7\3\7\3\7\3\b\3\b\3\b\3\b\3\t\3\t")
        buf.write("\3\t\7\tC\n\t\f\t\16\tF\13\t\3\n\3\n\3\n\3\13\3\13\3\13")
        buf.write("\3\13\3\f\3\f\5\fQ\n\f\3\f\2\2\r\2\4\6\b\n\f\16\20\22")
        buf.write("\24\26\2\3\3\2\5\n\2N\2\30\3\2\2\2\4\"\3\2\2\2\6$\3\2")
        buf.write("\2\2\b&\3\2\2\2\n.\3\2\2\2\f\61\3\2\2\2\16;\3\2\2\2\20")
        buf.write("?\3\2\2\2\22G\3\2\2\2\24J\3\2\2\2\26P\3\2\2\2\30\31\5")
        buf.write("\4\3\2\31\32\5\6\4\2\32\34\7\3\2\2\33\35\5\b\5\2\34\33")
        buf.write("\3\2\2\2\34\35\3\2\2\2\35\36\3\2\2\2\36 \7\4\2\2\37!\5")
        buf.write("\f\7\2 \37\3\2\2\2 !\3\2\2\2!\3\3\2\2\2\"#\t\2\2\2#\5")
        buf.write("\3\2\2\2$%\7\20\2\2%\7\3\2\2\2&+\5\n\6\2\'(\7\13\2\2(")
        buf.write("*\5\n\6\2)\'\3\2\2\2*-\3\2\2\2+)\3\2\2\2+,\3\2\2\2,\t")
        buf.write("\3\2\2\2-+\3\2\2\2./\5\4\3\2/\60\5\6\4\2\60\13\3\2\2\2")
        buf.write("\61\66\7\f\2\2\62\65\5\16\b\2\63\65\5\22\n\2\64\62\3\2")
        buf.write("\2\2\64\63\3\2\2\2\658\3\2\2\2\66\64\3\2\2\2\66\67\3\2")
        buf.write("\2\2\679\3\2\2\28\66\3\2\2\29:\7\r\2\2:\r\3\2\2\2;<\5")
        buf.write("\4\3\2<=\5\20\t\2=>\7\16\2\2>\17\3\2\2\2?D\5\6\4\2@A\7")
        buf.write("\13\2\2AC\5\6\4\2B@\3\2\2\2CF\3\2\2\2DB\3\2\2\2DE\3\2")
        buf.write("\2\2E\21\3\2\2\2FD\3\2\2\2GH\5\24\13\2HI\7\16\2\2I\23")
        buf.write("\3\2\2\2JK\5\6\4\2KL\7\17\2\2LM\5\26\f\2M\25\3\2\2\2N")
        buf.write("Q\5\6\4\2OQ\7\21\2\2PN\3\2\2\2PO\3\2\2\2Q\27\3\2\2\2\t")
        buf.write("\34 +\64\66DP")
        return buf.getvalue()


class CPPFunctionParser ( Parser ):

    grammarFileName = "CPPFunction.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'void'", "'int'", "'char'", 
                     "'float'", "'double'", "'bool'", "','", "'{'", "'}'", 
                     "';'", "'='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "ID", "INT_CONST", "WS" ]

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
    T__12=13
    ID=14
    INT_CONST=15
    WS=16

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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.type_specifier()
            self.state = 23
            self.identifier()
            self.state = 24
            self.match(CPPFunctionParser.T__0)
            self.state = 26
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CPPFunctionParser.T__2) | (1 << CPPFunctionParser.T__3) | (1 << CPPFunctionParser.T__4) | (1 << CPPFunctionParser.T__5) | (1 << CPPFunctionParser.T__6) | (1 << CPPFunctionParser.T__7))) != 0):
                self.state = 25
                self.parameter_list()


            self.state = 28
            self.match(CPPFunctionParser.T__1)
            self.state = 30
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CPPFunctionParser.T__9:
                self.state = 29
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
            self.state = 32
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CPPFunctionParser.T__2) | (1 << CPPFunctionParser.T__3) | (1 << CPPFunctionParser.T__4) | (1 << CPPFunctionParser.T__5) | (1 << CPPFunctionParser.T__6) | (1 << CPPFunctionParser.T__7))) != 0)):
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
            self.state = 34
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
            self.state = 36
            self.parameter()
            self.state = 41
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CPPFunctionParser.T__8:
                self.state = 37
                self.match(CPPFunctionParser.T__8)
                self.state = 38
                self.parameter()
                self.state = 43
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
            self.state = 44
            self.type_specifier()
            self.state = 45
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
            self.state = 47
            self.match(CPPFunctionParser.T__9)
            self.state = 52
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CPPFunctionParser.T__2) | (1 << CPPFunctionParser.T__3) | (1 << CPPFunctionParser.T__4) | (1 << CPPFunctionParser.T__5) | (1 << CPPFunctionParser.T__6) | (1 << CPPFunctionParser.T__7) | (1 << CPPFunctionParser.ID))) != 0):
                self.state = 50
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [CPPFunctionParser.T__2, CPPFunctionParser.T__3, CPPFunctionParser.T__4, CPPFunctionParser.T__5, CPPFunctionParser.T__6, CPPFunctionParser.T__7]:
                    self.state = 48
                    self.declaration()
                    pass
                elif token in [CPPFunctionParser.ID]:
                    self.state = 49
                    self.statement()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 54
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 55
            self.match(CPPFunctionParser.T__10)
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
            self.state = 57
            self.type_specifier()
            self.state = 58
            self.identifier_list()
            self.state = 59
            self.match(CPPFunctionParser.T__11)
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
            self.state = 61
            self.identifier()
            self.state = 66
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CPPFunctionParser.T__8:
                self.state = 62
                self.match(CPPFunctionParser.T__8)
                self.state = 63
                self.identifier()
                self.state = 68
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
            self.state = 69
            self.assignment_statement()
            self.state = 70
            self.match(CPPFunctionParser.T__11)
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
            self.state = 72
            self.identifier()
            self.state = 73
            self.match(CPPFunctionParser.T__12)
            self.state = 74
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
            self.state = 78
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CPPFunctionParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 76
                self.identifier()
                pass
            elif token in [CPPFunctionParser.INT_CONST]:
                self.enterOuterAlt(localctx, 2)
                self.state = 77
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





