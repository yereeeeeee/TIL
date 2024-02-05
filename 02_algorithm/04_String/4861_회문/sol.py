import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(str, input())) for _ in range(N)]

    i = 0
    j = 0
    result = []
    while i < N // 2:
        while j < N // 2:
            # 행 찾기
            if arr[i][j] == arr[i][N-j-1]:
                j += 1
                result.append(arr[i][j])
            else:
                i += 1
                result = []
            # 열 찾기
            if arr[i][j] == arr[N-i-1][j]:
                i += 1
                result.append(arr[i][j])
            else:
                j += 1
                result = []
    print(result)




