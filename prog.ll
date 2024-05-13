declare i32 @printf(i8*, ...)
declare i32 @__isoc99_scanf(i8*, ...)
@strp = constant [4 x i8] c"%d\0A\00"
@strs = constant [3 x i8] c"%d\00"
define i32 @main() nounwind{
%x = alloca i32
%1 = call i32 (i8*, ...) @__isoc99_scanf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @strs, i32 0, i32 0), i32* %x)
%y = alloca i32
store i32 2, i32* %y
%a = alloca i32
store i32 16, i32* %a
%2 = load i32, i32* %x
%3 = load i32, i32* %y
%4 = load i32, i32* %a
%5 = add i32 4, %4
%6 = add i32 %5, %3
%7 = add i32 %6, %2
%z = alloca i32
store i32 %7, i32* %z
%8 = load i32, i32* %z
%9 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strp, i32 0, i32 0), i32 %8)
%10 = load i32, i32* %x
%11 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strp, i32 0, i32 0), i32 %10)
ret i32 0 }
