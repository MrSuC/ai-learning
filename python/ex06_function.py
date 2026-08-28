# -*- coding: utf-8 -*-
"""
练习 6：函数进阶
================
目标：掌握 Python 函数的灵活特性——比 Java 的 method 灵活得多：
1. 默认参数（Java 用重载实现）
2. 关键字参数（Java 没有）
3. *args / **kwargs（Java 用可变参数 ... 实现 *args，**kwargs 没有对应物）
4. lambda 匿名函数
5. 函数是一等公民：可以当参数传、当返回值

运行方式：F5 或 python ex06_function.py
"""

# ---------- 1. 默认参数 ----------
# Java 要写两个重载：greet(name) / greet(name, prefix)
def greet(name: str, prefix: str = "你好"):
    """prefix 有默认值，调用时可不传。"""
    return f"{prefix}，{name}！"


print(greet("团团"))           # 不传 prefix，用默认值
print(greet("团团", "早上好"))  # 传了就用新的


# ---------- 2. 关键字参数 ----------
# 调用时指定参数名，顺序可以打乱（Java 没有这个）
def info(name: str, age: int, city: str):
    return f"{name} {age}岁 住{city}"


print(info(city="北京", name="团团", age=26))   # 按名字传，顺序随便
# 混用时：位置参数在前，关键字参数在后（有严格顺序要求）


# ---------- 3. *args：任意多个位置参数 ----------
# Java: public int sum(int... nums)
def total(*args):
    """args 是一个元组，装下所有位置参数。"""
    print("args 类型:", type(args), "内容:", args)
    return sum(args)          # 内置 sum() 对数字求和


print("total(1,2,3) =", total(1, 2, 3))
print("total(1,2,3,4,5) =", total(1, 2, 3, 4, 5))


# ---------- 4. **kwargs：任意多个关键字参数 ----------
def show_info(**kwargs):
    """kwargs 是一个字典，装下所有关键字参数。"""
    for key, value in kwargs.items():
        print(f"  {key} = {value}")


show_info(name="团团", age=26, hobby="写代码")


# ---------- 5. lambda 匿名函数 ----------
# Java: 函数式接口 + lambda，Python 语法更简单
# 格式：lambda 参数: 返回值表达式
double = lambda x: x * 2     # 等价 def double(x): return x * 2
print("lambda double(5) =", double(5))

# 经典用法：当排序的 key（类似 Java 的 Comparator.comparing）
people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Cathy", "age": 28},
]
# 按 age 排序（reverse=True 降序）
people.sort(key=lambda p: p["age"], reverse=True)
print("按年龄降序:", people)


# ---------- 6. 函数是一等公民 ----------
# 函数可以赋值给变量、当参数传、当返回值
def apply_twice(func, value):
    """把 func 对 value 执行两次。"""
    return func(func(value))


print("apply_twice(double, 3) =", apply_twice(double, 3))   # 3 -> 6 -> 12

# map / filter：函数式处理（了解，推导式更常用）
nums = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, nums))     # 等价推导式 [x*2 for x in nums]
evens = list(filter(lambda x: x % 2 == 0, nums))  # 等价 [x for x in nums if x%2==0]
print("map 翻倍:", doubled)
print("filter 偶数:", evens)


# ---------- 练习题（自己做）----------
# 1. 写一个函数 area(width, height=10)，默认高 10，测试两种调用方式
# 2. 用 *args 写一个 concatenate(*words)，把所有字符串拼成一个句子（用空格连接）
# 3. 给一个字符串列表，用 lambda + sorted 按字符串长度排序
# 验收标准：能用 keyword 传参、能处理不定长参数
