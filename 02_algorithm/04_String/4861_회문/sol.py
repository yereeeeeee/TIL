import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(str, input())) for _ in range(N)]
    start = 0
    end = M - 1

    result = []
    mid = (start + end) // 2
    # 행 탐색
    for i in range(N):
        cnt = 0
        for j in range(mid):
            for k in range(N-M+1):
                if arr[i][start + j + k] == arr[i][end - j + k]:
                    cnt += 1
            if cnt >= mid:
                result.extend(arr[i])
                print(*result, sep='')
                break

    # 열 탐색
    for j in range(N):
        cnt = 0
        for i in range(mid):
            for k in range(N-M+1):
                if arr[start + i + k][j] == arr[end - i + k][j]:
                    cnt += 1
            if cnt >= mid:
                for a in range(N):
                    result.extend(arr[a][j])
                print(*result, sep='')




