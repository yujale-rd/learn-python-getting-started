# Python 列表（List）
# 列表（list）是 Python 中的一种内置数据类型，用于存储多个有序的元素。列表中的元素可以是任何数据类型（整数、浮点数、字符串，甚至是另一个列表），且列表是可变的，这意味着可以修改列表中的元素。

# 创建列表
# 列表用方括号 [] 来表示，元素之间用逗号分隔。列表可以是空的，也可以包含多个元素：
# 定义一个空列表
empty_list = []

# 定义一个包含整数的列表
numbers = [1, 2, 3, 4, 5]

# 定义一个包含字符串的列表
fruits = ['apple', 'banana', 'cherry']

# 定义一个包含混合类型的列表
mixed_list = [1, 'apple', True, 3.14]

# 定义一个包含列表的列表（嵌套列表）
nested_list = [[1, 2], ['a', 'b', 'c'], [True, False]]

# 访问列表元素
# 通过索引可以访问列表中的元素，索引从 0 开始，也可以使用负数索引从列表末尾开始计数。


fruits = ["apple", "banana", "orange"]

# 访问第一个元素
print(fruits[0])  # 输出: apple

# 访问最后一个元素
print(fruits[-1])  # 输出: orange

# 修改列表元素
# 列表是可变的，可以修改列表中的元素

fruits = ["apple", "banana", "orange"]

# 修改第二个元素
fruits[1] = "pear"
print(fruits)  # 输出: ['apple', 'pear', 'orange']


# 列表添加元素
"""
append() 方法
append() 方法用于在列表的末尾添加一个元素。

list.append(element)
element：要添加到列表末尾的元素。


insert() 方法
insert() 方法用于在列表的指定位置插入一个元素。

list.insert(index, element)
index：要插入元素的位置索引。
element：要插入的元素。

extend() 方法
extend() 方法用于在列表的末尾一次性追加另一个序列中的多个元素（可以是列表、元组、集合等）。
list.extend(iterable)
iterable：一个可迭代对象，其元素将被添加到列表末尾。
使用 + 运算符
可以使用 + 运算符将两个列表合并，返回一个新的列表。

使用 += 运算符
可以使用 += 运算符将一个列表中的所有元素添加到另一个列表的末尾。
"""

fruits = ["apple", "banana"]

# 追加元素
fruits.append("orange")
print(fruits)  # 输出: ['apple', 'banana', 'orange']

# 在指定位置插入元素
fruits.insert(1, "pear")
print(fruits)  # 输出: ['apple', 'pear', 'banana', 'orange']

# 列表删除元素

# remove(element)：删除列表中的第一个匹配项。
# pop(index)：移除并返回指定索引处的元素，如果不指定索引，则移除最后一个元素。
# del list[index]：删除指定索引处的元素。
# clear()：清空列表。

fruits = ["apple", "banana", "orange"]

# 移除指定元素
fruits.remove("banana")
print(fruits)  # 输出: ['apple', 'orange']

# 删除指定索引的元素
fruits.pop(0)
print(fruits)  # 输出: ['orange']

# 清空列表
fruits.clear()
print(fruits)  # 输出: []

# 删除指定索引处的元素
fruits = ["apple", "banana", "orange"]
del fruits[1]
print(fruits)


# 列表的排序
# sort()：对列表中的元素进行升序排序。
# reverse()：反转列表中元素的顺序。

numbers = [5, 2, 9, 1, 5, 6]

# 升序排序
numbers.sort()
print(numbers)  # 输出: [1, 2, 5, 5, 6, 9]

# 反转顺序
numbers.reverse()
print(numbers)  # 输出: [9, 6, 5, 5, 2, 1]

# 列表的切片

# 可以使用切片一次性修改列表中的多个元素。
#
# list[start:end] = new_values
numbers = [1, 2, 3, 4, 5, 6]

# 获取前3个元素
print(numbers[:3])  # 输出: [1, 2, 3]

# 获取最后两个元素
print(numbers[-2:])  # 输出: [5, 6]

# 获取间隔为2的元素
print(numbers[::2])  # 输出: [1, 3, 5]

