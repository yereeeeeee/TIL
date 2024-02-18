import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    print(f'#{tc}', end=' ')
    N = int(input())
    n = N // 10

    memo = [0] * (n+1)
    memo[1] = 1
    memo[2] = 3

    for i in range(3, n+1):
        if i % 2 == 0:
            memo[i] = memo[i-1] * 2 + 1
        else:
            memo[i] = memo[i-1] * 2 - 1

    print(memo[n])

