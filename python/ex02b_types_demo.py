# -*- coding: utf-8 -*-
"""
ex02b_types_demo.py — Python 11 个基础类型完整示例
Java 对照学习版，运行方式：F5 或 终端 python ex02b_types_demo.py
"""

# ========== 1. int 整数 ==========
print("===== 1. int 整数 =====")
print(7 // 2)         # 3    整除（Java 的 7/2 是这个效果）
print(7 % 2)          # 1    取余
print(2 ** 10)        # 1024 幂运算（Java 要 Math.pow）
print(10 ** 100)      # 超大整数不溢出（Java 要 BigInteger）
print(type(100))      # <class 'int'>
# Java 对照：byte/short/int/long 四个类型，Python 一个 int 全包

# ========== 2. float 浮点数 ==========
print("\n===== 2. float 浮点数 =====")
print(3.14 * 2)       # 6.28
print(0.1 + 0.2)      # 0.30000000000000004  经典精度坑
print(round(0.1 + 0.2, 2))   # 0.3
print(type(3.0))      # <class 'float'>
print(3 == 3.0)       # True  int 和 float 可以比较
# Java 对照：Python 只有 float 一个浮点，对应 Java 的 double

# ========== 3. complex 复数 ==========
print("\n===== 3. complex 复数 =====")
z1 = 3 + 4j           # j 是虚数单位（数学里写作 i）
z2 = complex(1, 2)    # 函数写法
print(z1.real, z1.imag)   # 3.0 4.0  实部、虚部
print(z1 + z2)        # (4+6j)  复数可以直接加减乘除
print(abs(z1))        # 5.0  模长（勾股定理 3-4-5）
# Java 对照：Java 没有内置复数，得自己写类

# ========== 4. bool 布尔 ==========
print("\n===== 4. bool 布尔 =====")
print(3 > 2)          # True  比较运算
print(True and False) # False and：两边都真才真
print(True or False)  # True  or：有一边真就真
print(not True)       # False not：取反
print(True == 1)      # True  bool 是 int 的子类
print(bool(0), bool(""))   # False False  空值都是 False
print(bool(3), bool("a"))  # True True   非空都是 True
# Java 对照：Java 写 true/false 小写，Python 是 True/False 大写

# ========== 5. str 字符串 ==========
print("\n===== 5. str 字符串 =====")
name = "Alice"
print(name.upper())           # ALICE
print(name.replace("A", "E")) # Elice
msg = "hello world"
print(msg.split())            # ['hello', 'world']  拆成列表
print("-".join(["a", "b"]))   # a-b  拼接（Java 要写循环）
print(msg[0:5])               # hello  切片（含头不含尾）
print(msg[6:])                # world  从第 6 位到最后
print(len(msg))               # 11  长度
print(f"名字是 {name}")       # 名字是 Alice  f-string
# Java 对照：没有 char 类型，单个字符也是 str；str 不可变

# ========== 6. list 列表 ==========
print("\n===== 6. list 列表 =====")
fruits = ["apple", "banana", "cherry"]
fruits.append("durian")        # 尾部追加
fruits.insert(1, "blueberry")  # 指定位置插入
fruits[0] = "avocado"          # 按索引修改
fruits.remove("banana")        # 按值删除
popped = fruits.pop()          # 按索引删除，返回被删的值 first = fruits.pop(0) 带索引：删第 0 个  无参数 = 删【最后一个】
print(fruits)                  # 打印整个列表
print(fruits[-1])              # 最后一个元素（负数索引）
print(len(fruits))             # 列表长度
print(sorted(fruits))          # 排序（返回新列表，不改原列表）
for f in fruits:               # 直接遍历元素
    print(f)
# Java 对照：相当于 ArrayList，但可以混合类型、负数索引

# ========== 7. tuple 元组 ==========
print("\n===== 7. tuple 元组 =====")
point = (3, 4)
x, y = point          # 解包：一行拆成两个变量
print(x, y)           # 3 4
single = (1,)         # 注意逗号！一个元素的元组必须带逗号
print(type(single))   # <class 'tuple'>
# point[0] = 99      # 取消注释会报错：tuple 不可变
# Java 对照：不可变的列表，Java 没有直接对应

# ========== 8. dict 字典 ==========
print("\n===== 8. dict 字典 =====")
user = {"name": "团团", "age": 26}
print(user["name"])            # 团团  直接按 key 取
print(user.get("city", "未知"))# 未知  get 没有 key 时给默认值
user["age"] = 27               # 修改已有 key
user["city"] = "深圳"          # 新增 key
print(user.keys())             # 所有键
print(user.values())           # 所有值
for k, v in user.items():      # 遍历键值对
    print(k, v)
# Java 对照：相当于 HashMap，但遍历更简单

# ========== 9. set 集合 ==========
print("\n===== 9. set 集合 =====")
tags = {"a", "b", "a", "c"}
print(tags)               # {'a', 'c', 'b'}  自动去重
print("a" in tags)        # True  成员判断一行搞定
s1 = {1, 2, 3}
s2 = {2, 3, 4}
print(s1 & s2)            # {2, 3}        交集
print(s1 | s2)            # {1, 2, 3, 4}  并集
print(s1 - s2)            # {1}           差集
# Java 对照：相当于 HashSet，还自带交集并集运算

# ========== 10. None 空值 ==========
print("\n===== 10. None 空值 =====")
result = None
if result is None:        # 判断空用 is，不要用 ==
    print("没有结果")
print(type(None))         # <class 'NoneType'>
# Java 对照：类似 null，但 None 是真正的对象

# ========== 11. bytes 字节 ==========
print("\n===== 11. bytes 字节 =====")
b = b"hello"              # 直接写字节串
print(b)                  # b'hello'
print(type(b))            # <class 'bytes'>
s = "你好".encode("utf-8")   # 字符串 -> 字节
print(s)                  # b'\xe4\xbd\xa0\xe5\xa5\xbd'
print(s.decode("utf-8"))  # 你好  字节 -> 字符串
# Java 对照：相当于 byte[]，网络传输、文件读写常用
