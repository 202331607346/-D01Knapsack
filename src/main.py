# src/main.py 完整正确代码
from knapsack import d01_knapsack_solve
from file_io import read_data, save_txt, save_excel
from plot_draw import draw_scatter
from ui import KnapsackUI
import tkinter as tk

# 主程序
if __name__ == "__main__":
    root = tk.Tk()
    app = KnapsackUI(root, d01_knapsack_solve, read_data, save_txt, draw_scatter)
    root.mainloop()