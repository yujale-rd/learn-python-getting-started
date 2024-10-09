# Python 开发中常见的一些 Bug 往往与语言的特性、数据类型、作用域等相关。

# 1. 可变对象作为默认参数

# 现象
# 使用列表、字典等可变对象作为函数的默认参数时，容易导致意外的行为。默认参数在函数定义时只会初始化一次,而不是每次调用都重新初始化
def add_item(item, items=[]):
    items.append(item)
    return items

print(add_item(1))  # 输出: [1]
print(add_item(2))  # 输出: [1, 2]，预期应该是 [2]

# 原因 ：函数的默认参数在定义时被初始化，后续对该参数的修改会影响到所有的函数调用
# 解决办法
# 使用 None 作为默认参数，在函数内部进行处理。

def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items

print(add_item(1))  # 输出: [1]
print(add_item(2))  # 输出: [2]

print("===========")
# 2. 浮点数精度问题
# 现象：
# 由于浮点数的存储方式，计算时可能会出现精度问题。

print(0.1 + 0.2)  # 输出: 0.30000000000000004

#原因 浮点数在计算机中是二进制表示的，某些十进制数无法用有限的二进制小数表示，导致精度丢失。

# 解决方法：
# 可以使用 decimal 模块来处理精度问题。

from decimal import Decimal

print(Decimal('0.1') + Decimal('0.2'))  # 输出: 0.3

print("===========")


# 3. 误用 is 运算符
#
# 现象：
# 使用 is 比较两个变量的值时，可能得到意外结果。is 用于比较对象的身份，而不是比较它们的值。

a = 1000
b = 1000
print(a is b)  # 输出: False

# 原因：

# is 检查两个对象是否是同一个对象，而不是检查它们的值是否相同。对于小的整数和短字符串，Python 进行对象缓存，所以可能会遇到一些奇怪的结果。

# 解决方法：
# 使用 == 比较值，使用 is 比较对象身份。

print(a == b)  # 输出: True

print("===========")


# 4. 修改全局变量
#
# 现象：
# 在函数内部修改全局变量时，会导致错误的行为，通常是因为 Python 将局部变量与全局变量混淆。

count = 0

def increment():
    count += 1  # 报错：UnboundLocalError: local variable 'count' referenced before assignment

increment()

# 原因：
# Python 会在局部作用域中查找变量，如果要修改全局变量，必须显式声明。

# 解决方法
# 使用 global 关键字声明全局变量

count = 0

def increment():
    global count
    count += 1

increment()
print(count)  # 输出: 1

print("===========")


# 5. for 循环中的变量泄漏
#
# 现象：
# for 循环中的循环变量在循环结束后仍然可以访问，并且保存了最后一次循环的值。

for i in range(5):
    pass

print(i)  # 输出: 4

# 原因：
# 在 Python 中，for 循环的变量并不局限于循环内部，而是会泄漏到外部作用域。

# 解决方法：
# 在函数中使用循环变量可以避免变量泄漏的问题。

print("===========")


# 6. 引用可变对象导致意外修改
#
# 现象：
# 当一个变量赋值给另一个变量时，两个变量可能会指向同一个可变对象，修改其中一个会影响另一个。

list1 = [1, 2, 3]
list2 = list1
list2.append(4)

print(list1)  # 输出: [1, 2, 3, 4]

# 原因：
# list2 指向与 list1 相同的对象，因此修改 list2 也会影响 list1。
#
# 解决方法：
# 使用 copy() 方法或 deepcopy() 方法复制对象。

import copy
list1 = [1, 2, 3]
list2 = copy.copy(list1)  # 或 list2 = list1.copy()

list2.append(4)
print(list1)  # 输出: [1, 2, 3]
print(list2)  # 输出: [1, 2, 3, 4]

# 7. 错误的异常捕获
#
# 现象：
# 在捕获异常时，不指定异常类型可能导致捕获到不想要的异常，甚至是系统异常。

try:
    1 / 0
except:
    print("Something went wrong!")
# 原因：
# 没有明确捕获特定的异常类型，会捕获所有的异常，包括系统异常，这可能会隐藏真正的问题。
#
# 解决方法：
# 指定要捕获的具体异常类型。

try:
    1 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

# 8. 未关闭的文件对象
#
# 现象：
# 未关闭文件对象可能导致资源泄漏，尤其是在处理大量文件操作时。

file = open('example.txt', 'r')
# 忘记关闭文件

# 解决方法：
#
# 使用 with 语句，它可以确保文件在操作完成后自动关闭。

with open('example.txt', 'r') as file:
    content = file.read()
# 文件自动关闭

# 9. 字典遍历时修改
#
# 现象：
# 在遍历字典的同时修改字典，可能会导致 RuntimeError 错误。

my_dict = {'a': 1, 'b': 2, 'c': 3}
for key in my_dict:
    del my_dict[key]  # 报错：RuntimeError: dictionary changed size during iteration

# 解决方法：
# 遍历时先复制字典的键或使用 list()，避免直接修改原字典。

my_dict = {'a': 1, 'b': 2, 'c': 3}
for key in list(my_dict.keys()):
    del my_dict[key]
# 10. 错误理解的逻辑运算符优先级
#
# 现象：
# 可能因为错误的运算符优先级，导致逻辑判断的结果与预期不符。
a = True
b = False
c = False

if a and b or c:
    print("Condition met!")  # 输出: Condition met! (不符合预期)
# 原因：
# and 的优先级高于 or，因此表达式实际是 if (a and b) or c。

# 解决方法：
# 使用括号明确优先级，避免歧义。

if a and (b or c):
    print("Condition met!")  # 现在符合预期




