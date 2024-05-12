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
        4,0,8,60,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,
        2,1,3,4,3,32,8,3,11,3,12,3,33,1,4,4,4,37,8,4,11,4,12,4,38,1,5,1,
        5,1,6,3,6,44,8,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,52,8,6,1,7,4,7,55,8,
        7,11,7,12,7,56,1,7,1,7,0,0,8,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,
        1,0,2,2,0,65,90,97,122,2,0,9,9,32,32,64,0,1,1,0,0,0,0,3,1,0,0,0,
        0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,
        15,1,0,0,0,1,17,1,0,0,0,3,19,1,0,0,0,5,25,1,0,0,0,7,31,1,0,0,0,9,
        36,1,0,0,0,11,40,1,0,0,0,13,51,1,0,0,0,15,54,1,0,0,0,17,18,5,61,
        0,0,18,2,1,0,0,0,19,20,5,119,0,0,20,21,5,114,0,0,21,22,5,105,0,0,
        22,23,5,116,0,0,23,24,5,101,0,0,24,4,1,0,0,0,25,26,5,114,0,0,26,
        27,5,101,0,0,27,28,5,97,0,0,28,29,5,100,0,0,29,6,1,0,0,0,30,32,7,
        0,0,0,31,30,1,0,0,0,32,33,1,0,0,0,33,31,1,0,0,0,33,34,1,0,0,0,34,
        8,1,0,0,0,35,37,2,48,57,0,36,35,1,0,0,0,37,38,1,0,0,0,38,36,1,0,
        0,0,38,39,1,0,0,0,39,10,1,0,0,0,40,41,5,43,0,0,41,12,1,0,0,0,42,
        44,5,13,0,0,43,42,1,0,0,0,43,44,1,0,0,0,44,45,1,0,0,0,45,52,5,10,
        0,0,46,47,5,60,0,0,47,48,5,69,0,0,48,49,5,79,0,0,49,50,5,70,0,0,
        50,52,5,62,0,0,51,43,1,0,0,0,51,46,1,0,0,0,52,14,1,0,0,0,53,55,7,
        1,0,0,54,53,1,0,0,0,55,56,1,0,0,0,56,54,1,0,0,0,56,57,1,0,0,0,57,
        58,1,0,0,0,58,59,6,7,0,0,59,16,1,0,0,0,6,0,33,38,43,51,56,1,6,0,
        0
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


