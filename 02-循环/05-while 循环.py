# while 循环是另一种循环控制结构，用于重复执行一段代码，直到指定的条件为 False 为止。

"""
基本语法
while 条件:
    # 循环体

条件：这是一个返回 True 或 False 的表达式。当条件为 True 时，执行循环体；当条件为 False 时，循环结束。
循环体：这是在条件为 True 时重复执行的代码。
"""

count = 1
while count <= 5:
    print(f"Count: {count}")
    count += 1

# 在这个例子中，while 循环会一直运行，直到 count 超过 5。每次循环，count 的值增加 1，直到条件 count <= 5 不再成立。

# 注意事项
# 	1.	避免无限循环：如果 while 循环的条件始终为 True，则循环将一直进行下去，可能导致程序卡死。要小心设计循环条件，确保有退出的条件。

while True:
    print("This is an infinite loop!")  # 无限循环

# 	2.	循环中的变量更新：在循环体中需要更新循环条件涉及的变量，否则可能导致死循环。

count = 1
while count <= 5:
    print(count)
    # 错误，变量没有更新，导致死循环

# while 循环中的 break 和 continue
#
# 	•	break：立即终止循环。
# 	•	continue：跳过当前循环的剩余部分，直接进入下一次循环。


count = 1
while count <= 5:
    print(f"Count: {count}")
    if count == 3:
        break  # 当 count 等于 3 时，退出循环
    count += 1

count = 0
while count < 5:
    count += 1
    if count == 3:
        continue  # 当 count 等于 3 时，跳过后续代码，直接进入下一个循环
    print(f"Count: {count}")

# 在这个例子中，当 count == 3 时，continue 会跳过该次循环的 print 语句。

# 使用 else 子句
#
# while 循环可以带一个 else 子句，当循环正常结束时（即条件变为 False 而退出循环），会执行 else 中的代码。如果是通过 break 退出循环，则 else 部分不会被执行。
"""
while 条件:
    条件为真时执行的代码
else:
    条件为假时执行的代码
"""

count = 1
while count <= 5:
    print(f"Count: {count}")
    count += 1
else:
    print("循环结束")

# 如果循环被 break 提前结束，则 else 语句不会执行。

