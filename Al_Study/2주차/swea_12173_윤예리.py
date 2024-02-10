T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    i = 0
    j = 0
    cnt = 0


    # 그리디하게 해볼랬는데 안되넹 ㅎ..까비
    # while i < n or j < m:
    #     cnt += a[i][j]
    #     if i == n - 1 and j == m - 1:
    #         break
    #     elif i == n-1:
    #         j += 1
    #     elif j == m-1:
    #         i += 1
    #     else:
    #         if a[i+1][j] > a[i][j+1]:
    #             i += 1
    #         else:
    #             j += 1
    print(f'#{tc} {cnt}')
