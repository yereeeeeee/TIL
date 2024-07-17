import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
arr =[int(input()) for _ in range(n)]

# dp[i][j] = i 번째 글자를 j번째 줄에 넣었을 때 값

dp = [[0] * m for _ in range(n)]
dp[0][0] = arr[0]

for i in range(1, n):
    for j in range(m):
        
