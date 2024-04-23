import sys
input = sys.stdin.readline
from collections import deque

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def check(i, j):
    cnt = 0

    q =
    for d in range(4):
        ni = i + di[d]
        nj = j + dj[d]

        if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] = 0



    return cnt

n, m = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(n)]
result = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            arr[i][j] = 0
            result[i][j] = check(i, j)
            arr[i][j] = 1

