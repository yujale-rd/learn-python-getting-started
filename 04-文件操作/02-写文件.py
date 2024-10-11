# 在 Python 中，写文件通常使用 open() 函数，结合不同的模式，如写入模式 'w'、追加模式 'a'、以及二进制写入模式 'wb' 等。

# 基本写入操作
#
# open() 函数用来打开一个文件，返回一个文件对象。使用 write() 方法可以将内容写入文件。

"""
注意事项：

在写入文件时，要确保文件路径的正确性和文件名的合法性。
使用 with 语句管理文件操作可以自动处理文件的打开和关闭，是推荐的做法，特别是在处理文件时。
"""

#  使用 'w' 模式写文件
#
# 使用 'w' 模式时，如果文件不存在，会创建新文件；如果文件已存在，则会覆盖原有内容。

# 写入文本文件
with open('example.txt', 'w') as file:
    file.write("Hello, World!\n")
    file.write("This is a second line.\n")

# 注意：
#
# 'w' 模式会覆盖文件的原有内容。

# 使用 'a' 模式追加写入
#
# 使用 'a' 模式时，如果文件不存在，会创建新文件；如果文件已存在，则在文件末尾追加内容，而不覆盖原有内容。

# 追加内容到文件
with open('example.txt', 'a') as file:
    file.write("This is an appended line.\n")

# 写入多行数据
#
# 可以通过 writelines() 方法将一个字符串列表写入文件，每个元素作为文件中的一行。

lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open('example.txt', 'w') as file:
    file.writelines(lines)

# 写入二进制文件
#
# 对于非文本文件（如图像、音频等），需要使用二进制模式 'wb' 来写入文件。
data = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR'
with open('image.png', 'wb') as file:
    file.write(data)  # 写入二进制数据

# 使用 flush() 和 close()
#
# 文件操作后，系统会缓存写入内容。为了确保数据立即写入硬盘，你可以手动调用 flush() 方法或确保文件正确关闭。
with open('example.txt', 'w') as file:
    file.write("Some data.")
    file.flush()  # 强制刷新缓冲区，将数据写入硬盘
# 不过通常情况下，使用 with 语句会自动在块结束时关闭文件，确保内容被写入。

# 写入 JSON 数据
#
# 对于字典等结构化数据，可以使用 json 模块将其写入文件。

import json

data = {'name': 'Alice', 'age': 25, 'city': 'New York'}
with open('data.json', 'w') as file:
    json.dump(data, file)

# 写入 CSV 数据
#
# Python 的 csv 模块可以方便地写入 CSV 格式的数据。
import csv

data = [['Name', 'Age', 'City'], ['Alice', 25, 'New York'], ['Bob', 30, 'Los Angeles']]
with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)