"""
在 Python 中，迭代和迭代器是用来遍历可迭代对象（如列表、元组、字符串等）的核心概念。理解迭代和迭代器能够帮助你更高效地处理数据和控制程序流程。

1. 迭代（Iteration）

迭代是指逐个访问一个可迭代对象的元素，直到遍历完所有元素。最常见的迭代方式是使用 for 循环。
"""
# 示例：使用 for 循环进行迭代
my_list = [1, 2, 3, 4]

for item in my_list:
    print(item)
# 在上面的例子中，my_list 是一个可迭代对象，for 循环会依次返回列表中的每个元素。

"""
可迭代对象（Iterable）

是指可以通过 for...in... 语句进行迭代的对象，比如 list、tuple、str、dict 等。

任何可以返回一个迭代器的对象都称为可迭代对象。Python 中的一些常见可迭代对象包括：
	•	列表（list）
	•	元组（tuple）
	•	字符串（str）
	•	字典（dict）：对于字典来说，它默认迭代的是字典的键。
	•	集合（set）

所有这些对象都可以使用 for 循环进行迭代。

"""
# 迭代字典
my_dict = {"a": 1, "b": 2, "c": 3}
for key in my_dict:
    print(key)  # 迭代的是字典的键
for value in my_dict.values():
    print(value)  # 迭代的是字典的值
"""
不是可以迭代的数据类型

- 整型
- 浮点型

只要是通过`isinstance`来判断出是`Iterable`类的实例，即`isinstance`的结果是`True`那么就表示，这个数据类型是可以迭代的数据类型

"""
from collections.abc import Iterable

print(isinstance([1, 2, 3], Iterable))  # True，列表是可迭代的
print(isinstance(123, Iterable))       # False，整数不是可迭代的

# 迭代器

"""
迭代器

迭代器是一个可以记住遍历的位置的对象。迭代器对象从第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。

迭代器是一个实现了 __iter__() 和 __next__() 方法的对象。通过迭代器，我们可以手动地逐个获取可迭代对象中的元素。
	•	__iter__() 方法返回迭代器对象本身。
	•	__next__() 方法返回迭代器的下一个元素，并在没有更多元素时抛出 StopIteration 异常。

任何可迭代对象都可以使用 iter() 函数转换为迭代器，迭代器对象可以使用 next() 函数获取下一个元素。
"""
# 将列表转换为迭代器
my_list = [1, 2, 3]
my_iterator = iter(my_list)

# 使用 next() 获取元素
print(next(my_iterator))  # 输出: 1
print(next(my_iterator))  # 输出: 2
print(next(my_iterator))  # 输出: 3

# 再次调用 next() 会抛出 StopIteration 异常
# print(next(my_iterator))  # 会抛出 StopIteration 异常

# 再次调用 next() 会抛出 StopIteration 异常
# print(next(my_iterator))  # StopIteration
"""
迭代器与可迭代对象的区别
	•	可迭代对象：是支持 for 循环的对象，可以通过 iter() 转换为迭代器。
	•	迭代器对象：是实现了 __iter__() 和 __next__() 方法的对象，可以通过 next() 来逐个获取元素。

    
for循环会在底层自动的将迭代对象转为迭代器对象

迭代对象不一定是迭代器
迭代器一定是迭代对象


迭代器的使用方式
	1.	手动使用 next() 函数：你可以显式调用 next() 来获取下一个元素。
	2.	自动使用 for 循环：for 循环会在内部自动调用 next() 函数。
"""
# 通过迭代器进行手动迭代
my_iterator = iter([1, 2, 3])
print(next(my_iterator))  # 输出: 1
print(next(my_iterator))  # 输出: 2
# 自定义迭代器
"""
你可以通过自定义类来创建自己的迭代器。自定义的类需要实现 __iter__() 和 __next__() 方法。

"""


class Reverse:
    def __init__(self, data):
        self.data = data
        self.index = len(data)  # 设置开始的位置

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration  # 到达末尾时抛出 StopIteration
        self.index = self.index - 1
        return self.data[self.index]

rev = Reverse("giraffe")
for char in rev:
    print(char)  # 输出: e f f a r i g