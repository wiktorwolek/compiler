declare i32 @printf(i8*, ...)
declare i32 @__isoc99_scanf(i8*, ...)
@strp = constant [4 x i8] c"%d\0A\00"
@strs = constant [3 x i8] c"%d\00"
define i32 @main() nounwind{
%y = alloca i32
store i32 2, i32* %y
%a = alloca i32
store i32 16, i32* %a
%1 = load i32, i32* %a
%2 = load i32, i32* %y
%3 = add i32 %2, %1
%z = alloca i32
store i32 %3, i32* %z
%4 = load i32, i32* %z
%5 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpi, i32 0, i32 0), i32 %4)
ret i32 0 }
