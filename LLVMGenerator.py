class LLVMGenerator:
    header_text = ""
    main_text = ""
    reg = 1

    @staticmethod
    def printf_i32(id):
        LLVMGenerator.main_text += f"%{LLVMGenerator.reg} = load i32, i32* %{id}\n"
        LLVMGenerator.reg += 1
        LLVMGenerator.main_text += f"%{LLVMGenerator.reg} = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strp, i32 0, i32 0), i32 %{LLVMGenerator.reg - 1})\n"
        LLVMGenerator.reg += 1

    @staticmethod
    def printf_double(id):
        LLVMGenerator.main_text += f"%{LLVMGenerator.reg} = load double, double* %{id}\n"
        LLVMGenerator.reg += 1
        LLVMGenerator.main_text += f"%{LLVMGenerator.reg} = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpd, i32 0, i32 0), double %{LLVMGenerator.reg - 1})\n"
        LLVMGenerator.reg += 1

    @staticmethod
    def declare_i32(id):
        LLVMGenerator.main_text += f"%{id} = alloca i32\n"

    @staticmethod
    def declare_double(id):
        LLVMGenerator.main_text += f"%{id} = alloca double\n"

    @staticmethod
    def assign_i32(id, value):
        LLVMGenerator.main_text += f"store i32 {value}, i32* %{id}\n"

    @staticmethod
    def assign_double(id, value):
        LLVMGenerator.main_text += f"store double {value}, double* %{id}\n"

    @staticmethod
    def load_i32(id):
        LLVMGenerator.main_text += f"%{LLVMGenerator.reg} = load i32, i32* %{id}\n"
        LLVMGenerator.reg += 1

    @staticmethod
    def load_double(id):
        LLVMGenerator.main_text += f"%{LLVMGenerator.reg} = load double, double* %{id}\n"
        LLVMGenerator.reg += 1

    @staticmethod
    def add_i32(val1, val2):
        LLVMGenerator.main_text += f"%{LLVMGenerator.reg} = add i32 {val1}, {val2}\n"
        LLVMGenerator.reg += 1

    @staticmethod
    def add_double(val1, val2):
        LLVMGenerator.main_text += f"%{LLVMGenerator.reg} = fadd double {val1}, {val2}\n"
        LLVMGenerator.reg += 1

    @staticmethod
    def mult_i32(val1, val2):
        LLVMGenerator.main_text += f"%{LLVMGenerator.reg} = mul i32 {val1}, {val2}\n"
        LLVMGenerator.reg += 1

    @staticmethod
    def mult_double(val1, val2):
        LLVMGenerator.main_text += f"%{LLVMGenerator.reg} = fmul double {val1}, {val2}\n"
        LLVMGenerator.reg += 1

    @staticmethod
    def sitofp(id):
        LLVMGenerator.main_text += f"%{LLVMGenerator.reg} = sitofp i32 {id} to double\n"
        LLVMGenerator.reg += 1

    @staticmethod
    def fptosi(id):
        LLVMGenerator.main_text += f"%{LLVMGenerator.reg} = fptosi double {id} to i32\n"
        LLVMGenerator.reg += 1
    @staticmethod
    def scanf(id):
      LLVMGenerator.main_text += f"%{LLVMGenerator.reg} = call i32 (i8*, ...) @__isoc99_scanf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @strs, i32 0, i32 0), i32* %{id})\n"
      LLVMGenerator.reg += 1
    @staticmethod
    def generate():
      text = ""
      text += "declare i32 @printf(i8*, ...)\n"
      text += "declare i32 @__isoc99_scanf(i8*, ...)\n"
      text += "@strp = constant [4 x i8] c\"%d\\0A\\00\"\n"
      text += "@strpi = constant [4 x i8] c\"%d\\0A\\00\"\n";
      text += "@strpd = constant [4 x i8] c\"%f\\0A\\00\"\n";
      text += "@strs = constant [3 x i8] c\"%d\\00\"\n"
      text += LLVMGenerator.header_text
      text += "define i32 @main() nounwind{\n"
      text += LLVMGenerator.main_text
      text += "ret i32 0 }\n"
      return text
