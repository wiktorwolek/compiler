# Generated from Expr.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,16,86,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,3,0,26,8,0,1,0,
        5,0,29,8,0,10,0,12,0,32,9,0,1,0,1,0,1,1,1,1,1,1,3,1,39,8,1,1,2,1,
        2,1,2,1,2,1,3,1,3,1,3,1,4,1,4,1,4,1,5,1,5,3,5,53,8,5,1,6,1,6,3,6,
        57,8,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,70,8,7,1,
        8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,11,1,11,1,11,
        0,0,12,0,2,4,6,8,10,12,14,16,18,20,22,0,1,1,0,9,10,84,0,30,1,0,0,
        0,2,38,1,0,0,0,4,40,1,0,0,0,6,44,1,0,0,0,8,47,1,0,0,0,10,52,1,0,
        0,0,12,56,1,0,0,0,14,69,1,0,0,0,16,71,1,0,0,0,18,75,1,0,0,0,20,79,
        1,0,0,0,22,83,1,0,0,0,24,26,3,2,1,0,25,24,1,0,0,0,25,26,1,0,0,0,
        26,27,1,0,0,0,27,29,5,15,0,0,28,25,1,0,0,0,29,32,1,0,0,0,30,28,1,
        0,0,0,30,31,1,0,0,0,31,33,1,0,0,0,32,30,1,0,0,0,33,34,5,1,0,0,34,
        1,1,0,0,0,35,39,3,6,3,0,36,39,3,4,2,0,37,39,3,8,4,0,38,35,1,0,0,
        0,38,36,1,0,0,0,38,37,1,0,0,0,39,3,1,0,0,0,40,41,5,9,0,0,41,42,5,
        2,0,0,42,43,3,10,5,0,43,5,1,0,0,0,44,45,5,5,0,0,45,46,5,9,0,0,46,
        7,1,0,0,0,47,48,5,6,0,0,48,49,5,9,0,0,49,9,1,0,0,0,50,53,3,12,6,
        0,51,53,3,16,8,0,52,50,1,0,0,0,52,51,1,0,0,0,53,11,1,0,0,0,54,57,
        3,14,7,0,55,57,3,18,9,0,56,54,1,0,0,0,56,55,1,0,0,0,57,13,1,0,0,
        0,58,70,5,10,0,0,59,70,5,11,0,0,60,61,5,7,0,0,61,70,3,14,7,0,62,
        63,5,8,0,0,63,70,3,14,7,0,64,65,5,3,0,0,65,66,3,10,5,0,66,67,5,4,
        0,0,67,70,1,0,0,0,68,70,5,9,0,0,69,58,1,0,0,0,69,59,1,0,0,0,69,60,
        1,0,0,0,69,62,1,0,0,0,69,64,1,0,0,0,69,68,1,0,0,0,70,15,1,0,0,0,
        71,72,3,12,6,0,72,73,5,12,0,0,73,74,3,10,5,0,74,17,1,0,0,0,75,76,
        3,14,7,0,76,77,5,13,0,0,77,78,3,14,7,0,78,19,1,0,0,0,79,80,3,14,
        7,0,80,81,5,14,0,0,81,82,3,14,7,0,82,21,1,0,0,0,83,84,7,0,0,0,84,
        23,1,0,0,0,6,25,30,38,52,56,69
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'<EOF>'", "'='", "'('", "')'", "'write'", 
                     "'read'", "'(int)'", "'(real)'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'+'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "WRITE", "READ", "TOINT", "TOREAL", "ID", 
                      "INT", "REAL", "ADDOP", "MULOP", "DIVOP", "NEWLINE", 
                      "WS" ]

    RULE_prog = 0
    RULE_statement = 1
    RULE_assign = 2
    RULE_write = 3
    RULE_read = 4
    RULE_expression = 5
    RULE_expression1 = 6
    RULE_expression2 = 7
    RULE_add = 8
    RULE_multiply = 9
    RULE_divide = 10
    RULE_value = 11

    ruleNames =  [ "prog", "statement", "assign", "write", "read", "expression", 
                   "expression1", "expression2", "add", "multiply", "divide", 
                   "value" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    WRITE=5
    READ=6
    TOINT=7
    TOREAL=8
    ID=9
    INT=10
    REAL=11
    ADDOP=12
    MULOP=13
    DIVOP=14
    NEWLINE=15
    WS=16

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.NEWLINE)
            else:
                return self.getToken(ExprParser.NEWLINE, i)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.StatementContext)
            else:
                return self.getTypedRuleContext(ExprParser.StatementContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = ExprParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 33376) != 0):
                self.state = 25
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 608) != 0):
                    self.state = 24
                    self.statement()


                self.state = 27
                self.match(ExprParser.NEWLINE)
                self.state = 32
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 33
            self.match(ExprParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def write(self):
            return self.getTypedRuleContext(ExprParser.WriteContext,0)


        def assign(self):
            return self.getTypedRuleContext(ExprParser.AssignContext,0)


        def read(self):
            return self.getTypedRuleContext(ExprParser.ReadContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = ExprParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 38
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 35
                self.write()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 36
                self.assign()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 3)
                self.state = 37
                self.read()
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


    class AssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def expression(self):
            return self.getTypedRuleContext(ExprParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_assign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)




    def assign(self):

        localctx = ExprParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.match(ExprParser.ID)
            self.state = 41
            self.match(ExprParser.T__1)
            self.state = 42
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WriteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WRITE(self):
            return self.getToken(ExprParser.WRITE, 0)

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_write

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWrite" ):
                listener.enterWrite(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWrite" ):
                listener.exitWrite(self)




    def write(self):

        localctx = ExprParser.WriteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_write)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(ExprParser.WRITE)
            self.state = 45
            self.match(ExprParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReadContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def READ(self):
            return self.getToken(ExprParser.READ, 0)

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_read

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRead" ):
                listener.enterRead(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRead" ):
                listener.exitRead(self)




    def read(self):

        localctx = ExprParser.ReadContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_read)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(ExprParser.READ)
            self.state = 48
            self.match(ExprParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression1(self):
            return self.getTypedRuleContext(ExprParser.Expression1Context,0)


        def add(self):
            return self.getTypedRuleContext(ExprParser.AddContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = ExprParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_expression)
        try:
            self.state = 52
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 50
                self.expression1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 51
                self.add()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression2(self):
            return self.getTypedRuleContext(ExprParser.Expression2Context,0)


        def multiply(self):
            return self.getTypedRuleContext(ExprParser.MultiplyContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_expression1

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression1" ):
                listener.enterExpression1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression1" ):
                listener.exitExpression1(self)




    def expression1(self):

        localctx = ExprParser.Expression1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_expression1)
        try:
            self.state = 56
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 54
                self.expression2()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 55
                self.multiply()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_expression2

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ParContext(Expression2Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.Expression2Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(ExprParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPar" ):
                listener.enterPar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPar" ):
                listener.exitPar(self)


    class TointContext(Expression2Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.Expression2Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def TOINT(self):
            return self.getToken(ExprParser.TOINT, 0)
        def expression2(self):
            return self.getTypedRuleContext(ExprParser.Expression2Context,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterToint" ):
                listener.enterToint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitToint" ):
                listener.exitToint(self)


    class TorealContext(Expression2Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.Expression2Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def TOREAL(self):
            return self.getToken(ExprParser.TOREAL, 0)
        def expression2(self):
            return self.getTypedRuleContext(ExprParser.Expression2Context,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterToreal" ):
                listener.enterToreal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitToreal" ):
                listener.exitToreal(self)


    class RealContext(Expression2Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.Expression2Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def REAL(self):
            return self.getToken(ExprParser.REAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReal" ):
                listener.enterReal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReal" ):
                listener.exitReal(self)


    class IdContext(Expression2Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.Expression2Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId" ):
                listener.enterId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId" ):
                listener.exitId(self)


    class IntContext(Expression2Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.Expression2Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(ExprParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt" ):
                listener.enterInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt" ):
                listener.exitInt(self)



    def expression2(self):

        localctx = ExprParser.Expression2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_expression2)
        try:
            self.state = 69
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                localctx = ExprParser.IntContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 58
                self.match(ExprParser.INT)
                pass
            elif token in [11]:
                localctx = ExprParser.RealContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 59
                self.match(ExprParser.REAL)
                pass
            elif token in [7]:
                localctx = ExprParser.TointContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 60
                self.match(ExprParser.TOINT)
                self.state = 61
                self.expression2()
                pass
            elif token in [8]:
                localctx = ExprParser.TorealContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 62
                self.match(ExprParser.TOREAL)
                self.state = 63
                self.expression2()
                pass
            elif token in [3]:
                localctx = ExprParser.ParContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 64
                self.match(ExprParser.T__2)
                self.state = 65
                self.expression()
                self.state = 66
                self.match(ExprParser.T__3)
                pass
            elif token in [9]:
                localctx = ExprParser.IdContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 68
                self.match(ExprParser.ID)
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


    class AddContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression1(self):
            return self.getTypedRuleContext(ExprParser.Expression1Context,0)


        def ADDOP(self):
            return self.getToken(ExprParser.ADDOP, 0)

        def expression(self):
            return self.getTypedRuleContext(ExprParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_add

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdd" ):
                listener.enterAdd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdd" ):
                listener.exitAdd(self)




    def add(self):

        localctx = ExprParser.AddContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_add)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.expression1()
            self.state = 72
            self.match(ExprParser.ADDOP)
            self.state = 73
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiplyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.Expression2Context)
            else:
                return self.getTypedRuleContext(ExprParser.Expression2Context,i)


        def MULOP(self):
            return self.getToken(ExprParser.MULOP, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_multiply

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiply" ):
                listener.enterMultiply(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiply" ):
                listener.exitMultiply(self)




    def multiply(self):

        localctx = ExprParser.MultiplyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_multiply)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.expression2()
            self.state = 76
            self.match(ExprParser.MULOP)
            self.state = 77
            self.expression2()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DivideContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.Expression2Context)
            else:
                return self.getTypedRuleContext(ExprParser.Expression2Context,i)


        def DIVOP(self):
            return self.getToken(ExprParser.DIVOP, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_divide

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDivide" ):
                listener.enterDivide(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDivide" ):
                listener.exitDivide(self)




    def divide(self):

        localctx = ExprParser.DivideContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_divide)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.expression2()
            self.state = 80
            self.match(ExprParser.DIVOP)
            self.state = 81
            self.expression2()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def INT(self):
            return self.getToken(ExprParser.INT, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)




    def value(self):

        localctx = ExprParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            _la = self._input.LA(1)
            if not(_la==9 or _la==10):
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





