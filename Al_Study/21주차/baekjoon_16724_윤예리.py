import sys
input = sys.stdin.readline
from collections import deque

dir = {
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0 ,1)
}

def bfs():
    q = deque([(0, 0)])
    while q:
        x, y = q.popleft()
        visited[x][y] = num
        d = arr[x][y]
        dx, dy = dir[d]

        nx, ny = x + dx, y + dy 
        if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
            visited[nx][ny] = num
            q.append((nx, ny))


n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

num = 1
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            bfs()
            num += 1
            break

print(num-1)
# print(visited)



