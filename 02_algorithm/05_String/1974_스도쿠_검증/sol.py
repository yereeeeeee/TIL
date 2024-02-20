import sys
sys.stdin = open('input.txt')

def check(arr):
    for i in range(9):
        cnt = [0] * 9
        for j in range(9):
            cnt[arr[i][j]-1] = 1

        if 0 in cnt:
            return 0
    else:
        return 1

T = int(input())
for tc in range(1, T+1):
    print(f'#{tc}', end=' ')

    arr = [list(map(int, input().split())) for _ in range(9)]
    result = []

    # 가로
    result.append(check(arr))

    h_arr = [[0]*9 for _ in range(9)]
    # 세로
    for i in range(9):
        for j in range(9):
            h_arr[i][j] = arr[j][i]
    result.append(check(h_arr))
    #print(h_arr)

    new_arr = []
    # 3x3 격자
    for i in range(3):
        for j in range(3):
            A = []
            for a in range(i*3, i*3+3):
                for b in range(j*3, j*3+3):
                    A.append(arr[a][b])
            new_arr.append(A)
    result.append(check(new_arr))

    if 0 in result:
        print(0)
    else:
        print(1)