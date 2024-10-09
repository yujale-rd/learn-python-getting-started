# 在 Python 中，变量的类型转换（也称为类型强制转换）是指将一种数据类型转换为另一种数据类型。
# Python 提供了多种内置的类型转换函数，可以在不同类型之间进行转换。常见的转换操作有整型、浮点型、字符串、布尔型等。

"""
常见的类型转换函数

- int()：将数据转换为整型
- float()：将数据转换为浮点型
- str()：将数据转换为字符串
- bool()：将数据转换为布尔型
"""


# 1. 整型转换 (int())
# int() 函数可以将字符串、浮点数或布尔值转换为整型。如果是字符串，需要确保内容是可转换的数字，否则会引发异常。

# 浮点数转整型 (会去掉小数部分)
num_float = 12.99
num_int = int(num_float)
print(num_int)  # 输出: 12

# 字符串转整型
num_str = "123"
num_int = int(num_str)
print(num_int)  # 输出: 123

# 布尔值转整型 (True 转为 1, False 转为 0)
bool_value = True
num_int = int(bool_value)
print(num_int)  # 输出: 1

# 注意：无法将非数字的字符串直接转换为整数，否则会抛出 ValueError 异常。
num_str = "abc"
# num_int = int(num_str)  # ValueError: invalid literal for int() with base 10

# 2. 浮点型转换 (float())
# float() 函数可以将字符串、整数或布尔值转换为浮点型。
# 整型转浮点型
num_int = 10
num_float = float(num_int)
print(num_float)  # 输出: 10.0

# 字符串转浮点型
num_str = "12.34"
num_float = float(num_str)
print(num_float)  # 输出: 12.34

# 布尔值转浮点型 (True 转为 1.0, False 转为 0.0)
bool_value = False
num_float = float(bool_value)
print(num_float)  # 输出: 0.0

# 3. 字符串转换 (str())
# str() 函数可以将任何数据类型转换为字符串类型。

# 整型转字符串
num_int = 100
str_value = str(num_int)
print(str_value)  # 输出: "100"

# 浮点型转字符串
num_float = 12.56
str_value = str(num_float)
print(str_value)  # 输出: "12.56"

# 布尔型转字符串
bool_value = True
str_value = str(bool_value)
print(str_value)  # 输出: "True"

#4. 布尔型转换 (bool())

"""
bool() 函数可以将其他数据类型转换为布尔类型。在 Python 中，以下值被认为是 False：

- 0（整数或浮点数）
- 空字符串 ""
- 空列表、空元组、空字典、空集合
- None

其他任何非空或非零值均被认为是 True。
"""

# 整型转布尔型
print(bool(0))  # 输出: False
print(bool(1))  # 输出: True

# 字符串转布尔型
print(bool(""))    # 输出: False
print(bool("abc"))  # 输出: True

# 空列表、元组等
print(bool([]))  # 输出: False
print(bool([1, 2, 3]))  # 输出: True

# 5. 类型转换中的注意事项
#
#- 在转换过程中，确保数据能够被成功转换（如将非数字的字符串转换为数字时会报错）。
#- int() 和 float() 只会截取整数部分或数字部分，字符串中包含非数字字符会导致异常。

# 转换示例

int1 = 12
float1 = 14.9
str1 = '12'
str2 = '14.3'
str3 = 'python'

# int >> float
# int类型转换为float类型将会在整数末尾加.0
print(f'将 int 转换为 float: {float(int1)}')
print(f'类型: {type(float(int1))}')

# float >> int
# float转换为int类型,将会将小数部分去除,只保留整数部分
print(f'将 float 转换为 int: {int(float1)}')

# int >> str
# int类型可以随意转换为str类型,转化为str类型后可以使用str类型的各种函数
print(f'将 int 转换为 str: {str(int1)}')

# str >> int
# 字符串中是int类型数据,可以转换为int类型
print(f'将 str 转换为 int: {int(str1)}')
# 字符串中是float类型数据,不可以转换为int类型 (此行将引发 ValueError)
# 字符串中是字符型数据,不可以转换为int类型 (此行将引发 ValueError)
try:
    # str 转 int 失败示例
    print(int(str2))  # 这行代码会引发 ValueError
except ValueError:
    print(f'无法将字符串 "{str2}" 转换为整数。')
try:
    # str 转 int 失败示例
    print(int(str3))  # 这行代码会引发 ValueError
except ValueError:
    print(f'无法将字符串 "{str3}" 转换为整数。')

# float >> str
# float类型可以随意转换为str类型,转化为str类型后可以使用str类型的各种函数
print(f'将 float 转换为 str: {str(float1)}')

# str >> float
# 字符串中是int类型数据,可以转换为float类型,并且在末尾加.0
print(f'将 str 转换为 float: {float(str1)}')
# 字符串中是float类型数据,可以转换为float类型
print(f'将 str 转换为 float: {float(str2)}')
# 字符串中是字符型数据则不能转换为float类型 (此行将引发 ValueError)
try:
    # str 转 float 失败示例
    print(float(str3))  # 这行代码会引发 ValueError
except ValueError:
    print(f'无法将字符串 "{str3}" 转换为浮点数。')