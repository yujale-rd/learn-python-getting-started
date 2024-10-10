"""
条件表达式在 Python 中用于根据某个条件的真假执行不同的代码块。条件表达式可以是任何返回布尔值的表达式，通常包括比较运算符和逻辑运算符，来检查并处理程序中的不同情景。
通常包括比较运算符，如==, !=, <, >, <=, >=。
也可以使用逻辑运算符and, or, not来组合条件。
if 语句是条件表达式的主要实现方式。根据条件的不同，可以使用 if、elif 和 else 来组织程序的执行流程。


if condition:
    # 当 condition 为 True 时执行的代码块
elif another_condition:
    # 当另一个 condition 为 True 时执行的代码块
else:
    # 当上面所有条件都为 False 时执行的代码块

- condition: 这是一个布尔表达式，当其值为 True 时，执行 if 之后的代码块。
- elif: 可以有多个 elif，当上面的条件不成立时，逐一检查 elif 的条件。
- else: 如果所有 if 和 elif 的条件都为 False，就执行 else 的代码块。else 是可选的。

"""

# 基本 if 语句

age = 20
if age >= 18:
    print("成年人")

# 在上面的示例中，当 age 大于等于 18 时，会输出 “成年人”。

# if-else 语句

age = 15
if age >= 18:
    print("成年人")
else:
    print("未成年人")

# 在这个例子中，如果 age 小于 18，则输出 “未成年人”。

# if-elif-else 语句

score = 85
if score >= 90:
    print("优秀")
elif score >= 75:
    print("良好")
elif score >= 60:
    print("及格")
else:
    print("不及格")

# 根据 score 的值，程序会输出不同的成绩评价。


# 多个条件组合

age = 25
if age >= 18 and age < 60:
    print("成年人")
elif age >= 60:
    print("老年人")
else:
    print("未成年人")
# 通过使用 and 和 or 等逻辑运算符，可以组合多个条件进行判断。



# 嵌套 if 语句
# 条件语句可以嵌套使用，但建议在复杂情况下，尽量避免过多嵌套，以保持代码的清晰和易读性。

age = 65
if age >= 18:
    if age >= 60:
        print("老年人")
    else:
        print("成年人")
else:
    print("未成年人")

# 注意事项
#
# 	1.	缩进：Python 依赖缩进来区分代码块，if 语句的代码块需要正确缩进，通常是 4 个空格。
# 	2.	空 if 语句：如果暂时不想执行 if 语句中的代码，可以使用 pass 作为占位符。

if age >= 18:
    pass  # 占位符，表示暂时不执行任何操作
# 	3.	避免复杂嵌套：尽量避免嵌套过多的 if-else 语句，尤其是在条件复杂时，建议使用 elif 来简化逻辑。

# 注意事项
# 代码缩进
# 在 Python 中，缩进 是强制性的，它用于表示代码块的范围。
# if、elif、else 后面的代码必须缩进（通常是 四个空格），缩进不一致会导致语法错误。
# 缩进不正确会导致 IndentationError。

age = 20
if age >= 18:
    print("成年人")  # 正确缩进
else:
    print("未成年人")

# 条件顺序
#
# Python 的 if 语句是从上到下按顺序执行条件的，一旦找到满足条件的语句，后面的 elif 或 else 不会再执行。
# 确保条件按照正确的逻辑顺序排列，否则可能会得到意料之外的结果。

score = 85
if score >= 60:
    print("及格")  # 条件满足后，不再检查后续条件
elif score >= 75:
    print("良好")  # 永远不会执行

# 逻辑表达式
#
# 	可以通过 逻辑运算符 (and、or、not) 来组合多个条件，形成复杂的逻辑判断。
age = 20
has_license = True

if age >= 18 and has_license:
    print("可以驾驶")
else:
    print("不符合驾驶条件")

# 	and 表示两个条件都需要为 True，or 表示只要其中一个条件为 True 即可。

# 避免冗余判断
#
# 在 if-elif-else 结构中，避免不必要的条件判断。

if age >= 18:
    print("成年人")
elif age < 18:
    print("未成年人")  # 冗余判断，已经是 `else` 的情况

# 使用括号提高可读性
#
# 	•	对于复杂的逻辑判断，使用括号明确逻辑优先级，避免歧义。

if (age >= 18 and age < 60) or (has_license and age >= 16):
    print("可以驾驶")

# 空 if 语句占位符
# 	•	如果暂时不打算执行 if 语句中的代码，可以使用 pass 占位。

if age >= 18:
    pass  # 占位符，不执行任何操作



