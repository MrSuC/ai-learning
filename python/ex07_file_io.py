# -*- coding: utf-8 -*-
"""
练习 7：文件读写
================
目标：掌握 Python 文件操作。和 Java 的核心区别：
1. 用 with 语句自动关文件（Java 7+ 的 try-with-resources）
2. 不用手动 close，异常时也安全
3. 读文本要指定编码（Java 也要，但 Python 默认跟系统走，容易踩 GBK 的坑）

运行方式：F5 或 python ex07_file_io.py
（本练习会在当前目录生成 demo.txt，运行完可以看看内容）
"""

# ---------- 1. 写入文件 ----------
# 模式说明（同 Java 的 FileWriter 参数）：
#   "w" 覆盖写（文件存在会清空重写，同 Java new FileWriter(f)）
#   "a" 追加写（同 Java new FileWriter(f, true)）
#   "r" 只读（默认）
content = "第一行：你好\n第二行：Hello\n"

with open("demo.txt", "w", encoding="utf-8") as f:
    # encoding="utf-8" 一定要写！Windows 默认 GBK，中文容易乱码
    f.write(content)
# with 结束自动 f.close()，不用手写，出异常也会关

print("写入完成")


# ---------- 2. 读取文件 ----------
# 方式一：一次全读（小文件适用）
with open("demo.txt", "r", encoding="utf-8") as f:
    text = f.read()          # 整个文件内容变成一个字符串
print("--- read() 全部内容 ---")
print(text)

# 方式二：按行读成列表
with open("demo.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()    # 每行一个元素，含换行符
print("readlines():", lines)

# 方式三：逐行遍历（大文件推荐！内存友好，Java 用 BufferedReader.readLine）
print("--- 逐行遍历 ---")
with open("demo.txt", "r", encoding="utf-8") as f:
    for line in f:           # 直接 for 遍历文件对象
        print("读到:", line.strip())   # strip() 去掉行尾换行


# ---------- 3. 追加写入 ----------
with open("demo.txt", "a", encoding="utf-8") as f:
    f.write("第三行：追加的内容\n")
print("追加完成")


# ---------- 4. 文件不存在会怎样？ ----------
# FileNotFoundError 就是 Java 的 FileNotFoundException 的亲戚
try:
    with open("不存在的文件.txt", "r", encoding="utf-8") as f:
        f.read()
except FileNotFoundError as e:
    print("文件不存在，异常信息:", e)
    # 这在 Java 是受检异常必须处理，Python 里可处理可不处理


# ---------- 5. 路径小贴士 ----------
# 本练习的相对路径 "demo.txt" 相对"当前工作目录"
# 当前工作目录通常是打开终端/运行时的目录，不一定是 py 文件所在目录！
# 想基于 py 文件位置，用 os.path 或 pathlib（后面学了再深入）
import os
print("当前工作目录:", os.getcwd())


# ---------- 练习题（自己做）----------
# 1. 写一个记事本：让用户输入 3 行文字，保存到 notes.txt
# 2. 读取 notes.txt，把每行前面加上行号打印出来（如 "1: xxx"）
# 3. 追加一行 "第 4 行"，再读取验证
# 验收标准：文件真实生成，内容正确，中文不乱码
