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
def check_element(arr, v):
    return arr.count(v)
def set_variable(ID,type,object):
    if object.is_global:
        id = "@"+ID
        if len(list(filter(lambda x: x.name==ID,object.globalnames))) == 0:
            v = declareValue(ID,type,object)
            object.globalnames.append(v)
        
    else: 
        id = "%"+ID
        if len(list(filter(lambda x: x.name==ID,object.localnames))) == 0:
            v = declareValue(ID,type,object)
            object.localnames.append(v)
       
    return id
def declareValue(ID,type,object):  
        if type == VarType.INT:
            v = Value(ID,VarType.INT)
            LLVMGenerator.declare_i32(ID,object.is_global)
        elif type == VarType.REAL:
            v = Value(ID,VarType.REAL)
            LLVMGenerator.declare_double(ID,object.is_global)
        return v
def assignValue(ID,v):
        if v.type == VarType.INT:
            LLVMGenerator.assign_i32(ID, v.name)
        elif v.type == VarType.REAL:
            LLVMGenerator.assign_double(ID, v.name)
def loadValue(v, object):
    if v.type == VarType.INT:
        LLVMGenerator.load_i32(v.name)
    if v.type == VarType.REAL:
        LLVMGenerator.load_double(v.name)
    object.stack.append(Value("%"+str(LLVMGenerator.tmp-1),v.type))
def LoadOrCall(ID, object,ctx):
    print(object.globalnames)
    if  len(list(filter(lambda x: x.name==ID,object.localnames))) > 0:
        v = list(filter(lambda x: x.name==ID,object.localnames))[0]
        id = "%"+v.name
        loadValue(Value(id,v.type),object)
    elif len(list(filter(lambda x: x.name==ID,object.globalnames))) > 0:
        v = list(filter(lambda x: x.name==ID,object.globalnames))[0]
        id = '@'+v.name
        loadValue(Value(id,v.type),object)
    elif len(list(filter(lambda x: x==ID,object.functions))) > 0:
        id = ID
        LLVMGenerator.call(ID)
        object.stack.append(Value('%'+str(LLVMGenerator.tmp-1),VarType.INT))
    else:
        LLVMActions.error(ctx.getStart().getLine(),"Unknown "+ID+ ": local > global > function")
    return id
def GetV(ID, object,ctx):
    print(object.globalnames)
    if  len(list(filter(lambda x: x.name==ID,object.localnames))) > 0:
        v = list(filter(lambda x: x.name==ID,object.localnames))[0]
        id = "%"+v.name
    elif len(list(filter(lambda x: x.name==ID,object.globalnames))) > 0:
        v = list(filter(lambda x: x.name==ID,object.globalnames))[0]
        id = '@'+v.name
    elif len(list(filter(lambda x: x==ID,object.functions))) > 0:
        id = ID
    else:
        LLVMActions.error(ctx.getStart().getLine(),"Unknown "+ID+ ": local > global > function")
    return v

