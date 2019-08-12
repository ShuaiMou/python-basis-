#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 17:34:56 2019

@author: Saul

字符串基本操作
"""


# 所有标准序列操作(索引、切片、乘法、成员资格检查、长度、最小值和最 大值)都适用于字符串,
# 字符串是不可变的，因此所有的元素赋值和切片赋值都是非法的。

#3 字符串方法

#3.1 center
# 方法center通过在两边添加填充字符(默认为空格)让字符串居中。
print("The Middle by Jimmy Eat World".center(39));

print("The Middle by Jimmy Eat World".center(39, "*"));
#      The Middle by Jimmy Eat World     
# *****The Middle by Jimmy Eat World*****

#3.2 find
# 方法find在字符串中查找子串。如果找到，就返回子串的第一个字符的索引，否则返回-1。
print('With a moo-moo here, and a moo-moo there'.find('moo')); #7

title = "Monty Python's Flying Circus";
print(title.find('Monty'));  #0

# 还可指定搜索的起点和终点(它们都是可选的)。
subject = '$$$ Get rich now!!! $$$';
print(subject.find('$$$'));  # 0

print(subject.find('$$$', 1)); # 只指定了起点, 20
print(subject.find('!!!'));   # 16
print(subject.find('!!!', 0, 16)); # 同时指定了起点和终点, -1

# 3.3 join
# join是一个非常重要的字符串方法，其作用与split相反，用于合并序列的元素。

seq = ['1', '2', '3', '4', '5'];
sep = '+';
print(sep.join(seq)); # 合并一个字符串列表
# 1+2+3+4+5

dirs = '', 'usr', 'bin', 'env';
print('/'.join(dirs));  # /usr/bin/env

print('C:' + '\\'.join(dirs)); # C:\usr\bin\env

# 3.4 lower
#  返回字符串的小写版本。

name = 'Gumby';
names = ['gumby', 'smith', 'jones']
if name.lower() in names: print('Found it!');



# 3.5 replace
# 将指定子串都替换为另一个字符串，并返回替换后的结果。
print('This is a test'.replace('is', 'eez')); # Theez eez a test

# 3.6 split
# 其作用与join相反，用于将字符串拆分为序列。
# 注意，如果没有指定分隔符，将默认在单个或多个连续的空白字符(空格、制表符、换行符 等)处进行拆分。
print('1+2+3+4+5'.split('+')); #['1', '2', '3', '4', '5']
print('Using the default'.split()); # ['Using', 'the', 'default']


#3.7 strip 
# 将字符串开头和末尾的空白(但不包括中间的空白)删除，并返回删除后的结果。
print(' internal whitespace is kept ');
print(' internal whitespace is kept '.strip());
#  internal whitespace is kept 
# internal whitespace is kept

# 还可在一个字符串参数中指定要删除哪些字符
print('*** SPAM * for * everyone!!! ***'.strip('* !')); # SPAM * for * everyone
# 删除了开头和结尾的感叹号，星号和空格

















