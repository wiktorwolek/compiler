
class LLVMGenerator:
    header_text = ""
    main_text = ""
    main_tmp = 1
    buffer = ""
    method_buffer = ""
    str_counter = 1
    tmp = 1
    br = 0
    bstack = []

    
    @staticmethod
    def function_start(id):
        LLVMGenerator.main_text += LLVMGenerator.buffer
        LLVMGenerator.main_tmp = LLVMGenerator.tmp
        LLVMGenerator.buffer = "define i32 @" + id + "() nounwind {\n"
        LLVMGenerator.tmp = 1

    @staticmethod
    def method_start(id, className):

# define linkonce_odr dso_local void @_ZN9Something13incrementYearEv(%class.Something* noundef nonnull align 8 dereferenceable(16) %0) #6 comdat align 2 {
#   %2 = alloca %class.Something*, align 8
#   store %class.Something* %0, %class.Something** %2, align 8
#   %3 = load %class.Something*, %class.Something** %2, align 8
        LLVMGenerator.header_text += "$" + className + "0" + id + " = comdat any\n"

        LLVMGenerator.main_text += LLVMGenerator.buffer
        LLVMGenerator.main_tmp = LLVMGenerator.tmp
        LLVMGenerator.buffer += "define i32 @" + className + "0" + id + "(%struct."+className+"* noundef nonnull align 8 dereferenceable(16) %0) #6 comdat align 2 {\n"
        LLVMGenerator.buffer += "%2 = alloca %struct."+className+"*, align 8\n"
        LLVMGenerator.buffer += "store %struct."+className+"* %0, %struct."+className+"** %2, align 8\n"
        LLVMGenerator.buffer += "%3 = load %struct."+className+"*, %struct."+className+"** %2, align 8\n"
        LLVMGenerator.tmp = 4


    @staticmethod
    def function_end():
        LLVMGenerator.buffer += "ret i32 %" + str(LLVMGenerator.tmp - 1) + "\n"
        LLVMGenerator.buffer += "}\n"
        LLVMGenerator.header_text += LLVMGenerator.buffer
        LLVMGenerator.buffer = ""
        LLVMGenerator.tmp = LLVMGenerator.main_tmp

    @staticmethod
    def method_end():
        LLVMGenerator.buffer += "ret i32 %" + str(LLVMGenerator.tmp - 1) + "\n"
        LLVMGenerator.buffer += "}\n"
        LLVMGenerator.method_buffer += LLVMGenerator.buffer
        LLVMGenerator.buffer = ""
        LLVMGenerator.tmp = LLVMGenerator.main_tmp

    @staticmethod
    def printf_i32(id):
        #LLVMGenerator.buffer  += f"%{LLVMGenerator.tmp} = load i32, i32* {id}\n"
        #LLVMGenerator.tmp += 1
        LLVMGenerator.buffer  += f"%{LLVMGenerator.tmp} = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strp, i32 0, i32 0), i32 {id})\n"
        LLVMGenerator.tmp += 1

    @staticmethod
    def printf_double(id):
        #LLVMGenerator.buffer  += f"%{LLVMGenerator.tmp} = load double, double* {id}\n"
        #LLVMGenerator.tmp += 1
        LLVMGenerator.buffer  += f"%{LLVMGenerator.tmp} = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpd, i32 0, i32 0), double %{LLVMGenerator.tmp - 1})\n"
        LLVMGenerator.tmp += 1

    @staticmethod
    def printf_string(id):
        #LLVMGenerator.buffer  += f"%{LLVMGenerator.tmp} = load i8*, i8** {id}\n"
        #LLVMGenerator.tmp += 1
        LLVMGenerator.buffer  += f"%{LLVMGenerator.tmp} = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strps, i32 0, i32 0), i8* %{LLVMGenerator.tmp - 1})\n"
        LLVMGenerator.tmp += 1

        
    @staticmethod
    def declare_i32(id,is_global):
        if(is_global):
            LLVMGenerator.header_text += "@"+str(id)+" = global i32 0\n"
        else:
            LLVMGenerator.buffer += "%"+str(id)+" = alloca i32\n"

    @staticmethod
    def declare_double(id,is_global):
        if(is_global):
            LLVMGenerator.header_text += "@"+str(id)+" = global double 0.0\n"
        else:
            LLVMGenerator.buffer += "%"+str(id)+" = alloca double\n"

    @staticmethod
    def assign_i32(id, value):
        LLVMGenerator.buffer  += f"store i32 {value}, i32* {id}\n"

    @staticmethod
    def assign_double(id, value):
        LLVMGenerator.buffer  += f"store double {value}, double* {id}\n"

    @staticmethod
    def load_i32(id):
        LLVMGenerator.buffer  += f"%{LLVMGenerator.tmp} = load i32, i32* {id}\n"
        LLVMGenerator.tmp += 1
    @staticmethod
    def load_double(id):
        LLVMGenerator.buffer  += f"%{LLVMGenerator.tmp} = load double, double* {id}\n"
        LLVMGenerator.tmp += 1

    @staticmethod
    def add_i32(val1, val2):
        LLVMGenerator.buffer  += f"%{LLVMGenerator.tmp} = add i32 {val1}, {val2}\n"
        LLVMGenerator.tmp += 1

    @staticmethod
    def add_double(val1, val2):
        LLVMGenerator.buffer  += f"%{LLVMGenerator.tmp} = fadd double {val1}, {val2}\n"
        LLVMGenerator.tmp += 1

    @staticmethod
    def sub_i32(val1, val2):
        LLVMGenerator.main_text += f"%{LLVMGenerator.reg} = sub nuw i32 {val2}, {val1}\n"
        LLVMGenerator.reg += 1 

    @staticmethod
    def sub_double(val1, val2):
        LLVMGenerator.main_text += f"%{LLVMGenerator.reg} = fsub double {val2}, {val1}\n"
        LLVMGenerator.reg += 1 

    @staticmethod
    def mult_i32(val1, val2):
        LLVMGenerator.buffer  += f"%{LLVMGenerator.tmp} = mul i32 {val1}, {val2}\n"
        LLVMGenerator.tmp += 1

    @staticmethod
    def div_i32(val1, val2):
        # %11 = sdiv i32 %9, %10
        LLVMGenerator.buffer += f"%{LLVMGenerator.tmp} = sdiv i32 {val1}, {val2}\n"
        LLVMGenerator.tmp += 1

    @staticmethod
    def div_double(val1, val2):
        # %10 = fdiv float %8, %9
        LLVMGenerator.buffer += f"%{LLVMGenerator.tmp} = fdiv double {val1}, {val2}\n"
        LLVMGenerator.tmp += 1

    @staticmethod
    def mult_double(val1, val2):
        LLVMGenerator.buffer  += f"%{LLVMGenerator.tmp} = fmul double {val1}, {val2}\n"
        LLVMGenerator.tmp += 1

    @staticmethod
    def sitofp(id):
        LLVMGenerator.buffer  += f"%{LLVMGenerator.tmp} = sitofp i32 {id} to double\n"
        LLVMGenerator.tmp += 1

    @staticmethod
    def declare_string(id, is_global):
        if(is_global):
            LLVMGenerator.header_text += "@"+str(id)+" = global i8* zeroinitializer\n"
        # @__const.main.str = private unnamed_addr constant [6 x i8] c"Hello\00", align 1
        else:
            LLVMGenerator.buffer += "%"+id+" = alloca i8*\n"
            # LLVMGenerator.buffer += "%"+str(id)+" = alloca double\n"
            pass

    @staticmethod
    def const_len_string(content):
      length = len(content)+1 
      LLVMGenerator.header_text += "@str"+str(LLVMGenerator.str_counter)+" = constant ["+str(length)+" x i8] c\""+content+"\\00\"\n"
      num = "str"+str(LLVMGenerator.str_counter)
      LLVMGenerator.allocate_string(num, (length-1))
      LLVMGenerator.buffer += "%"+str(LLVMGenerator.tmp)+" = bitcast ["+str(length)+" x i8]* %"+num+" to i8*\n"
      LLVMGenerator.buffer += "call void @llvm.memcpy.p0i8.p0i8.i32(i8* align 1 %"+str(LLVMGenerator.tmp)+", i8* align 1 getelementptr inbounds (["+str(length)+" x i8], ["+str(length)+" x i8]* @"+num+", i32 0, i32 0), i32 "+str(length)+", i1 false)\n"
      LLVMGenerator.tmp +=1
      LLVMGenerator.buffer += "%ptr"+num+" = alloca i8*\n"
      LLVMGenerator.buffer += "%"+str(LLVMGenerator.tmp)+" = getelementptr inbounds ["+str(length)+" x i8], ["+str(length)+" x i8]* %"+num+", i32 0, i32 0\n"
      LLVMGenerator.tmp +=1
      LLVMGenerator.buffer += "store i8* %"+str(LLVMGenerator.tmp-1)+", i8** %ptr"+num+"\n"    
      LLVMGenerator.str_counter+=1

    @staticmethod
    def allocate_string(id, length):
        LLVMGenerator.buffer += "%"+id+" = alloca ["+str(length+1)+" x i8]\n"
    

    @staticmethod
    def assign_string(id, name):
        LLVMGenerator.buffer += "store i8* %"+str(LLVMGenerator.tmp-1)+", i8** "+id+"\n"

    @staticmethod
    def fptosi(id):
        LLVMGenerator.buffer  += f"%{LLVMGenerator.tmp} = fptosi double {id} to i32\n"
        LLVMGenerator.tmp += 1
    @staticmethod
    def scanf_i32(id):
      LLVMGenerator.buffer  += f"%{LLVMGenerator.tmp} = call i32 (i8*, ...) @__isoc99_scanf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @strs, i32 0, i32 0), i32* {id})\n"
      LLVMGenerator.tmp += 1
    @staticmethod
    def scanf_double(id):
    #   %7 = call i32 (i8*, ...) @__isoc99_scanf(i8* noundef getelementptr inbounds ([5 x i8], [5 x i8]* @.str, i64 0, i64 0), double* noundef %6)
      LLVMGenerator.buffer  += f"%{LLVMGenerator.tmp} = call i32 (i8*, ...) @__isoc99_scanf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strsd, i64 0, i64 0), double* {id})\n"
      LLVMGenerator.tmp += 1
    @staticmethod
    def call(id, parameters=""):
        LLVMGenerator.buffer += f"%{LLVMGenerator.tmp} = call i32 @"+id+"("+parameters+")\n"
        LLVMGenerator.tmp += 1




    @staticmethod
    def close_main():
        LLVMGenerator.main_text += LLVMGenerator.buffer
    @staticmethod
    def create_table(id, size, is_global):
        if(is_global):
            #   store i32 0, i32* getelementptr inbounds ([3 x i32], [3 x i32]* @table, i32 0, i32 0), align 4
            LLVMGenerator.header_text += "@"+str(id)+" = global "+str(size)+" zeroinitializer\n"
            return "@"+str(id)
        else:
            LLVMGenerator.buffer += "%"+str(id)+" = alloca "+str(size)+"\n"
            return "%"+str(id)
        
    @staticmethod
    def create_struct(id, object, is_global, structTypeList):
        # %struct.Person = type { i32, float, i32, [50 x i8] }
        if(is_global):
            LLVMGenerator.header_text += "%struct."+str(id)+" = type {"+structTypeList+"}\n"
            return "@"+str(id)
        # else:
            # object.error()
            # LLVMGenerator.buffer += "CREATING STRUCT\n"
            # return "%"+str(id)
    @staticmethod
    def declare_struct(id, struct_name, is_global):
        # %1 = alloca %struct.Person, align 4
        LLVMGenerator.buffer += "%"+str(id)+" = alloca %struct."+str(struct_name)+"\n"

    @staticmethod
    def get_table_element(id, size, index):
        LLVMGenerator.buffer += f"%{LLVMGenerator.tmp} = getelementptr inbounds {size}, {size}* {id}, i32 0, i32 {index}\n"
        LLVMGenerator.tmp += 1
        return "%"+str(LLVMGenerator.tmp - 1)
    
    @staticmethod
    def get_struct_element(id, structName, offset):
        LLVMGenerator.buffer += f"%{LLVMGenerator.tmp} = getelementptr inbounds %struct.{structName}, %struct.{structName}* {id}, i32 0, i32 {offset}\n"
        LLVMGenerator.tmp += 1
        return "%"+str(LLVMGenerator.tmp - 1)

    @staticmethod
    def repeatstart(repetitions):
        LLVMGenerator.buffer += "%"+str(LLVMGenerator.tmp)+" = alloca i32\n"
        counter = LLVMGenerator.tmp
        LLVMGenerator.tmp+=1
        LLVMGenerator.buffer += "store i32 "+"0"+", i32* %"+str(counter)+"\n"
        LLVMGenerator.br += 1
        LLVMGenerator.buffer += f"br label %cond"+str(LLVMGenerator.br)+"\n"
        LLVMGenerator.buffer += f"cond{str(LLVMGenerator.br)}:\n"
        LLVMGenerator.buffer += "%"+str(LLVMGenerator.tmp)+" = load i32, i32* %"+str(counter)+"\n"
        LLVMGenerator.tmp+=1
        LLVMGenerator.buffer += "%"+str(LLVMGenerator.tmp)+" = add i32 %"+str(LLVMGenerator.tmp-1)+", "+"1"+"\n"
        LLVMGenerator.tmp += 1
        LLVMGenerator.buffer += "store i32 %"+str(LLVMGenerator.tmp-1)+", i32* %"+str(counter)+"\n"
        LLVMGenerator.buffer += "%"+str(LLVMGenerator.tmp)+" = icmp slt i32 %"+str(LLVMGenerator.tmp-2)+", "+repetitions+"\n"
        LLVMGenerator.tmp += 1
        LLVMGenerator.buffer += "br i1 %"+str(LLVMGenerator.tmp-1)+", label %true"+str(LLVMGenerator.br)+", label %false"+str(LLVMGenerator.br)+"\n"
        LLVMGenerator.buffer += "true" + str(LLVMGenerator.br)+":\n"
        LLVMGenerator.bstack.append(LLVMGenerator.br)
    @staticmethod
    def repeatend():
        b = LLVMGenerator.bstack.pop()
        LLVMGenerator.buffer += "br label %cond"+str(b)+"\n"
        LLVMGenerator.buffer += "false"+str(b)+":\n"
    @staticmethod
    def ifstart():
        LLVMGenerator.br += 1
        LLVMGenerator.buffer += "br i1 %"+str(LLVMGenerator.tmp-1)+", label %true"+str(LLVMGenerator.br)+", label %false"+str(LLVMGenerator.br)+"\n"
        LLVMGenerator.buffer += "true"+str(LLVMGenerator.br)+":\n"
        LLVMGenerator.bstack.append(LLVMGenerator.br)
    @staticmethod
    def ifend():
        b = LLVMGenerator.bstack.pop()
        LLVMGenerator.buffer += "br label %false"+str(b)+"\n"
        LLVMGenerator.buffer += "false"+str(b)+":\n"
    @staticmethod
    def icmp(id,val):
        LLVMGenerator.buffer +="%"+str(LLVMGenerator.tmp)+" = load i32, i32* "+str(id)+"\n"
        LLVMGenerator.tmp += 1
        LLVMGenerator.buffer += "%"+str(LLVMGenerator.tmp)+" = icmp eq i32 %"+str(LLVMGenerator.tmp-1)+", "+val+"\n"
        LLVMGenerator.tmp += 1
    @staticmethod
    def generate():
    
      text = ""
      text += "declare i32 @printf(i8*, ...)\n"
      text += "declare i32 @__isoc99_scanf(i8*, ...)\n"
      text += "declare void @llvm.memcpy.p0i8.p0i8.i32(i8* noalias nocapture writeonly, i8* noalias nocapture readonly, i32, i1 immarg)\n"
      text += "@strp  = constant [4 x i8] c\"%d\\0A\\00\"\n"
      text += "@strpi = constant [4 x i8] c\"%d\\0A\\00\"\n"
      text += "@strpd = constant [4 x i8] c\"%f\\0A\\00\"\n"
      text += "@strsd = constant [4 x i8] c\"%lf\\00\"\n"
      text += "@strs  = constant [3 x i8] c\"%d\\00\"\n"
      text += "@strps = constant [4 x i8] c\"%s\\0A\\00\"\n"
      text += LLVMGenerator.header_text
      text += "define i32 @main() nounwind{\n"
      text += LLVMGenerator.main_text
      text += "ret i32 0 }\n"
      text += LLVMGenerator.method_buffer
      return text
