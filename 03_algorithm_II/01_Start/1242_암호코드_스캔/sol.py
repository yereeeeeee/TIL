import sys
sys.stdin = open('input.txt')

code = [
    [0, 0, 0, 1, 1, 0, 1],  # 0
    [0, 0, 1, 1, 0, 0, 1],  # 1
    [0, 0, 1, 0, 0, 1, 1],  # 2
    [0, 1, 1, 1, 1, 0, 1],  # 3
    [0, 1, 0, 0, 0, 1, 1],  # 4
    [0, 1, 1, 0, 0, 0, 1],  # 5
    [0, 1, 0, 1, 1, 1, 1],  # 6
    [0, 1, 1, 1, 0, 1, 1],  # 7
    [0, 1, 1, 0, 1, 1, 1],  # 8
    [0, 0, 0, 1, 0, 1, 1]   # 9
]

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input())) for _ in range(n)]


    for i in range(n):
        code_16 = []
        for j in range(m):
            if arr[i][j] != 0:
                code_16.append(arr[i][j])


# bin(int(a, 16))