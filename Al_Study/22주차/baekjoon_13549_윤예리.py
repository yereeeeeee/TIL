n, k = map(int, input().split())
dp = [0] + [100000] * (k+1)

for i in range(n, k+1):
    if i%n == 0: dp[i] = 0
    else:
        dp[i] = min(dp[i//2], dp[i-1] + 1, dp[i+1] + 1)

print(dp[k])