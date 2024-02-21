import sys
sys.stdin = open('input.txt')

# 오목인지 확인하는 함수
def check(arr):
    global N
    for i in arr:
        if 'ooooo' in i:
            return 1
    else:
        return 0

T = int(input())
for tc in range(1, T+1):
    print(f'#{tc}', end=' ')
    N = int(input())
    arr = [input() for _ in range(N)]
    #omok = ['o', 'o', 'o', 'o', 'o']
    # result = 'NO'

    # 전치 행렬
    rev_arr = [[' '] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            rev_arr[j][i] = arr[i][j]
    for i in range(N):
        a = rev_arr.pop(0)
        rev_arr.append(''.join(a))

    # 대각선
    left = []
    right = []
    for i in range(N):
        left.append(arr[i][i])
        right.append(arr[i][N-i-1])
    left_2 = [''.join(left)]
    right_2 = [''.join(right)]
    # N=5일 때만 고려한거라 N 이 더 커지면 대각선을 2차원 배열로 고려해줘야함

    if check(arr) + check(rev_arr) + check(left_2) + check(right_2) == 0:
        print('NO')
    else:
        print('YES')

