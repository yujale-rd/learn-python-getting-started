# 函数是编程中的基本概念之一，用于封装一段可以重复使用的代码。通过函数，可以将复杂的操作分解成一个个小的、可重用的模块，从而提高代码的可读性、可维护性和复用性。

# 函数的定义和调用
#
# 使用 def 关键字定义一个函数，并使用函数名来调用它。

"""
基本格式
def 函数名(参数列表):
    函数体
    return 返回值（可选）
"""


def greet(name):
    print(f"Hello, {name}!")


greet("Alice")  # 调用函数，输出: Hello, Alice!

"""

函数的重要性
1. 代码重用
当一段代码需要在多个地方使用时，将其封装为一个函数可以避免代码重复，提高代码的可维护性和可读性。
2. 逻辑分割
将复杂的代码逻辑分解为多个小函数，使得每个函数只负责一个明确的任务，这样代码更加清晰和易于理解。
3. 提高代码可读性
函数名称可以描述代码的意图，使代码更加自解释。读代码时，可以通过函数名称迅速理解代码的作用。方便调试：通过对函数进行单独测试，可以更容易地发现和修复问题。
4. 简化调试和测试
将代码分割成函数后，可以对每个函数进行独立测试和调试，从而更容易找到和修复问题。
5. 参数化处理
当处理一些需要传入不同参数的任务时，可以将任务逻辑封装为函数，通过参数来灵活处理不同的情况。
6. 避免全局变量污染
使用函数可以将变量的作用域限制在函数内部，避免全局变量污染，从而减少变量命名冲突的风险。
"""


# 函数的参数

# 位置参数
# 按顺序传递参数
def add(x, y):
    return x + y


result = add(5, 3)
print(result)  # 输出: 8


# 默认参数

# 定义函数时，可以为某些参数设置默认值，如果调用时不传递这些参数，将使用默认值

def greet(name="Guest"):
    print(f"Hello, {name}!")


greet()  # 输出: Hello, Guest!
greet("Bob")  # 输出: Hello, Bob!


# 关键字参数：

# 调用函数时，可以通过指定参数名称传递参数值，参数顺序可以改变
def greet(first_name, last_name):
    print(f"Hello, {first_name} {last_name}!")


greet(last_name="Smith", first_name="John")  # 输出: Hello, John Smith!


# 可变参数
# 使用 *args 和 **kwargs 接收任意数量的参数。
#
# *args 用于接收位置参数的元组。
# **kwargs 用于接收关键字参数的字典。

# 可变位置参数
def sum_numbers(*args):
    return sum(args)


result = sum_numbers(1, 2, 3, 4)
print(result)  # 输出: 10


# 可变关键字参数
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_info(name="Alice", age=30, city="New York")


# 返回值

# 函数可以使用 return 关键字返回结果。如果函数没有 return，则默认返回 None。
def multiply(x, y):
    return x * y

result = multiply(4, 5)
print(result)  # 输出: 20

'''
1.返回值是将函数内计算或运行的结果返回到函数外部调用位置,参与计算或运行
2.函数可以不写返回值或者只写一个return不写返回值内容,都会默认返回一个None
3.return后将会立即跳出函数,如果在retrun后仍有代码,则不会被执行
4.return只能返回一个元素,如果想返回多个元素需要使用容器类型
'''

# 函数的执行顺序
# 在 Python 中，函数的调用顺序遵循调用栈机制，当一个函数被调用时，程序会暂停当前的执行，跳转到被调用的函数进行执行，被调用的函数执行完毕后，会返回他被调用的地方，继续执行后续的代码

# 调用顺序的基本原则
#
# 顺序执行：函数调用遵循代码编写的顺序。
# 函数嵌套调用：如果一个函数在执行过程中调用了其他函数，那么会先执行被调用的函数，等被调用的函数执行完成后，返回到原函数继续执行。

# 函数嵌套调用
def func1():
    print("func1 开始")
    func2()  # 调用 func2
    print("func1 结束")

