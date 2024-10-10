# 编写一个程序，使用 while 循环计算 1 到 100 之间所有整数的和。
# 思路提示：
#
# 	•	使用一个计数器 num 从 1 开始，每次增加 1，直到 num 达到 100。
# 	•	用一个变量 total 来保存累加的结果。

num = 1
total = 0

while num <= 100:
    total += num
    num += 1

print(f"1 到 100 之间所有整数的和是: {total}")

# 编写一个程序，要求用户输入一系列整数，直到用户输入 0 时停止，程序最终输出输入数字中的最大值。
#
# 思路提示：
#
# 	•	使用一个变量 max_num 来保存当前最大的数字。
# 	•	每次用户输入一个数字时，与 max_num 比较，更新 max_num。
# 	•	当用户输入 0 时，循环终止。

max_num = None

while True:
    num = int(input("请输入一个整数 (输入 0 结束): "))

    if num == 0:
        break
    if max_num is None or num > max_num:
        max_num = num

print(f"最大值是: {max_num}")

# 编写一个程序，生成一个 1 到 50 之间的随机整数，让用户猜测这个数字。用户最多有 5 次机会，程序会在每次猜测后告诉用户猜测的数字是大了还是小了。如果用户在 5 次内猜中，则显示“恭喜猜对了！”，否则显示正确的数字并提示“机会用完了”。
#
# 思路提示：
#
# 	•	使用 random.randint() 生成一个随机数。
# 	•	使用一个变量记录用户猜测的次数。
# 	•	每次用户猜错时，给出提示是“大了”还是“小了”。

import random

target = random.randint(1, 50)
attempts = 0
max_attempts = 5

while attempts < max_attempts:
    guess = int(input("请输入你猜的数字 (1-50): "))
    attempts += 1

    if guess == target:
        print("恭喜你，猜对了!")
        break
    elif guess < target:
        print("太小了!")
    else:
        print("太大了!")

if attempts == max_attempts:
    print(f"很遗憾，机会用完了，正确的数字是: {target}")

# 编写一个程序，使用 while 循环计算一个给定整数的阶乘。
#
# 思路提示：
#
# 	•	阶乘的定义是 n! = n × (n-1) × (n-2) × … × 1。
# 	•	通过 while 循环逐步计算乘积。

num = int(input("请输入一个整数: "))
factorial = 1
i = 1

while i <= num:
    factorial *= i
    i += 1

print(f"{num} 的阶乘是: {factorial}")

# 使用 while 循环打印 1 到 9 的乘法表。
#
# 思路提示：
#
# 	•	使用两个嵌套的 while 循环，一个循环控制行，另一个循环控制列。

i = 1

while i <= 9:
    j = 1
    while j <= i:
        print(f"{j} * {i} = {j * i}", end="\t")
        j += 1
    print()  # 换行
    i += 1