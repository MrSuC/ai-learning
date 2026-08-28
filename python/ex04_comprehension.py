# -*- coding: utf-8 -*-
"""
练习 4：列表、字典与推导式（Comprehension）
==========================================
目标：掌握列表/字典推导式——Python 最优雅的语法之一。
Java 里要写循环 + 新建集合，Python 一行搞定。

运行方式：F5 或 python ex04_comprehension.py
"""

# ---------- 0. 基础回顾 ----------
# 列表（List）：类似 Java 的 ArrayList，可增删改，有序
fruits = ["苹果", "香蕉", "橘子"]
fruits.append("葡萄")          # add 元素，等价 Java .add()
print("列表:", fruits)
print("取第一个:", fruits[0])

# 字典（Dict）：类似 Java 的 HashMap，键值对
scores = {"语文": 90, "数学": 95}
print("字典:", scores)
print("取语文成绩:", scores["语文"])   # 键不存在会抛 KeyError（类似 Java 的 NoSuchElementException）


# ---------- 1. 列表推导式（重点！）----------
# 传统写法（Java 风格）：建空列表 -> for 循环 -> append
result_old = []
for i in range(10):
    result_old.append(i * 2)

# 推导式写法：一行搞定，格式 = [表达式 for 变量 in 可迭代对象]
result_new = [i * 2 for i in range(10)]

print("传统写法:", result_old)
print("推导式:  ", result_new)
# 两者完全等价。推导式更短、更快、更 Pythonic


# ---------- 2. 带条件的推导式 ----------
# 只要偶数：[表达式 for 变量 in 范围 if 条件]
evens = [i for i in range(20) if i % 2 == 0]
print("0-19 的偶数:", evens)

# 三元表达式 + 推导式：[A if 条件 else B for ...]
labels = ["偶数" if i % 2 == 0 else "奇数" for i in range(5)]
print("标签:", labels)


# ---------- 3. 字典推导式 ----------
# 传统写法 vs 推导式
squares_old = {}
for i in range(5):
    squares_old[i] = i * i

squares_new = {i: i * i for i in range(5)}   # 注意这里是 {键: 值 for ...}
print("字典推导式:", squares_new)

# 实用场景：把两个列表拼成字典（类似 Java 的 zip + put）
keys = ["name", "age", "city"]
values = ["团团", 26, "北京"]
user = {k: v for k, v in zip(keys, values)}   # zip 把两个列表"拉链"配对
print("zip 拼字典:", user)


# ---------- 4. enumerate：带下标遍历 ----------
# Java 用 for (int i = 0; i < list.size(); i++)
# Python 更优雅：for i, item in enumerate(list)
for index, fruit in enumerate(fruits):
    print(f"第 {index} 个是 {fruit}")


# ---------- 5. 嵌套推导式（了解即可）----------
# 生成 3x3 乘法表矩阵
matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print("乘法表矩阵:", matrix)


# ---------- 练习题（自己做）----------
# 1. 用推导式生成 1-100 中能被 3 和 5 同时整除的数
# 2. 有一个字符串列表，用推导式只保留长度 >= 4 的单词
# 3. 用推导式把 dict {"a": 1, "b": 2} 变成 {"a": 2, "b": 3}（值 +1）
# 验收标准：一行推导式完成，不要用循环 + append
