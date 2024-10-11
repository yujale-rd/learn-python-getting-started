# 在 Python 中，除了文件操作，文件夹（目录）的操作也是非常常见的任务。Python 提供了 os 和 pathlib 模块来处理文件夹操作，包括创建、删除、遍历文件夹等

# 1. 使用 os 模块进行文件夹操作
#
# 1.1 创建文件夹
#
# 使用 os.makedirs() 或 os.mkdir() 创建文件夹：
#
# os.mkdir()：创建单个目录。如果目录已经存在，则抛出 FileExistsError。
# os.makedirs()：递归创建目录。如果路径中存在多个目录且有些目录尚未创建，则会依次创建。

import os

# 创建单个目录
os.mkdir("new_folder")

# 创建嵌套目录
os.makedirs("parent_folder/child_folder")

# 删除文件夹
#
# 使用 os.rmdir() 和 os.removedirs() 删除文件夹：
#
# os.rmdir()：删除单个空目录。如果目录非空，则抛出 OSError。
# os.removedirs()：递归删除目录，只有在所有指定目录为空时才能成功删除。

import os

# 删除单个空目录
os.rmdir("new_folder")

# 递归删除空目录
os.removedirs("parent_folder/child_folder")

# 列出目录内容
#
# 使用 os.listdir() 列出目录中的所有文件和子目录。

import os

# 列出当前目录下的文件和文件夹
files_and_dirs = os.listdir(".")
print(files_and_dirs)

# 遍历目录树
#
# 使用 os.walk() 遍历目录树。os.walk() 返回一个生成器，生成三元组 (dirpath, dirnames, filenames)，表示当前目录路径、该目录下的子目录列表、文件列表。

import os

# 遍历目录树
for dirpath, dirnames, filenames in os.walk("."):
    print("Current Path:", dirpath)
    print("Directories:", dirnames)
    print("Files:", filenames)

# 重命名文件夹
#
# 使用 os.rename() 重命名文件夹。
import os

# 重命名文件夹
os.rename("old_folder", "new_folder_name")

# 检查文件夹是否存在
#
# 使用 os.path.exists() 来检查文件夹是否存在。

import os

# 检查文件夹是否存在
if os.path.exists("folder_name"):
    print("Directory exists.")
else:
    print("Directory does not exist.")

# 2. 使用 pathlib 模块进行文件夹操作
#
# 从 Python 3.4 开始，pathlib 提供了更方便和面向对象的文件路径处理方式。以下是使用 pathlib 进行文件夹操作的示例。
#
# 2.1 创建文件夹
#
# 使用 Path.mkdir() 创建目录。
from pathlib import Path

# 创建单个目录
Path("new_folder").mkdir()

# 创建嵌套目录，存在的目录不会引发错误
Path("parent_folder/child_folder").mkdir(parents=True, exist_ok=True)

# 2.2 删除文件夹
#
# 使用 Path.rmdir() 删除空目录。

from pathlib import Path

# 删除单个空目录
Path("new_folder").rmdir()

# 2.3 列出目录内容
#
# 使用 Path.iterdir() 列出目录内容。
from pathlib import Path

# 列出当前目录下的文件和文件夹
for item in Path(".").iterdir():
    print(item)

# 2.4 遍历目录树
#
# 使用 Path.glob() 或 Path.rglob() 遍历目录树。
from pathlib import Path

# 遍历当前目录及其子目录中的所有文件
for file in Path(".").rglob("*"):
    print(file)

# 2.5 重命名文件夹
#
# 使用 Path.rename() 重命名文件夹。

from pathlib import Path

# 重命名文件夹
Path("old_folder").rename("new_folder_name")

# 2.6 检查文件夹是否存在
#
# 使用 Path.exists() 来检查文件夹是否存在。

from pathlib import Path

# 检查文件夹是否存在
if Path("folder_name").exists():
    print("Directory exists.")
else:
    print("Directory does not exist.")

# 3. 删除非空目录
#
# 	•	使用 shutil.rmtree()：如果需要删除非空目录，可以使用 shutil 模块的 rmtree() 函数。
import shutil

# 删除非空目录
shutil.rmtree("folder_name")

