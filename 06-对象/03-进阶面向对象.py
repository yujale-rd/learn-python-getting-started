# 多态

"""
多态是面向对象编程中的一个重要概念，它允许不同类的对象对同一消息做出不同的响应。在 Python 中，多态主要体现在方法的重写（Overriding）上，即子类可以根据自身的需要重写父类的方法。

多态的核心思想是：不同类的对象可以调用同一个方法时表现出不同的行为。

1. 多态的特点
	•	多态性使得我们能够使用统一的接口（方法）处理不同类型的对象。
	•	它通常与继承和方法重写结合使用。
	•	多态使得代码更加灵活和可扩展，增加代码的复用性。

2. 实现多态的方式

在 Python 中，主要通过**方法重写（Overriding）和鸭子类型（Duck Typing）**来实现多态。

示例：方法重写实现多态

方法重写指的是子类重新定义父类中的方法，以便提供不同的实现。这使得父类和子类可以对相同的请求（方法调用）做出不同的响应。

1.必须有继承
2.必须有重写

"""
class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):  # 重写父类方法
        print("Dog barks")

class Cat(Animal):
    def sound(self):  # 重写父类方法
        print("Cat meows")

# 创建实例
animals = [Dog(), Cat()]

# 遍历所有动物并调用 sound 方法
for animal in animals:
    animal.sound()


"""
鸭子类型（Duck Typing）与多态

Python 是一种动态类型语言，它不强制要求对象是某个类的实例来调用其方法，而是根据对象是否具有特定的属性或方法来判断它是否符合要求。这种特性叫做鸭子类型（Duck Typing）。换句话说，“如果它像鸭子，叫声像鸭子，那么它就可以被当作鸭子来使用。”

这种动态的特性使得 Python 具备了更为灵活的多态性。

"""
class Bird:
    def sound(self):
        print("Bird sings")

class Duck:
    def sound(self):
        print("Duck quacks")

class Dog:
    def sound(self):
        print("Dog barks")

# 创建对象
animals = [Bird(), Duck(), Dog()]

# 遍历动物列表并调用 sound 方法
for animal in animals:
    animal.sound()

"""
4. 多态的好处
	•	可扩展性：新的子类可以轻松地添加进来，而不需要修改现有的代码。
	•	代码简洁：多态使得代码可以通过统一的接口处理多种类型的对象，从而避免了重复的代码。
	•	灵活性：程序可以根据对象的类型（而非类型本身）动态地做出不同的行为响应。

5. 多态与接口

Python 是一种动态语言，它没有显式的接口定义（与 Java 等语言不同），但是多态的实现依然有效，因为 Python 的类通常会根据方法的名称和行为来提供多态支持。这种灵活性是 Python 的一个重要特点。

"""
# 类属性和类方法

"""
在面向对象编程中，类属性和类方法是两个非常重要的概念，它们与实例属性和实例方法不同。理解它们的区别和用途能够帮助你更好地设计类和对象的行为。

1. 类属性（Class Attributes）

类属性是属于类的属性，而不是某个实例对象的属性。类属性对于类的所有实例对象是共享的。当你通过类访问类属性时，修改后的值会影响所有实例对象。
	•	类属性是在类中定义的，不依赖于实例化对象。
	•	类属性可以通过类名直接访问，也可以通过实例对象访问，但不推荐通过实例对象访问类属性。

"""
class Dog:
    species = "Canine"  # 类属性

    def __init__(self, name):
        self.name = name  # 实例属性

# 通过类名访问类属性
print(Dog.species)  # 输出: Canine

# 通过实例对象访问类属性
dog1 = Dog("Buddy")
dog2 = Dog("Charlie")
print(dog1.species)  # 输出: Canine
print(dog2.species)  # 输出: Canine

"""
	•	类属性 species 对于所有 Dog 类的实例是共享的。
	•	如果修改类属性，所有实例都会看到更新的值。
"""
Dog.species = "Canis lupus"
print(dog1.species)  # 输出: Canis lupus
print(dog2.species)  # 输出: Canis lupus

"""
2. 类方法（Class Methods）

类方法是绑定到类而不是实例对象的方法。类方法的第一个参数是类本身（通常命名为 cls），而不是实例对象（通常命名为 self）。
	•	类方法可以通过类名调用，也可以通过实例对象调用，但推荐通过类名调用。
	•	类方法通常用于操作类属性或做一些与类本身相关的操作。

类方法使用 @classmethod 装饰器来定义。
"""
class Dog:
    species = "Canine"  # 类属性

    def __init__(self, name):
        self.name = name

    @classmethod
    def get_species(cls):
        return cls.species  # 访问类属性

