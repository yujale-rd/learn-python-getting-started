# Python 元组（Tuple）
#
# 元组是一种 不可变 的数据类型，和列表相似，区别在于元组一旦创建后，不能再修改其中的元素。因此，元组通常用于存储不可更改的数据。元组用小括号 () 定义。

# 元组的特点：
#
# 不可变：元组中的元素不能被修改（无法添加、删除或更改元素）。
# 有序：元组中的元素有固定的顺序，可以通过索引访问。
# 可以包含不同类型的元素：一个元组可以包含任意类型的数据，例如字符串、数字、列表等。

# 创建元组

# 元组使用小括号 ()，逗号分隔元素。

# 空元组
empty_tuple = ()

# 只有一个元素的元组
# 注意，如果只有一个元素，需要在元素后加一个逗号 ,，否则 Python 会将其识别为普通的表达式。
single_element_tuple = (5,)

# 多个元素的元组
tuple1 = (1, 2, 3)

# 元组可以包含不同类型的数据
mixed_tuple = (1, "Python", [10, 20, 30], (4, 5, 6))

print(mixed_tuple)  # 输出: (1, 'Python', [10, 20, 30], (4, 5, 6))

# 访问元组元素
# 可以通过索引来访问元组中的元素，索引从 0 开始，也可以使用负索引从末尾访问。

my_tuple = ('a', 'b', 'c', 'd')
print(my_tuple[0])  # 输出: a
print(my_tuple[-1])  # 输出: d

# 元组切片
my_tuple = (0, 1, 2, 3, 4, 5)
print(my_tuple[1:4])  # 输出: (1, 2, 3)
print(my_tuple[:3])   # 输出: (0, 1, 2)
print(my_tuple[3:])   # 输出: (3, 4, 5)

# 元组解包
# 可以将元组中的值直接赋给多个变量，这称为元组解包。
my_tuple = (1, 2, 3)
a, b, c = my_tuple
print(a)  # 输出: 1
print(b)  # 输出: 2
print(c)  # 输出: 3
# 遍历元组
# 可以使用 for 循环来遍历元组中的元素。
my_tuple = (10, 20, 30)
for num in my_tuple:
    print(num)
# 连接与重复元组
# 可以使用 + 连接元组，或者使用 * 重复元组的元素。
tuple1 = (1, 2)
tuple2 = (3, 4)
# 连接元组
new_tuple = tuple1 + tuple2
print(new_tuple)  # 输出: (1, 2, 3, 4)

# 重复元组
repeated_tuple = tuple1 * 2
print(repeated_tuple)  # 输出: (1, 2, 1, 2)

# 检查元素是否存在
# 使用 in 关键字来检查元组中是否包含某个元素。

my_tuple = (10, 20, 30)
print(20 in my_tuple)  # 输出: True
print(40 in my_tuple)  # 输出: False

# 获取元组的长度
# 使用 len() 函数获取元组中元素的个数。

my_tuple = (1, 2, 3, 4, 5)
print(len(my_tuple))  # 输出: 5

# 元组中的最大值和最小值
# 对于数字类型的元组，可以使用 max() 和 min() 函数获取元组中的最大值和最小值。

my_tuple = (10, 20, 30, 40, 50)
print(max(my_tuple))  # 输出: 50
print(min(my_tuple))  # 输出: 10

# 组的不可变性
#
# 元组是不可变的，因此无法修改元组中的元素。这意味着不能进行以下操作：
#
# 不能改变元组的元素值
# 不能在元组中添加或删除元素

my_tuple = (1, 2, 3)
my_tuple[0] = 10  # 报错: TypeError: 'tuple' object does not support item assignment


# count()：统计某个元素在元组中出现的次数。
# index()：返回某个元素在元组中的索引位置。
my_tuple = (1, 2, 2, 3, 4, 2)
print(my_tuple.count(2))  # 输出: 3
print(my_tuple.index(3))  # 输出: 3