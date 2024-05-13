# Generated from Expr.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete listener for a parse tree produced by ExprParser.
class ExprListener(ParseTreeListener):

    # Enter a parse tree produced by ExprParser#prog.
    def enterProg(self, ctx:ExprParser.ProgContext):
        pass

    # Exit a parse tree produced by ExprParser#prog.
    def exitProg(self, ctx:ExprParser.ProgContext):
        pass


    # Enter a parse tree produced by ExprParser#stat.
    def enterStat(self, ctx:ExprParser.StatContext):
        pass

    # Exit a parse tree produced by ExprParser#stat.
    def exitStat(self, ctx:ExprParser.StatContext):
        pass


    # Enter a parse tree produced by ExprParser#assign.
    def enterAssign(self, ctx:ExprParser.AssignContext):
        pass

    # Exit a parse tree produced by ExprParser#assign.
    def exitAssign(self, ctx:ExprParser.AssignContext):
        pass


    # Enter a parse tree produced by ExprParser#expression.
    def enterExpression(self, ctx:ExprParser.ExpressionContext):
        pass

    # Exit a parse tree produced by ExprParser#expression.
    def exitExpression(self, ctx:ExprParser.ExpressionContext):
        pass


    # Enter a parse tree produced by ExprParser#expression1.
    def enterExpression1(self, ctx:ExprParser.Expression1Context):
        pass

    # Exit a parse tree produced by ExprParser#expression1.
    def exitExpression1(self, ctx:ExprParser.Expression1Context):
        pass


    # Enter a parse tree produced by ExprParser#write.
    def enterWrite(self, ctx:ExprParser.WriteContext):
        pass

    # Exit a parse tree produced by ExprParser#write.
    def exitWrite(self, ctx:ExprParser.WriteContext):
        pass


    # Enter a parse tree produced by ExprParser#read.
    def enterRead(self, ctx:ExprParser.ReadContext):
        pass

    # Exit a parse tree produced by ExprParser#read.
    def exitRead(self, ctx:ExprParser.ReadContext):
        pass


    # Enter a parse tree produced by ExprParser#add.
    def enterAdd(self, ctx:ExprParser.AddContext):
        pass

    # Exit a parse tree produced by ExprParser#add.
    def exitAdd(self, ctx:ExprParser.AddContext):
        pass


    # Enter a parse tree produced by ExprParser#multiply.
    def enterMultiply(self, ctx:ExprParser.MultiplyContext):
        pass

    # Exit a parse tree produced by ExprParser#multiply.
    def exitMultiply(self, ctx:ExprParser.MultiplyContext):
        pass


    # Enter a parse tree produced by ExprParser#expression2.
    def enterExpression2(self, ctx:ExprParser.Expression2Context):
        pass

    # Exit a parse tree produced by ExprParser#expression2.
    def exitExpression2(self, ctx:ExprParser.Expression2Context):
        pass



del ExprParser