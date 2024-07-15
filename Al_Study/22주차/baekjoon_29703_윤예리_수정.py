import sys
input = sys.stdin.readline
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def goEat(i, j):
    global answer

    q = deque([(i, j)])
    visited[i][j] = 1
    # 윤예리 바봉봉쇼콜라라랜드라이클리닝장고릴라조기린맥주량이어떻게되요단강강술래리페이지미펠런데빌런
    while q:
        x, y = q.popleft()

        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]

            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and arr[nx][ny] != 'D':
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))

    return

def goHome(i, j):
    global answer

    q = deque([(i, j)])
    visited = [[0] * m for _ in range(n)]
    visited[i][j] = 1

    while q:
        x, y = q.popleft()

        if arr[x][y] == 'H':
            answer += (visited[x][y] - 1)
            print(visited)
            return

        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]

            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and arr[nx][ny] != 'D':
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))

    return -1


n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
answer = 0
visited = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if arr[i][j] == 'S':
            goEat(i, j)
        
        if arr[i][j] == 'F':
            goHome(i, j)

            break
