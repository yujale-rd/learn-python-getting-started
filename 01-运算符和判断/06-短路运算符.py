# 短路运算（Short-circuit evaluation）指的是在逻辑运算中，如果运算符左侧的表达式已经能够决定最终的结果，那么右侧的表达式将不再计算。
# Python 中的逻辑运算符 and 和 or 都会进行短路运算。

# and 短路运算
# 在 and 运算中，如果左侧的条件为 False，则整体结果已经为 False，因此不会再计算右侧的表达式。
# 规则:
# and 运算符在遇到第一个 False 时，立即返回 False，并跳过后续的条件。

def is_true():
    print("is_true 被调用")
    return True


def is_false():
    print("is_false 被调用")
    return False


print(is_false() and is_true())
# 输出:
# is_false 被调用
# False
# 解释：第一个条件为 False，短路后不再执行 is_true 函数

# or 短路运算
# 在 or 运算中，如果左侧的条件为 True，则整体结果已经为 True，因此不会再计算右侧的表达式。
# 规则:
# or 运算符在遇到第一个 True 时，立即返回 True，并跳过后续的条件。

print(is_true() or is_false())
# 输出:
# is_true 被调用
# True
# 解释：第一个条件为 True，短路后不再执行 is_false 函数

# 短路运算的典型应用
# 1. 避免不必要的计算
# 短路运算可以提高代码效率，避免一些不必要的计算。

x = 0
y = 10
# 如果 x 为 0，跳过除法计算，避免错误
print(x != 0 and y / x > 1)  # 输出: False

# 在上例中，x != 0 为 False，因此 and 运算短路，不会执行 y / x，从而避免了除零错误。

# 2. 默认值的使用
#
# 短路运算可以用于为变量提供默认值。

name = None
default_name = "Guest"
# 如果 name 为空，则使用默认值
print(name or default_name)  # 输出: Guest
# 这里，如果 name 为 None 或其他 “假值”（如 0 或空字符串），or 运算会短路并返回 default_name。

#  多条件判断
# 短路运算可以在条件判断中优化代码，避免多余的判断。

user = None
age = 20

# 如果 user 存在并且年龄大于 18，则允许访问
if user and age > 18:
    print("允许访问")
else:
    print("拒绝访问")
# 输出: 拒绝访问
# 解释：user 为 None，第一个条件为 False，短路不再检查 age > 18
