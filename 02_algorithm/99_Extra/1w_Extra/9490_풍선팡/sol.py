import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]

    max_value = 0
    for i in range(1, N-1):
        for j in range(1, M-1):
            total = 0
            total += A[i][j]
            total += A[i+1][j]
            total += A[i-1][j]
            total += A[i][j+1]
            total += A[i][j-1]

    if max_value < total:
        max_value = total
    print(max_value)