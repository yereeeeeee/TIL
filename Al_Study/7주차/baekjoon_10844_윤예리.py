# dp
n = int(input())
dp = [0] * (n+1)

dp[1] = 9
dp[2] = 17
if n >= 3:
    for i in range(3, n+1):
        dp[i] = dp[i-1] * 2 - 2
print(dp[n])

# backtracking
# def backtraking(result, i):
#     if len(result) == n:
#         if result not in stepnum:
#             stepnum.append(result)
#             return
#
#     else:
#         if 0<=i+1<10:
#             backtraking(result+str(i), i+1)
#         if 0<=i-1<10:
#             backtraking(result+str(i), i-1)
#
#         else:
#             return
#
# n = int(input())
# stepnum = []
#
# for j in range(1, 10):
#     backtraking('', j)
#
# print(len(stepnum))