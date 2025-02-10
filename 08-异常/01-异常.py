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

# 异常的层级结构

"""
Python 中的异常类是一个层级结构，所有的异常都继承自 BaseException 类。常见的异常继承自 Exception 类，而一些更底层的异常（比如 SystemExit、KeyboardInterrupt）继承自 BaseException。理解这一点有助于更好地处理异常。
	•	BaseException：所有异常的基类。
	•	Exception：标准的异常基类，继承自 BaseException。
	•	ArithmeticError：算术相关的错误，如除零错误（ZeroDivisionError）。
	•	LookupError：查找相关的错误，如索引超出范围（IndexError）和键不存在（KeyError）。
	•	ValueError：值相关的错误，如传入了无效的参数类型。
	•	SystemExit：程序正常退出时抛出的异常，通常通过 sys.exit() 触发。
	•	KeyboardInterrupt：用户手动中断程序时抛出的异常，如按下 Ctrl+C。
	•	GeneratorExit：与生成器相关的异常。

这种层级结构说明了异常类型之间的关系，捕获父类异常时，子类异常也会被捕获，但如果你想捕获特定的异常，应该尽量避免捕获 Exception 类的通用异常，而是直接捕获具体的异常类。
"""

"""
2. 异常的作用域

异常捕获和处理时，需要注意异常的作用域。异常的作用域是指异常处理器的作用范围，通常遵循从内到外的原则。
如果在一个代码块中抛出了异常，而这个异常没有被当前代码块的 except 捕获，Python 会沿着调用栈向上查找直到找到合适的 except 语句。
如果没有找到合适的处理器，程序会终止并显示错误。

3. 异常的性能

异常机制的性能开销相对较高。在 Python 中，异常的抛出和捕获是比较重的操作，因此在性能敏感的代码中应尽量避免大量使用异常来控制程序流。
异常应该用于处理意外错误，而不是用来执行常规逻辑。
"""

"""
4. 异常的传递

异常可以传递给调用者，也可以通过 raise 语句向上层函数传递。通过 raise 语句的使用，程序可以在合适的时机停止执行并转交给上层的异常处理机制。这种传递机制有助于逐层捕获和处理错误，并且可以提供更详细的错误信息。
"""
def process_data(data):
    if data is None:
        raise ValueError("Data cannot be None")
    # 继续处理数据

def main():
    try:
        process_data(None)
    except ValueError as e:
        print(f"Error in main: {e}")

main()
# 在这个例子中，ValueError 从 process_data 函数抛出，并在 main 函数中被捕获，显示了异常传递的机制。

"""
5. with 语句与异常处理

with 语句是 Python 中的上下文管理器，通常用于需要清理资源的场景，如文件、数据库连接等。在异常发生时，with 语句的作用是自动处理资源的释放，确保无论是否发生异常，都会执行清理操作。
"""
with open("data.txt", "r") as file:
    content = file.read()
    if len(content) == 0:
        raise ValueError("File is empty")
    print(content)
# 在这个例子中，with 会确保文件在读取结束后正确关闭，避免在异常发生时文件没有被关闭的问题。