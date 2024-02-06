import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = list(input())
    M = list(input())
    cnt = [0] * len(N)

    for n in range(len(N)):
        for m in range(len(M)):
            if N[n] == M[m]:
                cnt[n] += 1
    print(f'#{tc} {max(cnt)}')