# 列表推导式
# 列表推导式是生成列表的一种简洁方式，可以使用循环、条件表达式等快速创建列表。

# 创建 0-9 的平方列表
squares = [x**2 for x in range(10)]
print(squares)  # 输出: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 生成偶数列表
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # 输出: [0, 2, 4, 6, 8]

# 列表的查询
# 通过索引查询
# 列表中的元素是有序的，能够通过索引直接访问元素。索引从 0 开始，负索引用于从列表末尾反向访问。
fruits = ["apple", "banana", "orange"]

# 查询第一个元素
print(fruits[0])  # 输出: apple

# 查询最后一个元素
print(fruits[-1])  # 输出: orange
# 如果索引超出了列表范围，会抛出 IndexError 异常。

# 使用 in 和 not in 操作符
# 可以使用 in 和 not in 操作符检查列表中是否包含某个元素。

fruits = ['apple', 'banana', 'cherry', 'date']

print('banana' in fruits)    # 输出：True
print('orange' in fruits)    # 输出：False
print('orange' not in fruits) # 输出：True

"""
使用 index() 方法查找元素位置
index() 方法返回列表中第一个匹配元素的索引。如果元素不在列表中，会引发 ValueError
"""
fruits = ['apple', 'banana', 'cherry', 'date', 'banana']

print(fruits.index('banana'))  # 输出：1
# 如果需要查找下一个 'banana'，可以指定起始位置
print(fruits.index('banana', 2))  # 输出：4

"""
使用 count() 方法统计元素出现次数
count() 方法返回元素在列表中出现的次数。
"""

fruits = ['apple', 'banana', 'cherry', 'banana', 'date', 'banana']

print(fruits.count('banana'))  # 输出：3
print(fruits.count('apple'))   # 输出：1
print(fruits.count('orange'))  # 输出：0

"""
使用列表推导式进行条件筛选
可以使用列表推导式根据条件筛选元素。
"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 筛选出所有的偶数
evens = [num for num in numbers if num % 2 == 0]
print(evens)  # 输出：[2, 4, 6, 8, 10]

# 筛选出所有大于5的数
greater_than_five = [num for num in numbers if num > 5]
print(greater_than_five)  # 输出：[6, 7, 8, 9, 10]


"""
使用 filter() 函数进行条件筛选
filter() 函数返回一个迭代器，包含所有满足条件的元素。
"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 筛选出所有的偶数
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # 输出：[2, 4, 6, 8, 10]

# 筛选出所有大于5的数
greater_than_five = list(filter(lambda x: x > 5, numbers))
print(greater_than_five)  # 输出：[6, 7, 8, 9, 10]

