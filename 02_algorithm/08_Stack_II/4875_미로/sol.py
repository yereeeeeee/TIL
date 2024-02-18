import sys
sys.stdin = open('input.txt')

def dfs(arr, i, j, n):
    stack.append((i, j))
    visited[i][j] = 1

    # 탐색
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]

    if arr[i][j] == 3:
        return 1
    else:
        while stack:
            (a, b) = stack.pop()
            for k in range(4):
                ni = a + di[k]
                nj = b + dj[k]
                if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] != 1:
                    if visited[ni][nj] == 0:
                        if dfs(arr, ni, nj, n):
                            return 1


T = int(input())
for tc in range(1, T+1):
    print(f'#{tc}', end=' ')
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    stack = []
    visited = [[0] * N for i in range(N)]

    # 출발지 찾기
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                start_i = i
                start_j = j
                break

    if dfs(arr, start_i, start_j, N) == None:
        print(0)
    else:
        print(1)
