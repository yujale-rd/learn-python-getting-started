# 字符串格式化 是一个非常重要且常用的操作，它允许我们以更加优雅和灵活的方式将变量嵌入到字符串中。

# python 提供三种主要的字符串格式方法
# - 百分号格式化（%）
# - str.format() 方法
# - f-string（格式化字符串字面量，Python 3.6+ 引入）


# 百分号格式化 （%）
name = "yujale"
age = 30

# 使用百分号格式化
formatted_string = "My name is %s and I am %d years old." % (name, age)
print(formatted_string)  # 输出: My name is yujale and I am 30 years old.


"""
常用占位符：

- %s：字符串
- %d：整数
- %f：浮点数
- %x：十六进制整数

"""

name = 'xiao_ming'
age = 18
height = 1.85
weight = 69.5
marriage = False

# 一个占位符的格式化输出
print('学员的姓名是 %s' % name)
print('学员的年龄是 %d' % age)
print('学员的身高是 %f' % height)
print('学员的体重是 %f' % weight)
print('学员的婚姻状况是 %s' % marriage)

# 有多个动态变量的时候,我们就需要使用多个占位符进行占位
print('学员的姓名是 %s, 学员的年龄是 %d 岁, 学员的身高是 %f 米, 学员的体重是 %f kg, 学员的婚姻状况是 %s' % (
    name, age, height, weight, marriage))

# str.format() 方法

# 相比于 %，str.format() 更加灵活和强大，它允许在字符串中插入占位符 {}，并在后面传入值进行替换。

name = "yujale"
age = 30

# 使用 format 方法
formatted_string = "My name is {} and I am {} years old.".format(name, age)
print(formatted_string)  # 输出: My name is yujale and I am 30 years old.


# 指定位置或变量名：
# 通过索引指定位置

formatted_string = "My name is {0} and I am {1} years old.".format(name, age)
print(formatted_string)  # 输出: My name is yujale and I am 30 years old.

# 通过变量名指定
formatted_string = "My name is {name} and I am {age} years old.".format(name="yujale", age=30)
print(formatted_string)  # 输出: My name is yujale and I am 30 years old.

# 精确控制格式：
# str.format() 也支持指定宽度、精度等，使用类似 {:.2f} 的语法。
pi = 3.1415926
formatted_string = "Pi is approximately {:.2f}".format(pi)
print(formatted_string)  # 输出: Pi is approximately 3.14

# f-string（格式化字符串字面量）
#
# f-string 是 Python 3.6+ 引入的一种格式化方式，使用更为简洁直接。它通过在字符串前加上 f，并直接在 {} 中插入变量名或表达式。

name = "yujale"
age = 30

# 使用 f-string
formatted_string = f"My name is {name} and I am {age} years old."
print(formatted_string)  # 输出: My name is yujale and I am 30 years old.

# f-string 支持表达式：

a = 10
b = 20
print(f"The sum of {a} and {b} is {a + b}.")  # 输出: The sum of 10 and 20 is 30.

# 精确控制格式：
#
# f-string 也可以像 format() 一样指定宽度、精度等：

pi = 3.1415926
print(f"Pi is approximately {pi:.2f}")  # 输出: Pi is approximately 3.14


# 总结

# - % 格式化：较老的方式，不够灵活，但简单常用。
# - str.format()：提供了更强大的功能，能够通过索引或命名参数传递值，推荐在 Python 3.x 中使用。
# - f-string：简洁且高效的格式化方式，推荐使用 Python 3.6+ 时优先使用 f-string。
