# f-string 拼接 可以通过简单的字符串连接方式实现。你可以直接把多个 f-string 用加号（+）连接，或者直接把它们写在一起（这种方式称为隐式拼接）。


"""
1. 使用加号 (+) 拼接 f-string

这种方式直观且易读，但要注意性能问题。字符串拼接在多次操作时会创建新的字符串对象，可能影响效率。
"""

name = "yujale"
age = 28
city = "Beijing"

message = f"My name is {name}, " + f"I am {age} years old, " + f"and I live in {city}."
print(message)  # 输出: My name is yujale, I am 28 years old, and I live in Beijing.
"""
2. 隐式拼接 f-string

隐式拼接更推荐，尤其在多行代码中，简化了写法，性能也更优。
"""
message = (
    f"My name is {name}, "
    f"I am {age} years old, "
    f"and I live in {city}."
)
print(message)  # 输出: My name is yujale, I am 28 years old, and I live in Beijing.

"""
注意事项：

隐式拼接只能在括号 () 内使用，否则会报错：
"""
# 报错示例：
message = f"Hello, "  # SyntaxError
f"My name is {name}"
"""
3. f-string 与常规字符串混合拼接

f-string 和普通字符串可以任意组合使用：
"""

name = "yujale"
message = f"Hello, " + "welcome to " + f"{name}'s world!"
print(message)  # 输出: Hello, welcome to yujale's world!

"""
4. f-string 内部拼接

f-string 中的大括号 {} 可以嵌套表达式，如拼接字符串或其他操作。
"""

name = "yujale"
greeting = f"Hello, {name + '!'}"  # f-string 内部拼接
message = f"{greeting} Welcome to Python programming."
print(message)  # 输出: Hello, yujale! Welcome to Python programming.

"""
	•	f-string 优点：
	•	语法简洁、可读性强。
	•	支持表达式、函数调用。
	•	性能优越，推荐在 Python 3.6+ 使用。
	•	拼接建议：
	•	小规模拼接可用 + 或隐式拼接。
	•	多行拼接时更推荐隐式拼接。
	•	避免频繁用 +，而是尽量用单个 f-string。
"""
