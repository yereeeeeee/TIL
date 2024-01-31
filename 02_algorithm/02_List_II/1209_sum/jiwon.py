import sys
sys.stdin = open('input.txt')

T = 10
for test_case in range(1, T + 1):
    t = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    max_alpha = 0
    max_beta = 0
    max_gamma = 0
    max_hexa = 0

    for i in range(100):
        alpha = 0
        beta = 0
        gamma = 0
        hexa = 0
        for j in range(100):
            alpha += arr[i][j]  # 행의 합
            beta += arr[j][i]  # 열의 합
            if i == j:
                gamma += arr[i][j]  # 첫 번째 대각선의 합
            if j == 100 - i:
                hexa += arr[j][i]  # 두 번째 대각선의 합
        max_alpha = max(max_alpha, alpha)
        max_beta = max(max_beta, beta)
        max_gamma = gamma
        max_hexa = hexa

    max_sum = max(max_alpha, max_beta, max_gamma, max_hexa)
    print(f'#{test_case} {max_sum}')
