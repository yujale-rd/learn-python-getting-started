"""
函数与函数之间相互隔离
在函数内部的变量是属于这个函数的
    也就是说不能通过函数1访问函数2中的变量对应的值

# 位置参数:按照位置顺序进行赋值的参数(形参)
# 如果有位置参数没有被赋值,则报错
# 如果位置参数传参过多也会报错
结论:位置参数在使用时需要保证每个参数都被赋值,且不要重复赋值或赋多个值


关键字参数 : 关键字参数就是通过"参数名 = 值"的形式进行赋值的参数(实参)

# 使用关键字参数,不需要按照顺序赋值,只要参数名称正确即可
使用参数=值的形式赋值,就是关键字参数
使用关键字参数赋值时,要注意所使用的参数是否存在,最好是提示出来在用
一般情况下,关键字参数都是给默认参数(缺省参数)赋值的
"""


# 缺省参数:就是在定义时给参数一个默认值,如果参数没有赋值,则使用默认值
def func(a, b, c, d=10):
    print(a)
    print(b)
    print(c)
    print(d)


func(1, 2, 3)  # 使用位置参数赋值

"""
函数的组包和拆包

1. 组包（Packing）

组包是指将多个值组合成一个容器类型（如元组、列表、字典等）。
在 Python 中，多个值通过逗号分隔时，Python 会自动将它们组合成一个元组，这是组包的过程。
"""


def func1():
    return 1, 2, 3, 4  # 自动将多个值打包为一个元组


print(func1())  # 输出 (1, 2, 3, 4)

# 手动将多个值打包为一个元组
a = 1, 2, 3, 4
print(a)  # 输出 (1, 2, 3, 4)

"""
2. 拆包（Unpacking）

拆包是指将一个容器类型（如元组、列表等）拆分为多个数据，并分别赋值给多个变量。这种做法在 Python 中非常常见，尤其在处理函数返回值时，通常会直接拆包获取多个值。

"""

# 拆包过程：将列表拆解为多个值
a, b, c, d = [1, 2, 3, 4]
print(a, b, c, d)  # 输出 1 2 3 4

"""
3. 在循环中使用拆包

Python 提供了非常方便的拆包语法，可以直接在循环中进行数据拆解。
"""

# 使用 `enumerate` 对列表进行拆包
list1 = [1, 2, 3, 4]
for index, value in enumerate(list1):
    print(index, value)

# 对字典进行拆包，拆解键和值
dict1 = {'name': 'xiaoming', 'age': 18}
for key, value in dict1.items():
    print(key, value)

"""
4. 同时使用组包与拆包

有时我们需要交换两个变量的值，可以使用 Python 的拆包语法来实现。
"""
a = 1
b = 2

# 交换 a 和 b 的值
a, b = b, a  # 先将 b 和 a 打包为一个元组 (b, a)，然后拆包赋值给 a 和 b
print(a, b)  # 输出 2 1

"""
5. 拆包字典与集合

字典和集合本身是无序的，因此拆包时会得到它们的键（字典）或元素（集合）。

"""
# 拆包字典
dict1 = {'a': 1, 'b': 2, 'c': 3}
char1, char2, char3 = dict1  # 只会得到字典的键
print(char1, char2, char3)  # 输出 'a' 'b' 'c'

# 拆包集合
set1 = {'Tom', 'Bob', 'Rose'}
a, b, c = set1  # 拆包集合的元素，顺序不可控制
print(a, b, c)  # 输出的顺序可能会变化，如 'Rose' 'Tom' 'Bob'


"""
函数的引用

在 Python 中，函数本身也是对象。函数名实际上是指向函数对象的引用。可以将函数赋值给变量或传递给其他函数。

1. 函数赋值给变量

可以将一个函数对象赋值给一个新的变量，这两个变量将指向同一个函数对象。
"""
def greet():
    print("Hello, world!")

# 函数的引用
greeting = greet
greeting()  # 输出: Hello, world!


"""
2. 函数作为参数传递

可以将函数作为参数传递给其他函数，其他函数可以通过该参数调用。
"""
def execute(func):
    func()

def greet():
    print("Hello from the function!")

# 将 greet 函数作为参数传递
execute(greet)  # 输出: Hello from the function!

"""
3. 函数的返回

可以让函数返回另一个函数对象，从而实现函数引用的传递和组合。
"""
def outer():
    def inner():
        print("This is the inner function.")
    return inner

# 获取内层函数的引用
inner_func = outer()
inner_func()  # 输出: This is the inner function.

"""
总结：
	•	==：判断值是否相等。
	•	type()：判断数据类型。
	•	id()：获取数据的内存地址。
	•	is：判断两个对象是否是同一内存空间的引用。
	•	函数引用：函数本身是对象，可以赋值给变量、作为参数传递、作为返回值返回等。
"""

"""
函数的递归

递归是一种在函数内部调用自身的编程技术。为了确保递归能够正确执行，以下三个条件必须满足：

函数递归的三个必备条件
1/函数体内部,调用函数本身
2/递归够明确的跳出条件
3/不能超出最大调用深度

"""

"""
函数调用: 通过小括号的方式让python解释器找到在内存中的函数代码并运行
函数引用: 通过函数名称本身获取函数地址, 这个不是运行代码
1. 函数内部调用自身

递归函数必须在其内部直接或间接地调用自身，这是递归的基本特性。

"""
def recursive_function(n):
    if n > 0:  # 递归条件
        print(n)
        recursive_function(n - 1)  # 函数调用自身

"""
2. 明确的跳出条件

递归函数必须有一个明确的结束条件（基线条件），否则会陷入无限递归，导致程序崩溃。

"""
def factorial(n):
    if n == 0:  # 跳出条件
        return 1
    else:
        return n * factorial(n - 1)  # 递归调用
