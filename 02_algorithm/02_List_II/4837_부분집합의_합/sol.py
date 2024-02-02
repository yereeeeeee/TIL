import sys
sys.stdin = open('input.txt')

n = 12
A = []
for a in range(1, 13):
    A.append(a)

T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())
    subset = []

    for i in range(1<<n):
        result = []
        for j in range(n):
            if i & (1<<j):
                result.append(A[j])
        subset.append(result)

    cnt = 0
    for s in subset:
        if len(s) == N and sum(s) == K:
            cnt += 1

    print(f'#{test_case} {cnt}')
