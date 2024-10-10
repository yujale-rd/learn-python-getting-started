# 在 Python 中，break 和 continue 是两种用于控制循环流程的语句，主要在循环体内使用，用于改变正常的循环执行流程。

"""
break 语句

break 语句用于立即退出当前所在的循环。无论循环是否已经完成所有的迭代，一旦遇到 break，循环都会终止，程序会继续执行循环后面的代码。
"""
# break 退出循环
for i in range(1, 6):
    if i == 3:
        break
    print(i)
print("循环结束")

# 在这个例子中，当 i == 3 时，break 语句执行，立即退出 for 循环。因此，只打印了 1 和 2，而循环后面的 “循环结束” 会被执行。

# break 在 while 循环中的使用

n = 1
while n <= 5:
    print(n)
    if n == 3:
        break
    n += 1
print("循环结束")

# 当 n == 3 时，break 语句执行，终止 while 循环，跳到循环之后的代码，打印 “循环结束”。

"""
continue 语句

continue 语句用于跳过当前循环中的剩余代码，并直接进入下一次循环迭代。它不会终止循环，只是跳过当前迭代的代码块。
"""

# continue 跳过当前迭代

for i in range(1, 6):
    if i == 3:
        continue
    print(i)

# 当 i == 3 时，continue 语句执行，跳过了打印 i 的那一行，并直接进入下一次循环。结果是 3 没有被打印出来，但循环继续进行。

# continue 在 while 循环中的使用

n = 0
while n < 5:
    n += 1
    if n == 3:
        continue
    print(n)
# 在这个例子中，当 n == 3 时，continue 语句跳过了 print(n) 语句，导致 3 没有被输出。循环继续运行，直到 n 达到 5。


"""
break 和 continue 的对比

    break：立即终止整个循环，跳出循环体。
    continue：仅跳过当前迭代，继续执行下一次循环。

使用场景

    break 常用于提前退出循环的场景，比如在搜索某个元素时，一旦找到就不需要继续搜索。
    continue 常用于跳过某些不符合条件的迭代，比如在处理数据时，需要跳过某些无效或不需要处理的数据项。
"""

numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num == 3:
        print(f"找到: {num}")
        break

for i in range(1, 6):
    if i % 2 == 0:  # 跳过偶数
        continue
    print(i)  # 只打印奇数