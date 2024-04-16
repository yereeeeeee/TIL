import sys
input = sys.stdin.readline

def dfs():
    pass

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if arr[i][j]:
            dfs()