# 跳出条件 if n == 0 确保递归在达到基线条件时结束。

"""
3. 不能超出最大调用深度

Python 中函数调用的最大递归深度默认值是 1000。如果递归深度超过限制，会抛出 RecursionError。
"""
import sys
print(sys.getrecursionlimit())  # 默认递归深度：1000

# 修改最大递归深度（谨慎使用）
sys.setrecursionlimit(2000)

"""
完整示例：斐波那契数列
"""
def fibonacci(n):
    if n <= 1:  # 跳出条件
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)  # 函数调用自身

# 测试递归函数
print(fibonacci(10))  # 输出: 55

"""
递归函数的优缺点
分析：
	1.	调用自身：fibonacci 在函数体内递归调用自身。
	2.	跳出条件：当 n <= 1 时，递归停止，返回结果。
	3.	递归深度：递归深度取决于输入值，输入过大可能超过最大调用深度。
"""

"""
注意事项
	•	递归效率：递归通常比循环效率低，尤其在深度较大时可能导致栈溢出。
	•	尾递归优化：Python 不支持尾递归优化（许多其他语言如 Lisp 支持），因此深度大的递归可能需要改写为循环或用显式栈模拟递归。
"""


"""
匿名函数
在 Python 中，匿名函数使用 lambda 关键字定义。匿名函数没有显式的 def 和函数名，是一类轻量级的函数，通常用于简短的、一次性的操作。
定义和基本语法
lambda 参数1, 参数2, ... : 表达式
	•	lambda 是关键字。
	•	参数列表后跟一个冒号 : 。
	•	冒号后是返回值的表达式，不能包含多行代码或复杂逻辑。

"""
# 一个简单的匿名函数，计算两个数的和
add = lambda x, y: x + y
print(add(3, 5))  # 输出: 8

# 不使用变量名直接调用
print((lambda x, y: x * y)(4, 6))  # 输出: 24

# 匿名函数的应用场景
nums = [1, 2, 3, 4]
squared = map(lambda x: x ** 2, nums)
print(list(squared))  # 输出: [1, 4, 9, 16]

nums = [1, 2, 3, 4, 5, 6]
even = filter(lambda x: x % 2 == 0, nums)
print(list(even))  # 输出: [2, 4, 6]

students = [
    {'name': 'Tom', 'age': 20},
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 22},
]
# 按年龄排序
sorted_students = sorted(students, key=lambda student: student['age'])
print(sorted_students)
# 输出: [{'name': 'Tom', 'age': 20}, {'name': 'Bob', 'age': 22}, {'name': 'Alice', 'age': 25}]


"""
匿名函数的局限性
	1.	只能包含单个表达式：匿名函数的功能有限，不能写多行代码。
	2.	没有名称：调试时可能不便于识别。
	3.	无类型注解：不支持为参数或返回值添加类型注解。
"""

"""
1. 装饰器（Decorators）

装饰器是 Python 中的一种高级功能，它允许你在不修改函数代码的情况下扩展函数的功能。装饰器本质上是一个函数，它接收一个函数作为参数并返回一个函数。
定义和应用装饰器

装饰器工作原理：
	1.	装饰器函数接收一个函数作为参数。
	2.	装饰器函数内部定义一个新的函数（通常称为 wrapper）。
	3.	在 wrapper 函数中，你可以添加额外的逻辑，比如日志记录、性能测试、权限检查等。
	4.	在 wrapper 函数中调用原始函数。
	5.	返回 wrapper 函数作为装饰后的函数。	
装饰器通常以 @ 符号应用到目标函数上：
"""
# 定义装饰器
def decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

# 使用装饰器
@decorator
def say_hello():
    print("Hello, World!")

say_hello()

"""
Before function call
Hello, World!
After function call
"""

"""
参数化装饰器

装饰器可以传入参数，例如，如果你希望一个装饰器能够接收一些配置参数，可以像下面这样实现：
"""
def decorator_with_args(arg):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"Decorator argument: {arg}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@decorator_with_args("My Argument")
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")

"""
2. 闭包（Closure）

闭包是指一个函数在其内部引用了外部函数的变量，并且返回了该函数。闭包可以保存外部函数的状态，即使外部函数已经执行完毕。
"""
def outer(x):
    def inner(y):
        return x + y  # inner 引用了外部函数 outer 的变量 x
    return inner

add_5 = outer(5)
print(add_5(3))  # 输出 8

# 在上面的例子中，add_5 是 inner 函数的引用，并且保存了外部函数 outer 中的变量 x 的值。闭包的特点是，它使得外部函数的变量可以在内部函数中长期有效。


"""
3. 函数注解（Function Annotations）

函数注解允许为函数的参数和返回值提供类型提示。虽然这些注解不会影响代码的执行，但是它们可以提高代码的可读性并帮助开发者理解函数的使用。
"""
def greet(name: str, age: int) -> str:
    return f"Hello, {name}. You are {age} years old."

print(greet("Alice", 30))

# 你可以通过 __annotations__ 属性来访问函数的注解：
print(greet.__annotations__)  # 输出 {'name': <class 'str'>, 'age': <class 'int'>, 'return': <class 'str'>}

"""
函数的调用栈与优化

Python 中的函数调用会有一个调用栈。每次函数调用时，会将当前函数的执行状态保存到栈中，直到当前函数返回。在递归中，调用栈的深度会逐步增加，如果深度过大，可能会导致 RecursionError。

为了优化递归调用，尽量避免过深的递归。对于深度较大的递归问题，可以使用迭代替代递归，或者使用显式栈来模拟递归。
"""