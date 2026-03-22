import pandas as pd
import os  # 新增

def read_data(file_path):
    itemsets = []
    with open(file_path, 'r', encoding='utf-8') as f:
        capacity = int(f.readline())
        for line in f:
            data = list(map(int, line.strip().split()))
            itemsets.append(data)
    return capacity, itemsets

def save_txt(path, best_val, time_cost):
    os.makedirs("result", exist_ok=True)  # 新增
    with open("result/result.txt", 'w') as f:
        f.write(f"最优价值：{best_val}\n")
        f.write(f"计算时间：{time_cost:.4f}s\n")