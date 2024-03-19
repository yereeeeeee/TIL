import sys
sys.stdin = open('input.txt')

def backtracking(cost, depth):
    global result

    if cost >= result:
        return

    if depth == n:
        result = cost
        return

    for j in num:
        if not visited[j]:
            visited[j] = 1
            backtracking(cost+arr_v[depth][j], depth+1)
            visited[j] = 0

T = int(input())
for tc in range(1, T+1):
    print(f'#{tc}', end=' ')

    n = int(input())
    arr_v = [list(map(int, input().split())) for _ in range(n)]
    visited = [0] * n
    result = float('inf')
    num = [i for i in range(n)]
    backtracking(0, 0)
    print(result)