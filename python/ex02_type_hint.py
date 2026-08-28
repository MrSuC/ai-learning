# -*- coding: utf-8 -*-
"""
练习 2：类型注解（Type Hints）
================================
目标：理解 Python 的类型注解 —— 语法上像 Java，但只是"提示"，不影响运行。
Java 是编译期强制类型，Python 是运行时动态类型，注解只给人和工具看。

运行方式：F5 或 python ex02_type_hint.py
"""

# ---------- 1. 变量注解 ----------
# Java:  int age = 26;
# 语法：变量名: 类型 = 值
age: int = 26              # 整数
name: str = "团团"         # 字符串
height: float = 175.5      # 浮点数
is_student: bool = False   # 布尔值

print(age, name, height, is_student)
# 注意：即使你写 age: int = "hello"，Python 也不报错
# 类型注解是"橡皮图章"，不是"门禁"。运行时不检查。


# ---------- 2. 函数参数和返回值注解 ----------
# Java:  public int add(int a, int b) { return a + b; }
def add(a: int, b: int) -> int:
    """返回 a + b。a: int 是参数注解，-> int 是返回值注解。"""
    return a + b


print("add(3, 5) =", add(3, 5))


# ---------- 3. typing 模块：复杂类型 ----------
# 只写 int/str 不够，列表、字典、可空值需要从 typing 导入
from typing import List, Dict, Optional, Tuple

# List[int] = "元素都是 int 的列表"（类似 Java 的 List<Integer>）
scores: List[int] = [90, 85, 95]

# Dict[str, int] = "键是 str、值是 int 的字典"（类似 Java 的 Map<String, Integer>）
price_map: Dict[str, int] = {"苹果": 5, "香蕉": 3}

# Optional[int] = "可能是 int，也可能是 None"（类似 Java 的 Integer 可空）
# 这在 Java 里就是 Nullable 注解的作用
nickname: Optional[str] = None  # 暂时没有昵称

# Tuple 元组：长度和类型都固定（Java 没有直接对应物，类似不可变数组）
point: Tuple[int, int] = (10, 20)

print(scores, price_map, nickname, point)


# ---------- 4. 注解不影响运行的证据 ----------
def demo(a: int, b: int) -> int:
    return a + b


# 故意传字符串，能跑吗？能！因为注解只是提示，运行时不拦
print("传字符串也能跑:", demo("你好", "世界"))
# 这就是 Python 和 Java 的本质区别：
# Java 编译期就报错，Python 要到运行时才可能暴露问题


# ---------- 练习题（自己做）----------
# 1. 定义一个函数 get_user_info(name: str, age: int) -> Dict[str, object]
#    返回 {"name": name, "age": age}，并打印结果
# 2. 定义一个变量 greeting: str，赋值为 f-string 拼接
# 验收标准：能正常运行，不报错
