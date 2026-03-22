import os
print("工作目录:", os.getcwd())

from knapsack import dpl_solve
from file_io import read_data, save_txt
from plot_draw import draw_scatter
from ui import KnapsackUI
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    app = KnapsackUI(root, dpl_solve, read_data, save_txt, draw_scatter)
    root.mainloop()