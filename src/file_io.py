import pandas as pd
import os

def read_data(file_path):
    itemsets = []
    # 增加 encoding=utf-8 解决编码报错
    with open(file_path, 'r', encoding='utf-8') as f:
        capacity = int(f.readline())
        for line in f:
            data = list(map(int, line.strip().split()))
            itemsets.append(data)
    return capacity, itemsets

def save_txt(path, best_val, time_cost):
    os.makedirs("result", exist_ok=True)
    with open("result/result.txt", 'w', encoding='utf-8') as f:
        f.write(f"最优价值：{best_val}\n")
        f.write(f"计算时间：{time_cost:.4f}s\n")

def save_excel(path, data):
    os.makedirs("result", exist_ok=True)
    df = pd.DataFrame(data, columns=["重量", "价值"])
    df.to_excel("result/items.xlsx", index=False)