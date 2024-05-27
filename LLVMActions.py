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
    TABLE = 4
    STRING = 5
    STRUCT = 6

# Define Value namedtuple to represent variables
Value = namedtuple('Value', ['name', 'type', 'length'])
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
            v = Value(ID,VarType.INT, 0)
            LLVMGenerator.declare_i32(ID,object.is_global)
        elif type == VarType.REAL:
            v = Value(ID,VarType.REAL, 0)
            LLVMGenerator.declare_double(ID,object.is_global)
        elif type == VarType.STRING:
            v = Value(ID,VarType.STRING, 0)
            LLVMGenerator.declare_string(ID,object.is_global) 
        elif type == VarType.TABLE:
            v = Value(ID,VarType.TABLE, 0)
            LLVMGenerator.create_table(ID,object.table_size,object.is_global)
            object.tableSizes.append(Table(ID,len(object.tableItems),len(object.tableItems[0])))
        elif type == VarType.STRUCT:
            v = Value(ID, VarType.STRUCT, object.structName)
            LLVMGenerator.declare_struct(ID, object.structName, object.is_global)
        return v

def assignValue(ID,v, object, ctx, original_ID = None):
        if original_ID != None:
            value = GetV(original_ID, object, ctx)
            if value.type != v.type:
                object.error(ctx.start.line, "Assign type mismatch in "+str(original_ID))


        if v.type == VarType.INT:
            LLVMGenerator.assign_i32(ID, v.name)
        elif v.type == VarType.REAL:
            LLVMGenerator.assign_double(ID, v.name)
        elif v.type == VarType.STRING:
            LLVMGenerator.assign_string(ID, v.name)
        

def loadValue(v, object):
    if v.type == VarType.INT:
        LLVMGenerator.load_i32(v.name)
    if v.type == VarType.REAL:
        LLVMGenerator.load_double(v.name)
    object.stack.append(Value("%"+str(LLVMGenerator.tmp-1),v.type, 0))

