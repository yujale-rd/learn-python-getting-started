"""
私有属性
Python 没有强制性的访问控制机制（像其他语言中的 private 和 protected），但是通过约定俗成的方式，我们可以模拟私有属性，以避免外部代码访问或修改对象的内部状态。

1. 使用双下划线实现私有属性

在 Python 中，使用双下划线（__）前缀表示私有属性。这种方式并不完全阻止访问，而是对属性名称进行了名称重整（Name Mangling），将属性名称改为 _ClassName__Attribute 形式，以避免与外部代码直接冲突。
"""

class Person:
    def __init__(self, name, age):
        self.__name = name  # 私有属性
        self.__age = age    # 私有属性

    def get_name(self):
        return self.__name  # 提供公共方法访问私有属性

    def set_name(self, name):
        self.__name = name  # 提供公共方法修改私有属性

p = Person("Alice", 30)

# 尝试访问私有属性（会报错）
# print(p.__name)  # AttributeError: 'Person' object has no attribute '__name'

# 使用公共方法访问和修改
print(p.get_name())  # 输出: Alice
p.set_name("Bob")
print(p.get_name())  # 输出: Bob

"""
访问规则：
	•	__name 会被转换成 _Person__name，这是 Python 的名称重整机制。
	•	尽管使用了双下划线，仍然可以通过 _ClassName__Attribute 访问私有属性，但这样做是不推荐的，违背了封装原则。
"""
print(p._Person__name)  # 输出: Alice

"""
2. 为什么使用双下划线而不是单下划线？
	•	单下划线（_name）：表示该属性或方法是受保护的（protected），不应直接访问，但可以被子类访问。
	•	双下划线（__name）：表示该属性或方法是私有的，不应在类外部访问。Python 会对其进行名称重整，以减少外部访问的风险。

3. 使用 property 装饰器实现私有属性的访问控制

Python 提供了 @property 装饰器，可以用于创建私有属性的“getter”方法，从而实现对私有属性的控制。
"""
class Person:
    def __init__(self, name, age):
        self.__name = name  # 私有属性
        self.__age = age    # 私有属性

    @property
    def name(self):
        return self.__name  # 获取 name 属性

    @name.setter
    def name(self, value):
        if len(value) < 3:
            raise ValueError("Name must be at least 3 characters long.")
        self.__name = value  # 设置 name 属性

p = Person("Alice", 30)

# 通过属性访问私有属性
print(p.name)  # 输出: Alice

# 修改私有属性
p.name = "Bob"  # 设置新值

# 尝试设置不合适的值
# p.name = "A"  # 会引发 ValueError: Name must be at least 3 characters long.

"""
@property 和 @<property_name>.setter 的用法：
	•	@property：将方法变成属性访问。
	•	@<property_name>.setter：用来定义一个 setter 方法，允许我们控制属性值的设置。
"""

# 私有方法

"""
与私有属性类似，Python 中的私有方法也是通过在方法名前添加双下划线（__）来实现的。私有方法的目的是防止外部代码直接调用它们。Python 本身没有强制的访问控制机制，使用双下划线只是通过名称重整来避免直接访问。

1. 私有方法的定义与使用

私有方法通常用于类内部的操作，不应被外部直接调用。它们一般通过公共方法（即对外接口）来间接调用。

"""

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start(self):
        print(f"{self.brand} {self.model} is starting.")
        self.__engine_start()  # 调用私有方法

    def stop(self):
        print(f"{self.brand} {self.model} is stopping.")
        self.__engine_stop()  # 调用私有方法

    # 私有方法
    def __engine_start(self):
        print("Engine started...")

    def __engine_stop(self):
        print("Engine stopped...")


car = Car("Tesla", "Model 3")
car.start()  # 输出: Tesla Model 3 is starting.
             # Engine started...

car.stop()   # 输出: Tesla Model 3 is stopping.
             # Engine stopped...

