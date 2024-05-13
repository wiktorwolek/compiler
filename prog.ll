declare i32 @printf(i8*, ...)
declare i32 @__isoc99_scanf(i8*, ...)
@strp = constant [4 x i8] c"%d\0A\00"
@strs = constant [3 x i8] c"%d\00"
define i32 @main() nounwind{
%x = alloca i32
store i32 1, i32* %x
%1 = load i32, i32* %x
%2 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strp, i32 0, i32 0), i32 %1)
%y = alloca i32
store i32 2, i32* %y
%a = alloca i32
store i32 3, i32* %a
%3 = load i32, i32* %x
%4 = load i32, i32* %y
%5 = add i32 %4, %3
%z = alloca i32
store i32 %5, i32* %z
ret i32 0 }
