import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    print(f'#{tc}', end=' ')
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    '''
    # 상하좌우
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    # 대각선
    di = [-1, -1, 1, 1]
    dj = [-1, 1, -1, 1]
    '''

    max_value = 0
    for i in range(n):
        for j in range(m):
            total = arr[i][j]   # 풍선 total에 저장

            if arr[i][j] % 2 == 0:  # 짝수
                di = [-1, 1, 0, 0]
                dj = [0, 0, -1, 1]
                for d in range(4):
                    ni = i + di[d]
                    nj = j + dj[d]

                    if 0 <= ni < n and 0 <= nj < m:
                        total += arr[ni][nj]
            else:                   # 홀수
                di = [-1, -1, 1, 1]
                dj = [-1, 1, -1, 1]
                for d in range(4):
                    ni = i + di[d]
                    nj = j + dj[d]

                    if 0 <= ni < n and 0 <= nj < m:
                        total += arr[ni][nj]

            if total > max_value:   # max값 비교
                max_value = total

    print(max_value)