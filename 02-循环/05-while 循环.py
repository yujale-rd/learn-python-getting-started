"""
while 循环是一种灵活的控制流结构，用于在条件为 True 时反复执行代码块。它特别适合在需要基于某个条件动态控制循环次数的场景中使用。


基本语法
while 条件:
    # 循环体

	•	条件：是一个布尔表达式。当其值为 True 时，执行循环体；当为 False 时，退出循环。
	•	循环体：条件为 True 时，重复执行的代码块。
"""

count = 1
while count <= 5:
    print(f"Count: {count}")
    count += 1

"""
2. 注意事项

(1) 避免无限循环

如果循环条件始终为 True 且没有退出逻辑，while 循环将进入死循环状态。
while True:
    print("This is an infinite loop!")  # 无限循环

"""

"""
(2) 变量更新

在循环体内应合理更新循环条件涉及的变量，否则可能导致死循环。
"""
count = 1
while count <= 5:
    print(count)
    # 错误，变量没有更新，导致死循环

"""
3. while 循环中的控制语句

(1) break：终止循环

break 用于立即退出当前循环，跳到循环后面的代码。
"""
count = 1
while count <= 5:
    print(f"Count: {count}")
    if count == 3:
        break  # 当 count 等于 3 时，退出循环
    count += 1

"""
(2) continue：跳过当前迭代

continue 用于跳过当前循环剩余的代码，直接进入下一次循环。
"""
count = 0
while count < 5:
    count += 1
    if count == 3:
        continue  # 当 count 等于 3 时，跳过后续代码，直接进入下一个循环
    print(f"Count: {count}")

# 在这个例子中，当 count == 3 时，continue 会跳过该次循环的 print 语句。
"""
4. 使用 else 子句

while 循环支持 else 子句。当循环正常结束时（条件为 False 退出），会执行 else 块；如果使用 break 退出循环，则不会执行 else 块。

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


#简单用户登录验证
password = "12345"
attempts = 3

while attempts > 0:
    user_input = input("请输入密码：")
    if user_input == password:
        print("密码正确，欢迎！")
        break
    else:
        attempts -= 1
        print(f"密码错误，您还有 {attempts} 次机会。")
else:
    print("尝试次数过多，账户已锁定。")

"""
6. 适用场景
	1.	基于条件的动态循环：例如读取用户输入，直到满足某个条件。
	2.	无限循环：配合 break 实现，如服务器监听。
	3.	实时监控状态：如检查任务完成状态或等待外部事件。
"""