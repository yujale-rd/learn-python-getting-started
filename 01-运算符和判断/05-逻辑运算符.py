# 逻辑运算符用于对布尔值进行逻辑运算，通常用于条件判断、循环控制等场景中。
# 逻辑运算符包括：and、or 和 not。这些运算符可以结合比较运算符使用，形成复杂的逻辑条件。


# and 运算符（与运算）
# 作用: 当所有条件都为 True 时，返回 True，否则返回 False。
# 语法: 条件1 and 条件2
# 逻辑: 两个条件都为真时，整个表达式才为真，否则为假。

a = 5
b = 10
print(a > 0 and b > 0)  # 输出: True，两个条件都为真
print(a > 0 and b < 0)  # 输出: False，一个条件为假

# or 运算符（或运算）
#
# 作用: 只要有一个条件为 True，返回 True；当所有条件都为 False 时，返回 False。
# 语法: 条件1 or 条件2
# 逻辑: 只要有一个条件为真，整个表达式就为真。

a = 5
b = 10
print(a > 0 or b < 0)  # 输出: True，第一个条件为真
print(a < 0 or b < 0)  # 输出: False，两个条件都为假

# not 运算符（非运算）
#
# 作用: 对条件取反，如果条件为 True，返回 False；如果条件为 False，返回 True。
# 语法: not 条件
# 逻辑: 取布尔值的反值。

a = True
b = False
print(not a)  # 输出: False，取反
print(not b)  # 输出: True，取反

# 逻辑运算符的应用

# 结合条件语句使用

# 在 if 语句或 while 循环中，逻辑运算符常用于合并多个条件。

age = 20
income = 4000
if age > 18 and income > 3000:
    print("符合条件")
else:
    print("不符合条件")

# 短路运算
#
# and 短路：如果第一个条件为 False，则不再计算第二个条件，因为整个表达式已经确定为 False。
# or 短路：如果第一个条件为 True，则不再计算第二个条件，因为整个表达式已经确定为 True。


a = 0
b = 5
print(a != 0 and b / a > 1)  # 不会报错，短路运算，第一个条件为 False，跳过除法
print(a == 0 or b / a > 1)   # 不会报错，短路运算，第一个条件为 True，跳过除法

# 结合比较运算符
#
# 可以通过逻辑运算符结合多个比较运算符，构建更复杂的条件判断。

x = 15
print(x > 10 and x < 20)  # 输出: True，x 在 10 和 20 之间
print(x < 5 or x > 10)    # 输出: True，x 大于 10

# 判断空值和非空值
#
# 在 Python 中，None、0、空字符串 "" 等被视为 False，可以用逻辑运算符直接进行判断。

a = None
b = "Hello"
print(not a)    # 输出: True，a 是空值
print(a or b)   # 输出: Hello，a 为 False，返回 b 的值

# 逻辑运算符优先级
#
# 在 Python 中，逻辑运算符的优先级如下（从高到低）：
#
# 	1.	not
# 	2.	and
# 	3.	or
#
# 如果多个逻辑运算符组合在一起，Python 会按照上述优先级顺序进行计算。可以通过使用括号来控制运算顺序。

