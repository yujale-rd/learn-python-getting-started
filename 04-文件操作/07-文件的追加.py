# 文件的追加操作可以使用 Python 的内置函数 open，并且使用模式 'a' 或 'a+'。模式 'a' 表示追加写入模式，如果文件不存在，会自动创建文件。如果文件存在，则在文件末尾追加内容。


"""
注意事项
文件路径：确保文件路径正确。如果使用相对路径，确保当前工作目录正确。
编码：确保读写操作的编码一致，避免编码问题引起的错误。
模式：'a' 模式只用于追加内容；'a+' 模式用于追加和读取内容。如果需要同时追加和读取内容，可以使用 'a+' 模式。
"""

# 创建一个新的文件并写入初始内容
with open('test_append.txt', 'w', encoding='utf-8') as f:
    f.write("这是初始内容。\n")

# 使用追加模式在文件末尾添加内容
with open('test_append.txt', 'a', encoding='utf-8') as f:
    f.write("这是追加的内容。\n")

# 使用追加模式再添加更多内容
with open('test_append.txt', 'a', encoding='utf-8') as f:
    f.write("这是再次追加的内容。\n")

# 读取文件内容并打印以验证追加操作
with open('test_append.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    print(content)