class LLVMActions(ExprListener):
    def __init__(self):
        self.stack = []
        self.tableItems = [[]]
        self.tableIndexes = []
        self.is_global = True
        self.globalnames = []
        self.localnames = []
        self.functions = []
        self.function = ""
    def exitAssign(self, ctx):
        ID = ctx.ID().getText()
        v = self.stack.pop()
        assignValue(set_variable(ID,v.type,self),v)
    def exitId(self, ctx: ExprParser.IdContext):
        ID = ctx.ID().getText()
        LoadOrCall(ID,self,ctx)
        print(self.stack)
    def enterProg(self, ctx):
        self.is_global = True;
    def exitProg(self, ctx):
        LLVMGenerator.close_main()
        code = LLVMGenerator.generate()
        f = open("prog.ll","w")
        f.write(code)
        print(code)
    def exitFparam(self,ctx:ExprParser.FparamContext):
        ID = ctx.ID().getText()
        self.functions.append(ID)
        self.function = ID
        LLVMGenerator.function_start(ID)
    def enterFblock(self,ctx:ExprParser.FblockContext):
        self.is_global = False;
    def exitFblock(self,ctx:ExprParser.FblockContext):
        if len(list(filter(lambda x: x.name==self.function,self.localnames))) == 0:
          assignValue(set_variable(self.function,VarType.INT,self),Value("0",VarType.INT))
        loadValue(Value("%"+self.function,VarType.INT),self)
        LLVMGenerator.function_end()
        self.localnames = []
        self.is_global = True   
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
                self.stack.append(Value("%" + str(LLVMGenerator.tmp - 1), VarType.INT))
            elif v1.type == VarType.REAL:
                LLVMGenerator.add_double(v1.name, v2.name)
                self.stack.append(Value("%" + str(LLVMGenerator.tmp - 1), VarType.REAL))
        else:
            self.error(ctx.getStart().getLine(), "add type mismatch")

    def exitMultiply(self, ctx):
        v1 = self.stack.pop()
        v2 = self.stack.pop()
        if v1.type == v2.type:
            if v1.type == VarType.INT:
                LLVMGenerator.mult_i32(v1.name, v2.name)
                self.stack.append(Value("%" + str(LLVMGenerator.tmp - 1), VarType.INT))
            elif v1.type == VarType.REAL:
                LLVMGenerator.mult_double(v1.name, v2.name)
                self.stack.append(Value("%" + str(LLVMGenerator.tmp - 1), VarType.REAL))
        else:
            self.error(ctx.getStart().getLine(), "mult type mismatch")

    def exitToint(self, ctx):
        v = self.stack.pop()
        LLVMGenerator.fptosi(v.name)
        self.stack.append(Value("%" + str(LLVMGenerator.tmp - 1), VarType.INT))

    def exitToreal(self, ctx):
        v = self.stack.pop()
        LLVMGenerator.sitofp(v.name)
        self.stack.append(Value("%" + str(LLVMGenerator.tmp - 1), VarType.REAL))

    def error(self, line, msg):
        print("Error, line " + str(line) + ", " + msg)
        exit(1)
    def exitCall(self,ctx:ExprParser.CallContext):
        LLVMGenerator.call(ctx.ID().getText())
        self.stack.append(Value('%'+str(LLVMGenerator.tmp-1),VarType.INT))
    def exitWrite(self, ctx:ExprParser.WriteContext):
        ID = ctx.ID().getText()
        v = GetV(ID,self,ctx)
        ID = LoadOrCall(ID,self,ctx)
        if v.type == VarType.INT:
            LLVMGenerator.printf_i32(ID)
        else:
            LLVMGenerator.printf_double(ID)
    
    def exitTablerow(self, ctx: ExprParser.TablerowContext):
        self.tableItems.append([])
        
    def exitTableitem(self, ctx: ExprParser.TableitemContext):
        v = self.stack.pop()
        self.tableItems[-1].append(v)
    def exitAssigntable(self, ctx: ExprParser.AssigntableContext):
        print(self.tableItems)
        for i in range(0, len(self.tableItems)):
            for j in range(0, len(self.tableItems[i])):
                name = str(ctx.ID()) + "_" + str(i) + '_' + str(j)
                assignValue(set_variable(name,self.tableItems[i][j].type,self), self.tableItems[i][j]);
        self.tableName = ctx.ID().getText()
        self.tableItems = [[]]
    def exitTable(self, ctx: ExprParser.TableContext):
        print(self.tableIndexes)
        name = str(ctx.ID())
        for i in self.tableIndexes:
            name += '_' + str(i)
        loadValue(LoadOrCall(name,object,ctx),self)
        self.tableIndexes = []
    def exitIndexes(self, ctx: ExprParser.IndexesContext):
        v = self.stack.pop()
        self.tableIndexes.append(v)
    def error(self, line, msg):
        print("Error, line " + str(line) + ", " + msg)
        exit(1)