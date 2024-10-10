# 编写一个程序，使用 for 循环计算从 1 到 100 的整数之和。

# 思路
#
# 	•	使用 range(1, 101) 来生成 1 到 100 的整数。
# 	•	初始化一个变量 total，用来存储和的值。
# 	•	在循环中，依次将每个数加到 total 中。

total = 0
for i in range(1, 101):
    total += i
print(f"1 到 100 的和是: {total}")



# 给定一个整数列表 numbers，使用 for 循环找出列表中的最大值。
# 思路
#
# 	•	初始化一个变量 max_value，将其设置为列表的第一个元素。
# 	•	遍历列表，比较当前元素和 max_value，如果当前元素更大，则更新 max_value。

numbers = [10, 3, 45, 67, 23, 12]
max_value = numbers[0]

for num in numbers:
    if num > max_value:
        max_value = num

print(f"列表中的最大值是: {max_value}")

# 编写一个程序，使用 for 循环打印 1 到 9 的乘法表。

# 思路
#
# 	•	使用嵌套的 for 循环。外层循环控制行，内层循环控制列。
# 	•	使用格式化输出结果。

for i in range(1, 10):
    for j in range(1, 10):
        print(f'{i} * {j} = {i * j}', end='\t')
    print()  # 换行

# 编写一个程序，输入一个字符串，使用 for 循环统计该字符串中出现的元音字母（a, e, i, o, u）的次数。
# 思路
#
# 	•	初始化一个计数器 count。
# 	•	遍历字符串的每个字符，如果是元音，则增加计数器。

text = "Hello World"
vowels = "aeiouAEIOU"
count = 0

for char in text:
    if char in vowels:
        count += 1

print(f"字符串中的元音字母数量是: {count}")


# 给定一个列表 lst，使用 for 循环将其反转，并输出新的反转列表。
# 	•	使用倒序遍历原列表，将每个元素添加到新的列表中。

lst = [1, 2, 3, 4, 5]
reversed_list = []

for i in range(len(lst)-1, -1, -1):
    reversed_list.append(lst[i])

print(f"反转后的列表是: {reversed_list}")

# 给定一个整数列表 numbers，使用 for 循环筛选出其中的偶数，并将其存储到一个新列表中。

# 思路
#
# 	•	遍历列表，使用条件判断检查每个数字是否为偶数。
# 	•	将偶数添加到新列表中。
numbers = [10, 3, 45, 67, 22, 12]
even_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

print(f"偶数列表: {even_numbers}")


# 编写一个程序，使用 for 循环输出一个星形图案。

# 思路
#
# 	•	使用一个 for 循环，逐行增加星号的数量。

for i in range(1, 6):
    print('*' * i)


# 给定一个字典 person，使用 for 循环将字典中的键值对转换为格式化的字符串输出。
# 思路
#
# 	•	使用 for 循环遍历字典的键和值。
# 	•	使用格式化字符串输出结果。
person = {'name': 'Alice', 'age': 25, 'city': 'New York'}

for key, value in person.items():
    print(f"{key}: {value}")


# 统计列表中每个数字出现的次数。
# 思路
#
# 	•	使用一个空字典 count_dict 来存储每个数字的出现次数。
# 	•	遍历列表中的每个数字，更新字典中的计数。

numbers = [1, 2, 2, 3, 4, 4, 4, 5]
count_dict = {}

for num in numbers:
    if num in count_dict:
        count_dict[num] += 1
    else:
        count_dict[num] = 1

print(f"数字出现的次数: {count_dict}")