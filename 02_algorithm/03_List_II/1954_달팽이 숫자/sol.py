import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    result = []
    for i in range(N):
        for j in range(N):
            result[i][j] = 0
    print(result)

    while N > 0:
        for n in range(N):
            result.append()