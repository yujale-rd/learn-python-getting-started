# 在 Python 中，csv 模块用于读取和写入 CSV（逗号分隔值）文件。这种文件格式通常用于存储表格数据，如电子表格或数据库导出。csv 模块提供了简单且强大的工具来处理 CSV 文件，支持读取、写入、更新和删除等操作。

# 读取 CSV 文件
#
# 可以使用 csv.reader() 来读取 CSV 文件，将文件中的每一行读取为一个列表。


import csv

# 打开 CSV 文件
with open('data.csv', 'r') as file:
    reader = csv.reader(file)

    # 读取 CSV 文件中的内容
    for row in reader:
        print(row)

# 说明：
#
# 	•	每一行将会被读取为一个列表，列表中的每个元素对应一列的数据。
# 	•	csv.reader() 会自动处理文件中的换行符和逗号等分隔符。

# 写入 CSV 文件
#
# 可以使用 csv.writer() 来写入 CSV 文件。
import csv

# 打开 CSV 文件
with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    # 写入一行表头
    writer.writerow(['name', 'age', 'city'])

    # 写入多行数据
    writer.writerows([
        ['Alice', 30, 'New York'],
        ['Bob', 25, 'Los Angeles'],
        ['Charlie', 35, 'Chicago']
    ])

# 说明：
#
# 	•	csv.writer() 用于写入 CSV 文件，writerow() 方法写入一行数据，writerows() 方法写入多行数据。
# 	•	参数 newline='' 防止写入多余的空行。

# 使用字典形式读写 CSV 文件
#
# 可以使用 csv.DictReader() 和 csv.DictWriter() 以字典形式读写 CSV 文件，字典的键是 CSV 文件的列标题，值是每一列的数据。

# 读取 CSV 文件为字典
import csv

with open('data.csv', 'r') as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row)  # 每一行是一个字典

# 写入字典形式的数据到 CSV 文件
import csv

# 数据列表，其中每个元素是一个字典
data = [
    {'name': 'Alice', 'age': 30, 'city': 'New York'},
    {'name': 'Bob', 'age': 25, 'city': 'Los Angeles'},
    {'name': 'Charlie', 'age': 35, 'city': 'Chicago'}
]

with open('output.csv', 'w', newline='') as file:
    fieldnames = ['name', 'age', 'city']
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()  # 写入表头
    writer.writerows(data)  # 写入数据

# CSV 文件的常见操作
#
# 设置分隔符
#
# 默认情况下，CSV 文件使用逗号 , 作为分隔符。如果需要使用其他分隔符（如制表符 \t 或分号 ;），可以指定 delimiter 参数。
with open('data.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')  # 使用分号作为分隔符

# 处理 CSV 文件中的引号
#
# csv 模块支持不同的引号处理方式，可以通过 quotechar 参数自定义引号字符。
with open('data.csv', 'r') as file:
    reader = csv.reader(file, quotechar='"')
# 忽略
with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        if any(row):  # 忽略空行
            print(row)