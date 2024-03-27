from collections import deque

# 좌, 상, 우, 하
di = [0, -1, 0, 1]
dj = [-1, 0, 1, 0]

def bfs(i, j):
    q = deque([i, j])

    while q:
        pass

n = map(int, input())
arr = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            bfs(i, j)