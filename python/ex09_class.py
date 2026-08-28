# -*- coding: utf-8 -*-
"""
练习 9：类与对象
================
目标：掌握 Python 面向对象。和 Java 的核心区别：
1. 没有 public/private/protected 关键字——约定用 _ 前缀表示"私有"
2. 构造方法是 __init__（Java 是类同名方法）
3. 每个实例方法第一个参数是 self（Java 是 this，但隐式的）
4. 没有 new 关键字，直接 类名() 创建对象

运行方式：F5 或 python ex09_class.py
"""


# ---------- 1. 定义一个类 ----------
class Dog:
    """狗类。docstring 就是文档，类似 Java 的注释。"""

    # 类属性：所有实例共享（类似 Java 的 static 字段）
    species = "犬科"

    # 构造方法：创建对象时自动调用（Java 的构造函数）
    def __init__(self, name: str, age: int):
        self.name = name        # 实例属性：每个对象自己的（Java 的 this.name = name）
        self.age = age

    # 实例方法（Java 的普通成员方法）
    def bark(self):
        """叫一声。self 表示"当前这个对象"，不用自己传。"""
        return f"{self.name} 汪汪叫！"

    # 方法里访问自己的属性，必须通过 self
    def info(self):
        return f"我叫{self.name}，今年{self.age}岁，属于{self.species}"


# ---------- 2. 创建对象（没有 new！）----------
dog1 = Dog("旺财", 3)          # Java: new Dog("旺财", 3)
dog2 = Dog("小黑", 5)

print(dog1.bark())
print(dog1.info())
print("类属性共享:", dog1.species, dog2.species)   # 都是"犬科"

# 属性可以随便改（Java 需要 setter，Python 直接赋值）
dog1.age = 4
print("改年龄后:", dog1.info())


# ---------- 3. 继承 ----------
# Java: class Cat extends Animal，Python: class Cat(Animal)
class Cat(Dog):
    """猫类继承狗类——因为 Dog 的代码结构通用，拿来演示继承。"""

    # 重写父类方法（Java 的 @Override）
    def bark(self):
        return f"{self.name} 喵喵叫！"

    # 调用父类构造方法
    def __init__(self, name: str, age: int, color: str):
        super().__init__(name, age)   # super() 同 Java 的 super()
        self.color = color            # 子类自己的新属性

    # 子类自己的新方法
    def meow_extra(self):
        return f"{self.name} 是{self.color}色的猫"


cat1 = Cat("咪咪", 2, "橘")
print(cat1.bark())                   # 多态：调用的是 Cat 重写后的版本
print(cat1.info())                   # 继承来的方法
print(cat1.meow_extra())             # 子类新增的方法


# ---------- 4. __str__ 魔法方法 ----------
# Java 重写 toString()，Python 重写 __str__()
# 重写后，print(对象) 就会调用它
class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"


p = Point(10, 20)
print("打印对象:", p)                # 有 __str__ 就不打印内存地址了
# 常见魔法方法：__init__ 构造、__str__ 转字符串、__repr__ 调试显示、
# __len__ 支持 len()、__add__ 支持 + 号...（后面用到再学）


# ---------- 5. 类方法 / 静态方法（了解）----------
# Java: static 方法，Python 里更细分：
class MathUtils:
    # @staticmethod：不依赖实例和类，纯工具函数（Java 的静态方法）
    @staticmethod
    def add(a, b):
        return a + b

    # @classmethod：能访问类属性，第一个参数是 cls（用的不多，先了解）
    @classmethod
    def create_zero(cls):
        return cls()


print("静态方法:", MathUtils.add(1, 2))


# ---------- 练习题（自己做）----------
# 1. 定义一个 Student 类：name、age、scores（列表），方法 avg() 算平均分
# 2. 定义 Undergraduate 继承 Student，加字段 major，重写 __str__
# 3. 创建 2 个学生对象，打印信息并算平均分
# 验收标准：对象能创建、方法能调用、__str__ 输出友好
