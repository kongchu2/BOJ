n, m = map(int, input().split())

dp = [0, 1]
for i in range(2, 101):
    dp.append(dp[i-1] * i)

print(dp[n] // (dp[m] * dp[n-m]))