# 外部不能直接调用私有方法
# car.__engine_start()  # AttributeError: 'Car' object has no attribute '__engine_start'

"""
2. 如何访问私有方法？

虽然我们不能直接调用私有方法，但它们可以通过类内部的其他公共方法来调用，确保对外界封装良好。通过类内部的公共方法，我们可以在一定程度上间接操作私有方法。

访问规则：
	•	私有方法名会被 Python 的名称重整机制修改。比如，如果类名是 Car，那么私有方法 __engine_start 会被修改为 _Car__engine_start。
	•	通过名称重整，可以访问私有方法，但这种方式并不推荐使用，因为它破坏了封装性。
3. 私有方法的目的和作用
	•	封装性：私有方法通常只在类的内部使用，外部不应直接调用。通过私有方法，可以在类的内部进行复杂的操作，而不暴露给外部。
	•	避免外部干扰：如果外部调用私有方法，可能会破坏类的内部状态或导致不希望的副作用。使用私有方法可以防止这种情况的发生。
	•	维护性：当私有方法发生改变时，不会影响外部的代码，因为外部代码根本不应该调用它们。这使得代码在维护和修改时更加灵活。

4. 与私有属性的关系
	•	私有属性：控制类的内部数据，防止外部直接访问和修改。
	•	私有方法：控制类的内部操作，防止外部直接调用这些方法，从而避免外部对内部实现的干扰。

通过私有方法和属性，类可以更好地隐藏其内部实现，确保数据和行为的一致性和安全性。
"""

# python 封装

"""
封装是面向对象编程（OOP）的一个核心概念之一。封装的主要思想是将数据（属性）和操作数据的方法（函数）捆绑在一起，限制外部对数据的直接访问，从而提供更安全、更灵活的接口。封装允许你将类的实现细节隐藏在内部，只暴露出你希望外部使用的接口。

1. 封装的目标和作用
	•	隐藏内部实现细节：通过封装，用户无需了解类内部的实现，只需要关心外部接口。
	•	保护数据：通过控制对属性和方法的访问，确保数据的完整性和一致性。
	•	提供灵活性：可以在不影响外部代码的情况下修改内部实现。

2. 封装的实现

在 Python 中，封装通常通过访问控制来实现。访问控制是指限制外部代码访问类的属性和方法。Python 主要通过三种方式实现封装：
	1.	公有属性和方法（Public）
	2.	私有属性和方法（Private）
	3.	保护属性和方法（Protected）

1. 公有属性和方法（Public）
	•	公有属性和方法可以直接在外部访问和调用。默认情况下，类的所有属性和方法都是公有的。
"""
class Car:
    def __init__(self, brand, model):
        self.brand = brand  # 公有属性
        self.model = model  # 公有属性

    def start(self):  # 公有方法
        print(f"{self.brand} {self.model} is starting.")


car = Car("Tesla", "Model 3")
print(car.brand)  # 直接访问公有属性
car.start()  # 直接调用公有方法

"""
2. 私有属性和方法（Private）
	•	私有属性和方法使用双下划线（__）开头，在外部无法直接访问或修改。Python 的名称重整（name mangling）机制使得类的私有属性和方法在外部被重命名为 _ClassName__AttributeName。
	•	私有属性和方法主要用于类的内部逻辑，外部不应直接访问。
"""
class Car:
    def __init__(self, brand, model):
        self.__brand = brand  # 私有属性
        self.__model = model  # 私有属性

    def __start(self):  # 私有方法
        print(f"{self.__brand} {self.__model} is starting.")

    def public_start(self):
        self.__start()  # 通过公共方法访问私有方法


car = Car("Tesla", "Model 3")
# print(car.__brand)  # AttributeError: 'Car' object has no attribute '__brand'
# car.__start()  # AttributeError: 'Car' object has no attribute '__start'

car.public_start()  # 正常调用公共方法，间接调用私有方法

