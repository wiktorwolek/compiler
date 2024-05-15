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
%d = alloca i32
store i32 %1, i32* %d
ret i32 0 }
