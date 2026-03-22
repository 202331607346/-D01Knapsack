# src/ui.py 完整正确代码
import tkinter as tk
from tkinter import filedialog, messagebox
import time


class KnapsackUI:
    def __init__(self, root, solver, reader, saver, drawer):
        self.root = root
        self.root.title("D{0-1}背包问题求解器")
        self.solver = solver  # 动态规划函数
        self.reader = reader  # read_data 函数
        self.saver = saver  # save_txt 函数
        self.drawer = drawer  # draw_scatter 函数

        # 界面组件
        tk.Button(root, text="选择数据文件", command=self.load_file).pack(pady=5)
        tk.Button(root, text="绘制散点图", command=self.draw_plot).pack(pady=5)
        tk.Button(root, text="开始求解", command=self.solve).pack(pady=5)
        tk.Button(root, text="保存结果", command=self.save_result).pack(pady=5)

        self.result_label = tk.Label(root, text="结果：等待操作")
        self.result_label.pack(pady=10)

        self.data = None
        self.capacity = None
        self.best_val = 0
        self.time_cost = 0

    def load_file(self):
        path = filedialog.askopenfilename()
        self.capacity, self.data = self.reader(path)
        messagebox.showinfo("成功", "数据加载完成")

    def draw_plot(self):
        if self.data:
            self.drawer(self.data)

    def solve(self):
        start = time.time()
        self.best_val, _ = self.solver(self.data, self.capacity)
        self.time_cost = time.time() - start
        self.result_label.config(text=f"最优价值：{self.best_val} | 耗时：{self.time_cost:.4f}s")

    def save_result(self):
        save_path = r"E:\软件工程\实验二\D01Knapsack\result\result.txt"
        self.saver(save_path, self.best_val, self.time_cost)
        messagebox.showinfo("保存成功", "已保存到result文件夹")