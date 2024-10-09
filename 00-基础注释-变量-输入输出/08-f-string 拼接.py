# f-string 拼接 可以通过简单的字符串连接方式实现。你可以直接把多个 f-string 用加号（+）连接，或者直接把它们写在一起（这种方式称为隐式拼接）。

# 1. 使用加号（+）拼接 f-string

name = "yujale"
age = 28
city = "Beijing"

# 使用 + 拼接 f-string
message = f"My name is {name}, " + f"I am {age} years old, " + f"and I live in {city}."
print(message)

# 2. 隐式拼接 f-string

# 隐式拼接是直接将多个 f-string 写在一起，不需要加号，只要将它们放在一行或者多行的括号中即可。

name = "yujale"
age = 28
city = "Beijing"

# 使用隐式拼接
message = (
    f"My name is {name}, "
    f"I am {age} years old, "
    f"and I live in {city}."
)
print(message)

# 3. f-string 与常规字符串拼接

# 你可以在 f-string 中直接拼接普通的字符串。

name = "yujale"
message = f"Hello, " + "welcome to " + f"{name}'s world!"
print(message)

# 4. f-string 内部拼接
#
# f-string 还允许在大括号 {} 内进行字符串拼接。

name = "yujale"
greeting = f"Hello, " + f"{name}" + "!"
message = f"{greeting} Welcome to Python programming."
print(message)

