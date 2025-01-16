"""
字典（Dictionary）
字典是一种 可变 的、无序的数据类型，存储键值对（Key-Value）。
在字典中，每个键是唯一的，值可以是任何数据类型。
字典使用大括号 {} 定义，每个键值对用 : 分隔，多个键值对之间用逗号 , 分隔。


字典的特点：

键唯一：字典中的每个键必须是唯一的，不能重复。
无序：字典自 Python 3.7 起，虽然保留插入顺序，但其实现并不基于有序结构。
键值对存储：每个键都有对应的值，可以通过键来访问对应的值。
"""

"""
# 字典的创建
# 字典定义格式: 变量 = {键1:值1, 键2:值2.....}
# 使用大括号 {} 或者 dict() 函数创建字典。
"""

# 空字典
empty_dict = {}

# 含有键值对的字典
person = {"name": "Alice", "age": 25, "city": "New York"}
print(person)  # 输出: {'name': 'Alice', 'age': 25, 'city': 'New York'}

# 使用 dict() 函数创建字典
person = dict(name="Bob", age=30, city="Los Angeles")
print(person)  # 输出: {'name': 'Bob', 'age': 30, 'city': 'Los Angeles'}

"""
# 访问字典中的值
#
# 可以通过键来访问字典中的值。如果访问的键不存在，会抛出 KeyError 错误。为了避免错误，可以使用 get() 方法，它在键不存在时返回 None 或自定义的默认值。
"""

person = {"name": "Alice", "age": 25}

# 通过键访问值
print(person["name"])  # 输出: Alice

# 使用 get() 方法访问值
print(person.get("age"))       # 输出: 25
print(person.get("address"))   # 输出: None
print(person.get("address", "未知地址"))  # 输出: 未知地址


"""
# 获取所有键：
#
# keys() 方法返回一个包含字典中所有键的视图对象，可以通过 list() 函数转换为列表。
"""

keys = person.keys()
print("字典中的所有键:", keys)


# 获取所有值：
#
# values() 方法返回一个包含字典中所有值的视图对象，可以通过 list() 函数转换为列表。

values = person.values()
print("字典中的所有值:", values)

# 获取所有键值对：
#
# items() 方法返回一个包含字典中所有键值对的视图对象，可以通过 list() 函数转换为列表，其中每个键值对是一个元组。

# 获取所有键值对
items = person.items()
print("字典中的所有键值对:", items)

# 查询字典中是否包含某个键：
#
# 使用 in 关键字检查字典中是否包含指定的键。
has_name = 'name' in person
print("字典中是否包含键'name':", has_name)

has_address = 'address' in person
print("字典中是否包含键'address':", has_address)

# 通过键获取值并进行运算或其他操作
age_double = person.get('age', 0) * 2
print("将'age'的值翻倍:", age_double)

# 遍历字典中的所有键值对：
#
# 使用 for 循环遍历字典中的所有键值对，使用 items() 方法可以同时获取键和值。
for key, value in person.items():
    print(f"键: {key}, 值: {value}")


# 添加键值对

# 增加字典中的键值对可以通过直接赋值的方式完成。如果键已经存在，赋值操作会更新对应的值；如果键不存在，赋值操作会新增一个键值对。
 # 初始化一个字典
dict1 = {'name': 'xiaoming', 'age': 18}

# 增加新的键值对
dict1['gender'] = '男'
print(dict1)  # 输出: {'name': 'xiaoming', 'age': 18, 'gender': '男'}

# 更新已有的键值对
dict1['age'] = 19
print(dict1)  # 输出: {'name': 'xiaoming', 'age': 19, 'gender': '男'}

# 增加多个键值对
dict1['address'] = 'Beijing'
dict1['hobby'] = 'coding'
print(dict1)  # 输出: {'name': 'xiaoming', 'age': 19, 'gender': '男', 'address': 'Beijing', 'hobby': 'coding'}

# 使用 update() 方法增加键值对
# update() 方法可以一次性增加或更新多个键值对。如果传入的字典中有键在目标字典中已存在，update() 方法会更新该键对应的值；如果键不存在，则会新增该键值对。

# 初始化一个字典
dict1 = {'name': 'xiaoming', 'age': 18}

# 使用update方法增加键值对
dict1.update({'gender': '男', 'address': 'Beijing'})
print(dict1)  # 输出: {'name': 'xiaoming', 'age': 18, 'gender': '男', 'address': 'Beijing'}