def func2():
    print("func2 开始")
    func3()  # 调用 func3
    print("func2 结束")

def func3():
    print("func3 执行")

func1()

# 输出顺序：
# func1 开始
# func2 开始
# func3 执行
# func2 结束
# func1 结束


# 调用栈示意
#
# 每次函数被调用时，都会将当前执行位置保存在调用栈中，等函数执行完毕后，程序会回到栈顶的函数继续执行。
#
# 	1.	func1() 调用，进入 func1()。
# 	2.	func1() 调用 func2()，暂停 func1()，进入 func2()。
# 	3.	func2() 调用 func3()，暂停 func2()，进入 func3()。
# 	4.	func3() 执行完毕，返回到 func2()。
# 	5.	func2() 执行完毕，返回到 func1()。
# 	6.	func1() 执行完毕，程序结束。

# 递归调用中的顺序
#
# 递归调用是函数调用自己的情况，通常需要明确一个终止条件，防止无限递归。

def factorial(n):
    if n == 1:  # 基本条件（终止条件）
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))

# 调用顺序：
# factorial(5) -> factorial(4) -> factorial(3) -> factorial(2) -> factorial(1)
# 返回顺序：
# factorial(1) -> factorial(2) -> factorial(3) -> factorial(4) -> factorial(5)

# 在递归调用中，每次调用会将当前函数的状态（即参数值）保存到调用栈中，直到遇到终止条件为止。之后按照调用栈的顺序依次返回。


# 函数的局部变量和全局变量

# 在 Python 中，局部变量和全局变量是变量的两种作用域类型，它们决定了变量的可见性和使用范围。理解局部变量和全局变量的区别有助于编写高效且易于维护的代码。
# 局部变量是在函数内部定义的变量，只在该函数的作用域内有效。他们在函数调用时创建，函数执行完毕后销毁，局部变量不会影响函数外的变量，函数外的变量也无法访问局部变量


def my_function():
    x = 10  # x 是局部变量，只在函数内部有效
    print(x)

my_function()  # 输出 10
# print(x)  # 这将抛出 NameError，因为 x 是局部变量，函数外无法访问

# 特点：
#
# 局部变量只能在定义它的函数内部使用。
# 一旦函数结束，局部变量就会被销毁。
# 不同函数中的局部变量之间互不影响。

# 全局变量是在函数外部定义的量，他们在整个程序中都可以访问，全局变量在程序启动时创建，并且在程序执行过程中一直存在，函数内部默认无法直接修改全局变量，但可以读取他们的值
y = 20  # y 是全局变量

def my_function():
    print(y)  # 可以在函数内部访问全局变量

my_function()  # 输出 20

# 修改全局变量 global

# 如果在函数内部需要修改全局变量，需要使用 global 关键字声明该变量是全局的，否则 Python 会默认在函数内部创建一个新的局部变量，而不会修改全局变量。

z = 30  # 全局变量

def modify_global():
    global z  # 声明 z 是全局变量
    z = 40    # 修改全局变量的值

modify_global()
print(z)  # 输出 40

# 	•	如果不使用 global 关键字，Python 会认为 z 是一个局部变量，修改不会影响全局变量。

# 局部变量与全局变量同名

# 当局部变量和全局变量同名时，在函数内部，局部变量会覆盖全局变量。也就是说，函数内部优先使用局部变量，而不会修改全局变量的值。

a = 100  # 全局变量

def my_function():
    a = 200  # 局部变量，覆盖全局变量
    print(a)  # 输出 200

my_function()
print(a)  # 输出 100，外部的全局变量 a 没有受到影响

# nonlocal 关键字

# nonlocal 用于修改嵌套函数中外部函数的局部变量。在嵌套函数中，如果需要修改外层函数的局部变量，可以使用 nonlocal 声明。

def outer_function():
    x = 10

    def inner_function():
        nonlocal x  # 声明 x 是外部函数的局部变量
        x = 20

    inner_function()
    print(x)  # 输出 20

outer_function()