# 通过类名访问类方法
print(Dog.get_species())  # 输出: Canine

# 通过实例对象访问类方法
dog1 = Dog("Buddy")
print(dog1.get_species())  # 输出: Canine

"""
get_species 方法是一个类方法，通过 cls 参数访问类属性 species。

3. @classmethod 装饰器

@classmethod 装饰器用于将一个方法标记为类方法。类方法的第一个参数是类本身，它可以用来访问类属性或调用类中的其他方法。
"""
class Dog:
    species = "Canine"  # 类属性

    def __init__(self, name):
        self.name = name

    @classmethod
    def set_species(cls, species):
        cls.species = species  # 修改类属性

# 通过类方法修改类属性
Dog.set_species("Canis lupus")

# 查看类属性的修改
dog1 = Dog("Buddy")
dog2 = Dog("Charlie")
print(dog1.species)  # 输出: Canis lupus
print(dog2.species)  # 输出: Canis lupus

"""
@staticmethod 和 @classmethod 的区别
	•	@staticmethod：静态方法，它不会自动接收实例对象 (self) 或类本身 (cls) 作为第一个参数。它和普通函数类似，只是定义在类内部。静态方法适用于那些与类或实例对象无关的操作。
	•	@classmethod：类方法，类方法的第一个参数是类本身 (cls)，它可以访问类属性和其他类方法。
"""
class Dog:
    species = "Canine"

    def __init__(self, name):
        self.name = name

    @staticmethod
    def bark():
        print("Woof!")

# 静态方法不需要通过实例对象或类来访问
Dog.bark()  # 输出: Woof!

"""
类属性和类方法区别
- 访问范围
	•	类属性是类的属性，属于类本身，所有实例对象共享。
	•	类方法是绑定到类的方法，可以通过类名或实例对象调用，但推荐通过类名调用。
	
- 访问方式
    •	类属性可以通过类名或实例对象访问，但不推荐通过实例对象访问类属性。
    •	类方法可以通过类名或实例对象调用，但推荐通过类名调用。
- 用途
    •	类属性用于存储与类相关的数据，如所有实例对象共享的信息。
    •	类方法用于操作类属性或执行与类本身相关的操作。
- 第一个参数
    •	类属性没有第一个参数。
    •	类方法的第一个参数是类本身 (cls)。

类方法与实例方法的区别
	•	实例方法 是依赖于实例对象的，需要通过实例对象来调用，且它的第一个参数是 self，表示实例本身。
	•	类方法 是依赖于类的，可以通过类名或实例对象调用，且它的第一个参数是 cls，表示类本身。

"""
class Dog:
    species = "Canine"  # 类属性

    def __init__(self, name):
        self.name = name

    def speak(self):  # 实例方法
        print(f"{self.name} barks.")

    @classmethod
    def get_species(cls):  # 类方法
        return cls.species

# 创建对象
dog = Dog("Buddy")

# 调用实例方法
dog.speak()  # 输出: Buddy barks.

# 调用类方法
print(Dog.get_species())  # 输出: Canine
print(dog.get_species())  # 输出: Canine

# 静态方法
"""
静态方法通常是与类和实例对象都无关的函数，它只是一个类内部的普通函数。你可以通过类名或实例对象来调用它。
"""

class Dog:
    @staticmethod
    def bark():
        print("Woof!")

# 静态方法可以通过类名调用
Dog.bark()  # 输出: Woof!

# 也可以通过实例对象调用
dog = Dog()
dog.bark()  # 输出: Woof!


# 类对象

"""
类对象:
    指的是当前这个类本身

实例对象:
    指的是对一个类进行实例化之后得到的对象本身
"""


class A:
    def __init__(self, name):
        self.name = name
    pass

    def print_a(self):
        print()


print(id(A))
print(A)

a_1 = A('顾安')
a_2 = A('安娜')
a_3 = A('双双')
print(id(a_1), id(a_2), id(a_3))  # 多个实例对象中的地址是不一样的, 是隔离的状态
print(a_1, a_2, a_3)

"""
类对象在全局内存中只有一个
实例对象随着多次的创建会在内存中开辟多个空间来存储这个实例对象

实例对象的内存地址存储的是当前这个实例对象的实例属性以及类对象的地址
类对象的内存地址中存储的是这个类的类属性和所有方法[实例方法] *

实例对象中除了保存自身的实例属性之外, 还保存了类的地址

在实例对象中有一些属性和方法, 怎么去查询实例对象与类对象中包含的属性和方法？
    dir()
"""
print(id(a_1.__class__))  # __class__是一个方法
print(id(a_2.__class__))
print(id(a_3.__class__))


print(dir(A))
print(dir(a_1))