"""
3. 保护属性和方法（Protected）
	•	Python 中没有真正的“保护”访问控制，但通过在属性或方法名前加一个单下划线（_）来表示它是“保护的”，即不建议外部直接访问，虽然它依然可以被访问。
"""
class Car:
    def __init__(self, brand, model):
        self._brand = brand  # 保护属性
        self._model = model  # 保护属性

    def _start(self):  # 保护方法
        print(f"{self._brand} {self._model} is starting.")


car = Car("Tesla", "Model 3")
print(car._brand)  # 外部依然能访问，但不建议访问
car._start()  # 外部能调用，但不建议调用

"""
3. 使用属性（Property）

Python 提供了 property() 函数，可以将类中的方法当作属性来访问。@property 装饰器使得你可以使用方法访问私有属性或进行计算，而不直接暴露属性本身。
"""
class Car:
    def __init__(self, brand, model):
        self._brand = brand  # 保护属性
        self._model = model  # 保护属性

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        if value not in ["Tesla", "BMW", "Audi"]:  # 控制修改规则
            print("Invalid brand!")
        else:
            self._brand = value

    @property
    def model(self):
        return self._model


car = Car("Tesla", "Model 3")
print(car.brand)  # 使用 @property 方法访问保护属性
car.brand = "BMW"  # 使用 @brand.setter 方法修改属性
print(car.brand)

# 试图修改为无效值
car.brand = "Ford"  # 输出: Invalid brand!

"""
4. 封装的好处
	•	数据安全：通过私有属性和方法，可以防止外部代码直接修改数据，确保数据的完整性。
	•	简化接口：封装将复杂的实现细节隐藏起来，只暴露简洁的接口，简化了外部的使用。
	•	灵活性：可以在不影响外部代码的情况下修改类的内部实现。

"""

# 继承

"""
继承是面向对象编程（OOP）中的一个重要概念。它允许一个类从另一个类继承属性和方法，从而实现代码的重用和扩展。继承使得我们可以创建一个新类（子类），该类能够继承现有类（父类）的特性，并且可以添加自己特有的属性和方法。

1. 继承的基本概念
	•	父类（基类/Base Class）：被继承的类。
	•	子类（派生类/Derived Class）：继承父类的类，可以添加新的属性和方法，也可以重写父类的方法。
	•	子类通过继承父类，获得父类的所有公有属性和方法，但不能直接访问父类的私有属性和方法。
2. 继承的基本语法

"""

class ParentClass:
    # 父类的属性和方法
    pass

class ChildClass(ParentClass):
    # 子类继承父类的属性和方法
    pass
"""
继承的示例
单继承是指一个子类只继承一个父类的属性和方法。子类继承父类后，可以访问父类的公有属性和方法，也可以重写父类的方法来满足自己的需求。

"""
# 父类
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")


# 子类继承父类
class Dog(Animal):
    def __init__(self, name, breed):
        # 调用父类的构造方法
        super().__init__(name)
        self.breed = breed

    # 重写父类的方法
    def speak(self):
        print(f"{self.name} barks.")


# 创建子类对象
dog = Dog("Buddy", "Golden Retriever")
dog.speak()  # 输出: Buddy barks.

"""
多继承
多继承是指一个子类可以继承多个父类的属性和方法。Python 允许一个子类同时继承多个父类，这样可以组合不同父类的功能。

"""
# 父类1
class Animal:
    def speak(self):
        print("Animal makes a sound.")

# 父类2
class Mammal:
    def has_fur(self):
        print("Mammal has fur.")

# 子类
class Dog(Animal, Mammal):
    def speak(self):
        print("Dog barks.")

# 创建子类对象
dog = Dog()
dog.speak()       # 输出: Dog barks.
dog.has_fur()     # 输出: Mammal has fur.

"""
	•	Dog 类 继承了 Animal 和 Mammal 两个父类。
	•	子类不仅可以使用 Animal 类的 speak() 方法，还可以使用 Mammal 类的 has_fur() 方法。
"""

