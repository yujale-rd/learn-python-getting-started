# 在 Python 中，转义字符（escape character）用于表示一些特殊字符或者无法直接在字符串中使用的字符。转义字符以反斜杠 (\) 开头，后跟一个或多个字符，表示不同的特殊含义。

# 换行符 \n 和制表符 \t：

print("Hello\nWorld")  # 输出 "Hello" 后换行再输出 "World"
print("Hello\tWorld")  # 输出 "Hello"，然后插入一个水平制表符再输出 "World"

# 单引号和双引号的转义：

# 在字符串中使用单引号和双引号
print('I\'m learning Python.')  # 单引号前面需要加反斜杠进行转义
print("He said, \"Python is awesome!\"")  # 双引号需要加反斜杠

# 反斜杠 \\ 的转义：


# 打印反斜杠
print("This is a backslash: \\")

# Unicode 字符 \u：
print("The Unicode for 'π' is: \u03C0")

# 八进制和十六进制转义：
# 使用八进制和十六进制表示字符
print("\101")   # 八进制，输出字符 'A'
print("\x41")   # 十六进制，输出字符 'A'

# 原始字符串（Raw String）
#
# 有时候我们希望字符串中的反斜杠不被解释为转义字符，可以使用 原始字符串（raw string），它以 r 或 R 开头。
print(r"C:\Users\new_folder")  # 使用原始字符串，反斜杠不会被转义

# - 转义字符 允许你在字符串中使用不可见或特殊的字符。
# - 使用 原始字符串 可以避免反斜杠的转义，常用于路径或正则表达式中。