# 在 Python 中，文件路径的操作是文件操作的重要组成部分。理解并正确使用文件路径可以确保程序在不同的操作系统环境下正确地读取和写入文件。

# 绝对路径 vs 相对路径

# 绝对路径： 是从文件系统的根目录开始的完整路径。例如，/home/user/documents/file.txt（Linux/Mac） 或 C:\Users\User\Documents\file.txt（Windows）。
# 相对路径： 是相对于当前工作目录的路径.当前工作目录可以通过 os.getcwd() 获取。相对路径可以使用 .（当前目录）或 ..（上一级目录）进行导航。例如，./file.txt 或 ../file.txt。

# 使用 os 模块处理文件路径

import os

# 获取当前工作目录
current_directory = os.getcwd()
print("Current Directory:", current_directory)

# 更改当前工作目录
os.chdir('/path/to/directory')

# 连接路径
path = os.path.join('/home/user', 'documents', 'file.txt')
print("File Path:", path)

# 获取文件名
file_name = os.path.basename(path)
print("File Name:", file_name)

# 获取目录名
directory_name = os.path.dirname(path)
print("Directory Name:", directory_name)

# 分离路径和文件名
directory, file_name = os.path.split(path)
print("Directory:", directory)
print("File Name:", file_name)

# 检查路径是否存在
if os.path.exists(path):
    print("Path exists.")
else:
    print("Path does not exist.")

# 使用 os.path 模块

# 	os.path 提供了对路径进行操作的函数，包括路径组合、拆分、获取文件名和目录名等。
#
# 常用的函数包括：
#
# os.path.join()：连接多个路径部分，生成正确的路径。
# os.path.basename()：返回路径中的文件名。
# os.path.dirname()：返回路径中的目录名。
# os.path.split()：同时返回目录名和文件名。
# os.path.exists()：检查路径是否存在。
# os.path.isfile()：检查是否是文件。
# os.path.isdir()：检查是否是目录。

# 使用 pathlib 模块
#
# Python 3.4 引入了 pathlib 模块，该模块提供了更加面向对象的方式来处理文件路径。

from pathlib import Path

# 获取当前工作目录
current_directory = Path.cwd()
print("Current Directory:", current_directory)

# 连接路径
path = Path('/home/user') / 'documents' / 'file.txt'
print("File Path:", path)

# 获取文件名
file_name = path.name
print("File Name:", file_name)

# 获取文件后缀
file_extension = path.suffix
print("File Extension:", file_extension)

# 获取目录名
directory_name = path.parent
print("Directory Name:", directory_name)

# 检查路径是否存在
if path.exists():
    print("Path exists.")
else:
    print("Path does not exist.")

# 获取脚本文件所在的目录

import os

# 获取当前脚本文件的绝对路径
script_directory = os.path.dirname(os.path.abspath(__file__))
print("Script Directory:", script_directory)

# import os
#
# # 获取当前脚本文件的绝对路径
# script_directory = os.path.dirname(os.path.abspath(__file__))
# print("Script Directory:", script_directory)

# 获取当前文件所在目录下的一个文件路径

import os

# 获取当前脚本所在的目录
script_directory = os.path.dirname(os.path.abspath(__file__))

# 构建当前目录下的文件路径
file_path = os.path.join(script_directory, 'example.txt')
print("File Path:", file_path)

# 使用 pathlib 获取当前脚本所在的目录
from pathlib import Path

# 获取当前脚本所在目录
script_directory = Path(__file__).parent
print("Script Directory:", script_directory)

# 构建当前目录下的文件路径
file_path = script_directory / 'example.txt'
print("File Path:", file_path)

# 使用相对路径读取文件
with open('./data/input.txt', 'r') as file:
    content = file.read()
    print(content)

# 路径跨平台兼容
#
# 文件路径的分隔符在不同操作系统中可能有所不同：
#
# 	•	在 Windows 中，路径分隔符是 \。
# 	•	在 Unix/Linux 和 MacOS 中，路径分隔符是 /。
#
# 为了在不同操作系统上编写兼容的代码，可以使用 os.path.join() 或 pathlib 来自动处理路径的分隔符。

# 不推荐：手动拼接路径，可能导致跨平台问题
path = 'C:\\Users\\User\\Documents\\file.txt'  # Windows
path = '/home/user/documents/file.txt'  # Linux

# 推荐：使用 os.path.join 或 pathlib 进行路径拼接
import os
path = os.path.join('home', 'user', 'documents', 'file.txt')

# 或者使用 pathlib
from pathlib import Path
path = Path('home') / 'user' / 'documents' / 'file.txt'