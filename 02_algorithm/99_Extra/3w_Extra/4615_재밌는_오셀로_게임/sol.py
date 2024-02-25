import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = [[0] * n for _ in range(n)]
    for _ in range(m):
        print(f'#{tc}', end=' ')
        C, R, color = map(int, input().split())
        r = R-1
        c = C-1

        for i in range(n):




            # for j in range(n):
            #     if arr[i][j] == color:
            #         for k in range(r, i):
            #             print(k)
            #             if arr[k][j] == arr % 2 + 1:
            #                 arr[i][k] = color   # 가로
            #
            #         for k in arr[j:c]:
            #             if k == arr % 2 + 1:
            #                 arr[k][j] = color   # 세로

        arr[r][c] = color

print()