"""
在 Python 中，异常（Exception） 是程序运行过程中发生的错误事件。当程序出现错误时，Python 会抛出一个异常，程序会终止当前执行，除非有适当的异常处理机制来捕获并处理它。
理解和使用异常可以帮助程序更加健壮，能够处理各种运行时错误。

程序在运行的过程中可能因为代码不规范而导致的报错
    报错其实就是异常

通过异常名称源码发现异常其实是一个类, 异常类
    普遍异常类会继承同一个基类：Exception

    1. 异常概念

异常 是程序运行时发生的错误或意外情况。Python 内置了多种异常类型，涵盖了大部分常见的错误。常见的异常类型有：
	•	ZeroDivisionError：除零错误
	•	ValueError：值错误
	•	IndexError：索引错误
	•	TypeError：类型错误
	•	FileNotFoundError：文件未找到
	•	KeyError：字典中键不存在
	•	AttributeError：对象没有该属性

异常发生时，Python 会生成一个异常对象，并通过异常的栈追踪来报告错误的具体信息。

2. 异常处理

Python 使用 try、except 语句来捕获和处理异常。基本结构如下：
"""
try:
    # 可能发生异常的代码
    x = 1 / 0  # 会抛出 ZeroDivisionError
except ZeroDivisionError as e:
    # 处理异常的代码
    print(f"Error occurred: {e}")
else:
    # 没有异常时执行的代码
    print("No errors occurred.")
finally:
    # 无论是否发生异常都会执行的代码
    print("This will always be executed.")
"""
	•	try：包含可能抛出异常的代码块。
	•	except：捕获并处理异常。
	•	else：如果没有异常发生，执行该部分代码。
	•	finally：无论是否发生异常，都会执行该部分代码（通常用于清理资源，如关闭文件、释放数据库连接等）。

"""

"""
3. 手动捕获异常

你可以捕获不同类型的异常，甚至捕获多个异常。
"""
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Cannot divide by zero.")
except ValueError:
    print("Invalid input. Please enter a number.")

"""
4. 手动抛出异常

有时我们希望在程序中手动抛出异常，使用 raise 语句。
"""
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    print(f"Age is {age}")

try:
    validate_age(-5)
except ValueError as e:
    print(e)

# 	通过 raise 语句手动抛出一个 ValueError 异常，并传递一个自定义的错误消息。

"""
 断言（Assertion）

断言 是一种用于调试的工具，通常用于检查程序中的不变量。assert 语句会检查给定的条件，如果条件为 False，则会抛出 AssertionError 异常。
"""
x = 10
assert x > 0, "x should be greater than 0"
assert x < 0, "x should be less than 0"  # 这行会抛出异常

# 断言语句用于开发过程中进行调试，检查程序逻辑是否符合预期。在生产环境中，Python 可以通过运行时参数禁用断言（使用 python -O 选项运行）。

"""
自定义异常

你可以自定义异常类，继承自 Exception 基类。自定义异常使得你能够根据需要抛出更加特定的异常。
"""
class NegativeAgeError(Exception):
    def __init__(self, message="Age cannot be negative"):
        self.message = message
        super().__init__(self.message)

def set_age(age):
    if age < 0:
        raise NegativeAgeError("Age is negative!")
    print(f"Age is set to {age}")

try:
    set_age(-10)
except NegativeAgeError as e:
    print(f"Custom Error: {e}")

"""
 finally 语句

finally 块总是会被执行，不论是否发生异常。通常用于清理操作，如关闭文件、网络连接等。
"""
try:
    file = open("data.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found!")
else:
    print(content)
finally:
    print("Closing file.")
    file.close()

"""
异常链（Exception Chaining）

Python 支持异常链，通过 raise ... from ... 可以将一个异常重新抛出并附加上一个原始异常。
"""
try:
    x = 1 / 0
except ZeroDivisionError as e:
    raise ValueError("Invalid operation") from e

"""
ValueError: Invalid operation
  Caused by: ZeroDivisionError: division by zero
	•	from e 表示将原始的 ZeroDivisionError 异常附加到新抛出的 ValueError 异常上，形成异常链。
"""