#  字符串（str）

# Python 中，字符串是用于表示文本数据的数据类型，他是不可变的数据类型。这意味着字符串一旦创建，就无法更改它的值。
# Python 的字符串可以使用单引号 ' '、双引号 " "、三引号 ''' ''' 或 """ """ 来定义。

# 使用建议
# 如果字符串中含有单引号 ' 而不含有双引号 "，则可以使用双引号来定义字符串，反之亦然。
# 如果字符串需要跨多行，推荐使用三重引号 ''' ''' 或者 """ """，以保持代码的可读性。
# 在多行文本或需要包含大量格式化内容的情况下，使用三重引号可以更方便地管理字符串


# 字符串创建

# 单引号
str1 = 'Hello, World!'
print(str1)

# 双引号
str2 = "Python is fun!"
print(str2)

# 三引号（用于多行字符串）
str3 = '''This is a 
multi-line string'''
print(str3)

# 或者使用双引号的三引号
str4 = """Another
multi-line string"""
print(str4)

# 字符串输出
# 在Python中，使用 print() 函数来输出字符串是最常见的方式

str5 = "Hello, World!"
print(str5)

# 字符串输入
# 在Python中，使用 input() 函数接收用户输入的字符串


# 字符串拼接

# k可以使用 + 运算符将多个字符串连接起来
greeting = "Hello" + ", " + "World!"
print(greeting)  # 输出: Hello, World!


# 重复字符串
repeat_str = "Ha" * 3
print(repeat_str)  # 输出: HaHaHa

# 字符串索引
# 字符串是一个字符序列，可以通过索引访问某个位置的字符。索引从 0 开始。
text = "Python"
print(text[0])  # 输出: P
print(text[1])  # 输出: y
print(text[-1])  # 输出: n（负数索引表示从右向左）

# 字符串切片
# 可以通过切片操作获取字符串的子串。切片的格式是 字符串[start:end:step]。
"""
string[start:end:step]
start：起始索引，表示切片开始的位置（包含在切片内）。
end：结束索引，表示切片结束的位置（不包含在切片内）。
step：步长，表示从起始索引到结束索引的间隔，默认为1（可选参数）。
    # 起始位置: 字符串切片的起点(包含)
    # 结束位置:字符串切片的终点(不包含)
    # 在开发中绝大多数范围区间是左闭右开区间,其余内容单独记忆(例如 randint是一个闭区间)
    # 步长:步长就是每一次查找数据的间隔(相邻两个索引的差值就是步长)
注意事项
切片操作不会改变原始序列，而是返回一个新的序列。字符串切片以及其他容器类型的切片操作,都会重新生成一个新的数据序列,不会对原有数据序列产生影响
如果省略start，则默认从序列的开头开始；如果省略end，则默认到序列的末尾；如果省略step，则默认为1。
切片操作是左闭右开的，即包含start索引，不包含end索引。
"""

s = "Hello, World!"
print(s[7:])  # 输出 'World!' 从索引7开始到末尾。
print(s[:5])  # 输出 'Hello' 从开头到索引5之前。
print(s[7:12])  # 输出 'World' 从索引7到索引12之前。
s = "Hello, World!"
print(s[-6:])  # 输出 'World!' 从倒数第6个字符到末尾。
print(s[:-8])  # 输出 'Hello' 从开头到倒数第8个字符之前。
print(s[-6:-1])  # 输出 'World' 从倒数第6个字符到倒数第1个字符。

s = "0123456789"
print(s[2:9:2])  # 输出 '2468' 从索引2开始到索引9之前，步长为2。


# 字符串长度

# 可以使用 len() 函数获取字符串的长度。

text = "Python"
print(len(text))  # 输出: 6

# 字符串大小写转换
# upper()：将字符串全部转换为大写。
# lower()：将字符串全部转换为小写。
# capitalize()：将字符串的第一个字符转换为大写。
# title()：将字符串中每个单词的首字母大写。

text = "hello python"
print(text.upper())      # 输出: HELLO PYTHON
print(text.lower())      # 输出: hello python
print(text.capitalize()) # 输出: Hello python
print(text.title())      # 输出: Hello Python

# 字符串去除空格
# strip()：移除字符串两端的空格。
# lstrip()：移除左边的空格。
# rstrip()：移除右边的空格。
text = "   Hello, Python!   "
print(text.strip())  # 输出: Hello, Python!
print(text.lstrip())  # 输出: Hello, Python!
print(text.rstrip())  # 输出:    Hello, Python!

# 字符串查找

