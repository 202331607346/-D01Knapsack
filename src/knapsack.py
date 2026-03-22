def dp_solve(weights, values, capacity):
    """
    动态规划求解0-1背包问题
    :param weights: 物品重量列表
    :param values: 物品价值列表
    :param capacity: 背包容量
    :return: 最大价值
    """
    n = len(weights)
    # 创建dp数组，dp[i][j]表示前i个物品，容量j时的最大价值
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # 动态规划填表
    for i in range(1, n + 1):
        for j in range(1, capacity + 1):
            if weights[i - 1] <= j:
                # 选或不选当前物品，取最大值
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weights[i - 1]] + values[i - 1])
            else:
                # 无法选当前物品
                dp[i][j] = dp[i - 1][j]

    return dp[n][capacity]