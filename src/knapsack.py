# D{0-1}背包动态规划求解
def d01_knapsack_solve(itemsets, capacity):
    # 初始化dp数组
    dp = [0] * (capacity + 1)
    selected = []  # 记录选择结果

    # 遍历每个项集（3个物品为一组）
    for idx, (w1, v1, w2, v2, w3, v3) in enumerate(itemsets):
        # 逆序遍历防止重复选择
        for j in range(capacity, -1, -1):
            opt = [0]  # 不选
            if j >= w1:
                opt.append(dp[j - w1] + v1)
            if j >= w2:
                opt.append(dp[j - w2] + v2)
            if j >= w3:
                opt.append(dp[j - w3] + v3)
            dp[j] = max(opt)
    return dp[capacity], dp