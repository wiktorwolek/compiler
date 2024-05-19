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
    TABLE = 4
    UNKNOWN = 3

# Define Value namedtuple to represent variables
Value = namedtuple('Value', ['name', 'type'])
Table = namedtuple('Table',['name','i','j'])
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
        elif type == VarType.TABLE:
            v = Value(ID,VarType.TABLE)
            LLVMGenerator.create_table(ID,object.table_size,object.is_global)
            object.tableSizes.append(Table(ID,len(object.tableItems),len(object.tableItems[0])))
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
        LLVMActions.error(ctx.start.line,"Unknown "+ID+ ": local > global > function")
    return id
def GetV(ID, object,ctx):
    if  len(list(filter(lambda x: x.name==ID,object.localnames))) > 0:
        v = list(filter(lambda x: x.name==ID,object.localnames))[0]
        id = "%"+v.name
    elif len(list(filter(lambda x: x.name==ID,object.globalnames))) > 0:
        v = list(filter(lambda x: x.name==ID,object.globalnames))[0]
        id = '@'+v.name
    elif len(list(filter(lambda x: x==ID,object.functions))) > 0:
        id = ID
    else:
        LLVMActions.error(ctx.start.line,"Unknown "+ID+ ": local > global > function")
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
        self.tableSizes = []

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
            self.error(ctx.start.line, "add type mismatch")

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
            self.error(ctx.start.line, "mult type mismatch")

    def exitDivide(self, ctx: ExprParser.DivideContext):
        v1 = self.stack.pop()
        v2 = self.stack.pop()

        if v2.type == VarType.REAL and v1.type == VarType.INT:
            LLVMGenerator.sitofp(v1.name)
            self.stack.append(Value("%" + str(LLVMGenerator.tmp - 1), VarType.REAL))
            v1 = self.stack.pop()
        if v2.type == VarType.INT and v1.type == VarType.REAL:
            LLVMGenerator.sitofp(v2.name)
            self.stack.append(Value("%" + str(LLVMGenerator.tmp - 1), VarType.REAL))
            v2 = self.stack.pop()

        if v1.type == v2.type:
            if v1.type == VarType.INT:
                LLVMGenerator.div_i32(v2.name, v1.name)
                self.stack.append(Value("%" + str(LLVMGenerator.tmp - 1), VarType.INT))
            if v1.type == VarType.REAL:
                LLVMGenerator.div_i32(v2.name, v1.name)
                self.stack.append(Value("%" + str(LLVMGenerator.tmp - 1), VarType.REAL))
        else:
            self.error(ctx.start.line, "mult type mismatch")



    def exitToint(self, ctx):
        v = self.stack.pop()
        LLVMGenerator.fptosi(v.name)
        self.stack.append(Value("%" + str(LLVMGenerator.tmp - 1), VarType.INT))

    def exitToreal(self, ctx):
        v = self.stack.pop()
        LLVMGenerator.sitofp(v.name)
        self.stack.append(Value("%" + str(LLVMGenerator.tmp - 1), VarType.REAL))

    def exitCall(self,ctx:ExprParser.CallContext):
        LLVMGenerator.call(ctx.ID().getText())
        self.stack.append(Value('%'+str(LLVMGenerator.tmp-1),VarType.INT))

    def exitRead(self, ctx:ExprParser.ReadContext):
        ID = ctx.ID().getText()
        assignValue(set_variable(ID,VarType.INT,self),Value('%'+str(LLVMGenerator.tmp-1),VarType.INT))
        LLVMGenerator.scanf(ID)

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
        tableName = ctx.ID().getText()
        del self.tableItems[-1]
        if len(self.tableItems)==1:
            size = f"[{len(self.tableItems[0])} x i64]"
            
        else:
            size = f"[{len(self.tableItems)} x [{len(self.tableItems[0])} x i64]]"
        self.table_size = size 
        tableName = set_variable(tableName,VarType.TABLE,self)
       # name = LLVMGenerator.get_table_element(tableName,size)
        for i in range(0, len(self.tableItems)):
            if len(self.tableItems)!=1:
                name = LLVMGenerator.get_table_element(tableName,size,str(i))
            else:
                name = tableName
            for j in range(0, len(self.tableItems[i])):
                varName = LLVMGenerator.get_table_element(name,f"[{len(self.tableItems[i][j])} x i64]",str(j))
                assignValue(varName, self.tableItems[i][j]);
       
        self.tableItems = [[]]
    def exitTable(self, ctx: ExprParser.TableContext):
        print(self.tableIndexes)
        name = set_variable(GetV(str(ctx.ID()),self,ctx).name,VarType.TABLE,self)
        table = list(filter(lambda x: x.name==GetV(str(ctx.ID()),self,ctx).name,self.tableSizes))[0]
        if self.tableIndexes != 1:
            name = LLVMGenerator.get_table_element(name,f"[{table.i} x [{table.j} x i64]]",str(self.tableIndexes[0].name))
            del self.tableIndexes[0]
        varName =  LLVMGenerator.get_table_element(name,f"[{table.j} x i64]",self.tableIndexes[0].name)
        loadValue(Value(varName,VarType.INT),self)
        self.tableIndexes = []
    def exitIndexes(self, ctx: ExprParser.IndexesContext):
        v = self.stack.pop()
        self.tableIndexes.append(v)
    def error(self, line, msg):
        print("Error, line " + str(line) + ", " + msg)
        exit(1)