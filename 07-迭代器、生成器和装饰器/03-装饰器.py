"""

在 Python 中，装饰器是一种高阶函数，它允许在不修改函数本身的情况下动态地为其添加功能。装饰器本质上是接收一个函数作为输入，返回一个新的函数，通常用来增强或修改原函数的行为。

装饰器的核心思想是“函数的函数”，即一个函数接受另一个函数作为参数，并返回一个新的函数。

1. 装饰器的概念

装饰器允许你在运行时动态地修改函数、方法或类的行为，而不需要修改其源代码。装饰器常用于：
	•	日志记录
	•	权限检查
	•	性能监控
	•	缓存等
2. 装饰器的基本定义

一个简单的装饰器是一个接受函数作为参数，并返回一个新函数的函数。
"""
def decorator(func):
    def wrapper():
        print("Before function execution.")
        func()  # 调用原函数
        print("After function execution.")
    return wrapper

# 使用装饰器
@decorator
def say_hello():
    print("Hello!")

say_hello()
# 	•	@decorator 是一个装饰器语法糖，它会自动把 say_hello 函数传递给 decorator 函数，并返回一个新的 wrapper 函数来替代原函数。

"""
3. 装饰器的执行过程
	1.	@decorator 将 say_hello 函数传递给装饰器 decorator。
	2.	装饰器 decorator 返回一个新的函数 wrapper，该函数包含原函数的调用并在前后加上额外的功能。
	3.	当调用 say_hello() 时，实际上是在调用 wrapper() 函数，执行额外功能并调用原函数。

"""

"""
4. 带有参数的装饰器

如果装饰器需要处理带参数的函数（如 say_hello("Alice")），我们需要让 wrapper 函数接受任意数量的参数和关键字参数
"""
def decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function execution.")
        func(*args, **kwargs)
        print("After function execution.")
    return wrapper

@decorator
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Alice")

"""
5. 装饰器返回值

装饰器不仅可以修改原函数的行为，还可以修改返回值。如果你需要在装饰器中改变原函数的返回值，可以在 wrapper 函数中处理。
"""
def decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()  # 修改返回值
    return wrapper

@decorator
def say_hello(name):
    return f"Hello, {name}!"

print(say_hello("Alice"))

"""
使用 functools.wraps 保持原函数的元数据

使用装饰器时，wrapper 函数通常会替代原函数。这会导致一些元数据（如函数的名称、文档字符串等）丢失。为了避免这种情况，可以使用 functools.wraps 来保持原函数的元数据。
"""
from functools import wraps

def decorator(func):
    @wraps(func)  # 保留原函数的元数据
    def wrapper(*args, **kwargs):
        print("Before function execution.")
        result = func(*args, **kwargs)
        print("After function execution.")
        return result
    return wrapper

@decorator
def say_hello(name):
    """This function greets the user."""
    return f"Hello, {name}!"

print(say_hello.__name__)  # 输出 say_hello
print(say_hello.__doc__)   # 输出 This function greets the user.

"""
装饰器链（多个装饰器）

可以对一个函数应用多个装饰器，这时多个装饰器将会按从下往上的顺序依次执行。
"""
def decorator1(func):
    def wrapper(*args, **kwargs):
        print("Decorator 1 before")
        return func(*args, **kwargs)
    return wrapper

def decorator2(func):
    def wrapper(*args, **kwargs):
        print("Decorator 2 before")
        return func(*args, **kwargs)
    return wrapper

@decorator1
@decorator2
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Alice")

"""
装饰器的缺点
	1.	调试困难：装饰器可能使得调试变得复杂，因为堆栈跟踪可能不清晰，装饰器包裹的函数会隐藏原始函数的堆栈信息。
	2.	性能开销：每次函数调用时，装饰器都会增加额外的开销，尤其是装饰器链的使用。
	3.	元数据丢失：装饰器可能会导致原函数的文档字符串、名称等元数据丢失，除非使用 functools.wraps。
"""

"""
1. 装饰器与类

装饰器不仅可以用于函数，也可以用于类。通过类装饰器，你可以对类的行为进行修改。例如，可以修改类的初始化方法，或者在创建类实例时添加一些额外的功能。
"""


def class_decorator(cls):
    # 修改类的行为，例如为类添加一个新的方法
    cls.new_method = lambda self: "This is a new method"
    return cls


@class_decorator
class MyClass:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}!"


obj = MyClass("Alice")
print(obj.greet())  # 输出: Hello, Alice!
print(obj.new_method())  # 输出: This is a new method

"""
2. 装饰器的参数化

有时我们需要在装饰器外部传递一些参数给装饰器。为此，可以编写一个装饰器工厂（即返回装饰器的装饰器）。
"""
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Alice")
# 输出：
# Hello, Alice!
# Hello, Alice!
# Hello, Alice!

"""
3. 缓存装饰器

装饰器也可以用于实现缓存功能，以避免重复计算昂贵的操作。例如，使用 functools.lru_cache 来为一个函数自动实现缓存功能：
"""
from functools import lru_cache

@lru_cache(maxsize=128)  # 设置缓存最大容量
def expensive_computation(n):
    print(f"Computing {n}...")
    return n * n

print(expensive_computation(10))  # 输出: Computing 10... 100
print(expensive_computation(10))  # 不会打印计算过程，直接输出结果: 100

"""
5. 装饰器中的异常处理

装饰器中也可以处理异常，在函数执行时捕获异常并进行处理。例如，我们可以写一个装饰器，在函数抛出异常时记录日志：
"""
def exception_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"An error occurred: {e}")
            return None  # 可以选择返回一个默认值
    return wrapper

@exception_handler
def divide(a, b):
    return a / b

print(divide(10, 2))  # 输出: 5.0
print(divide(10, 0))  # 输出: An error occurred: division by zero

"""
装饰器与 staticmethod 和 classmethod

当装饰器用于类方法时，需要特别注意 staticmethod 和 classmethod。这些方法的第一个参数是 self 或 cls，因此装饰器需要正确处理它们。
"""
def staticmethod_decorator(func):
    def wrapper(*args, **kwargs):
        print("This is a static method.")
        return func(*args, **kwargs)
    return wrapper

class MyClass:
    @staticmethod
    @staticmethod_decorator
    def greet(name):
        return f"Hello, {name}!"

print(MyClass.greet("Alice"))

"""
装饰器链的顺序

当多个装饰器应用到同一个函数时，装饰器的应用顺序是从内到外的，也就是说最靠近函数定义的装饰器首先执行。例如，@decorator1 @decorator2 先执行 decorator2，然后执行 decorator1。
"""
def decorator1(func):
    def wrapper(*args, **kwargs):
        print("Decorator 1 before")
        return func(*args, **kwargs)
    return wrapper

def decorator2(func):
    def wrapper(*args, **kwargs):
        print("Decorator 2 before")
        return func(*args, **kwargs)
    return wrapper

@decorator1
@decorator2
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Alice")
# 输出：
# Decorator 1 before
# Decorator 2 before
# Hello, Alice!