# 更新已有的键值对
dict1.update({'age': 20})
print(dict1)  # 输出: {'name': 'xiaoming', 'age': 20, 'gender': '男', 'address': 'Beijing'}


# 删除键值对
# 使用 pop('key') 可以删除指定键并返回被删除的值。
# 如果键不存在，可以提供一个默认值，避免抛出异常。
person = {"name": "Alice", "age": 25, "city": "New York"}

# 删除 'age' 键，并返回其值
age = person.pop("age")
print(age)        # 输出: 25
print(person)     # 输出: {'name': 'Alice', 'city': 'New York'}

# 删除不存在的键，提供默认值
country = person.pop("country", "未知")
print(country)    # 输出: 未知

# 使用 del dict['key'] 可以删除指定键值对。
# 如果键不存在，会抛出 KeyError 异常。
person = {"name": "Alice", "age": 25, "city": "New York"}

# 删除 'city' 键
del person["city"]
print(person)  # 输出: {'name': 'Alice', 'age': 25}

# 处理删除不存在键时的异常
try:
    del person["country"]
except KeyError:
    print("键 'country' 不存在")

# 删除最后一个键值对 - popitem() 方法：
#
# 使用 popitem() 可以删除字典中的最后一个键值对，并返回该键值对。
# 如果字典为空，会抛出 KeyError 异常。

person = {"name": "Alice", "age": 25, "city": "New York"}

# 删除最后一个键值对
last_item = person.popitem()
print(last_item)  # 输出: ('city', 'New York')
print(person)     # 输出: {'name': 'Alice', 'age': 25}

# 清空后再调用 popitem 会抛出异常
person.clear()  # 清空字典
try:
    person.popitem()
except KeyError:
    print("字典为空，无法删除键值对")

# 清空字典 - clear() 方法：
#
# 使用 clear() 可以清空字典，删除所有键值对。

person = {"name": "Alice", "age": 25, "city": "New York"}

# 清空字典
person.clear()
print(person)  # 输出: {}
# 处理删除不存在的键：
# 使用 pop() 方法时，可以提供一个默认值来避免 KeyError 异常。
person = {"name": "Alice", "age": 25}

# 使用 pop() 时提供默认值
address = person.pop("address", "未知地址")
print(address)  # 输出: 未知地址
# 使用 del 关键字时，需要通过 try...except 结构捕获 KeyError 异常。
person = {"name": "Alice", "age": 25}

# 使用 del 时捕获异常
try:
    del person["address"]
except KeyError:
    print("键 'address' 不存在")


# 修改字典键值对

# 修改已有的键值对：
#
# 直接通过字典键进行赋值操作，如 dict1['age'] = 20。
person = {"name": "Alice", "age": 25, "city": "New York"}

# 修改 'age' 的值
person["age"] = 30
print(person)  # 输出: {'name': 'Alice', 'age': 30, 'city': 'New York'}

# 使用 setdefault() 方法：
#
# setdefault() 方法在字典中查找键，如果键存在则返回其对应的值，不会修改字典。
# 如果键不存在，则插入该键并设置其默认值。


# 修改字典的值 - 使用 setdefault() 方法
# 如果键存在，不修改字典并返回该键对应的值
# 如果键不存在，插入该键并设置默认值
dict1.setdefault('age', 21)
print("使用 setdefault() 方法修改后的字典:", dict1)
dict1.setdefault('grade', 'A')
print("使用 setdefault() 方法添加新的键值对后的字典:", dict1)


"""
遍历字典的键值对：

使用 items() 方法可以获取字典的所有键值对，并使用 for key, value in dict1.items() 进行遍历。
遍历字典的键：

使用 keys() 方法可以获取字典的所有键，并使用 for key in dict1.keys() 进行遍历。
遍历字典的值：

使用 values() 方法可以获取字典的所有值，并使用 for value in dict1.values() 进行遍历。
遍历字典的键值对并进行操作：

在遍历键值对的过程中，可以根据键的不同进行特定操作，如对年龄值进行翻倍操作。
使用 enumerate() 函数遍历字典的键值对并获取索引：

enumerate() 函数可以在遍历时获取索引，适用于需要索引的场景。
"""
person = {"name": "Alice", "age": 25, "city": "New York"}

# 遍历键
for key in person:
    print(key)

# 遍历值
for value in person.values():
    print(value)

# 遍历键值对
for key, value in person.items():
    print(f"{key}: {value}")
