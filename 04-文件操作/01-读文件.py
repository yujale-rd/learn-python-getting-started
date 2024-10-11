# # 在 Python 中，读取文件主要通过内置的 open() 函数和文件对象的方法来完成。常用的方法有 read(), readline(), 和 readlines()，分别用于读取整个文件、读取单行和读取所有行。
# 使用 open() 函数打开文件，指定文件名和模式。

"""
read()：一次性读取整个文件，适合小文件。
readline()：逐行读取，适合处理较大文件。
readlines()：读取所有行，返回列表。
文件迭代：对文件对象进行逐行迭代是一种 Pythonic 的方式。
二进制读取：对于非文本文件，使用 'rb' 模式。


注意事项
在文件路径前加上 r（如 r'path\to\file.txt'），以避免路径中的反斜杠被转义。
使用 with 语句可以确保文件正确关闭，避免资源泄漏。
在处理大文件时，逐行读取（readline() 或 for line in file）比一次性读取（read()）更节省内存。
"""


# read()：一次性读取整个文件

# read() 方法将文件的所有内容作为一个字符串返回，适用于读取小型文件。

# 使用 'r' 模式打开文件，即只读模式
with open('example.txt', 'r') as file:
    content = file.read()  # 一次性读取整个文件
    print(content)

# 指定读取大小
#
# 你也可以在 read() 中传入一个参数，指定要读取的字符数。

with open('example.txt', 'r') as file:
    content = file.read(10)  # 读取前 10 个字符
    print(content)

# readline()：逐行读取
#
# readline() 方法每次读取文件的一行，适合处理较大文件或只需要逐行读取的情况。

with open('example.txt', 'r') as file:
    line = file.readline()
    while line:
        print(line, end='')  # 每次读取一行并输出
        line = file.readline()  # 继续读取下一行

# readlines()：读取所有行，返回列表
#
# readlines() 方法将文件的每一行作为一个元素存入列表，并返回该列表。

with open('example.txt', 'r') as file:
    lines = file.readlines()  # 读取所有行并存为列表
    for line in lines:
        print(line, end='')

# 逐行迭代读取
#
# Python 提供了更加 Pythonic 的方式来逐行读取文件，直接对文件对象进行迭代：

with open('example.txt', 'r') as file:
    for line in file:
        print(line, end='')

# 读取二进制文件
#
# 对于非文本文件（如图片、音频等），需要以二进制模式打开文件。使用 'rb' 模式。
with open('image.png', 'rb') as file:
    data = file.read()  # 读取二进制文件的内容

# 文件指针操作
#
# 当你读取文件时，文件指针会指向文件中的某个位置。你可以使用 seek() 方法移动文件指针，用 tell() 方法获取当前文件指针的位置。

with open('example.txt', 'r') as file:
    file.seek(5)  # 将指针移动到第 5 个字符位置
    print(file.read())  # 从指针当前位置读取文件
