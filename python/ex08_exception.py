# -*- coding: utf-8 -*-
"""
练习 8：异常处理
================
目标：掌握 Python 的异常机制。和 Java 的核心区别：
1. 语法差不多：try / except / else / finally
2. Java 是 catch，Python 是 except
3. Java 的异常分受检/非受检，Python 没有这种强制区分
4. Python 可以一个 except 捕获多种异常，还能 except Exception 兜底

运行方式：F5 或 python ex08_exception.py
"""

# ---------- 1. 最基本的 try / except ----------
# Java:  try { ... } catch (Exception e) { ... }
try:
    result = 10 / 0          # ZeroDivisionError（除零）
    print("这行不会执行")
except ZeroDivisionError as e:
    print("捕获到除零错误:", e)


# ---------- 2. 捕获多种异常 ----------
# Java: catch (ArithmeticException | NumberFormatException e)
try:
    num = int("abc")         # ValueError：字符串转 int 失败
except (ValueError, TypeError) as e:
    print("捕获到转换错误:", e)
    # 注意：int("abc") 抛的是 ValueError，int(None) 才是 TypeError


# ---------- 3. else 和 finally ----------
# else：没有异常时执行（Java 没有直接对应，可理解为 try 成功分支）
# finally：无论有没有异常都执行（同 Java，适合关资源/清理）
try:
    num = int("42")
except ValueError as e:
    print("出错:", e)
else:
    print(f"转换成功: {num}")     # 只有没异常才走这里
finally:
    print("finally 总会执行")     # 有没有异常都走这里


# ---------- 4. 兜底捕获 ----------
# 不知道会抛什么时，用 Exception 兜底（类似 Java 的 catch (Exception e)）
try:
    lst = [1, 2, 3]
    print(lst[99])             # IndexError：下标越界
except Exception as e:
    print("兜底捕获:", type(e).__name__, "-", e)
    # type(e).__name__ 能得到异常类型名，方便排查


# ---------- 5. 主动抛出异常 raise ----------
# 等价 Java 的 throw new IllegalArgumentException("...")
def set_age(age: int):
    if age < 0 or age > 150:
        raise ValueError(f"年龄不合法: {age}")   # 主动抛异常
    print(f"年龄设为 {age}")


try:
    set_age(200)
except ValueError as e:
    print("捕获到主动抛出的异常:", e)


# ---------- 6. 自定义异常 ----------
# Java 是 extends Exception，Python 是继承 Exception
class BalanceNotEnoughError(Exception):
    """余额不足异常。pass 表示类体为空，继承父类全部行为即可。"""
    pass


def withdraw(balance: float, amount: float):
    if amount > balance:
        raise BalanceNotEnoughError(f"余额 {balance}，想取 {amount}")
    return balance - amount


try:
    withdraw(100, 500)
except BalanceNotEnoughError as e:
    print("业务异常:", e)


# ---------- 练习题（自己做）----------
# 1. 写一个函数 safe_divide(a, b)，b 为 0 时返回 None 而不是崩溃
# 2. 读一个可能不存在的文件，捕获 FileNotFoundError，打印"文件不存在"
# 3. 自定义一个 AgeError，set_age 传入负数时抛它，并在外面捕获
# 验收标准：程序任何输入都不崩溃，错误信息友好
