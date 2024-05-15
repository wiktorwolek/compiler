from antlr4 import *
from ExprParser import ExprParser
from ExprListener import ExprListener
from LLVMGenerator import LLVMGenerator

from enum import Enum
from collections import namedtuple

# Define Enum for variable types
class VarType(Enum):
    INT = 1
    REAL = 2
    UNKNOWN = 3

# Define Value namedtuple to represent variables
Value = namedtuple('Value', ['name', 'type'])

class LLVMActions(ExprListener):
    def __init__(self):
        self.variables = {}
        self.stack = []


    def exitAssign(self, ctx):
        ID = ctx.ID().getText()
        v = self.stack.pop()
        self.variables[ID] = Value(ID, v.type)
        if v.type == VarType.INT:
            LLVMGenerator.declare_i32(ID)
            LLVMGenerator.assign_i32(ID, v.name)
        elif v.type == VarType.REAL:
            LLVMGenerator.declare_double(ID)
            LLVMGenerator.assign_double(ID, v.name)


    def exitId(self, ctx: ExprParser.IdContext):
        v = self.variables.get(str(ctx.ID()))
        if v.type == VarType.INT:
            LLVMGenerator.load_i32(v.name)
        if v.type == VarType.REAL:
            LLVMGenerator.load_double(v.name)
        self.stack.append(Value("%"+str(LLVMGenerator.reg-1),v.type))
        print(self.stack)

        
    def exitProg(self, ctx):
        code = LLVMGenerator.generate()
        f = open("prog.ll","w")
        f.write(code)
        print(code)

    def exitExpression2(self, ctx: ExprParser.IntContext):
        self.stack.append(Value(ctx.INT().getText(), VarType.INT))
        
    def exitInt(self, ctx):
        self.stack.append(Value(ctx.INT().getText(), VarType.INT))

    def exitReal(self, ctx):
        self.stack.append(Value(ctx.REAL().getText(), VarType.REAL))

    def exitAdd(self, ctx):
        print(self.stack)
        v1 = self.stack.pop()
        v2 = self.stack.pop()
        if v1.type == v2.type:
            if v1.type == VarType.INT:
                LLVMGenerator.add_i32(v1.name, v2.name)
                self.stack.append(Value("%" + str(LLVMGenerator.reg - 1), VarType.INT))
            elif v1.type == VarType.REAL:
                LLVMGenerator.add_double(v1.name, v2.name)
                self.stack.append(Value("%" + str(LLVMGenerator.reg - 1), VarType.REAL))
        else:
            self.error(ctx.getStart().getLine(), "add type mismatch")

    def exitMultiply(self, ctx):
        v1 = self.stack.pop()
        v2 = self.stack.pop()
        if v1.type == v2.type:
            if v1.type == VarType.INT:
                LLVMGenerator.mult_i32(v1.name, v2.name)
                self.stack.append(Value("%" + str(LLVMGenerator.reg - 1), VarType.INT))
            elif v1.type == VarType.REAL:
                LLVMGenerator.mult_double(v1.name, v2.name)
                self.stack.append(Value("%" + str(LLVMGenerator.reg - 1), VarType.REAL))
        else:
            self.error(ctx.getStart().getLine(), "mult type mismatch")

    def exitDivide(self, ctx: ExprParser.DivideContext):
        v1 = self.stack.pop()
        v2 = self.stack.pop()
        if v1.type == v2.type:
            if v1.type == VarType.INT:
                LLVMGenerator.div_i32(v1.name, v2.name)
                self.stack.append(Value("%" + str(LLVMGenerator.reg - 1), VarType.INT))
        else:
            self.error(ctx.getStart().getLine(), "div unimplemented")

    def exitToint(self, ctx):
        v = self.stack.pop()
        LLVMGenerator.fptosi(v.name)
        self.stack.append(Value("%" + str(LLVMGenerator.reg - 1), VarType.INT))

    def exitToreal(self, ctx):
        v = self.stack.pop()
        LLVMGenerator.sitofp(v.name)
        self.stack.append(Value("%" + str(LLVMGenerator.reg - 1), VarType.REAL))

    def exitPrint(self, ctx):
        ID = ctx.ID().getText()
        print(ID)
        vtype = self.variables.get(ID)
        if vtype:
            if vtype == VarType.INT:
                LLVMGenerator.printf_i32(ID)
            elif vtype == VarType.REAL:
                LLVMGenerator.printf_double(ID)
        else:
            self.error(ctx.getStart().getLine(), "unknown variable " + ID)

    def error(self, line, msg):
        print("Error, line " + str(line) + ", " + msg)
        exit(1)

    def exitWrite(self, ctx:ExprParser.WriteContext):
        ID = ctx.ID().getText()
        print(ID)
        if ID in self.variables:
            v = self.variables.get(ID)
            if v.type == VarType.INT:
                LLVMGenerator.printf_i32(v.name)
            elif v.type == VarType.REAL:
                LLVMGenerator.printf_double(v.name)
        else:
            self.error(ctx.getStart().getLine(), "unknown variable " + ID)

    def error(self, line, msg):
        print("Error, line " + str(line) + ", " + msg)
        exit(1)