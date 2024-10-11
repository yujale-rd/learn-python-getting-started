# 在 Python 中，集合（Set） 是一种无序且不重复的元素集合。集合支持数学中的集合运算，如并集、交集、差集等。Python 中的集合主要有两种类型：set 和 frozenset。其中，set 是可变的，而 frozenset 是不可变的。


"""
集合的特点

无序：集合中的元素没有特定的顺序，不能通过索引访问。
不重复：集合中的元素是唯一的，重复的元素会被自动去除。
可变性：set 是可变的，可以添加或删除元素；frozenset 是不可变的。
"""

# 集合创建

# 使用大括号 {} 或 set() 函数创建集合：

# 创建集合
fruits = {"apple", "banana", "orange"}
print(fruits)  # 输出: {'banana', 'orange', 'apple'}

# 使用 set() 创建集合
numbers = set([1, 2, 3, 4, 4, 5])
print(numbers)  # 输出: {1, 2, 3, 4, 5}

# 注意：创建空集合只能使用 set()，因为 {} 会创建一个空字典。
empty_set = set()  # 空集合

# 添加元素

# 1. 使用 add() 方法增加元素
# add() 方法用于向集合中添加一个单独的元素。如果该元素已经存在于集合中，则不会有任何变化。

fruits = {"apple", "banana"}
fruits.add("orange")
print(fruits)  # 输出: {'banana', 'apple', 'orange'}

#
"""
 使用 update() 方法增加多个元素
update() 方法用于向集合中添加多个元素，可以是列表、元组、字符串或其他集合。update() 会将这些数据序列中的每个元素逐一添加到集合中。
"""
# 定义一个集合
set2 = {1, 2, 3}

# 使用 update() 方法增加多个元素（列表）
set2.update([4, 5, 6])
print(set2)  # 输出: {1, 2, 3, 4, 5, 6}

# 使用 update() 方法增加多个元素（元组）
set2.update((7, 8))
print(set2)  # 输出: {1, 2, 3, 4, 5, 6, 7, 8}

# 使用 update() 方法增加多个元素（字符串）
set2.update("9")
print(set2)  # 输出: {1, 2, 3, 4, 5, 6, 7, 8, '9'}

# 删除元素
#
"""
1. 使用 remove() 方法删除元素
remove() 方法用于删除集合中的指定元素。如果指定的元素不存在于集合中，则会引发 KeyError 异常。

使用 discard() 方法删除元素
discard() 方法也用于删除集合中的指定元素。如果指定的元素不存在于集合中，则不会引发异常。

使用 pop() 方法删除元素
pop() 方法用于随机删除集合中的一个元素，并返回该元素。如果集合为空，则会引发 KeyError 异常。

 使用 clear() 方法清空集合
clear() 方法用于清空集合中的所有元素。

使用 del 关键字删除集合
使用 del 关键字可以删除整个集合对象。
"""
fruits = {"apple", "banana", "orange"}

# 删除 'banana'
fruits.remove("banana")
print(fruits)  # 输出: {'apple', 'orange'}

# 删除不存在的元素不会报错
fruits.discard("pear")

# 随机删除一个元素
removed = fruits.pop()
print(removed)  # 输出: 'apple'（随机）

# 清空集合
fruits.clear()
print(fruits)  # 输出: set()

# 集合的数学运算

# 并集 (union() 或 |)
#
# 并集操作返回两个集合中的所有元素，去除重复项。

set1 = {1, 2, 3}
set2 = {3, 4, 5}

# 使用 union() 方法
print(set1.union(set2))  # 输出: {1, 2, 3, 4, 5}

# 使用 | 运算符
print(set1 | set2)  # 输出: {1, 2, 3, 4, 5}

# 交集 (intersection() 或 &)
#
# 交集操作返回两个集合中的公共元素。

set1 = {1, 2, 3}
set2 = {3, 4, 5}

# 使用 intersection() 方法
print(set1.intersection(set2))  # 输出: {3}

# 使用 & 运算符
print(set1 & set2)  # 输出: {3}

# 差集 (difference() 或 -)
#
# 差集操作返回只存在于第一个集合，而不存在于第二个集合中的元素。

set1 = {1, 2, 3}
set2 = {3, 4, 5}

# 使用 difference() 方法
print(set1.difference(set2))  # 输出: {1, 2}

# 使用 - 运算符
print(set1 - set2)  # 输出: {1, 2}

# 对称差集 (symmetric_difference() 或 ^)
#
# 对称差集返回两个集合中不同时存在的元素（即不在交集中的元素）。

set1 = {1, 2, 3}
set2 = {3, 4, 5}

# 使用 symmetric_difference() 方法
print(set1.symmetric_difference(set2))  # 输出: {1, 2, 4, 5}

# 使用 ^ 运算符
print(set1 ^ set2)  # 输出: {1, 2, 4, 5}

# 检查元素是否存在
#
# 	•	使用 in 运算符可以检查元素是否在集合中。

fruits = {"apple", "banana", "orange"}
print("apple" in fruits)  # 输出: True
print("pear" in fruits)  # 输出: False

# 集合的长度
#
# 	•	使用 len() 函数可以获取集合中元素的个数。

fruits = {"apple", "banana", "orange"}
print(len(fruits))  # 输出: 3


# 判断子集和超集
#
# 	•	使用 issubset() 方法检查一个集合是否是另一个集合的子集。
# 	•	使用 issuperset() 方法检查一个集合是否是另一个集合的超集。

set1 = {1, 2}
set2 = {1, 2, 3}

print(set1.issubset(set2))  # 输出: True
print(set2.issuperset(set1))  # 输出: True

# 不可变集合 frozenset
#
# 	•	frozenset 是不可变的集合，一旦创建，不能修改其内容。frozenset 支持与 set 类似的操作，如并集、交集等，但不支持修改操作。

fs = frozenset([1, 2, 3, 4])
print(fs)  # 输出: frozenset({1, 2, 3, 4})

# 尝试修改 frozenset 会抛出错误
# fs.add(5)  # AttributeError: 'frozenset' object has no attribute 'add'


# 集合遍历

# 定义一个集合
fruits = {"apple", "banana", "orange"}

# 使用 for 循环遍历集合
for fruit in fruits:
    print(fruit)
# 注意：由于集合是无序的，所以遍历的顺序不一定是定义时的顺序。

# 遍历集合的同时访问索引
# 虽然集合本身不支持通过索引访问元素，但可以使用 enumerate() 函数在遍历集合时生成索引。
fruits = {"apple", "banana", "orange"}

# 使用 enumerate() 函数遍历集合并获取索引
for index, fruit in enumerate(fruits):
    print(f"Index: {index}, Fruit: {fruit}")

# 集合推导式遍历
#
# 集合推导式（Set Comprehension）可以用于遍历集合并生成一个新的集合。
numbers = {1, 2, 3, 4, 5}

# 使用集合推导式遍历集合并创建新集合
squared_numbers = {num ** 2 for num in numbers}
print(squared_numbers)  # 输出: {1, 4, 9, 16, 25}

# 使用 while 循环遍历集合
#
# 尽管 for 循环是集合遍历的推荐方式，某些情况下也可以通过 while 循环结合迭代器来遍历集合。

numbers = {1, 2, 3, 4, 5}

# 使用 iter() 和 next() 来遍历集合
it = iter(numbers)
while True:
    try:
        num = next(it)
        print(num)
    except StopIteration:
        break  # 当迭代完成时，结束循环