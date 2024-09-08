import sys
input = sys.stdin.readline
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y, dasom):
    global answer
    q = deque([(x, y, 1, dasom)])
    visited = [[0] * 5 for _ in range(5)]
    visited[x][y] = 1

    while q:
        x, y, total, dasom = q.popleft()

        if 7 - total + dasom < 4: continue

        if total == 7:
            if dasom >= 4:
                answer += 1
            continue

        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny]:
                if arr[nx][ny] == 'Y':
                    q.append((nx, ny, total+1, dasom))
                    visited[nx][ny] = 1
                else:
                    q.append((nx, ny, total+1, dasom+1))
                    visited[nx][ny] = 1

arr = [list(input()) for _ in range(5)]
answer = 0
for i in range(5):
    for j in range(5):
        if arr[i][j] == 'Y':
            bfs(i, j, 0)
        else:
            bfs(i, j, 1)

print(answer)