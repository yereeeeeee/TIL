import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    print(f'#{tc}', end=' ')
    N = int(input())
    arr = [list(map(str, input())) for _ in range(N)]
    omok = ['o', 'o', 'o', 'o', 'o']
    result = 'NO'

    rev_arr = [[' '] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            rev_arr[j][i] = arr[i][j]

    #  가로
    for i in range(N):
        if omok in arr[i]:
            result = 'YES'

    # 세로
    for i in range(N):
        if omok in rev_arr[i]:
            result = 'YES'

    # 대각선
    left = []
    right = []
    for i in range(N):
        left.append(arr[i][i])
        right.append(arr[N-i-1][N-i-1])
    if (omok in left) or (omok in right):
        result = 'YES'

    print(result)

