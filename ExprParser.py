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
        4,1,12,71,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,3,0,22,8,0,1,0,5,0,25,8,0,10,0,12,
        0,28,9,0,1,0,1,0,1,1,1,1,1,1,3,1,35,8,1,1,2,1,2,1,2,1,2,1,3,1,3,
        3,3,43,8,3,1,4,1,4,3,4,47,8,4,1,5,1,5,1,5,1,6,1,6,1,6,1,7,1,7,1,
        7,1,7,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,3,9,69,8,9,1,9,0,0,
        10,0,2,4,6,8,10,12,14,16,18,0,0,68,0,26,1,0,0,0,2,34,1,0,0,0,4,36,
        1,0,0,0,6,42,1,0,0,0,8,46,1,0,0,0,10,48,1,0,0,0,12,51,1,0,0,0,14,
        54,1,0,0,0,16,58,1,0,0,0,18,68,1,0,0,0,20,22,3,2,1,0,21,20,1,0,0,
        0,21,22,1,0,0,0,22,23,1,0,0,0,23,25,5,11,0,0,24,21,1,0,0,0,25,28,
        1,0,0,0,26,24,1,0,0,0,26,27,1,0,0,0,27,29,1,0,0,0,28,26,1,0,0,0,
        29,30,5,1,0,0,30,1,1,0,0,0,31,35,3,10,5,0,32,35,3,4,2,0,33,35,3,
        12,6,0,34,31,1,0,0,0,34,32,1,0,0,0,34,33,1,0,0,0,35,3,1,0,0,0,36,
        37,5,7,0,0,37,38,5,2,0,0,38,39,3,6,3,0,39,5,1,0,0,0,40,43,3,8,4,
        0,41,43,3,14,7,0,42,40,1,0,0,0,42,41,1,0,0,0,43,7,1,0,0,0,44,47,
        3,18,9,0,45,47,3,16,8,0,46,44,1,0,0,0,46,45,1,0,0,0,47,9,1,0,0,0,
        48,49,5,5,0,0,49,50,5,7,0,0,50,11,1,0,0,0,51,52,5,6,0,0,52,53,5,
        7,0,0,53,13,1,0,0,0,54,55,3,8,4,0,55,56,5,9,0,0,56,57,3,8,4,0,57,
        15,1,0,0,0,58,59,3,18,9,0,59,60,5,10,0,0,60,61,3,18,9,0,61,17,1,
        0,0,0,62,69,5,7,0,0,63,69,5,8,0,0,64,65,5,3,0,0,65,66,3,6,3,0,66,
        67,5,4,0,0,67,69,1,0,0,0,68,62,1,0,0,0,68,63,1,0,0,0,68,64,1,0,0,
        0,69,19,1,0,0,0,6,21,26,34,42,46,68
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'<EOF>'", "'='", "'('", "')'", "'write'", 
                     "'read'", "<INVALID>", "<INVALID>", "'+'", "'*'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "WRITE", "READ", "ID", "INT", "ADD", 
                      "MUL", "NEWLINE", "WS" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_assign = 2
    RULE_expression = 3
    RULE_expression1 = 4
    RULE_write = 5
    RULE_read = 6
    RULE_add = 7
    RULE_multiply = 8
    RULE_expression2 = 9

    ruleNames =  [ "prog", "stat", "assign", "expression", "expression1", 
                   "write", "read", "add", "multiply", "expression2" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    WRITE=5
    READ=6
    ID=7
    INT=8
    ADD=9
    MUL=10
    NEWLINE=11
    WS=12

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

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.StatContext)
            else:
                return self.getTypedRuleContext(ExprParser.StatContext,i)


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
            self.state = 26
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2272) != 0):
                self.state = 21
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 224) != 0):
                    self.state = 20
                    self.stat()


                self.state = 23
                self.match(ExprParser.NEWLINE)
                self.state = 28
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 29
            self.match(ExprParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatContext(ParserRuleContext):
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
            return ExprParser.RULE_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStat" ):
                listener.enterStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStat" ):
                listener.exitStat(self)




    def stat(self):

        localctx = ExprParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        try:
            self.state = 34
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 31
                self.write()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 32
                self.assign()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 3)
                self.state = 33
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
            self.state = 36
            self.match(ExprParser.ID)
            self.state = 37
            self.match(ExprParser.T__1)
            self.state = 38
            self.expression()
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
        self.enterRule(localctx, 6, self.RULE_expression)
        try:
            self.state = 42
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 40
                self.expression1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 41
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
        self.enterRule(localctx, 8, self.RULE_expression1)
        try:
            self.state = 46
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 44
                self.expression2()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 45
                self.multiply()
                pass


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
        self.enterRule(localctx, 10, self.RULE_write)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(ExprParser.WRITE)
            self.state = 49
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
        self.enterRule(localctx, 12, self.RULE_read)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.match(ExprParser.READ)
            self.state = 52
            self.match(ExprParser.ID)
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

        def expression1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.Expression1Context)
            else:
                return self.getTypedRuleContext(ExprParser.Expression1Context,i)


        def ADD(self):
            return self.getToken(ExprParser.ADD, 0)

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
        self.enterRule(localctx, 14, self.RULE_add)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.expression1()
            self.state = 55
            self.match(ExprParser.ADD)
            self.state = 56
            self.expression1()
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


        def MUL(self):
            return self.getToken(ExprParser.MUL, 0)

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
        self.enterRule(localctx, 16, self.RULE_multiply)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.expression2()
            self.state = 59
            self.match(ExprParser.MUL)
            self.state = 60
            self.expression2()
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

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def INT(self):
            return self.getToken(ExprParser.INT, 0)

        def expression(self):
            return self.getTypedRuleContext(ExprParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_expression2

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression2" ):
                listener.enterExpression2(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression2" ):
                listener.exitExpression2(self)




    def expression2(self):

        localctx = ExprParser.Expression2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_expression2)
        try:
            self.state = 68
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 62
                self.match(ExprParser.ID)
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 63
                self.match(ExprParser.INT)
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 3)
                self.state = 64
                self.match(ExprParser.T__2)
                self.state = 65
                self.expression()
                self.state = 66
                self.match(ExprParser.T__3)
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





