import tkinter as tk
from tkinter import filedialog, messagebox
import time

class KnapsackUI:
    def __init__(self, root, solver, reader, saver, drawer):
        self.root = root
        self.root.title("D{0-1}背包问题求解器 —— 软件工程实验")

        self.solver = solver
        self.reader = reader
        self.saver = saver
        self.drawer = drawer

        self.data = None
        self.capacity = None
        self.best_val = 0
        self.time_cost = 0

        # 按钮区域
        tk.Button(root, text="选择数据文件", command=self.load_file).pack(pady=5)
        tk.Button(root, text="绘制物品散点图", command=self.draw_plot).pack(pady=5)
        tk.Button(root, text="开始计算最优价值", command=self.solve).pack(pady=5)
        tk.Button(root, text="保存结果到文件", command=self.save_result).pack(pady=5)

        # 结果标签（优化提示文字）
        self.result_label = tk.Label(root, text="状态：请先加载数据文件", font=("微软雅黑", 12))
        self.result_label.pack(pady=10)

    def load_file(self):
        path = filedialog.askopenfilename(filetypes=[("文本文件", "*.txt")])
        if not path:
            return
        self.capacity, self.data = self.reader(path)
        messagebox.showinfo("成功", "数据加载完成！")
        self.result_label.config(text="状态：数据已加载，可以计算")

    def draw_plot(self):
        if self.data is None:
            messagebox.showwarning("提示", "请先加载数据！")
            return
        self.drawer(self.data)

    def solve(self):
        if self.data is None:
            messagebox.showwarning("提示", "请先加载数据！")
            return

        weights = [x[0] for x in self.data]
        values = [x[1] for x in self.data]

        start = time.time()
        self.best_val = self.solver(weights, values, self.capacity)
        self.time_cost = time.time() - start

        self.result_label.config(text=f"最优价值：{self.best_val} | 耗时：{self.time_cost:.4f}s")

    def save_result(self):
        if self.best_val == 0:
            messagebox.showwarning("提示", "请先完成计算！")
            return
        self.saver("result/result.txt", self.best_val, self.time_cost)
        messagebox.showinfo("成功", "结果已保存到 result/result.txt")