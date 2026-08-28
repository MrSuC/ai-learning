# -*- coding: utf-8 -*-
"""
练习 5：控制流（if / for / while）
==================================
目标：掌握 Python 的流程控制。语法和 Java 类似，但有几个关键差异：
1. 用冒号 + 缩进代替 Java 的 {}（缩进是语法，不是风格！）
2. 没有 switch（Python 3.10+ 有 match，可了解）
3. 没有 do-while
4. for 循环不是 C 风格，而是"遍历可迭代对象"

运行方式：F5 或 python ex05_control_flow.py
"""

# ---------- 1. if / elif / else ----------
# Java:  if (x > 0) { ... } else if (x == 0) { ... } else { ... }
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:          # 注意是 elif，不是 else if
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "D"

print(f"分数 {score} -> 等级 {grade}")

# Python 的条件不需要括号，逻辑运算符用 and / or / not（不是 && || !）
age = 26
if 18 <= age < 60 and age != 0:   # 还能链式比较：18 <= age < 60，Java 写不出这么舒服的
    print("成年且未退休")


# ---------- 2. for 循环 ----------
# Java: for (int i = 0; i < 5; i++)
# Python: for i in range(5) —— range(5) 生成 0,1,2,3,4
print("for + range:", end=" ")
for i in range(5):
    print(i, end=" ")
print()

# range(起, 止, 步长)：range(2, 10, 2) -> 2,4,6,8
print("range(2,10,2):", list(range(2, 10, 2)))

# 遍历列表/字符串（Java 的 for-each）
for fruit in ["苹果", "香蕉", "橘子"]:
    print("水果:", fruit)

for ch in "Python":
    print("字符:", ch)


# ---------- 3. while 循环 ----------
# 和 Java 基本一样
count = 3
while count > 0:
    print(f"倒计时 {count}")
    count -= 1
print("发射！")


# ---------- 4. break / continue ----------
# break：跳出整个循环（同 Java）
for i in range(10):
    if i == 5:
        break          # 到 5 就停
    print("break 测试 i =", i)

# continue：跳过本次，进下一次（同 Java）
for i in range(10):
    if i % 2 == 1:
        continue       # 跳过奇数
    print("continue 测试偶数:", i)


# ---------- 5. 小游戏：猜数字（综合 if/while/break）----------
import random

secret = random.randint(1, 10)   # 随机 1-10，等价 Java 的 Random().nextInt(10)+1
print("\n--- 猜数字游戏（1-10）---")

while True:                      # 死循环，靠 break 退出（Java 的 while(true)）
    guess = int(input("猜一个数: "))   # input() 从键盘读，int() 转成整数
    if guess == secret:
        print("猜对了！")
        break                    # 猜对就退出
    elif guess > secret:
        print("大了")
    else:
        print("小了")


# ---------- 练习题（自己做）----------
# 1. 打印九九乘法表（两层 for + f-string 对齐）
# 2. 用 while 实现：累加 1 加到 100，结果为 5050
# 3. 给一个列表 [3, 7, 1, 9, 4]，用 for 找出最大值（不要用 max()）
# 验收标准：能运行、输出正确
