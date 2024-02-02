import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    k = 1
    n = 0
    w = 0
    s = N - 1
    e = N - 1

    while n <= s and w <= e:
        # 좌 -> 우
        for i in range(w, e+1):
            arr[n][i] = k
            k += 1
        n += 1

        # 상 -> 하
        for i in range(n, s+1):
            arr[i][e] = k
            k += 1
        e -= 1

        # 우 -> 좌
        for i in range(e, w-1, -1):
            arr[s][i] = k
            k += 1
        s -= 1

        # 하 -> 상
        for i in range(s, n-1, -1):
            arr[i][w] = k
            k += 1
        w += 1

    print(f'#{test_case}')
    for i in arr:
        print(*i)

