"""
生成器是 Python 中的一种迭代器创建工具，通常用于创建懒加载（惰性求值）类型的迭代器。与普通的迭代器不同，生成器每次迭代时会生成一个值，并在下一次请求时继续执行。
生成器非常适合处理大量数据的场景，因为它可以节省内存开销。
1. 生成器的概念

生成器是通过 yield 关键字创建的函数或表达式。每次遇到 yield，生成器会返回一个值，并暂停执行。生成器在后续迭代中会从上次暂停的位置继续执行，直到执行完毕或遇到 StopIteration 异常。
2. 生成器的定义

生成器可以通过两种方式定义：
	•	生成器函数：使用 yield 关键字代替 return，返回一个生成器对象。
	•	生成器表达式：类似于列表推导式，用圆括号包裹的表达式，可以返回一个生成器对象。

3. 创建生成器

3.1 创建生成器函数

生成器函数是一个普通的 Python 函数，在需要返回值时使用 yield。每次 yield 执行时，生成器会暂停，返回值并保持函数状态，直到下一次调用时继续执行。"""
def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()  # 创建生成器
print(next(gen))  # 输出: 1
print(next(gen))  # 输出: 2
print(next(gen))  # 输出: 3
# 再次调用 next() 会抛出 StopIteration 异常
# print(next(gen))  # StopIteration

"""
3.2 创建生成器表达式

生成器表达式的语法与列表推导式类似，只是使用圆括号而非方括号。生成器表达式会返回一个生成器对象，可以逐个计算其值，而不会一次性将所有值加载到内存中。
"""
gen_expr = (x * x for x in range(5))

print(next(gen_expr))  # 输出: 0
print(next(gen_expr))  # 输出: 1
print(next(gen_expr))  # 输出: 4

"""
4. 生成器的执行过程

生成器的执行过程分为几个步骤：
	1.	创建生成器对象：当生成器函数被调用时，返回一个生成器对象，但此时函数并未执行。
	2.	第一次迭代：调用 next() 或者 for 循环触发生成器函数的执行，执行到 yield 语句返回值并暂停。
	3.	后续迭代：每次调用 next() 时，生成器会从上次暂停的 yield 语句处继续执行，直到函数结束或遇到 StopIteration 异常。
"""

"""
5. 生成器推导式（Generator Comprehension）

生成器推导式与列表推导式类似，但使用圆括号，而不是方括号，它返回一个生成器对象。
"""
gen_expr = (x ** 2 for x in range(3))
for num in gen_expr:
    print(num)

"""
6. send() 方法

生成器不仅可以通过 next() 来获取值，还可以通过 send() 方法向生成器传递数据。send() 方法用于恢复生成器的执行，并向 yield 表达式传递一个值。
"""
def my_generator():
    value = yield "Start"  # 先返回 "Start"
    print(f"Received: {value}")
    yield "End"

gen = my_generator()
print(next(gen))  # 输出: Start
print(gen.send("Hello"))  # 输出: Received: Hello
                         # 输出: End

"""
	1.	第一次调用 next(gen) 时，生成器执行到第一个 yield，返回 “Start”。
	2.	然后 send() 方法被调用，发送一个值给生成器，生成器接收该值并打印出来。
"""

"""
7. close() 方法

close() 方法用于关闭生成器，停止它的执行。当你调用 close() 时，生成器会引发一个 GeneratorExit 异常。如果生成器正在执行，close() 会终止执行并清理任何资源。
"""
def my_generator():
    try:
        yield 1
        yield 2
    except GeneratorExit:
        print("Generator closed")

gen = my_generator()
print(next(gen))  # 输出: 1
gen.close()  # 关闭生成器，输出: Generator closed

"""
8. 生成器的应用

生成器非常适合以下几种场景：
	•	懒加载（Lazy Loading）：生成器按需生成值，而不是一次性创建所有值。适用于处理大数据集或流式数据。
	•	内存优化：生成器不会一次性将所有数据加载到内存中，节省内存空间，尤其在处理大量数据时。
	•	无限序列：生成器可以创建无限大的数据流，因为它们是按需生成值的，不会因为内存限制而出错。
"""
def count_up():
    count = 1
    while True:
        yield count
        count += 1

gen = count_up()
print(next(gen))  # 输出: 1
print(next(gen))  # 输出: 2
"""
9. 生成器的缺点

尽管生成器具有很多优点，但它们也有一些限制：
	1.	一次性使用：生成器只能迭代一次，无法重复使用。如果需要多次迭代，必须重新创建生成器。
	2.	不可回退：生成器是单向的，不能像列表一样随机访问元素。如果你需要回退到之前的值，生成器不适合。
	3.	调试难度：由于生成器的惰性求值特性，在调试时不容易查看所有值。如果你需要检查生成器中的值，可能需要使用其他方法。

"""