# -*- coding: utf-8 -*-
"""
练习 3：字符串（String）
========================
目标：掌握 Python 字符串的常用操作。
Java 里字符串是不可变对象，Python 也是不可变的——每次"修改"都是生成新字符串。

运行方式：F5 或 python ex03_string.py
"""

# ---------- 1. 定义 ----------
s = "Hello, Python"          # 双引号
s2 = '单引号也可以'           # 单引号（字符串里含引号时很方便）
s3 = """三引号可以
跨多行
写字符串"""                   # 长文本 / 文档字符串

print(s, "|", s2)
print(s3)


# ---------- 2. 索引和切片（Java 用 substring，Python 用切片）----------
text = "Hello, World"
print("第一个字符:", text[0])        # H —— 索引从 0 开始，同 Java
print("最后一个字符:", text[-1])     # d —— 负数索引从末尾数，Java 没有
print("前 5 个:", text[0:5])        # Hello —— [起:止)，左闭右开，同 substring(0,5)
print("第 7 到 12:", text[7:12])    # World
print("每 2 个取 1 个:", text[::2]) # Hlo ol —— [起:止:步长]
print("反转:", text[::-1])          # dlroW ,olleH —— 经典反转技巧，Java 要用循环


# ---------- 3. 常用方法（对比 Java String 方法）----------
# len(): 长度，等价 Java 的 .length()
print("长度:", len(text))

# upper() / lower(): 大小写，等价 Java .toUpperCase() / .toLowerCase()
print("大写:", text.upper())
print("小写:", text.lower())

# strip(): 去首尾空白，等价 Java .trim()（但 strip 还能去换行等更多空白）
dirty = "  有空白  \n"
print("去空白后:", repr(dirty.strip()))

# replace(): 替换，等价 Java .replace()
print("替换:", text.replace("World", "Python"))

# split(): 按分隔符拆成列表，等价 Java .split() 返回 String[]
csv = "苹果,香蕉,橘子"
fruits = csv.split(",")
print("split 结果:", fruits)         # ['苹果', '香蕉', '橘子']

# join(): 列表拼回字符串 —— Java 里是 String.join(",", list)
print("join 结果:", "-".join(fruits))  # 苹果-香蕉-橘子

# find() / startswith() / endswith(): 查找，等价 Java .indexOf() / .startsWith() / .endsWith()
print("'World' 的位置:", text.find("World"))   # 7，找不到返回 -1（Java 返回 -1 也一样）
print("以 Hello 开头?", text.startswith("Hello"))
print("以 World 结尾?", text.endswith("World"))

# count(): 统计出现次数
print("'l' 出现次数:", text.count("l"))


# ---------- 4. f-string 格式化（Python 3.6+，最常用）----------
name = "团团"
age = 26
# Java 是 String.format("我叫%s，今年%d岁", name, age) 或 "..." + name
print(f"我叫{name}，今年{age}岁")

# 还能在里面做计算和调用方法
price = 3.14159
print(f"价格保留 2 位: {price:.2f}")          # 3.14，类似 Java 的 %.2f
print(f"名字大写: {name.upper()}")


# ---------- 练习题（自己做）----------
# 1. 给出一句英文句子，用 split 拆成单词列表，再用 join 用 " " 拼回去
# 2. 写一个反转句子的功能："I love Python" -> "Python love I"
#    （提示：split -> 反转列表 -> join，列表反转用 [::-1]）
# 3. 用 f-string 打印一个表格，3 个商品名和价格对齐
# 验收标准：能运行、结果正确
