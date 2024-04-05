from collections import deque

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def bfs(i, j):
    cnt = 0
    q = deque([i, j])

    for d in range(4):
        ni = i + di[d]
        nj = j + dj[d]

        if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] == 1:
            cnt += 1
            q.append([ni, nj])



n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
