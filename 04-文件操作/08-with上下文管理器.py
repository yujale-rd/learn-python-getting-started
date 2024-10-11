# Python 中的上下文管理器通过 with 语句使用，提供了在特定代码块执行前后自动处理资源（如文件、网络连接、锁等）的机制，确保在代码执行完成后，资源能够被正确关闭或释放。
# 上下文管理器实现了资源的自动管理，通常用于文件操作、数据库连接等需要在使用后进行清理的操作。

# 1. 基本语法
#
# 上下文管理器的使用主要依赖于 with 语句。

# with expression as variable:
    # 在这个代码块中可以使用变量
    # 代码块结束后，资源将自动清理

# 2. 使用上下文管理器操作文件
#
# 操作文件是上下文管理器的常见应用场景。
# 自动管理文件资源的打开和关闭
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

# 在 with 语句中打开文件后，文件将会在代码块结束时自动关闭，即使代码块内出现异常也能保证文件被关闭。

# 3. 自定义上下文管理器
#
# 可以通过实现特殊方法 __enter__() 和 __exit__() 来创建自定义的上下文管理器。

class MyContextManager:
    def __enter__(self):
        print("进入上下文管理器")
        # 返回的对象可以在 `with` 语句块中使用
        return "资源已分配"

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("退出上下文管理器")
        # 清理资源的代码放在这里
        # 如果返回 True, 则异常不会被传递出去
        return True

# 使用自定义上下文管理器
with MyContextManager() as resource:
    print(resource)
    raise ValueError("触发异常")

# 即使触发了异常，上下文管理器依然执行了 __exit__() 方法，确保资源被正确释放。

# 4. contextlib 模块
#
# Python 提供了 contextlib 模块，用于简化上下文管理器的创建。常用的工具包括 contextlib.contextmanager 装饰器，可以使用函数形式创建上下文管理器。

from contextlib import contextmanager

@contextmanager
def my_context():
    print("进入上下文")
    yield "资源已分配"
    print("退出上下文")

# 使用函数形式的上下文管理器
with my_context() as resource:
    print(resource)

# 5. 上下文管理器的优势
#
# 	•	自动管理资源：上下文管理器自动管理资源的分配和释放，避免忘记关闭文件或释放锁等情况。
# 	•	异常安全性：即使在 with 语句块中发生异常，也会执行资源的清理操作，确保代码健壮性。