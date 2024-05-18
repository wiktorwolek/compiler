class LLVMGenerator:
    header_text = ""
    main_text = ""
    main_tmp = 1
    buffer = ""
    tmp = 1;
    @staticmethod
    def function_start(id):
        LLVMGenerator.main_text += LLVMGenerator.buffer
        LLVMGenerator.main_tmp = LLVMGenerator.tmp
        LLVMGenerator.buffer = "define i32 @" + id + "() nounwind {\n"
        LLVMGenerator.tmp = 1
    @staticmethod
    def function_end():
        LLVMGenerator.buffer += "ret i32 %" + str(LLVMGenerator.tmp - 1) + "\n"
        LLVMGenerator.buffer += "}\n"
        LLVMGenerator.header_text += LLVMGenerator.buffer
        LLVMGenerator.buffer = ""
        LLVMGenerator.tmp = LLVMGenerator.main_tmp
    
    @staticmethod
    def printf_i32(id):
        LLVMGenerator.buffer  += f"%{LLVMGenerator.tmp} = load i32, i32* {id}\n"
        LLVMGenerator.tmp += 1
        LLVMGenerator.buffer  += f"%{LLVMGenerator.tmp} = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strp, i32 0, i32 0), i32 %{LLVMGenerator.tmp - 1})\n"
        LLVMGenerator.tmp += 1

    @staticmethod
    def printf_double(id):
        LLVMGenerator.buffer  += f"%{LLVMGenerator.tmp} = load double, double* {id}\n"
        LLVMGenerator.tmp += 1
        LLVMGenerator.buffer  += f"%{LLVMGenerator.tmp} = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpd, i32 0, i32 0), double %{LLVMGenerator.tmp - 1})\n"
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
            LLVMGenerator.header_text += "@"+str(id)+" = global double 0\n"
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
    def mult_i32(val1, val2):
        LLVMGenerator.buffer  += f"%{LLVMGenerator.tmp} = mul i32 {val1}, {val2}\n"
        LLVMGenerator.tmp += 1

    @staticmethod
    def div_i32(val1, val2):
        # %11 = sdiv i32 %9, %10
        LLVMGenerator.main_text += f"%{LLVMGenerator.tmp} = sdiv i32 {val1}, {val2}\n"
        LLVMGenerator.tmp += 1

    @staticmethod
    def div_double(val1, val2):
        # %10 = fdiv float %8, %9
        LLVMGenerator.main_text += f"%{LLVMGenerator.tmp} = fdiv double {val1}, {val2}\n"
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
    def fptosi(id):
        LLVMGenerator.buffer  += f"%{LLVMGenerator.tmp} = fptosi double {id} to i32\n"
        LLVMGenerator.tmp += 1
    @staticmethod
    def scanf(id):
      LLVMGenerator.buffer  += f"%{LLVMGenerator.tmp} = call i32 (i8*, ...) @__isoc99_scanf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @strs, i32 0, i32 0), i32* {id})\n"
      LLVMGenerator.tmp += 1
    @staticmethod
    def call(id):
        LLVMGenerator.buffer += f"%{LLVMGenerator.tmp} = call i32 @"+id+"()\n";
        LLVMGenerator.tmp += 1
    @staticmethod
    def close_main():
        LLVMGenerator.main_text += LLVMGenerator.buffer;
    @staticmethod
    def generate():
      text = ""
      text += "declare i32 @printf(i8*, ...)\n"
      text += "declare i32 @__isoc99_scanf(i8*, ...)\n"
      text += "@strp  = constant [4 x i8] c\"%d\\0A\\00\"\n"
      text += "@strpi = constant [4 x i8] c\"%d\\0A\\00\"\n";
      text += "@strpd = constant [4 x i8] c\"%f\\0A\\00\"\n";
      text += "@strs  = constant [3 x i8] c\"%d\\00\"\n"
      text += LLVMGenerator.header_text
      text += "define i32 @main() nounwind{\n"
      text += LLVMGenerator.main_text
      text += "ret i32 0 }\n"
      return text
