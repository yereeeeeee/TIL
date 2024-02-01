import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    bal = [list(map(int, input().split())) for _ in range(N)]

    max_value = 0
    for i in range(1, N-1):
        for j in range(1, M-1):
            pol = bal[i][j] + bal[i-1][j] + bal[i][j-1] + bal[i+1][j] + bal[i][j+1]

            if pol > max_value:
                max_value = pol
    print(f'#{test_case} {max_value}')