import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    A, B = list(map(str, input().split()))
    cnt = 0

    a = 0
    b = 0
    while a < len(A):
        if A[a] == B[b]:
            a += 1
            if b + 1 == len(B):
                b = 0
                cnt -= (len(B) - 2)
            else:
                b += 1
                cnt += 1
        else:
            cnt += 1
            b = 0
            a += 1
    print(f'#{tc} {cnt}')
