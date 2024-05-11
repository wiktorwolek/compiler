from antlr4 import *
from ExprParser import ExprParser
from ExprListener import ExprListener
from LLVMGenerator import LLVMGenerator

class LLVMActions(ExprListener):

    def __init__(self):
        self.variables = set()
        self.stack = []

    def exitAssign(self, ctx:ExprParser.AssignContext): 
        ID = ctx.ID().getText()
        if ID not in self.variables:
            self.variables.add(ID)
            LLVMGenerator.declare(ID)
        LLVMGenerator.assign(ID, self.stack.pop())

    def exitProg(self, ctx:ExprParser.ProgContext): 
        print(LLVMGenerator.generate())

    def exitValue(self, ctx:ExprParser.ValueContext): 
        if ctx.ID() is not None:
            ID = ctx.ID().getText()
            if ID in self.variables:
                LLVMGenerator.load(ID)
                self.stack.append("%" + str(LLVMGenerator.reg - 1))
            else:
                self.error(ctx.getStart().getLine(), "unknown variable " + ID)
        if ctx.INT() is not None:
            self.stack.append(ctx.INT().getText())

    def exitAdd(self, ctx:ExprParser.AddContext): 
        LLVMGenerator.add(self.stack.pop(), self.stack.pop())
        self.stack.append("%" + str(LLVMGenerator.reg - 1))

    def exitSingle(self, ctx:ExprParser.SingleContext): 
        pass

    def exitWrite(self, ctx:ExprParser.WriteContext):
        ID = ctx.ID().getText()
        if ID in self.variables:
            LLVMGenerator.printf(ID)
        else:
            self.error(ctx.getStart().getLine(), "unknown variable " + ID)

    def exitRead(self, ctx:ExprParser.ReadContext):
        ID = ctx.ID().getText()
        if ID not in self.variables:
            self.variables.add(ID)
            LLVMGenerator.declare(ID)
        LLVMGenerator.scanf(ID)

    def error(self, line, msg):
        print("Error, line " + str(line) + ", " + msg)
        exit(1)