def LoadOrCall(ID, object,ctx):
    id = ""
    if  len(list(filter(lambda x: x.name==ID,object.localnames))) > 0:
        v = list(filter(lambda x: x.name==ID,object.localnames))[0]
        id = "%"+v.name
        loadValue(Value(id,v.type, 0),object)
    elif len(list(filter(lambda x: x.name==ID,object.globalnames))) > 0:
        v = list(filter(lambda x: x.name==ID,object.globalnames))[0]
        id = '@'+v.name
        loadValue(Value(id,v.type, 0),object)
    elif len(list(filter(lambda x: x==ID,object.functions))) > 0:
        id = ID
        LLVMGenerator.call(ID)
        object.stack.append(Value('%'+str(LLVMGenerator.tmp-1),VarType.INT, 0))
    else:
        object.error(ctx.start.line,"Unknown "+str(ID)+ ": local > global > function")
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
        self.structures = dict()
        # self.structItems = []
        # self.structItemTypes = []

    def exitAssign(self, ctx):
        v = self.stack.pop()
        if type(ctx.children[0].children[0]) is ExprParser.IdContext:
            ID = ctx.children[0].children[0].ID().getText()
            original_ID = ID
        else:
            ID = self.stack.pop().name
            original_ID = None


        if ID[0] != '%':
            if ID[0]=='@':
                ID = ID[1:]
            ID = set_variable(ID, v.type, self)
        
        assignValue(ID,v, self, ctx, original_ID)


    def exitIdToken(self, ctx: ExprParser.IdTokenContext):

        if hasattr(ctx,"ID") and callable(ctx.ID) and ctx.ID() != None:
            a = ctx.ID()
            ID = ctx.ID().getText()
            id = LoadOrCall(ID,self,ctx)
            if id == "":
                self.stack.append(Value(ID, VarType.INT, 0))
            # print(self.stack)
        else:
            v = self.stack.pop()
            loadValue(v,self)

    def enterProg(self, ctx):
        self.is_global = True
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
        self.is_global = False
        set_variable(self.function,VarType.INT,self)

    def exitFblock(self,ctx:ExprParser.FblockContext):
        if len(list(filter(lambda x: x.name==self.function,self.localnames))) == 0:
          assignValue(set_variable(self.function,VarType.INT,self),Value("0",VarType.INT, 0), self, ctx)
        loadValue(Value("%"+self.function,VarType.INT, 0),self)
        LLVMGenerator.function_end()
        self.localnames = []
        self.is_global = True

    def enterSblock(self, ctx:ExprParser.SblockContext):
        print(ctx.children[1].children[0].children[0].symbol.text)
        print(self.stack)

    def exitDeclStruct(self, ctx:ExprParser.DeclStructContext):
        self.structName = ctx.children[0].stop.text
        set_variable(ctx.ID().getText(), VarType.STRUCT, self)

    def exitStructref(self, ctx: ExprParser.StructrefContext):
        structName = ctx.children[0].symbol.text
        fieldName = ctx.children[2].symbol.text
        structItems = self.structures[GetV(structName, self, ctx).length]
        try:
            value = list(filter(lambda x: x.name==fieldName, structItems))[0]
            offset = structItems.index(value)
        except:
            self.error(ctx.start.line, "undeclared structure field is referenced")
        tmpID = LLVMGenerator.get_struct_element("%"+structName, GetV(structName, self, ctx).length, offset)
        self.stack.append(Value(tmpID, value.type, 0))
        

    def exitDeclInt(self, ctx:ExprParser.DeclIntContext):
        self.structures[self.structName].append(
            Value(ctx.ID().getText(), VarType.INT, 0)
            )

    def exitDeclReal(self, ctx:ExprParser.DeclRealContext):
        self.structures[self.structName].append(
            Value(ctx.ID().getText(), VarType.REAL, 0)
            )

    def exitSblock(self, ctx:ExprParser.SblockContext):
        itemTypeNames = []
        for item in self.structures[self.structName]:
            if item.type == VarType.INT:
                itemTypeNames.append('i32')
            elif item.type == VarType.REAL:
                itemTypeNames.append('double')

        structTypeList = ', '.join(itemTypeNames)

        LLVMGenerator.create_struct(self.structName, self, self.is_global, structTypeList)


    def enterStruct(self, ctx:ExprParser.StructContext):
        self.structName = ctx.children[1].children[0].symbol.text
        self.structures.update({self.structName : []})

    def exitID(self, ctx:ExprParser.IdContext):
        print(self.stack)
           
    def exitInt(self, ctx):
        self.stack.append(Value(ctx.INT().getText(), VarType.INT, 0))

    def exitReal(self, ctx):
        self.stack.append(Value(ctx.REAL().getText(), VarType.REAL, 0))

    def exitString(self, ctx):
        self.string_value = ctx.STRING().getText()
        self.stack.append(Value(ctx.STRING().getText(), VarType.STRING, 0))
        
        str_value = ctx.STRING().getText()

        str_content = str_value[1:len(str_value)-1]
        LLVMGenerator.const_len_string(str_content)
        num = "ptrstr"+str(LLVMGenerator.str_counter-1)
        self.stack.append(Value(num, VarType.STRING, len(str_content)) )

    def exitAdd(self, ctx):
        v1 = self.stack.pop()
        v2 = self.stack.pop()
        if v1.type == v2.type:
            if v1.type == VarType.INT:
                LLVMGenerator.add_i32(v1.name, v2.name)
                self.stack.append(Value("%" + str(LLVMGenerator.tmp - 1), VarType.INT, 0))
            elif v1.type == VarType.REAL:
                LLVMGenerator.add_double(v1.name, v2.name)
                self.stack.append(Value("%" + str(LLVMGenerator.tmp - 1), VarType.REAL, 0))
        else:
            self.error(ctx.start.line, "add type mismatch")

    def exitSubstract(self, ctx: ExprParser.SubstractContext):
        v1 = self.stack.pop()
        v2 = self.stack.pop()
        if v1.type == v2.type:
            if v1.type == VarType.INT:
                LLVMGenerator.sub_i32(v1.name, v2.name)
                self.stack.append(Value("%" + str(LLVMGenerator.reg - 1), VarType.INT))
            elif v1.type == VarType.REAL:
                LLVMGenerator.sub_double(v1.name, v2.name)
                self.stack.append(Value("%" + str(LLVMGenerator.reg - 1), VarType.REAL))
        else:
            self.error(ctx.getStart().getLine(), "substract type mismatch")

    def exitMultiply(self, ctx):
        v1 = self.stack.pop()
        v2 = self.stack.pop()
        if v1.type == v2.type:
            if v1.type == VarType.INT:
                LLVMGenerator.mult_i32(v1.name, v2.name)
                self.stack.append(Value("%" + str(LLVMGenerator.tmp - 1), VarType.INT, 0))
            elif v1.type == VarType.REAL:
                LLVMGenerator.mult_double(v1.name, v2.name)
                self.stack.append(Value("%" + str(LLVMGenerator.tmp - 1), VarType.REAL, 0))
        else:
            self.error(ctx.start.line, "mult type mismatch")

    def exitDivide(self, ctx: ExprParser.DivideContext):
        v1 = self.stack.pop()
        v2 = self.stack.pop()

        if v2.type == VarType.REAL and v1.type == VarType.INT:
            LLVMGenerator.sitofp(v1.name)
            self.stack.append(Value("%" + str(LLVMGenerator.tmp - 1), VarType.REAL, 0))
            v1 = self.stack.pop()
        if v2.type == VarType.INT and v1.type == VarType.REAL:
            LLVMGenerator.sitofp(v2.name)
            self.stack.append(Value("%" + str(LLVMGenerator.tmp - 1), VarType.REAL, 0))
            v2 = self.stack.pop()

        if v1.type == v2.type:
            if v1.type == VarType.INT:
                LLVMGenerator.div_i32(v2.name, v1.name)
                self.stack.append(Value("%" + str(LLVMGenerator.tmp - 1), VarType.INT, 0))
            if v1.type == VarType.REAL:
                LLVMGenerator.div_double(v2.name, v1.name)
                self.stack.append(Value("%" + str(LLVMGenerator.tmp - 1), VarType.REAL, 0))
        else:
            self.error(ctx.start.line, "div type mismatch")



    def exitToint(self, ctx):
        v = self.stack.pop()
        LLVMGenerator.fptosi(v.name)
        self.stack.append(Value("%" + str(LLVMGenerator.tmp - 1), VarType.INT, 0))

    def exitToreal(self, ctx):
        v = self.stack.pop()
        LLVMGenerator.sitofp(v.name)
        self.stack.append(Value("%" + str(LLVMGenerator.tmp - 1), VarType.REAL, 0))

    def exitCall(self,ctx:ExprParser.CallContext):
        LLVMGenerator.call(ctx.ID().getText())
        self.stack.append(Value('%'+str(LLVMGenerator.tmp-1),VarType.INT, 0))

    def exitReadInt(self, ctx:ExprParser.ReadIntContext):
        ID = ctx.ID().getText()
        v = set_variable(ID,VarType.INT,self)
        LLVMGenerator.scanf_i32(v)
        # assignValue(v,Value('%'+str(LLVMGenerator.tmp-1),VarType.INT, 0))

    def exitReadDouble(self, ctx:ExprParser.ReadDoubleContext):
        ID = ctx.ID().getText()
        v = set_variable(ID,VarType.REAL,self)
        LLVMGenerator.scanf_double(v)
        # assignValue(v,Value('%'+str(LLVMGenerator.tmp-1),VarType.REAL, 0))

    def exitWrite(self, ctx:ExprParser.WriteContext):
        v = self.stack.pop()
        ID = v.name
        #ID = LoadOrCall(ID,self,ctx)
        if v.type == VarType.INT:
            LLVMGenerator.printf_i32(ID)
        elif v.type == VarType.REAL:
            LLVMGenerator.printf_double(ID)
        elif v.type == VarType.STRING:
            LLVMGenerator.printf_string(ID)
    
    def exitTablerow(self, ctx: ExprParser.TablerowContext):
        self.tableItems.append([])
        
    def exitTableitem(self, ctx: ExprParser.TableitemContext):
        v = self.stack.pop()
        self.tableItems[-1].append(v)

    def exitAssigntable(self, ctx: ExprParser.AssigntableContext):
        # print(self.tableItems) 
        tableName = ctx.ID().getText()

        del self.tableItems[-1]
        if len(self.tableItems)==1:
            size = f"[{len(self.tableItems[0])} x i32]"
            
        else:
            size = f"[{len(self.tableItems)} x [{len(self.tableItems[0])} x i32]]"
        self.table_size = size 
        self.tableSizes.append(Table(tableName,len(self.tableItems),len(self.tableItems[0])))
        tableName = set_variable(tableName,VarType.TABLE,self)
       # name = LLVMGenerator.get_table_element(tableName,size)
       
        for i in range(0, len(self.tableItems)):
            if len(self.tableItems)!=1:
                name = LLVMGenerator.get_table_element(tableName,size,str(i))
            else:
                name = tableName
            for j in range(0, len(self.tableItems[i])):
                varName = LLVMGenerator.get_table_element(name,f"[{len(self.tableItems[i])} x i32]",str(j))
                assignValue(varName, self.tableItems[i][j], self, ctx)
       
        self.tableItems = [[]]


    def exitTable(self, ctx: ExprParser.TableContext):
        # print(self.tableIndexes)

        name = set_variable(GetV(str(ctx.ID()),self,ctx).name,VarType.TABLE,self)
        table = list(filter(lambda x: x.name == GetV(str(ctx.ID()),self,ctx).name,self.tableSizes))[0]

        if len(self.tableIndexes) != 1:
            name = LLVMGenerator.get_table_element(name,f"[{table.i} x [{table.j} x i32]]",str(self.tableIndexes[0].name))
            del self.tableIndexes[0]
        varName =  LLVMGenerator.get_table_element(name,f"[{table.j} x i32]",self.tableIndexes[0].name)
        #loadValue(Value(varName,VarType.INT, 0),self)
        self.stack.append(Value(varName,VarType.INT, 0))
        self.tableIndexes = []
        self.tableValue = self.stack[-1]


    def exitIndexes(self, ctx: ExprParser.IndexesContext):
        v = self.stack.pop()
        self.tableIndexes.append(v)
    def exitRepetitions(self, ctx: ExprParser.RepetitionsContext ):
        v = self.stack.pop()
        if v.type != VarType.INT:
            self.error(ctx.start.line, "repeticions are not int")
        LLVMGenerator.repeatstart(v.name)
    def exitBlockrep(self, ctx:ExprParser.BlockrepContext):
        LLVMGenerator.repeatend()
    def enterBlockif(self,ctx:ExprParser.BlockifContext):
        LLVMGenerator.ifstart()
    def exitBlockif(self, ctx: ExprParser.BlockifContext):
        LLVMGenerator.ifend()
    def exitEqual(self,ctx:ExprParser.EqualContext):
        ID = ctx.ID().getText()
        INT = self.stack.pop()
        v  = set_variable(ID,VarType.INT,self)
        LLVMGenerator.icmp(v,INT.name)
    def error(self, line, msg):
        print("Error, line " + str(line) + ", " + msg)
        exit(1)