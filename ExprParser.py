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
        4,1,8,36,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,3,0,10,8,0,1,0,5,0,
        13,8,0,10,0,12,0,16,9,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,25,8,1,1,
        2,1,2,1,2,1,2,1,2,3,2,32,8,2,1,3,1,3,1,3,0,0,4,0,2,4,6,0,1,1,0,4,
        5,36,0,14,1,0,0,0,2,24,1,0,0,0,4,31,1,0,0,0,6,33,1,0,0,0,8,10,3,
        2,1,0,9,8,1,0,0,0,9,10,1,0,0,0,10,11,1,0,0,0,11,13,5,7,0,0,12,9,
        1,0,0,0,13,16,1,0,0,0,14,12,1,0,0,0,14,15,1,0,0,0,15,1,1,0,0,0,16,
        14,1,0,0,0,17,18,5,2,0,0,18,25,5,4,0,0,19,20,5,4,0,0,20,21,5,1,0,
        0,21,25,3,4,2,0,22,23,5,3,0,0,23,25,5,4,0,0,24,17,1,0,0,0,24,19,
        1,0,0,0,24,22,1,0,0,0,25,3,1,0,0,0,26,27,3,6,3,0,27,28,5,6,0,0,28,
        29,3,4,2,0,29,32,1,0,0,0,30,32,3,6,3,0,31,26,1,0,0,0,31,30,1,0,0,
        0,32,5,1,0,0,0,33,34,7,0,0,0,34,7,1,0,0,0,4,9,14,24,31
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'write'", "'read'", "<INVALID>", 
                     "<INVALID>", "'+'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "WRITE", "READ", "ID", "INT", 
                      "ADD", "NEWLINE", "WS" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_expr = 2
    RULE_value = 3

    ruleNames =  [ "prog", "stat", "expr", "value" ]

    EOF = Token.EOF
    T__0=1
    WRITE=2
    READ=3
    ID=4
    INT=5
    ADD=6
    NEWLINE=7
    WS=8

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
            self.state = 14
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 156) != 0):
                self.state = 9
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 28) != 0):
                    self.state = 8
                    self.stat()


                self.state = 11
                self.match(ExprParser.NEWLINE)
                self.state = 16
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def WRITE(self):
            return self.getToken(ExprParser.WRITE, 0)

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def READ(self):
            return self.getToken(ExprParser.READ, 0)

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
            self.state = 24
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 17
                self.match(ExprParser.WRITE)
                self.state = 18
                self.match(ExprParser.ID)
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 19
                self.match(ExprParser.ID)
                self.state = 20
                self.match(ExprParser.T__0)
                self.state = 21
                self.expr()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 3)
                self.state = 22
                self.match(ExprParser.READ)
                self.state = 23
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


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self):
            return self.getTypedRuleContext(ExprParser.ValueContext,0)


        def ADD(self):
            return self.getToken(ExprParser.ADD, 0)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)




    def expr(self):

        localctx = ExprParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_expr)
        try:
            self.state = 31
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 26
                self.value()
                self.state = 27
                self.match(ExprParser.ADD)
                self.state = 28
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 30
                self.value()
                pass


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
        self.enterRule(localctx, 6, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            _la = self._input.LA(1)
            if not(_la==4 or _la==5):
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





