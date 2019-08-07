#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 20:29:27 2019

@author: Saul
"""
# 1.整除运算，使用双斜杠 //
print(5 // 2); # 2

print(5 // 2.0); #2.0

# 2.乘方运算 **
print(5 ** 2); #25

# 3. 十六进制，八进制和二进制
print(0x10);  #16
print(0o10);  #8
print(0b0011); #3

# 4.不同于其他一些语言，使用Python变量前必须给它赋值，因为Python变量没有默认值
#    在Python中，名称(标识符)只能由字母、数字和下划线(_)构成，且不能以数字打头。
#    因此Plan9是合法的变量名，而9Plan不是。
x = 5;
print(2 ** x); # 32

# 5.获取用户输入 input:以文本或字符串的方式返回
y = input("please input the value of y:"); # 输入 3
print(y); # 3
x = int(y); #将字符串转换为整数。
print(2 * x); # 8

# 6.函数
# abs计算绝对值, round将浮点数圆整为与之 最接近的整数

print(pow(x,x)); # equals (x ** x), 27
print(abs(-10)); # 10

# 整数总是向下圆整，而round圆整到最接近的整数，并在两个整数一样近时圆整到偶数。
print(round(2.5)); #2
print(round(2.6)); #3
print(round(3.5)); #4

# 7. 模块
import math;
print(math.floor(2.7)); #2
print(int(2.7)); #2
print(math.ceil(2.1)); #3

# 除非必须使用from版的import命令，否则应坚持使用 常规版import命令。用from..import 容易造
# 成很隐蔽的冲突。
from math import sqrt;
print(sqrt(9)); #3.0

# 事实上，可使用变量来引用函数(以及其他大部分Python元素)。执行赋值语句foo =math.sqrt后，
# 就可使用foo来计算平方根。例如，foo(4)的结果为2.0。
foo = math.log10;
print(foo(100)); #2.0

# Python标准库提供了一个专门用于处理 复数的模块。
import cmath;
print(cmath.sqrt(-1)); # 1j


# 8. 字符串
# 8.1引号字符串以及对引号转义
print("let's go!"); # let's go!
print('let"s go!'); # let"s go!
print('let\'s go!'); # let's go!

# 8.2拼接字符串
x = "hello, ";
y = "world"
print(x + y); # hello, world

# 8.3字符串表示str和repr
print("hi,\nhow are you?"); 
# hi,
# how are you?

print(repr("hi,\nhow are you?"));
# 'hi,\nhow are you?'

print(str("hi,\nhow are you?"));
# hi,
# how are you?


# 8.4长字符串、原始字符串和字节
# 8.4.1 要表示很长的字符串(跨越多行的字符串)，可使用三引号(而不是普通引号)。
print('''this is a very long
      string. And it's not over yet. 
      "hello world"
      still here.''');

# 8.4.2 原始字符串不以特殊方式处理反斜杠，因此在有些情况下很有用2。在常规字符串中，反斜
#杠扮演着特殊角色:它对字符进行转义，让你能够在字符串中包含原本无法包含的字符。
print("hello, \nworld!");
#hello, 
#world!

# 在这样的情况下，原始字符串可派上用场，因为它们根本不会对反斜杠做特殊处理，
# 而是让 字符串包含的每个字符都保持原样。另外，原始字符串不能以单个反斜杠结尾。
print(r'hello, \nworld!'); # hello, \nworld!




