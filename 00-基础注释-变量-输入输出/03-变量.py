# 关键字（keywords）
"""
1. 关键字（Keywords）

定义与作用：
	•	关键字是 Python 语言中预定义的保留字，它们具有特定的功能或意义，并且不能用作变量名、函数名等标识符。
	•	关键字是构成 Python 语法结构的基本元素，用来表示控制流、定义函数与类、处理异常等。


常见的关键字：
	•	条件语句：if, else, elif
	•	循环控制：for, while
	•	函数与类定义：def, class
	•	异常处理：try, except, finally
	•	其他：print（虽然 print 现在是一个内置函数，但在早期 Python 版本中它是一个语句）
"""
age = 10
if age > 18:
    print("Adult")
else:
    print("Not an adult")
# 标识符(Identifiers)

"""
2. 标识符（Identifiers）

定义与命名规则：
	•	标识符是程序员自定义的名称，用来表示变量、函数、类、模块等。
	•	命名规则：
	•	只能由字母、数字和下划线（_）组成。
	•	不能以数字开头。
	•	不能是关键字。
	•	区分大小写，例如 myVar 和 myvar 是不同的标识符。

常见的命名风格：
	•	变量与函数名：小写字母，并用下划线分隔（例如 total_amount, calculate_price）。
	•	类名：使用大驼峰命名法（例如 UserProfile, ProductManager）。
	•	模块名：通常使用小写字母和下划线（例如 user_auth.py）。

注意：

- 标识符命名的推荐风格：Python 社区推荐遵循 PEP 8 风格指南。例如：
- 变量和函数名应使用小写字母，并以 _ 分隔词（如 total_amount）。
- 类名应使用大驼峰命名法（如 PersonProfile）。

"""

age = 25              # 变量名
def calculate_age():   # 函数名
    pass
class UserProfile:     # 类名
    pass

# 变量（Variables）

"""
3. 变量（Variables）

定义与特性：
	•	变量是程序用来存储数据的容器，可以随时更改其值。
	•	在 Python 中，变量是动态类型的，意味着你不需要预先声明变量的类型，Python 会根据赋值自动推断变量类型。

变量的使用：
	•	变量在使用之前必须先赋值。
	•	变量的类型是可变的，类型会随着赋值的变化而改变。
"""
age = 25
name = "Alice"
is_active = True

x = 10       # 整数类型
x = "hello"  # 变量类型变为字符串类型
print(x)     # 输出：hello

# 常量(Constants)

"""
定义与特性：
	•	常量是程序中不应修改的值，它通常在整个程序中保持不变。
	•	Python 并没有专门的常量类型或语法（不像 C++ 的 const 或 Java 的 final），但是开发者通常通过约定使用全大写字母命名常量，以表示它们的不可变性。

常量的命名规则：
	•	使用全大写字母并用下划线分隔（例如 PI = 3.14159）。
	•	Python 并不会强制常量不可变，但它是一种约定俗成的规则。
"""

PI = 3.14159
MAX_CONNECTIONS = 100
