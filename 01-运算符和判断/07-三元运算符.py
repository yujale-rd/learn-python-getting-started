# 三元运算符是一种简洁的条件表达式语法，允许在一行代码中根据条件返回不同的结果
# 通过用于简单的条件判断和赋值操作，类似于 if-else 语句，但是语法简洁

# 基本语法
# 格式： value_if_true if condition else value_if_false
# condition: 条件表达式，结果为 True 或 False。
# value_if_true: 当条件为 True 时返回的值。
# value_if_false: 当条件为 False 时返回的值。


# 简单条件判断

age = 20
status = "成年人" if age >= 18 else "未成年人"
print(status)  # 输出: 成年人

# 在这个示例中，age 的值是 20，满足条件 age >= 18，因此返回 成年人。


# 嵌套三元运算符
# 可以在三元运算符中嵌套使用，但可读性会降低。尽量避免过度嵌套，复杂条件推荐使用常规 if-else 语句。

score = 85
result = "优秀" if score >= 90 else ("及格" if score >= 60 else "不及格")
print(result)  # 输出: 及格

# 在此示例中，根据 score 值返回不同的结果。

# 结合逻辑运算符
# 三元运算符可以与逻辑运算符结合使用，实现更复杂的条件判断。

x = 5
y = 10
max_value = x if x > y else y
print(max_value)  # 输出: 10

# 在这个例子中，使用三元运算符计算两个值中的最大值。

# 注意事项
#
# 简洁性：三元运算符适用于简单的条件判断，代码更为简洁。但在条件复杂的情况下，建议使用标准的 if-else 结构来提高代码的可读性。
# 嵌套问题：嵌套三元运算符会使代码难以阅读和维护，尽量避免。
# 返回值：三元运算符会返回一个值，你可以将它赋值给变量或者直接用于表达式。

