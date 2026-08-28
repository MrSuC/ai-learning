# -*- coding: utf-8 -*-
"""
练习 10：TODO 管理器（综合实战）
================================
把前面所有知识串起来：类 + 文件读写 + 控制流 + 异常处理 + 推导式。
这是一个真实的命令行小应用：增、删、查、完成标记、持久化到文件。

运行方式：F5 或 python ex10_todo.py
"""
import os

DATA_FILE = "todo_data.txt"   # 保存任务的文件


class Task:
    """单个任务。"""

    def __init__(self, title: str, done: bool = False):
        self.title = title
        self.done = done

    def __str__(self):
        # 已完成的加 [x]，未完成的加 [ ]
        mark = "[x]" if self.done else "[ ]"
        return f"{mark} {self.title}"

    # 序列化：转成文件里的一行文本
    # 格式约定：title 与 done 用 | 分隔，比如 "买菜|1"
    def to_line(self) -> str:
        done_flag = "1" if self.done else "0"
        return f"{self.title}|{done_flag}"

    # 反序列化：从一行文本还原成 Task 对象（类方法，类似 Java 静态工厂）
    @classmethod
    def from_line(cls, line: str) -> "Task":
        title, done_flag = line.strip().split("|")
        return cls(title, done_flag == "1")


class TodoApp:
    """TODO 应用：负责管理任务列表和文件持久化。"""

    def __init__(self):
        self.tasks: list[Task] = []
        self.load()   # 启动时从文件加载已有任务

    # ---------- 持久化 ----------
    def load(self):
        """从文件读入任务。文件不存在就当作空列表。"""
        if not os.path.exists(DATA_FILE):
            return
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                for line in f:
                    if line.strip():   # 跳过空行
                        self.tasks.append(Task.from_line(line))
        except Exception as e:
            print(f"加载失败，从空列表开始: {e}")

    def save(self):
        """把所有任务写回文件（覆盖写）。"""
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            for task in self.tasks:
                f.write(task.to_line() + "\n")

    # ---------- 业务操作 ----------
    def add(self, title: str):
        self.tasks.append(Task(title))
        self.save()
        print(f"已添加: {title}")

    def list_all(self):
        """列出所有任务，前面带编号。"""
        if not self.tasks:
            print("（暂无任务）")
            return
        for i, task in enumerate(self.tasks, start=1):   # start=1：编号从 1 开始
            print(f"{i}. {task}")

    def done(self, index: int):
        """把第 index 个任务标记为完成。下标从 1 开始，方便人看。"""
        try:
            task = self.tasks[index - 1]   # 转成 0 开始的索引
        except IndexError:
            print(f"没有第 {index} 个任务")
            return
        task.done = True
        self.save()
        print(f"已完成: {task.title}")

    def remove(self, index: int):
        """删除第 index 个任务。"""
        try:
            removed = self.tasks.pop(index - 1)
        except IndexError:
            print(f"没有第 {index} 个任务")
            return
        self.save()
        print(f"已删除: {removed.title}")

    # ---------- 主循环 ----------
    def run(self):
        """命令行菜单循环。"""
        while True:
            print("\n===== TODO 管理器 =====")
            print("1. 查看任务")
            print("2. 添加任务")
            print("3. 完成任务")
            print("4. 删除任务")
            print("5. 退出")

            choice = input("请选择: ").strip()

            if choice == "1":
                self.list_all()
            elif choice == "2":
                title = input("任务内容: ").strip()
                if title:
                    self.add(title)
                else:
                    print("内容不能为空")
            elif choice == "3":
                self.list_all()
                try:
                    idx = int(input("要完成哪个（输编号）: "))
                    self.done(idx)
                except ValueError:
                    print("请输入数字")
            elif choice == "4":
                self.list_all()
                try:
                    idx = int(input("要删除哪个（输编号）: "))
                    self.remove(idx)
                except ValueError:
                    print("请输入数字")
            elif choice == "5":
                print("再见！")
                break
            else:
                print("无效选择，请输入 1-5")


if __name__ == "__main__":
    # 只有直接运行本文件时才执行（被 import 时不会跑）
    # 这是 Python 的标准写法，等价 Java 的 public static void main
    app = TodoApp()
    app.run()
