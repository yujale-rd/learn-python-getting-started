# 在 Python 中，for 循环是非常常见且强大的控制流工具，用于遍历各种可迭代对象（如列表、元组、字符串、字典、集合等）以及通过 range() 函数生成的数字序列。
# for 循环使我们可以轻松遍历元素并执行相应的操作。
"""
1. for 循环的基本语法
for 变量 in 可迭代对象:
    # 循环体
	•	变量：在每次迭代中，变量会依次获取可迭代对象中的元素。
	•	可迭代对象：任何可以迭代的对象，例如列表、字符串、字典、集合、元组等。
	•	循环体：执行的代码块。

"""
"""
2. 遍历常见的数据结构
"""

# 遍历列表

fruits = ['苹果', '香蕉', '橙子']
for fruit in fruits:
    print(fruit)
# 输出:
# 苹果
# 香蕉
# 橙子

# 遍历字符串
for char in "Python":
    print(char)
# 输出:
# P
# y
# t
# h
# o
# n

# 遍历范围

# 可以使用 range() 函数生成数字序列来遍历。
for i in range(5):
    print(i)

# range(5) 生成 0 到 4 的整数序列，默认从 0 开始。
# range(1, 6) 表示从 1 到 5：

# 遍历字典
# Python 中的字典可以通过 for 循环遍历 key-value 对。常见用法是使用 .items() 方法获取键和值的元组对：
person = {'name': 'Alice', 'age': 25, 'city': 'New York'}
for key, value in person.items():
    print(f'{key}: {value}')
# 输出:
# name: Alice
# age: 25
# city: New York

# 遍历元组

tuple_values = (10, 20, 30)
for value in tuple_values:
    print(value)
# 输出:
# 10
# 20
# 30

# for 循环中的嵌套
# 在某些情况下，可能需要在 for 循环中嵌套另一个 for 循环。这在处理多维数据结构（如二维数组、矩阵）时非常有用。以下是嵌套 for 循环的一个简单示例，用于输出九九乘法表：

for i in range(1, 10):
    for j in range(1, 10):
        print(f'{i} * {j} = {i * j}', end='\t')
    print()  # 换行

# enumerate() 函数

# 在需要获取索引和值的场景中，enumerate() 是非常实用的工具。它在遍历时不仅返回元素，还会返回元素的索引值：
fruits = ['苹果', '香蕉', '橙子']
for index, fruit in enumerate(fruits):
    print(f'索引 {index} - 水果: {fruit}')
# 输出:
# 索引 0 - 水果: 苹果
# 索引 1 - 水果: 香蕉
# 索引 2 - 水果: 橙子

# for 循环与 else
# 在 Python 中，for 循环可以和 else 语句结合使用。当 for 循环正常执行完毕时，会执行 else 代码块；如果在循环中使用了 break，else 代码块将不会执行。

for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("循环正常结束")
# 输出:
# 0
# 1
# 2
# pass 语句
#
# 在循环中，如果不想执行任何操作，可以使用 pass 作为占位符。

for i in range(5):
    if i == 3:
        pass  # 占位符，不执行任何操作
    else:
        print(i)