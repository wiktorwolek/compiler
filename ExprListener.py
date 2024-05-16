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


    # Enter a parse tree produced by ExprParser#write1.
    def enterWrite1(self, ctx:ExprParser.Write1Context):
        pass

    # Exit a parse tree produced by ExprParser#write1.
    def exitWrite1(self, ctx:ExprParser.Write1Context):
        pass


    # Enter a parse tree produced by ExprParser#assign1.
    def enterAssign1(self, ctx:ExprParser.Assign1Context):
        pass

    # Exit a parse tree produced by ExprParser#assign1.
    def exitAssign1(self, ctx:ExprParser.Assign1Context):
        pass


    # Enter a parse tree produced by ExprParser#read1.
    def enterRead1(self, ctx:ExprParser.Read1Context):
        pass

    # Exit a parse tree produced by ExprParser#read1.
    def exitRead1(self, ctx:ExprParser.Read1Context):
        pass


    # Enter a parse tree produced by ExprParser#assigntable1.
    def enterAssigntable1(self, ctx:ExprParser.Assigntable1Context):
        pass

    # Exit a parse tree produced by ExprParser#assigntable1.
    def exitAssigntable1(self, ctx:ExprParser.Assigntable1Context):
        pass


    # Enter a parse tree produced by ExprParser#assign.
    def enterAssign(self, ctx:ExprParser.AssignContext):
        pass

    # Exit a parse tree produced by ExprParser#assign.
    def exitAssign(self, ctx:ExprParser.AssignContext):
        pass


    # Enter a parse tree produced by ExprParser#assigntable.
    def enterAssigntable(self, ctx:ExprParser.AssigntableContext):
        pass

    # Exit a parse tree produced by ExprParser#assigntable.
    def exitAssigntable(self, ctx:ExprParser.AssigntableContext):
        pass


    # Enter a parse tree produced by ExprParser#newtable.
    def enterNewtable(self, ctx:ExprParser.NewtableContext):
        pass

    # Exit a parse tree produced by ExprParser#newtable.
    def exitNewtable(self, ctx:ExprParser.NewtableContext):
        pass


    # Enter a parse tree produced by ExprParser#tablerow.
    def enterTablerow(self, ctx:ExprParser.TablerowContext):
        pass

    # Exit a parse tree produced by ExprParser#tablerow.
    def exitTablerow(self, ctx:ExprParser.TablerowContext):
        pass


    # Enter a parse tree produced by ExprParser#tableitem.
    def enterTableitem(self, ctx:ExprParser.TableitemContext):
        pass

    # Exit a parse tree produced by ExprParser#tableitem.
    def exitTableitem(self, ctx:ExprParser.TableitemContext):
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


    # Enter a parse tree produced by ExprParser#int.
    def enterInt(self, ctx:ExprParser.IntContext):
        pass

    # Exit a parse tree produced by ExprParser#int.
    def exitInt(self, ctx:ExprParser.IntContext):
        pass


    # Enter a parse tree produced by ExprParser#real.
    def enterReal(self, ctx:ExprParser.RealContext):
        pass

    # Exit a parse tree produced by ExprParser#real.
    def exitReal(self, ctx:ExprParser.RealContext):
        pass


    # Enter a parse tree produced by ExprParser#toint.
    def enterToint(self, ctx:ExprParser.TointContext):
        pass

    # Exit a parse tree produced by ExprParser#toint.
    def exitToint(self, ctx:ExprParser.TointContext):
        pass


    # Enter a parse tree produced by ExprParser#toreal.
    def enterToreal(self, ctx:ExprParser.TorealContext):
        pass

    # Exit a parse tree produced by ExprParser#toreal.
    def exitToreal(self, ctx:ExprParser.TorealContext):
        pass


    # Enter a parse tree produced by ExprParser#par.
    def enterPar(self, ctx:ExprParser.ParContext):
        pass

    # Exit a parse tree produced by ExprParser#par.
    def exitPar(self, ctx:ExprParser.ParContext):
        pass


    # Enter a parse tree produced by ExprParser#ids.
    def enterIds(self, ctx:ExprParser.IdsContext):
        pass

    # Exit a parse tree produced by ExprParser#ids.
    def exitIds(self, ctx:ExprParser.IdsContext):
        pass


    # Enter a parse tree produced by ExprParser#call.
    def enterCall(self, ctx:ExprParser.CallContext):
        pass

    # Exit a parse tree produced by ExprParser#call.
    def exitCall(self, ctx:ExprParser.CallContext):
        pass


    # Enter a parse tree produced by ExprParser#id.
    def enterId(self, ctx:ExprParser.IdContext):
        pass

    # Exit a parse tree produced by ExprParser#id.
    def exitId(self, ctx:ExprParser.IdContext):
        pass


    # Enter a parse tree produced by ExprParser#table.
    def enterTable(self, ctx:ExprParser.TableContext):
        pass

    # Exit a parse tree produced by ExprParser#table.
    def exitTable(self, ctx:ExprParser.TableContext):
        pass


    # Enter a parse tree produced by ExprParser#indexes.
    def enterIndexes(self, ctx:ExprParser.IndexesContext):
        pass

    # Exit a parse tree produced by ExprParser#indexes.
    def exitIndexes(self, ctx:ExprParser.IndexesContext):
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


    # Enter a parse tree produced by ExprParser#divide.
    def enterDivide(self, ctx:ExprParser.DivideContext):
        pass

    # Exit a parse tree produced by ExprParser#divide.
    def exitDivide(self, ctx:ExprParser.DivideContext):
        pass


    # Enter a parse tree produced by ExprParser#function.
    def enterFunction(self, ctx:ExprParser.FunctionContext):
        pass

    # Exit a parse tree produced by ExprParser#function.
    def exitFunction(self, ctx:ExprParser.FunctionContext):
        pass


    # Enter a parse tree produced by ExprParser#fparam.
    def enterFparam(self, ctx:ExprParser.FparamContext):
        pass

    # Exit a parse tree produced by ExprParser#fparam.
    def exitFparam(self, ctx:ExprParser.FparamContext):
        pass


    # Enter a parse tree produced by ExprParser#fblock.
    def enterFblock(self, ctx:ExprParser.FblockContext):
        pass

    # Exit a parse tree produced by ExprParser#fblock.
    def exitFblock(self, ctx:ExprParser.FblockContext):
        pass



del ExprParser