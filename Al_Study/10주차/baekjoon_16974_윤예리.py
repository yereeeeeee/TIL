# 메모리 초과
# dp 싫어!!!!
# n, x = map(int, input().split())
#
# dp = []
# dp.append('P')
#
# for i in range(1, n+1):
#     dp.append('B'+str(dp[i-1])+'P'+str(dp[i-1])+'B')
# print(dp[n][:x].count('P'))