"""
使用 any() 和 all() 函数进行条件判断
any() 函数检查是否至少有一个元素满足条件，all() 函数检查是否所有元素都满足条件。
"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 检查是否有元素大于5
print(any(num > 5 for num in numbers))  # 输出：True

# 检查是否所有元素都大于0
print(all(num > 0 for num in numbers))  # 输出：True

# 检查是否所有元素都大于5
print(all(num > 5 for num in numbers))  # 输出：False


# 列表常用内置函数
# len()
#
# len() 函数用于返回列表中元素的个数。
fruits = ["apple", "banana", "orange"]
print(len(fruits))  # 输出: 3

# max() 和 min()
#
# 	•	max()：返回列表中的最大值。
# 	•	min()：返回列表中的最小值。
numbers = [1, 2, 3, 4, 5]
print(max(numbers))  # 输出: 5
print(min(numbers))  # 输出: 1

# sum()
#
# sum() 函数用于计算列表中数值的总和。
numbers = [1, 2, 3, 4, 5]
print(sum(numbers))  # 输出: 15
# sorted()
#
# sorted() 函数用于对列表进行排序，并返回一个新的排序后的列表。可以指定 reverse=True 参数实现降序排序。
numbers = [3, 1, 4, 1, 5, 9]
print(sorted(numbers))  # 输出: [1, 1, 3, 4, 5, 9]
print(sorted(numbers, reverse=True))  # 输出: [9, 5, 4, 3, 1, 1]

# list()
#
# list() 函数用于将其他可迭代对象（如字符串、元组、集合等）转换为列表。
s = "hello"
char_list = list(s)
print(char_list)  # 输出: ['h', 'e', 'l', 'l', 'o']
# reversed()
#
# reversed() 函数用于反转列表中的元素，返回一个反向迭代器。
fruits = ["apple", "banana", "orange"]
for index, fruit in enumerate(fruits):
    print(f"索引: {index}, 值: {fruit}")

# 列表的复制

# 在 Python 中，列表的复制有多种方式，但需要注意的是，简单的赋值操作会将原列表的引用赋给新的变量，这意味着对新变量的修改会影响原始列表。为了避免这个问题，可以使用以下几种方法进行列表的深拷贝和浅拷贝。
# 1. 使用 = 进行引用赋值（非复制）
#
# 使用 = 只是将列表的引用赋值给新变量，两个变量指向的是同一个列表对象，改变其中一个列表，另一个列表也会受到影响。
list1 = [1, 2, 3]
list2 = list1  # 这是引用赋值
list2[0] = 99
print(list1)  # 输出: [99, 2, 3]，原列表也被修改了

# 2. 使用 copy() 进行浅拷贝
#
# copy() 方法用于创建列表的浅拷贝。浅拷贝会创建一个新列表对象，但内部元素的引用依然指向原来的对象（如果元素是可变对象，如嵌套列表）。
list1 = [1, 2, 3]
list2 = list1.copy()  # 浅拷贝
list2[0] = 99
print(list1)  # 输出: [1, 2, 3]，原列表不受影响
print(list2)  # 输出: [99, 2, 3]，新列表被修改了

# 对于嵌套列表，浅拷贝只复制了外层的列表，内层列表还是引用同一个对象：
list1 = [[1, 2], [3, 4]]
list2 = list1.copy()
list2[0][0] = 99
print(list1)  # 输出: [[99, 2], [3, 4]]，原列表被修改
print(list2)  # 输出: [[99, 2], [3, 4]]，新列表也被修改

#  使用切片 [:] 进行浅拷贝
#
# 使用列表切片 [:] 可以复制整个列表，这种方法与 copy() 类似，也是浅拷贝。

list1 = [1, 2, 3]
list2 = list1[:]  # 使用切片进行浅拷贝
list2[0] = 99
print(list1)  # 输出: [1, 2, 3]
print(list2)  # 输出: [99, 2, 3]

# 使用 list() 构造函数进行浅拷贝
#
# list() 构造函数也可以用于复制一个列表，这也是浅拷贝。

list1 = [1, 2, 3]
list2 = list(list1)  # 使用 list() 进行浅拷贝
list2[0] = 99
print(list1)  # 输出: [1, 2, 3]
print(list2)  # 输出: [99, 2, 3]

# 使用 deepcopy() 进行深拷贝
#
# deepcopy() 方法可以实现列表的深拷贝，深拷贝会递归地复制所有的元素，创建完全独立的新对象，即使是嵌套的可变对象也会被深度复制。
#
# 要使用 deepcopy()，需要导入 copy 模块：

import copy

list1 = [[1, 2], [3, 4]]
list2 = copy.deepcopy(list1)  # 深拷贝
list2[0][0] = 99
print(list1)  # 输出: [[1, 2], [3, 4]]，原列表不受影响
print(list2)  # 输出: [[99, 2], [3, 4]]，新列表被修改了

# 列表的遍历

"""
使用 for 循环
for element in list:
    # 操作


使用 for 循环和 range 函数

for i in range(len(list)):
    # 操作 list[i]

使用 enumerate 函数
for index, element in enumerate(list):
    # 操作

使用列表推导式
[operation for element in list]

使用 while 循环
i = 0
while i < len(list):
    # 操作 list[i]
    i += 1
"""
fruits = ['苹果', '香蕉', '橙子']
for fruit in fruits:
    print(fruit)

fruits = ['苹果', '香蕉', '橙子']
for i in range(len(fruits)):
    print(f"索引 {i}: {fruits[i]}")

fruits = ['苹果', '香蕉', '橙子']
for index, fruit in enumerate(fruits):
    print(f"索引 {index} - 水果: {fruit}")


fruits = ['苹果', '香蕉', '橙子']
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()