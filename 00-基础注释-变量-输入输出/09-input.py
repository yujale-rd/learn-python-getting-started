# input() 函数用于从用户处获取输入。它会暂停程序执行，直到用户输入数据并按下回车键。
# input() 函数返回的始终是字符串类型，即使用户输入的是数字，也需要手动进行类型转换。

user_input = input("Please enter your name: ")
print(f"Hello, {user_input}!")

# 	当程序运行时，它会提示用户输入名字，用户输入后程序会继续执行，并将输入的值存储在变量 user_input 中。



# 输入类型转换
# 因为 input() 返回的总是字符串，有时需要手动将输入转换为其他类型（如整型或浮点型）。
#
# 将输入转换为整数 (int)

age = int(input("Please enter your age: "))
print(f"Next year, you will be {age + 1} years old.")

# 将输入转换为浮点数 (float)
price = float(input("Please enter the price: "))
print(f"The price with tax is {price * 1.1:.2f}.")

# 捕获异常
#
# 如果用户输入无法转换为指定类型（如输入文本而要求整数），会产生 ValueError 异常。因此，在输入转换时，可以使用 try-except 块来处理错误。

try:
    number = int(input("Please enter a number: "))
    print(f"Your number is {number}.")
except ValueError:
    print("That's not a valid number!")


# 3. 输入提示清晰

# 为了避免用户输入错误，提供清晰的提示信息非常重要。提示应说明预期的输入类型和要求。
number = input("Enter a number between 1 and 10: ")
# 4. 输入限制和验证
#
# 你可以对输入的数据进行验证或限制。例如，限制输入的长度、数据范围等。
#
# 	•	限制输入长度：

name = input("Please enter your name (max 10 characters): ")
if len(name) > 10:
    print("Name is too long! Please enter up to 10 characters.")
# 	•	限制输入范围：
try:
    number = int(input("Enter a number between 1 and 10: "))
    if 1 <= number <= 10:
        print(f"Great! You entered {number}.")
    else:
        print("The number is out of the allowed range!")
except ValueError:
    print("That's not a valid number!")

# 5. 强制输入格式
#
# 如果需要用户输入满足特定格式的数据，可以添加检查逻辑。例如，要求输入特定的日期格式。

date = input("Enter a date in YYYY-MM-DD format: ")
if len(date) == 10 and date[4] == '-' and date[7] == '-':
    print(f"The entered date is {date}.")
else:
    print("Invalid date format!")

# 6. 多次输入
#
# 在某些情况下，可能需要让用户重新输入直到满足要求。可以使用 while 循环实现反复询问。
while True:
    user_input = input("Please enter a valid number: ")
    try:
        num = int(user_input)
        break  # 输入正确，跳出循环
    except ValueError:
        print("That's not a valid number. Please try again.")
# 	•	空输入处理：避免空输入或误输入。
# 	•	异常处理：通过 try...except 防止非预期类型的数据导致程序崩溃。
# 	•	清晰的输入提示：提供明确的输入指示，告知用户应该输入什么。
# 	•	输入限制与验证：根据需求对输入的长度、范围或格式进行限制和检查。