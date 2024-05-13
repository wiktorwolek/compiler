declare i32 @printf(i8*, ...)
declare i32 @__isoc99_scanf(i8*, ...)
@strp = constant [4 x i8] c"%d\0A\00"
@strpi = constant [4 x i8] c"%d\0A\00"
@strpd = constant [4 x i8] c"%f\0A\00"
@strs = constant [3 x i8] c"%d\00"
define i32 @main() nounwind{
%y = alloca double
store double 2.1, double* %y
%a = alloca double
store double 16.1, double* %a
%1 = load double, double* %a
%2 = fadd double 1.1, %1
%3 = load double, double* %y
%4 = fmul double %3, %2
%5 = fptosi double %4 to i32
%z = alloca i32
store i32 %5, i32* %z
%6 = load i32, i32* %z
%7 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strp, i32 0, i32 0), i32 %6)
ret i32 0 }
