"""
函数是编程中的基本概念之一，用于封装一段可以重复使用的代码。
通过函数，可以将复杂的操作分解成一个个小的、可重用的模块，从而提高代码的可读性、可维护性和复用性。

函数在python中也是一种对象
    可以理解成是一个容器: 这个容器存储的不是数据, 代码


函数的定义和调用

使用 def 关键字定义一个函数，并使用函数名来调用它。

"""

"""
基本格式
def 函数名(参数列表):
    函数体
    return 返回值（可选）
    
1.定义函数需要使用python中的一个关键字: def
2.函数名称的后面需要加上小括号和冒号开启一段代码块
3.在代码块的内部写入你想要执行的代码逻辑
4.运行函数代码需要写入函数名称并加上小括号
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


"""
函数的分类
- 内置函数
- 自定义函数

内置函数是 Python 提供的、已经定义好的函数，可以直接使用，无需用户自己定义。Python 提供了大量的内置函数，常见的内置函数包括：
	•	print()：打印输出
	•	input()：获取用户输入
	
2. 自定义函数

自定义函数是由程序员根据实际需要自己定义的函数，通常用来封装一段特定的功能或任务。
	

def function_name(parameters):
    # 函数体
    return result  # 可选

•	function_name 是函数名。
•	parameters 是函数的输入参数（可选）。
•	function body 是函数的执行代码。
•	return 语句用于返回函数的结果（可选）。

    
"""

"""
函数参数是函数定义时指定的变量，用于接收调用时传入的值。在 Python 中，函数支持多种类型的参数：
	1.	位置参数（Positional Parameters）
	2.	默认参数（Default Parameters）
	3.	关键字参数（Keyword Parameters）
	4.	可变参数（Variable-length Parameters）
"""

"""
1. 位置参数

位置参数是最常见的函数参数类型。调用函数时，传入的值必须按照定义时的参数顺序进行传递。
"""
def greet(name, age):
    print(f"Hello, {name}. You are {age} years old.")

greet("Alice", 30)  # 输出: Hello, Alice. You are 30 years old.


"""
2. 默认参数

默认参数是为函数参数设置一个默认值。如果调用时没有传入该参数，函数会使用默认值。
"""

def greet(name="Guest", age=18):
    print(f"Hello, {name}. You are {age} years old.")

greet()  # 输出: Hello, Guest. You are 18 years old.
greet("Bob")  # 输出: Hello, Bob. You are 18 years old.
greet("Alice", 30)  # 输出: Hello, Alice. You are 30 years old.

"""
3. 关键字参数

关键字参数允许你在调用函数时，通过指定参数名来传递值，而不是按位置顺序传递。这样可以使调用函数时参数的顺序不重要，增加代码的可读性。
"""
def greet(name, age):
    print(f"Hello, {name}. You are {age} years old.")

greet(age=25, name="Alice")  # 输出: Hello, Alice. You are 25 years old.


"""
4. 可变参数

可变参数可以让函数接收任意数量的位置参数或关键字参数，使用 *args 和 **kwargs 来实现。
# *args 用于接收位置参数的元组。
# **kwargs 用于接收关键字参数的字典。
"""

"""
4.1 可变位置参数 (*args)

*args 可以接收一个元组，表示函数的可变数量的非关键字参数。
"""
def sum_numbers(*args):
    return sum(args)

print(sum_numbers(1, 2, 3, 4))  # 输出: 10
# 	•	*args 将所有传入的参数打包成一个元组。在上面的例子中，args 是一个包含所有传入数值的元组。

"""
4.2 可变关键字参数 (**kwargs)

**kwargs 用来接收任意数量的关键字参数，并将其打包成一个字典。
"""
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, city="New York")
# 输出:
# name: Alice
# age: 30
# city: New York

# 	•	**kwargs 将所有传入的关键字参数打包成一个字典。在这个例子中，kwargs 是一个字典，包含所有传入的键值对。

"""
参数的使用顺序

当定义一个函数时，参数的顺序必须遵循以下规则：
	1.	位置参数必须在默认参数之前。
	2.	默认参数必须在关键字参数之前。
	3.	如果函数接受可变参数（*args 和 **kwargs），它们必须在常规参数和默认参数之后，且 *args 在 **kwargs 之前。
"""

def example_function(a, b, c=10, *args, d=20, **kwargs):
    print(a, b, c, args, d, kwargs)


"""
5. 返回值
函数的返回值是执行完函数后返回的结果，它允许将计算或操作的结果传递给函数外部的调用者。return 关键字用于返回结果。

