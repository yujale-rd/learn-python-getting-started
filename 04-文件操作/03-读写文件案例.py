# 读取文件并输出每一行
#
# 编写一个程序，读取一个文本文件 example.txt，并将文件中的每一行内容输出到控制台。
#
# 解答思路：
# 使用 open() 函数打开文件，使用 for 循环逐行读取内容，并打印出来。

# 读取文件并输出每一行
with open('example.txt', 'r') as file:
    for line in file:
        print(line.strip())  # strip() 去除每行末尾的换行符

# 统计文件中的单词数
#
# 要求：
# 读取一个文本文件，并统计文件中出现的总单词数。
#
# 解答思路：
#
# 	•	使用 read() 方法一次性读取文件内容。
# 	•	使用 split() 方法将文本按空格拆分为单词列表，然后统计单词数量。

# 统计文件中的单词数
with open('example.txt', 'r') as file:
    content = file.read()  # 读取整个文件
    words = content.split()  # 按空格拆分为单词列表
    print(f"Total words: {len(words)}")

# 将用户输入写入文件
#
# 要求：
# 编写一个程序，要求用户输入几行文本，将这些输入写入到一个新文件 output.txt 中。
#
# 解答思路：
#
# 	•	使用 input() 函数让用户输入多行内容。
# 	•	将用户输入的内容写入文件中，直到用户输入结束（例如输入空行时结束）。

# 将用户输入写入文件
with open('output.txt', 'w') as file:
    while True:
        user_input = input("Enter text (or just press Enter to stop): ")
        if not user_input:
            break
        file.write(user_input + '\n')  # 每次输入一行，写入文件

# 文件复制
#
# 要求：
# 编写一个程序，将一个文件 source.txt 的内容复制到另一个文件 destination.txt 中。
#
# 解答思路：
#
# 	•	使用 open() 函数以读模式打开源文件，以写模式打开目标文件。
# 	•	使用 read() 方法读取源文件内容，并将其写入目标文件。

# 文件复制
with open('source.txt', 'r') as source_file:
    content = source_file.read()  # 读取源文件内容

with open('destination.txt', 'w') as destination_file:
    destination_file.write(content)  # 将内容写入目标文件

# 读取 CSV 文件并计算总和
#
# 要求：
# 编写一个程序，读取一个 CSV 文件，假设其中一列是数值，计算这些数值的总和。例如，data.csv 文件的内容为：

"""
Item,Price
Apple,1.2
Banana,0.8
Orange,1.5
"""
# 解答思路：
#
# 	•	使用 csv 模块读取 CSV 文件。
# 	•	遍历每一行，将数值列的数据累加。

import csv

# 读取 CSV 文件并计算数值总和
total = 0
with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # 跳过标题行
    for row in reader:
        total += float(row[1])  # 累加价格列的数值

print(f"Total price: {total}")

#  统计每个字符出现的次数
#
# 要求：
# 编写一个程序，读取一个文件中的内容，统计文件中每个字符出现的次数，并将统计结果写入到另一个文件 char_count.txt 中。
#
# 解答思路：
#
# 	•	使用 read() 方法读取文件的全部内容。
# 	•	使用字典统计每个字符出现的次数。
# 	•	将统计结果写入新文件。

# 统计文件中每个字符出现的次数
char_count = {}

with open('example.txt', 'r') as file:
    content = file.read()  # 读取文件内容
    for char in content:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

# 将统计结果写入到新文件
with open('char_count.txt', 'w') as file:
    for char, count in char_count.items():
        file.write(f"{char}: {count}\n")

# 查找文件中的最长单词
#
# 要求：
# 编写一个程序，读取一个文本文件，找出其中最长的单词，并输出该单词及其长度。
#
# 解答思路：
#
# 	•	读取文件内容，将其拆分为单词列表。
# 	•	遍历列表，找出最长的单词。

# 查找文件中的最长单词
longest_word = ""
with open('example.txt', 'r') as file:
    content = file.read()
    words = content.split()  # 将内容按空格拆分成单词列表

    for word in words:
        if len(word) > len(longest_word):
            longest_word = word

print(f"Longest word: {longest_word}, Length: {len(longest_word)}")