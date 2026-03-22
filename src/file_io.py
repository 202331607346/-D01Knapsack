import pandas as pd

# 读取数据文件
def read_data(file_path):
    itemsets = []
    with open(file_path, 'r') as f:
        capacity = int(f.readline())
        for line in f:
            data = list(map(int, line.strip().split()))
            itemsets.append(data)  # w1,v1,w2,v2,w3,v3
    return capacity, itemsets

# 保存结果到txt
def save_txt(path, best_val, time_cost):
    with open(path, 'w') as f:
        f.write(f"最优价值：{best_val}\n")
        f.write(f"求解时间：{time_cost:.4f}s\n")

# 导出Excel
def save_excel(path, data):
    df = pd.DataFrame(data, columns=["项集", "物品1(w/v)", "物品2(w/v)", "物品3(w/v)"])
    df.to_excel(path, index=False)