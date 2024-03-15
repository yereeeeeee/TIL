'''
위 아래 집의 색이 달라야 함
'''

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

memo = [[0] * 3 for _ in range(n)]

for k in range(3):
    memo[0][k] = arr[-1][k]

for i in range(1, n):
    memo[i][0] = min(memo[i-1][1], memo[i-1][2]) + arr[i][0]    # r
    memo[i][1] = min(memo[i-1][0], memo[i-1][2]) + arr[i][1]    # g
    memo[i][2] = min(memo[i-1][0], memo[i-1][1]) + arr[i][2]    # b

# 최종 작은 수
print(min(memo[n-1]))