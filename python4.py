#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 12:12:48 2019

@author: moushuai
 字典
"""

# 4 创建和使用字典
# 字典由键及其相应的值组成，这种键值对称为项(item)。每个键与其值之间都用冒号(:)分隔，
#项之间用逗号分隔，而整个字典放在花括号内。空字典(没有任何项)用两个花括号表示，类似于这样:{}。

# 4.1 函数 dict
# 可使用函数dict1从其他映射(如其他字典)或键值对序列创建字典。
items = [('name', 'Gumby'), ('age', 42)];
d = dict(items);
print(d);  #{'name': 'Gumby', 'age': 42}
print(d['name']); #Gumby

# 还可使用关键字实参来调用这个函数
d1 = dict(name='Gumby', age=42);
print(d1);  # {'name': 'Gumby', 'age': 42}

# 4.2 基本的字典操作
# 字典的基本行为在很多方面都类似于序列。
# len(d)返回字典d包含的项(键值对)数。
# d[k]返回与键k相关联的值。
# d[k] = v将值v关联到键k。
# del d[k]删除键为k的项。
# k in d检查字典d是否包含键为k的项。

#  一个简单的数据库
# 一个将人名用作键的字典。每个人都用一个字典表示，
# 字典包含键'phone'和'addr'，它们分别与电话号码和地址相关联

people = {
        'Alice' : {
                'phone' : '2341',
                'address': 'bourke st 12'
                },
        'Beth' : {
                'phone' : '9120',
                'address' : 'bar st 23'
                },
        'Saul' : {
                'phone' : '110',
                'address' : 'swasonton st 33'
                }
        };
        
# 电话号码和地址的描述性标签，供打印输出时使用
labels = {
        'phone' : 'phone number',
        'address' : 'address'
        };
name = input('name; ');

# 要查找电话号码还是地址?
request = input('phone number(p) or address(a)? ');

# 使用正确的键
if request == 'p' : key  = 'phone';
if request == 'a' : key = 'address';

# 仅当名字是字典包含的键时才打印信息:
if name in people : print("{}'s {} is {}.".format(name, labels[key], people[name][key]));


# name; Saul

# phone number(p) or address(a)? a
# Saul's address is swasonton st 33.


# 4.3 将字符串格式设置功能用于字典
phonebook = {'Beth': '9102', 'Alice': '2341', 'Cecil': '3258'};
print( "Cecil's phone number is {Cecil}.".format_map(phonebook));

# 在模板系统中，这种字符串格式设置方式很有用(下面的示例使用的是HTML)
template = ''' <html>
    <head><title>{title}</title></head>
    <body>
    <h1>{title}</h1>
    <p>{text}</p>
    </body>
    </html>''';
data = {'title' : 'My home page', 'text' : 'welcome to my homepage!'};
print(template.format_map(data));

"""
<html>
    <head><title>My home page</title></head>
    <body>
    <h1>My home page</h1>
    <p>welcome to my homepage!</p>
    </body>
    </html>
"""


# 4.4 字典方法
# 4.4.1 clear
# 删除所有的字典项，这种操作是就地执行的(就像list.sort一样)，因此什么都不 返回(或者说返回None)。
x = {};
y = x;
x['key'] = 'value';
print(y);    # {'key': 'value'}
x = {};
print(y);     # {'key': 'value'}

x = {};
y = x;
x['key'] = 'value';
print(y);    # {'key': 'value'}
x.clear();
print(y);   # {}

"""
在这两个场景中，x和y最初都指向同一个字典。在第一个场景中，通过将一个空字典赋给x来“清空”它。
这对y没有任何影响，它依然指向原来的字典。这种行为可能正是你想要的，但要删除原来字典的所有元素，
必须使用clear。如果这样做，y也将是空的，如第二个场景所示。
"""

# 4.4.2. copy
# 返回一个新字典，其包含的键值对与原来的字典相同(这个方法执行的是浅复制， 因为值本身是原件，而非副本)。
x = {'username': 'admin', 'machines': ['foo', 'bar', 'baz']};
y = x.copy();
y['username'] = 'saul';
y['machines'].remove('bar');
print(y);
print(x);

"""
{'username': 'saul', 'machines': ['foo', 'baz']}
{'username': 'admin', 'machines': ['foo', 'baz']}

当替换副本中的值时，原件不受影响。然而，如果修改副本中的值(就地修改而 不是替换)，
原件也将发生变化，因为原件指向的也是被修改的值(如这个示例中的'machines' 列表所示)

为避免这种问题，一种办法是执行深复制，即同时复制值及其包含的所有值，等等。为此， 
可使用模块copy中的函数deepcopy。

"""
from copy import deepcopy
x = {'username': 'admin', 'machines': ['foo', 'bar', 'baz']};
y = deepcopy(x);
y['username'] = 'saul';
y['machines'].remove('bar');
print(y);
print(x);

"""
{'username': 'saul', 'machines': ['foo', 'baz']}
{'username': 'admin', 'machines': ['foo', 'bar', 'baz']}
"""

# 4.4.3 fromkeys
# 创建一个新字典，其中包含指定的键，且每个键对应的值都是None。
a = {}.fromkeys(['name', 'age']);
print(a);  # {'name': None, 'age': None}

b = dict.fromkeys(['anme','age']);
print(b);  # {'anme': None, 'age': None}

# 如果不想使用默认值None，可提供特定的值。
c = dict.fromkeys(['anme','age'], 'unknown');
print(c); # {'anme': 'unknown', 'age': 'unknown'}


# 4.4.4 get
# 方法get为访问字典项提供了宽松的环境。通常，如果你试图访问字典中没有的项，将引发错误。而使用get不会这样.
d = {};
print(d.get('name')); # None

# 使用get来访问不存在的键时，没有引发异常，而是返回None。你可指定“默认” 值，
# 这样将返回你指定的值而不是None。
print(d.get('name', 'N/A')); # N/A


# 4.4.5  pop
# 可用于获取与指定键相关联的值，并将该键值对从字典中删除。
d = {'x': 1, 'y': 2};
print(d.pop('x'));  # 1
print(d);  # {'y': 2}

# 4.4.6  setdefault
# 方法setdefault有点像get，因为它也获取与指定键相关联的值，但除此之外，setdefault 
# 还在字典不包含指定的键时，在字典中添加指定的键值对。

# 4.4.6 update
# 使用一个字典中的项来更新另一个字典。
d = {
'title': 'Python Web Site',
'url': 'http://www.python.org', 
'changed': 'Mar 14 22:09:15 MET 2016'
};
x = {'title': 'Python Language Website'};
d.update(x);
print(d);

"""
{
'title': 'Python Language Website', 
'url': 'http://www.python.org', 
'changed': 'Mar 14 22:09:15 MET 2016'
}
"""

# 4.4.7 values
# 返回一个由字典中的值组成的字典视图。不同于方法keys，方法values返回的视图可能包含重复的值。
d = {};
d[1] = 2;
d[2] = 3;
d[3] = 2;
d[4] = 1;
e = d.values();
print(e);  # dict_values([2, 3, 2, 1])













































