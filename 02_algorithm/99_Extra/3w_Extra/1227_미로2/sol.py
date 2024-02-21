import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10000)

def find(arr, i, j):
    arr[i][j] = 1
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    for d in range(4):
        ni = i + di[d]
        nj = j + dj[d]
        if 0<=ni<100 and 0<=nj<100 and arr[ni][nj] == 0:
            find(arr, ni, nj)
        elif 0<=ni<100 and 0<=nj<100 and arr[ni][nj] == 3:
            return 1

for _ in range(10):
    tc = int(input())
    maze = [list(map(int, input())) for _ in range(100)]

    for m in range(100):
        for n in range(100):
            if maze[m][n] == 2:
                print(find(maze, m, n))
