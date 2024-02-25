import sys
sys.stdin = open('input.txt')
from collections import deque

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def find(i, j):
    q = deque([(i, j)])

    while q:
        i, j = q.popleft()
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            if 0 <= ni < 16 and 0 <= nj < 16 and arr[ni][nj] != 1:
                if arr[ni][nj] == 3:
                    return 1
                arr[ni][nj] = 1
                q.append((ni, nj))
    return 0

for _ in range(1, 11):
    tc = int(input())
    arr = [list(map(int, input())) for _ in range(16)]

    result = None
    for i in range(16):
        for j in range(16):
            if arr[i][j] == 2:
                result = find(i, j)
                break

        if result != None:
            break

    print(f'#{tc} {result}')