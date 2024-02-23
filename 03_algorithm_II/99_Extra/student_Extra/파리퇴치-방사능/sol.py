import sys
sys.stdin = open('input.txt')
import copy

T = int(input())
for tc in range(1, T+1):
    print(f'#{tc}', end=' ')

    N, M, B = map(int, input().split())
    rad = []    # 방사능 파리 위치
    for _ in range(B):
        i, j = map(int, input().split())
        rad.append((i-1, j-1))

    arr = [list(map(int, input().split())) for _ in range(N)]

    # 대각선
    di = [-1, -1, 1, 1]
    dj = [-1, 1, -1, 1]

    max_value = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            total = 0
            copied_arr = copy.deepcopy(arr)

            for m in range(i, i+M):   # 파리채 범위 내의 파리 계산
                for n in range(j, j+M):
                    total += copied_arr[m][n]
                    copied_arr[m][n] = 0

                    if (m, n) in rad:   # 방사능 파리
                        for d in range(4):
                            ni = m + di[d]
                            nj = n + dj[d]
                            if 0<=ni<N and 0<=nj<N:
                                total += copied_arr[ni][nj]
                                copied_arr[ni][nj] = 0

            if total > max_value:
                max_value = total

    print(max_value)