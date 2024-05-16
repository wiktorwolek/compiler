declare i32 @printf(i8*, ...)
declare i32 @__isoc99_scanf(i8*, ...)
@strp = constant [4 x i8] c"%d\0A\00"
@strpi = constant [4 x i8] c"%d\0A\00"
@strpd = constant [4 x i8] c"%f\0A\00"
@strs = constant [3 x i8] c"%d\00"
@x = global i32 0
define i32 @fun() nounwind {
%fun = alloca i32
store i32 3, i32* %fun
%1 = load i32, i32* %fun
ret i32 %1
}
@zosia = global i32 0
define i32 @main() nounwind{
store i32 1, i32* @x
%1 = call i32 @fun()
%2 = add i32 4, %1
%3 = mul i32 2, %2
%4 = call i32 @fun()
%5 = sitofp i32 %4 to double
%6 = fadd double 1.6, %5
%7 = fptosi double %6 to i32
%8 = add i32 %7, %3
store i32 %8, i32* @zosia
%9 = load i32, i32* @zosia
%10 = load i32, i32* @zosia
%11 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strp, i32 0, i32 0), i32 %10)
ret i32 0 }
