import sys
sys.stdin = open('input.txt')

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

def pinball(x, y, d):
    if arr[x][y] == 1:
        if d == 4:
            d = 1
        elif d == 1:
            d = 4




T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]


