from collections import deque

# 상, 좌, 우, 하
di = [-1, 0, 0, 1]
dj = [0, -1, 1, 0]

def bfs(i, j):
    global size
    global fish

    q = deque([[(i, j), 0]])
    sec = 0

    while q:
        # print(q)
        if fish == size:
            size += 1
            fish = 0

        now = q.popleft()
        sec = max(sec, now[1])
        # print(now)

        for d in range(4):
            ni = now[0][0] + di[d]
            nj = now[0][1] + dj[d]

            if 0 <= ni < n and 0 <= nj < n and 0 <= arr[ni][nj] <= size:
                if arr[ni][nj] == 0:        # 빈 칸일 때
                    q.append([(ni, nj), now[1]+1])
                    arr[ni][nj] = -1
                elif arr[ni][nj] < size:    # 잡아먹는 경우
                    arr[ni][nj] = 9
                    fish += 1
                elif arr[ni][nj] == size:   # 같을 때
                    q.append([(ni, nj), now[1]+1])
    return sec


def cnt(baby):
    for i in range(n):
        for j in range(n):
            if 0 < arr[i][j] <= baby:
                return True     # 먹을 물고기가 있음
    return False

def reset():
    for i in range(n):
        for j in range(n):
            if arr[i][j] == -1:
                arr[i][j] = 0

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
size = 2
fish = 0

while cnt(size):
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 9:
                arr[i][j] = 0
                bfs(i, j)
                reset()
else:
    print(0)