; ModuleID = "C:\Users\santi\OneDrive\Documents\GitHub\PythonCompiler\codegen.py"
target triple = "x86_64-pc-windows-msvc"
target datalayout = ""

define void @"main"()
{
entry:
  %".2" = udiv i8 2, 6
  %".3" = mul i8 6, %".2"
  %".4" = bitcast [5 x i8]* @"fstr" to i8*
  %".5" = call i32 (i8*, ...) @"write"(i8* %".4", i8 %".3")
  ret void
}

declare i32 @"write"(i8* %".1", ...)

@"fstr" = internal constant [5 x i8] c"%i \0a\00"