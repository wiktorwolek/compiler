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
        4,1,23,169,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,1,0,1,0,3,0,45,8,0,1,0,5,0,48,8,0,10,0,12,0,51,9,0,1,0,1,0,
        1,1,1,1,1,1,1,1,3,1,59,8,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,4,1,
        4,1,4,1,4,5,4,73,8,4,10,4,12,4,76,9,4,1,4,1,4,1,5,1,5,1,5,5,5,83,
        8,5,10,5,12,5,86,9,5,1,6,1,6,1,7,1,7,1,7,1,8,1,8,1,8,1,9,1,9,3,9,
        98,8,9,1,10,1,10,3,10,102,8,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,
        1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,3,11,119,8,11,1,12,1,12,
        3,12,123,8,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,
        1,13,1,13,3,13,137,8,13,1,14,1,14,1,15,1,15,1,15,1,15,1,16,1,16,
        1,16,1,16,1,17,1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,18,1,19,1,19,
        1,20,3,20,161,8,20,1,20,5,20,164,8,20,10,20,12,20,167,9,20,1,20,
        0,0,21,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,
        0,0,167,0,49,1,0,0,0,2,58,1,0,0,0,4,60,1,0,0,0,6,64,1,0,0,0,8,68,
        1,0,0,0,10,84,1,0,0,0,12,87,1,0,0,0,14,89,1,0,0,0,16,92,1,0,0,0,
        18,97,1,0,0,0,20,101,1,0,0,0,22,118,1,0,0,0,24,122,1,0,0,0,26,136,
        1,0,0,0,28,138,1,0,0,0,30,140,1,0,0,0,32,144,1,0,0,0,34,148,1,0,
        0,0,36,152,1,0,0,0,38,157,1,0,0,0,40,165,1,0,0,0,42,45,3,2,1,0,43,
        45,3,36,18,0,44,42,1,0,0,0,44,43,1,0,0,0,44,45,1,0,0,0,45,46,1,0,
        0,0,46,48,5,22,0,0,47,44,1,0,0,0,48,51,1,0,0,0,49,47,1,0,0,0,49,
        50,1,0,0,0,50,52,1,0,0,0,51,49,1,0,0,0,52,53,5,1,0,0,53,1,1,0,0,
        0,54,59,3,14,7,0,55,59,3,4,2,0,56,59,3,16,8,0,57,59,3,6,3,0,58,54,
        1,0,0,0,58,55,1,0,0,0,58,56,1,0,0,0,58,57,1,0,0,0,59,3,1,0,0,0,60,
        61,5,16,0,0,61,62,5,2,0,0,62,63,3,18,9,0,63,5,1,0,0,0,64,65,5,16,
        0,0,65,66,5,2,0,0,66,67,3,8,4,0,67,7,1,0,0,0,68,74,5,3,0,0,69,70,
        3,10,5,0,70,71,5,4,0,0,71,73,1,0,0,0,72,69,1,0,0,0,73,76,1,0,0,0,
        74,72,1,0,0,0,74,75,1,0,0,0,75,77,1,0,0,0,76,74,1,0,0,0,77,78,5,
        5,0,0,78,9,1,0,0,0,79,80,3,12,6,0,80,81,5,6,0,0,81,83,1,0,0,0,82,
        79,1,0,0,0,83,86,1,0,0,0,84,82,1,0,0,0,84,85,1,0,0,0,85,11,1,0,0,
        0,86,84,1,0,0,0,87,88,3,18,9,0,88,13,1,0,0,0,89,90,5,12,0,0,90,91,
        5,16,0,0,91,15,1,0,0,0,92,93,5,13,0,0,93,94,5,16,0,0,94,17,1,0,0,
        0,95,98,3,20,10,0,96,98,3,30,15,0,97,95,1,0,0,0,97,96,1,0,0,0,98,
        19,1,0,0,0,99,102,3,22,11,0,100,102,3,32,16,0,101,99,1,0,0,0,101,
        100,1,0,0,0,102,21,1,0,0,0,103,119,5,17,0,0,104,119,5,18,0,0,105,
        106,5,14,0,0,106,119,3,22,11,0,107,108,5,15,0,0,108,119,3,22,11,
        0,109,110,5,7,0,0,110,111,3,18,9,0,111,112,5,8,0,0,112,119,1,0,0,
        0,113,119,3,24,12,0,114,115,5,9,0,0,115,116,5,16,0,0,116,117,5,7,
        0,0,117,119,5,8,0,0,118,103,1,0,0,0,118,104,1,0,0,0,118,105,1,0,
        0,0,118,107,1,0,0,0,118,109,1,0,0,0,118,113,1,0,0,0,118,114,1,0,
        0,0,119,23,1,0,0,0,120,123,5,16,0,0,121,123,3,26,13,0,122,120,1,
        0,0,0,122,121,1,0,0,0,123,25,1,0,0,0,124,125,5,16,0,0,125,126,5,
        3,0,0,126,127,3,28,14,0,127,128,5,5,0,0,128,137,1,0,0,0,129,130,
        5,16,0,0,130,131,5,3,0,0,131,132,3,28,14,0,132,133,5,6,0,0,133,134,
        3,28,14,0,134,135,5,5,0,0,135,137,1,0,0,0,136,124,1,0,0,0,136,129,
        1,0,0,0,137,27,1,0,0,0,138,139,3,18,9,0,139,29,1,0,0,0,140,141,3,
        20,10,0,141,142,5,19,0,0,142,143,3,18,9,0,143,31,1,0,0,0,144,145,
        3,22,11,0,145,146,5,20,0,0,146,147,3,22,11,0,147,33,1,0,0,0,148,
        149,3,22,11,0,149,150,5,21,0,0,150,151,3,22,11,0,151,35,1,0,0,0,
        152,153,5,10,0,0,153,154,3,38,19,0,154,155,3,40,20,0,155,156,5,11,
        0,0,156,37,1,0,0,0,157,158,5,16,0,0,158,39,1,0,0,0,159,161,3,2,1,
        0,160,159,1,0,0,0,160,161,1,0,0,0,161,162,1,0,0,0,162,164,5,22,0,
        0,163,160,1,0,0,0,164,167,1,0,0,0,165,163,1,0,0,0,165,166,1,0,0,
        0,166,41,1,0,0,0,167,165,1,0,0,0,12,44,49,58,74,84,97,101,118,122,
        136,160,165
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'<EOF>'", "'='", "'['", "';'", "']'", 
                     "','", "'('", "')'", "'call'", "'function'", "'endfunction'", 
                     "'write'", "'read'", "'(int)'", "'(real)'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'+'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "CALL", "FUNCTION", "ENDFUNCTION", "WRITE", 
                      "READ", "TOINT", "TOREAL", "ID", "INT", "REAL", "ADDOP", 
                      "MULOP", "DIVOP", "NEWLINE", "WS" ]

    RULE_prog = 0
    RULE_statement = 1
    RULE_assign = 2
    RULE_assigntable = 3
    RULE_newtable = 4
    RULE_tablerow = 5
    RULE_tableitem = 6
    RULE_write = 7
    RULE_read = 8
    RULE_expression = 9
    RULE_expression1 = 10
    RULE_expression2 = 11
    RULE_id = 12
    RULE_table = 13
    RULE_indexes = 14
    RULE_add = 15
    RULE_multiply = 16
    RULE_divide = 17
    RULE_function = 18
    RULE_fparam = 19
    RULE_fblock = 20

    ruleNames =  [ "prog", "statement", "assign", "assigntable", "newtable", 
                   "tablerow", "tableitem", "write", "read", "expression", 
                   "expression1", "expression2", "id", "table", "indexes", 
                   "add", "multiply", "divide", "function", "fparam", "fblock" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    CALL=9
    FUNCTION=10
    ENDFUNCTION=11
    WRITE=12
    READ=13
    TOINT=14
    TOREAL=15
    ID=16
    INT=17
    REAL=18
    ADDOP=19
    MULOP=20
    DIVOP=21
    NEWLINE=22
    WS=23

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


        def function(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.FunctionContext)
            else:
                return self.getTypedRuleContext(ExprParser.FunctionContext,i)


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
            self.state = 49
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4273152) != 0):
                self.state = 44
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [12, 13, 16]:
                    self.state = 42
                    self.statement()
                    pass
                elif token in [10]:
                    self.state = 43
                    self.function()
                    pass
                elif token in [22]:
                    pass
                else:
                    pass
                self.state = 46
                self.match(ExprParser.NEWLINE)
                self.state = 51
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 52
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


        def getRuleIndex(self):
            return ExprParser.RULE_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Write1Context(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def write(self):
            return self.getTypedRuleContext(ExprParser.WriteContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWrite1" ):
                listener.enterWrite1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWrite1" ):
                listener.exitWrite1(self)


    class Assigntable1Context(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def assigntable(self):
            return self.getTypedRuleContext(ExprParser.AssigntableContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssigntable1" ):
                listener.enterAssigntable1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssigntable1" ):
                listener.exitAssigntable1(self)


    class Assign1Context(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def assign(self):
            return self.getTypedRuleContext(ExprParser.AssignContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign1" ):
                listener.enterAssign1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign1" ):
                listener.exitAssign1(self)


    class Read1Context(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def read(self):
            return self.getTypedRuleContext(ExprParser.ReadContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRead1" ):
                listener.enterRead1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRead1" ):
                listener.exitRead1(self)



    def statement(self):

        localctx = ExprParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 58
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                localctx = ExprParser.Write1Context(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 54
                self.write()
                pass

            elif la_ == 2:
                localctx = ExprParser.Assign1Context(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 55
                self.assign()
                pass

            elif la_ == 3:
                localctx = ExprParser.Read1Context(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 56
                self.read()
                pass

            elif la_ == 4:
                localctx = ExprParser.Assigntable1Context(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 57
                self.assigntable()
                pass


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
            self.state = 60
            self.match(ExprParser.ID)
            self.state = 61
            self.match(ExprParser.T__1)
            self.state = 62
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssigntableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def newtable(self):
            return self.getTypedRuleContext(ExprParser.NewtableContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_assigntable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssigntable" ):
                listener.enterAssigntable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssigntable" ):
                listener.exitAssigntable(self)




    def assigntable(self):

        localctx = ExprParser.AssigntableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_assigntable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(ExprParser.ID)
            self.state = 65
            self.match(ExprParser.T__1)
            self.state = 66
            self.newtable()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NewtableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tablerow(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.TablerowContext)
            else:
                return self.getTypedRuleContext(ExprParser.TablerowContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_newtable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNewtable" ):
                listener.enterNewtable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNewtable" ):
                listener.exitNewtable(self)




    def newtable(self):

        localctx = ExprParser.NewtableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_newtable)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(ExprParser.T__2)
            self.state = 74
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 508560) != 0):
                self.state = 69
                self.tablerow()
                self.state = 70
                self.match(ExprParser.T__3)
                self.state = 76
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 77
            self.match(ExprParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TablerowContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tableitem(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.TableitemContext)
            else:
                return self.getTypedRuleContext(ExprParser.TableitemContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_tablerow

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTablerow" ):
                listener.enterTablerow(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTablerow" ):
                listener.exitTablerow(self)




    def tablerow(self):

        localctx = ExprParser.TablerowContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_tablerow)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 508544) != 0):
                self.state = 79
                self.tableitem()
                self.state = 80
                self.match(ExprParser.T__5)
                self.state = 86
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TableitemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(ExprParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_tableitem

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTableitem" ):
                listener.enterTableitem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTableitem" ):
                listener.exitTableitem(self)




    def tableitem(self):

        localctx = ExprParser.TableitemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_tableitem)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
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
        self.enterRule(localctx, 14, self.RULE_write)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.match(ExprParser.WRITE)
            self.state = 90
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
        self.enterRule(localctx, 16, self.RULE_read)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.match(ExprParser.READ)
            self.state = 93
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
        self.enterRule(localctx, 18, self.RULE_expression)
        try:
            self.state = 97
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 95
                self.expression1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 96
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
        self.enterRule(localctx, 20, self.RULE_expression1)
        try:
            self.state = 101
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 99
                self.expression2()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 100
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


    class CallContext(Expression2Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.Expression2Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def CALL(self):
            return self.getToken(ExprParser.CALL, 0)
        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCall" ):
                listener.enterCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCall" ):
                listener.exitCall(self)


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


    class IdsContext(Expression2Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.Expression2Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def id_(self):
            return self.getTypedRuleContext(ExprParser.IdContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIds" ):
                listener.enterIds(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIds" ):
                listener.exitIds(self)


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
        self.enterRule(localctx, 22, self.RULE_expression2)
        try:
            self.state = 118
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17]:
                localctx = ExprParser.IntContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 103
                self.match(ExprParser.INT)
                pass
            elif token in [18]:
                localctx = ExprParser.RealContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 104
                self.match(ExprParser.REAL)
                pass
            elif token in [14]:
                localctx = ExprParser.TointContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 105
                self.match(ExprParser.TOINT)
                self.state = 106
                self.expression2()
                pass
            elif token in [15]:
                localctx = ExprParser.TorealContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 107
                self.match(ExprParser.TOREAL)
                self.state = 108
                self.expression2()
                pass
            elif token in [7]:
                localctx = ExprParser.ParContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 109
                self.match(ExprParser.T__6)
                self.state = 110
                self.expression()
                self.state = 111
                self.match(ExprParser.T__7)
                pass
            elif token in [16]:
                localctx = ExprParser.IdsContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 113
                self.id_()
                pass
            elif token in [9]:
                localctx = ExprParser.CallContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 114
                self.match(ExprParser.CALL)
                self.state = 115
                self.match(ExprParser.ID)
                self.state = 116
                self.match(ExprParser.T__6)
                self.state = 117
                self.match(ExprParser.T__7)
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


    class IdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def table(self):
            return self.getTypedRuleContext(ExprParser.TableContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_id

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId" ):
                listener.enterId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId" ):
                listener.exitId(self)




    def id_(self):

        localctx = ExprParser.IdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_id)
        try:
            self.state = 122
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 120
                self.match(ExprParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 121
                self.table()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def indexes(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.IndexesContext)
            else:
                return self.getTypedRuleContext(ExprParser.IndexesContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_table

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTable" ):
                listener.enterTable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTable" ):
                listener.exitTable(self)




    def table(self):

        localctx = ExprParser.TableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_table)
        try:
            self.state = 136
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 124
                self.match(ExprParser.ID)
                self.state = 125
                self.match(ExprParser.T__2)
                self.state = 126
                self.indexes()
                self.state = 127
                self.match(ExprParser.T__4)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 129
                self.match(ExprParser.ID)
                self.state = 130
                self.match(ExprParser.T__2)
                self.state = 131
                self.indexes()
                self.state = 132
                self.match(ExprParser.T__5)
                self.state = 133
                self.indexes()
                self.state = 134
                self.match(ExprParser.T__4)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndexesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(ExprParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_indexes

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIndexes" ):
                listener.enterIndexes(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIndexes" ):
                listener.exitIndexes(self)




    def indexes(self):

        localctx = ExprParser.IndexesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_indexes)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self.expression()
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
        self.enterRule(localctx, 30, self.RULE_add)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.expression1()
            self.state = 141
            self.match(ExprParser.ADDOP)
            self.state = 142
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
        self.enterRule(localctx, 32, self.RULE_multiply)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self.expression2()
            self.state = 145
            self.match(ExprParser.MULOP)
            self.state = 146
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
        self.enterRule(localctx, 34, self.RULE_divide)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.expression2()
            self.state = 149
            self.match(ExprParser.DIVOP)
            self.state = 150
            self.expression2()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION(self):
            return self.getToken(ExprParser.FUNCTION, 0)

        def fparam(self):
            return self.getTypedRuleContext(ExprParser.FparamContext,0)


        def fblock(self):
            return self.getTypedRuleContext(ExprParser.FblockContext,0)


        def ENDFUNCTION(self):
            return self.getToken(ExprParser.ENDFUNCTION, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction" ):
                listener.enterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction" ):
                listener.exitFunction(self)




    def function(self):

        localctx = ExprParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_function)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self.match(ExprParser.FUNCTION)
            self.state = 153
            self.fparam()
            self.state = 154
            self.fblock()
            self.state = 155
            self.match(ExprParser.ENDFUNCTION)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FparamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_fparam

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFparam" ):
                listener.enterFparam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFparam" ):
                listener.exitFparam(self)




    def fparam(self):

        localctx = ExprParser.FparamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_fparam)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            self.match(ExprParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FblockContext(ParserRuleContext):
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
            return ExprParser.RULE_fblock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFblock" ):
                listener.enterFblock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFblock" ):
                listener.exitFblock(self)




    def fblock(self):

        localctx = ExprParser.FblockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_fblock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4272128) != 0):
                self.state = 160
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 77824) != 0):
                    self.state = 159
                    self.statement()


                self.state = 162
                self.match(ExprParser.NEWLINE)
                self.state = 167
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