"""
注意事项
在完成继承代码时大家需要遵守一个原则:
    如果需要给代码增加方法时, 去修改子类代码, 不要修改父类代码！！！
    
    父类可以被多个子类继承, 如果修改父类中的代码, 那么会影响所有继承的子类！
    
如果类本身存在需要的属性, 则直接找自身属性, 如果没有, 则按照类的继承顺序依次查找
    如果在第一个类中已经找到了需要的属性或方法, 那么python不会继续向上查找
"""

"""
方法重写（Override）

子类可以重写（覆盖）父类的方法来实现自己特定的功能。方法重写使得子类可以定制父类方法的行为。重写的方法必须具有相同的函数签名（即方法名、参数和返回类型）。
"""

class Animal:
    def speak(self):
        print("Animal makes a sound.")

class Dog(Animal):
    def speak(self):  # 重写父类的 speak 方法
        print("Dog barks.")

class Cat(Animal):
    def speak(self):  # 重写父类的 speak 方法
        print("Cat meows.")

# 创建子类对象
dog = Dog()
cat = Cat()

dog.speak()  # 输出: Dog barks.
cat.speak()  # 输出: Cat meows.

"""
子类中如果存在一个方法, 并且方法名与继承的父类方法一致
    子类重写了父类的方法

    子类调用父类中的重写方法后, 不会查询父类中的方法, 而是找自身方法

如果父类提供的方法不能满足当前编程需求, 那么可以考虑重写父类方法的方式进行方法覆盖

1.重写是在父类方法不满足需求的时候可以使用
2.如果父类方法不满足当前编程需求, 一定要修改当前这个父类继承的子类
    方法一定是修改子类的, 修改父类会造成继承的子类全部受影响
        如果父类中的代码被修改, 子类没有重写, 那么所有子类运行的结果全部都是修改后的结果
"""

"""
super() 函数

super() 函数用于调用父类的方法，特别是在方法重写时，子类可以通过 super() 调用父类的实现。super() 是多继承中的一个重要工具，它能够按照方法解析顺序（MRO）自动查找父类。
"""

class Animal:
    def speak(self):
        print("Animal makes a sound.")

class Dog(Animal):
    def speak(self):
        super().speak()  # 调用父类的 speak 方法
        print("Dog barks.")

dog = Dog()
dog.speak()  # 输出: Animal makes a sound.
             #       Dog barks.

"""
	•	在 Dog 类中，使用 super().speak() 调用父类 Animal 中的 speak() 方法。
1.子类可以获取父类的属性与方法,如果子类定义的属性与父类相同则不用定义,直接使用父类的属性
2.子类构造初始化方法要检查父类中是否存在__init__方法。如果存在必须手动调用
    当父类的__init__有参数的话则子类负责补齐参数
"""

"""
mro() 方法

mro() 方法返回一个类的所有父类的列表，按照方法解析顺序（MRO）排列。这对于多继承特别有用，帮助你理解 Python 如何解析多个父类的调用顺序。

"""
class A:
    def speak(self):
        print("A speaks.")

class B(A):
    def speak(self):
        print("B speaks.")

class C(A):
    def speak(self):
        print("C speaks.")

class D(B, C):
    pass

print(D.mro())  # 输出：[<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]

"""
	•	MRO 确定了方法调用的顺序：D -> B -> C -> A -> object。
	•	D 类首先查找方法，如果找不到就按照 MRO 顺序查找父类。
"""

"""
 issubclass() 和 isinstance()
	•	issubclass() 检查一个类是否是另一个类的子类。
	•	isinstance() 检查一个对象是否是某个类或子类的实例。
"""
print(issubclass(Dog, Animal))  # 输出: True，Dog 是 Animal 的子类
print(isinstance(dog, Dog))     # 输出: True，dog 是 Dog 类的实例
print(isinstance(dog, Animal))  # 输出: True，dog 是 Animal 类的实例，因为 Dog 继承自 Animal