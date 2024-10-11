# 任务：给定一个 CSV 文件 data.csv，文件中包含多行数据。请编写 Python 程序，读取文件中的所有数据并打印出来。
#
# 思路：
#
# 	•	使用内置的 csv 模块。
# 	•	使用 csv.reader 逐行读取数据。
import csv

# 打开 CSV 文件
with open('data.csv', mode='r', newline='') as file:
    reader = csv.reader(file)

    # 逐行读取并打印
    for row in reader:
        print(row)

# 任务：给定一个列表，列表包含一些人的姓名和年龄，例如 [['Alice', 30], ['Bob', 25], ['Charlie', 35]]。将这些数据写入一个新的 CSV 文件 people.csv 中，并设置列标题为 “Name” 和 “Age”。
#
# 思路：
#
# 	•	使用 csv.writer 写入文件。
# 	•	首先写入列标题，然后逐行写入数据。

import csv

data = [['Alice', 30], ['Bob', 25], ['Charlie', 35]]

# 打开 CSV 文件，写入数据
with open('people.csv', mode='w', newline='') as file:
    writer = csv.writer(file)

    # 写入列标题
    writer.writerow(['Name', 'Age'])

    # 写入数据
    writer.writerows(data)

# 任务：给定一个 CSV 文件 scores.csv，其中包含学生的姓名和考试成绩。请读取这些数据，并计算所有学生的平均成绩。
#
# 思路：
#
# 	•	使用 csv.reader 读取文件。
# 	•	提取成绩列并计算平均值。

import csv

# 读取 CSV 文件并计算平均分
with open('scores.csv', mode='r', newline='') as file:
    reader = csv.reader(file)

    # 跳过标题行
    next(reader)

    # 初始化总分和计数
    total_score = 0
    count = 0

    # 遍历每行，计算总分
    for row in reader:
        score = int(row[1])  # 假设成绩在第二列
        total_score += score
        count += 1

# 计算平均分
average_score = total_score / count
print(f"Average score: {average_score}")

# 任务：给定一个 CSV 文件 employees.csv，其中包含员工的姓名、年龄和职位等信息。请筛选出所有年龄大于 30 岁的员工，并将这些员工的信息保存到新的 CSV 文件 filtered_employees.csv 中。
#
# 思路：
#
# 	•	读取 CSV 文件，使用条件筛选数据。
# 	•	将筛选后的数据写入新的 CSV 文件。

import csv

# 打开原始 CSV 文件和目标 CSV 文件
with open('employees.csv', mode='r', newline='') as infile, open('filtered_employees.csv', mode='w',
                                                                 newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    # 读取并写入标题行
    headers = next(reader)
    writer.writerow(headers)

    # 筛选并写入符合条件的行
    for row in reader:
        age = int(row[1])  # 假设年龄在第二列
        if age > 30:
            writer.writerow(row)

# 任务：给定一个 CSV 文件 sales.csv，其中包含每月的销售数据。请使用 pandas 读取数据，筛选出销售额大于 10000 的月份，并将这些数据保存到新的 CSV 文件 high_sales.csv 中。
#
# 思路：
#
# 	•	使用 pandas 读取 CSV 文件。
# 	•	使用条件筛选数据。
# 	•	将筛选结果保存为新的 CSV 文件。
import pandas as pd

# 读取 CSV 文件
df = pd.read_csv('sales.csv')

# 筛选销售额大于 10000 的月份
filtered_df = df[df['Sales'] > 10000]

# 将筛选结果保存到新的 CSV 文件
filtered_df.to_csv('high_sales.csv', index=False)

# 任务：给定一个 CSV 文件 data.csv，其中包含一些人的姓名和年龄。请向该文件追加新的数据，如 ['Dave', 28]。
#
# 思路：
#
# 	•	使用 csv.writer 的追加模式 a 打开文件。
# 	•	使用 writerow() 方法追加一行数据。

import csv

# 追加新数据到 CSV 文件
with open('data.csv', mode='a', newline='') as file:
    writer = csv.writer(file)

    # 追加一行
    writer.writerow(['Dave', 28])

# 任务：给定一个 CSV 文件 products.csv，其中包含产品的名称和价格。请删除所有价格低于 50 的产品，并将结果保存到新的 CSV 文件 filtered_products.csv 中。
#
# 思路：
#
# 	•	使用 csv.reader 读取原始文件。
# 	•	使用 csv.writer 写入新的文件。
# 	•	筛选符合条件的数据。

import csv

# 打开原始 CSV 文件和目标 CSV 文件
with open('products.csv', mode='r', newline='') as infile, open('filtered_products.csv', mode='w',
                                                                newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    # 读取并写入标题行
    headers = next(reader)
    writer.writerow(headers)

    # 筛选并写入符合条件的行
    for row in reader:
        price = float(row[1])  # 假设价格在第二列
        if price >= 50:
            writer.writerow(row)