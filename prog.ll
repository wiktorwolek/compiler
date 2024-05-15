declare i32 @printf(i8*, ...)
declare i32 @__isoc99_scanf(i8*, ...)
@strp = constant [4 x i8] c"%d\0A\00"
@strpi = constant [4 x i8] c"%d\0A\00"
@strpd = constant [4 x i8] c"%f\0A\00"
@strs = constant [3 x i8] c"%d\00"
define i32 @main() nounwind{
%a = alloca i32
store i32 32, i32* %a
%b = alloca i32
store i32 8, i32* %b
%c = alloca i32
store i32 3, i32* %c
%1 = load i32, i32* %a
%2 = load i32, i32* %b
; taken from stack: v1:%2, v2:%1
%3 = sdiv i32 %2, %1
%d = alloca i32
store i32 %3, i32* %d
%4 = load i32, i32* %a
%5 = load i32, i32* %c
; taken from stack: v1:%5, v2:%4
%6 = sdiv i32 %5, %4
%e = alloca i32
store i32 %6, i32* %e
%7 = load i32, i32* %d
%8 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strp, i32 0, i32 0), i32 %7)
ret i32 0 }
