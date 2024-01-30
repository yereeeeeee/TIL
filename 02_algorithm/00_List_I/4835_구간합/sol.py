import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    a_i = list(map(int, input().split()))

    total = []
    for n in range(0, N-M+1):
        ls = []
        for m in range(n, M+n):
            ls.append(a_i[m])
        total.append(sum(ls))
    print(f'#{t+1} {max(total) - min(total)}')