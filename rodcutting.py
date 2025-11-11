def rod_cutting(prices, n):
    dp = [0] * (n + 1)

    # dp[i]: uzunluğu i olan çubuk için maksimum gelir
    for i in range(1, n + 1):
        max_val = float('-inf')
        for j in range(1, i + 1):
            max_val = max(max_val, prices[j - 1] + dp[i - j])
        dp[i] = max_val

    return dp[n], dp


# Örnek kullanım
prices = [1, 5, 8, 9, 10, 17, 17, 20]
n = 8
result, table = rod_cutting(prices, n)
print("Maksimum gelir:", result)
print("DP Tablosu:", table)