# find(sub)：查找子字符串，返回第一个匹配项的索引，找不到返回 -1。
# index(sub)：与 find() 类似，但找不到时抛出异常。
# count(sub)：返回子字符串在字符串中的出现次数。
text = "Python is awesome!"
print(text.find("is"))      # 输出: 7
print(text.count("o"))      # 输出: 2


# 字符串替换

"""
replace() 方法允许你将字符串中的指定子字符串替换为新的字符串。它返回一个新的字符串，原始字符串不会被改变。
str.replace() 函数与 replace() 方法类似，不同之处在于它作为字符串对象的一个函数调用，而不是作为方法调用。用法和效果与 replace() 方法完全相同：

注意事项
replace() 方法和 str.replace() 函数都是区分大小写的。如果要进行大小写不敏感的替换，可以在替换前将字符串转换为统一的大小写。
如果需要删除特定的子字符串，可以将替换成空字符串 ''。
如果要在字符串中进行多次替换，可以通过循环或者多次调用 replace() 完成。
"""

text = "I love Python"
print(text.replace("Python", "coding"))  # 输出: I love coding


# 字符串拆分（split）
# split() 方法是Python字符串对象的内置方法，用于将字符串根据指定的分隔符拆分成子字符串，并返回一个列表。

text = "apple,banana,orange"
fruits = text.split(",")
print(fruits)  # 输出: ['apple', 'banana', 'orange']

# 字符串合并（join）
# 字符串合并是将多个字符串连接成一个字符串的操作。通常是使用一个分隔符将多个字符串连接起来。
# join() 方法是Python中 str 对象的方法，它可以将一个可迭代对象中的字符串元素使用指定的分隔符连接起来，形成一个新的字符串。

fruits = ["apple", "banana", "orange"]
result = ", ".join(fruits)
print(result)  # 输出: apple, banana, orange


# 字符串对齐
# Python 提供了三种字符串对齐方法：
#
# ljust(width, fillchar)：左对齐，右侧用指定字符填充（默认为空格）。
# rjust(width, fillchar)：右对齐，左侧用指定字符填充（默认为空格）。
# center(width, fillchar)：居中对齐，两侧用指定字符填充（默认为空格）。

text = "Python"

"""
左对齐 (ljust() 方法)
使用 ljust(width, fillchar) 方法可以将字符串左对齐，并使用 fillchar（默认为空格）填充至指定宽度 width。
"""
str1 = "hello"
# 左对齐至总宽度为 10，使用 '*' 填充
left_aligned = str1.ljust(10, '*')
print(left_aligned)  # Output: 'hello*****'

"""
右对齐 (rjust() 方法)
使用 rjust(width, fillchar) 方法可以将字符串右对齐，并使用 fillchar（默认为空格）填充至指定宽度 width。
"""

str1 = "hello"
# 右对齐至总宽度为 10，使用 '*' 填充
right_aligned = str1.rjust(10, '*')
print(right_aligned)  # Output: '*****hello'


"""
 居中对齐 (center() 方法)
使用 center(width, fillchar) 方法可以将字符串居中对齐，并使用 fillchar（默认为空格）填充至指定宽度 width。
"""
str1 = "hello"
# 居中对齐至总宽度为 10，使用 '*' 填充
centered = str1.center(10, '*')
print(centered)  # Output: '**hello***'


# 字符串判断方法

# isalpha()：检查字符串是否只包含字母（不包含空格或特殊字符）。
# isdigit()：检查字符串是否只包含数字。
# isalnum()：检查字符串是否只包含字母和数字。
# isspace()：检查字符串是否只包含空白字符。
# islower()：检查字符串中的字母是否全是小写。
# isupper()：检查字符串中的字母是否全是大写。
# istitle()：检查字符串是否是标题形式（每个单词首字母大写）。

text1 = "Python3"
text2 = "12345"
text3 = "Hello World"

# 检查是否只包含字母
print(text1.isalpha())  # 输出: False

# 检查是否只包含数字
print(text2.isdigit())  # 输出: True

# 检查是否只包含字母和数字
print(text1.isalnum())  # 输出: True

# 检查字符串是否全是小写
print(text1.islower())  # 输出: False

# 检查字符串是否是标题形式
print(text3.istitle())  # 输出: True


# 字符串检查开头和结尾以某个子串开始或结束
# startswith() 和 endswith() 用于检查字符串是否以某个子串开始或结束。
text = "Python is fun"
print(text.startswith("Python"))  # 输出: True
print(text.endswith("fun"))       # 输出: True

# 判断子字符串

# in 运算符：用于检查一个字符串是否包含另一个子字符串。

text = "Python programming is fun"
print("programming" in text)  # 输出: True
print("Java" in text)  # 输出: False
