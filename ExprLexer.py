# Generated from Expr.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,8,54,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,
        2,1,3,4,3,32,8,3,11,3,12,3,33,1,4,4,4,37,8,4,11,4,12,4,38,1,5,1,
        5,1,6,3,6,44,8,6,1,6,1,6,1,7,4,7,49,8,7,11,7,12,7,50,1,7,1,7,0,0,
        8,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,1,0,2,2,0,65,90,97,122,2,0,
        9,9,32,32,57,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,
        1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,1,17,1,0,0,0,3,19,
        1,0,0,0,5,25,1,0,0,0,7,31,1,0,0,0,9,36,1,0,0,0,11,40,1,0,0,0,13,
        43,1,0,0,0,15,48,1,0,0,0,17,18,5,61,0,0,18,2,1,0,0,0,19,20,5,119,
        0,0,20,21,5,114,0,0,21,22,5,105,0,0,22,23,5,116,0,0,23,24,5,101,
        0,0,24,4,1,0,0,0,25,26,5,114,0,0,26,27,5,101,0,0,27,28,5,97,0,0,
        28,29,5,100,0,0,29,6,1,0,0,0,30,32,7,0,0,0,31,30,1,0,0,0,32,33,1,
        0,0,0,33,31,1,0,0,0,33,34,1,0,0,0,34,8,1,0,0,0,35,37,2,48,57,0,36,
        35,1,0,0,0,37,38,1,0,0,0,38,36,1,0,0,0,38,39,1,0,0,0,39,10,1,0,0,
        0,40,41,5,43,0,0,41,12,1,0,0,0,42,44,5,13,0,0,43,42,1,0,0,0,43,44,
        1,0,0,0,44,45,1,0,0,0,45,46,5,10,0,0,46,14,1,0,0,0,47,49,7,1,0,0,
        48,47,1,0,0,0,49,50,1,0,0,0,50,48,1,0,0,0,50,51,1,0,0,0,51,52,1,
        0,0,0,52,53,6,7,0,0,53,16,1,0,0,0,5,0,33,38,43,50,1,1,7,0
    ]

class ExprLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    WRITE = 2
    READ = 3
    ID = 4
    INT = 5
    ADD = 6
    NEWLINE = 7
    WS = 8

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'='", "'write'", "'read'", "'+'" ]

    symbolicNames = [ "<INVALID>",
            "WRITE", "READ", "ID", "INT", "ADD", "NEWLINE", "WS" ]

    ruleNames = [ "T__0", "WRITE", "READ", "ID", "INT", "ADD", "NEWLINE", 
                  "WS" ]

    grammarFileName = "Expr.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[7] = self.WS_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def WS_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
             skip(); 
     