1. 函数返回值的基本使用


	•	返回值的作用：return 使得函数能够返回计算结果，供调用处使用。
	•	没有返回值的情况：如果没有 return，或者只有 return 但没有指定返回值，函数默认返回 None。
	
	2. 关于 return 关键字
	•	return 语句不仅返回一个结果，而且立即结束当前函数的执行，后面的代码不会被执行。
	•	return 只能返回一个值，但你可以使用容器类型（如元组、列表或字典）来返回多个值。
"""
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

"""
在 Python 中，函数的调用顺序遵循调用栈机制，当一个函数被调用时，程序会暂停当前的执行，跳转到被调用的函数进行执行，被调用的函数执行完毕后，会返回他被调用的地方，继续执行后续的代码
1. 顺序执行与函数嵌套调用

在 Python 中，函数调用遵循调用栈机制：当一个函数被调用时，程序会暂停当前的执行，跳转到被调用的函数进行执行；函数执行完后，会返回到原函数继续执行。

"""
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


"""
调用栈的示意
	1.	执行 func1()，进入 func1。
	2.	func1 调用 func2，暂停 func1，进入 func2。
	3.	func2 调用 func3，暂停 func2，进入 func3。
	4.	func3 执行完毕，返回到 func2。
	5.	func2 执行完毕，返回到 func1。
	6.	func1 执行完毕，程序结束。
"""
"""
2. 递归调用

递归调用是指函数在其定义中调用自身。递归通常需要一个明确的终止条件，以避免无限递归。
"""

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

"""
	•	在递归过程中，factorial 函数不断调用自身，每一次都将当前的参数值压入调用栈中。当达到终止条件时（n == 1），开始返回并执行回溯过程，逐步返回计算结果。

递归的工作原理：
	•	每次递归调用时，都会将当前函数的状态（如参数值）保存在调用栈中。
	•	递归调用直到遇到终止条件时停止，然后按照调用栈的顺序返回并执行余下的操作。
"""

"""
函数的局部变量和全局变量

在 Python 中，变量的作用域决定了变量可以在哪些位置访问。常见的作用域有局部作用域和全局作用域。

"""

"""
1. 局部变量（Local Variables）

局部变量是定义在函数内部的变量，只能在该函数内部使用。当函数执行时，局部变量被创建，函数执行完毕后，它们被销毁，无法在函数外部访问。
"""


def my_function():
    x = 10  # x 是局部变量，只在函数内部有效
    print(x)

my_function()  # 输出: 10
# print(x)  # 这将抛出 NameError，因为 x 是局部变量，函数外无法访问

# 特点：
#
# 局部变量只能在定义它的函数内部使用。
# 一旦函数结束，局部变量就会被销毁。
# 不同函数中的局部变量之间互不影响。

"""
2. 全局变量（Global Variables）

全局变量是在函数外部定义的变量，程序中的任何地方都可以访问它们。全局变量在程序运行时创建，并且在程序结束时销毁。
"""

y = 20  # y 是全局变量

def my_function():
    print(y)  # 可以在函数内部访问全局变量

my_function()  # 输出 20

"""
	特点：
	•	全局变量可以在程序中的任何地方访问。
	•	函数内部默认无法修改全局变量，但可以读取它们的值。
"""

"""
3. 修改全局变量

如果需要在函数内部修改全局变量，必须使用 global 关键字声明变量是全局变量。
"""
z = 30  # 全局变量

def modify_global():
    global z  # 声明 z 是全局变量
    z = 40    # 修改全局变量的值

modify_global()
print(z)  # 输出: 40

# 	•	如果不使用 global 关键字，Python 会认为 z 是一个局部变量，修改不会影响全局变量。

"""
4. 局部变量与全局变量同名

如果局部变量和全局变量同名，那么局部变量会覆盖全局变量。函数内部会优先使用局部变量，而不会修改全局变量的值。
"""
a = 100  # 全局变量

def my_function():
    a = 200  # 局部变量，覆盖全局变量
    print(a)  # 输出: 200

my_function()
print(a)  # 输出: 100，外部的全局变量 a 没有受到影响

# 	•	说明：局部变量 a 覆盖了函数内部的全局变量 a，但函数外的全局变量 a 没有变化。

"""
5. nonlocal 关键字

nonlocal 关键字用于修改外部（但不在全局作用域中）函数的局部变量。在嵌套函数中，如果需要修改外层函数的局部变量，可以使用 nonlocal。
"""
def outer_function():
    x = 10  # 外部函数的局部变量

    def inner_function():
        nonlocal x  # 声明 x 是外部函数的局部变量
        x = 20  # 修改外层函数的局部变量

    inner_function()
    print(x)  # 输出: 20

outer_function()

# •    说明：nonlocal 使得内层函数能够修改外层函数的局部变量，而不是创建一个新的局部变量。