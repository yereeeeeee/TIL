import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    A, B = input().split()
    cnt = A.count(B)
    result = len(A) - ((len(B)-1) * cnt)
    print(f'#{tc} {result}')