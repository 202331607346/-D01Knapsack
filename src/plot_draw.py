# src/plot_draw.py 完整修复版
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题


def draw_scatter(itemsets):
    weights = []
    values = []
    for item in itemsets:
        w1, v1, w2, v2, w3, v3 = item
        weights.extend([w1, w2, w3])
        values.extend([v1, v2, v3])

    plt.figure(figsize=(8, 5))
    plt.scatter(weights, values, c='blue', alpha=0.7)
    plt.xlabel("重量")
    plt.ylabel("价值")
    plt.title("D{0-1}背包数据散点图")
    plt.grid(True)
    plt.show()