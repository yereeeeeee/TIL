import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

r, c, t = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(r)]
airMachine = []

def findMachine():
    for i in range(r):
        for j in range(c):
            if arr[i][j] == -1:
                airMachine.append((i, j))
                return

findMachine()

# 1. 미세먼지가 확산된다.
def diff():
    for x in range(r):
        for y in range(c):
            if arr[x][y]:
                dvalue = arr[x][y] // 5
                for d in range(4):
                    nx, ny = x + dx[d], y + dy[d]

                    if 0 <= nx < r and 0 <= ny < c and arr[nx][ny] != -1:
                        arr[nx][ny] += dvalue
                        arr[x][y] -= dvalue

# 2. 공기청정기가 작동한다.
dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
def airClean():
    x, y = airMachine[0]

    