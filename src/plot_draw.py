import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

# 新增下面两行
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False

def draw_scatter(itemsets):
    weights = []
    values = []
    for item in itemsets:
        w1, v1, w2, v2, w3, v3 = item
        weights.extend([w1, w2, w3])
        values.extend([v1, v2, v3])
    
    plt.figure(figsize=(8,5))
    plt.scatter(weights, values, c='blue', alpha=0.7)
    plt.xlabel("重量")
    plt.ylabel("价值")
    plt.title("D{0-1}背包物品分布散点图")
    plt.grid(True)
    plt.show()