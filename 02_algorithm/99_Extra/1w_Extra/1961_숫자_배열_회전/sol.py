import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 90도
    result_90 = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            result_90[j][N-1-i] = arr[i][j]

    # 180도
    result_180 = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            result_180[N-1-i][N-1-j] = arr[i][j]

    # 270도
    result_270 = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            result_270[N-1-j][i] = arr[i][j]

    print(f'#{t}')
    for i in range(N):
        print(*result_90[i], sep='', end=' ')
        print(*result_180[i], sep='', end=' ')
        print(*result_270[i], sep='')

