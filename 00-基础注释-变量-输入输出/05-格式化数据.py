# 字符串格式化 是一个非常重要且常用的操作，它允许我们以更加优雅和灵活的方式将变量嵌入到字符串中。

# python 提供三种主要的字符串格式方法
# - 百分号格式化（%）
# - str.format() 方法
# - f-string（格式化字符串字面量，Python 3.6+ 引入）

"""
1. 百分号格式化（%）

这种方式是 Python 中最早的字符串格式化方法，它使用占位符（如 %s、%d）来格式化字符串。虽然它简单直接，但相对不够灵活，特别是在处理多个变量时。

常用占位符：
	•	%s：字符串
	•	%d：整数
	•	%f：浮点数
	•	%x：十六进制整数
	•	%e：科学计数法表示法
"""
name = "yujale"
age = 30
formatted_string = "My name is %s and I am %d years old." % (name, age)
print(formatted_string)  # 输出: My name is yujale and I am 30 years old.

height = 1.75
marriage = False


# 一个占位符的格式化输出
print('学员的姓名是 %s' % name)
print('学员的年龄是 %d' % age)
print('学员的身高是 %f' % height)
print('学员的婚姻状况是 %s' % marriage)
print("姓名：%s, 年龄：%d, 身高：%.2f, 婚姻状况：%s" % (name, age, height, marriage))


"""
2. str.format() 方法

str.format() 方法比百分号格式化更加灵活，支持使用位置参数、命名参数、格式说明符以及表达式。这使得它在多种场景下都非常有用。
"""

formatted_string = "My name is {} and I am {} years old.".format(name, age)
print(formatted_string)  # 输出: My name is yujale and I am 30 years old.

"""
使用索引指定位置：
"""
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
"""
3. f-string（格式化字符串字面量）

Python 3.6 引入的 f-string 语法提供了一种更简洁且高效的字符串格式化方式。通过在字符串前加上 f，可以直接将变量嵌入字符串中，支持表达式、格式说明符等功能。
"""
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

"""
f-string 的优势：
	•	简洁性：相比 str.format() 和 % 格式化，代码更简洁。
	•	性能：f-string 在性能上优于 str.format() 和 % 格式化，特别是在需要频繁格式化字符串的情况下。
	•	表达式支持：f-string 允许直接在花括号内插入表达式，这使得代码更具可读性和灵活性。
"""

# 总结

# - % 格式化：较老的方式，不够灵活，但简单常用。
# - str.format()：提供了更强大的功能，能够通过索引或命名参数传递值，推荐在 Python 3.x 中使用。
# - f-string：简洁且高效的格式化方式，推荐使用 Python 3.6+ 时优先使用 f-string。
