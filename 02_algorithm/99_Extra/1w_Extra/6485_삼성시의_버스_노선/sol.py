import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    A = []
    B = []
    for n in range(1, N+1):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    P = int(input())
    C = []
    for m in range(1, P+1):
        c = int(input())
        C.append(c)

    result = [0] * P
    for bus in range(len(C)):
        for n in range(N):
            if A[n] <= C[bus] <= B[n]:
                result[bus] += 1

    print(f'#{test_case}', end=' ')
    print(*result)
