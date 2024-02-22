import sys
sys.stdin = open('input.txt')

# 16진수 -> 2진수
def to2_(n):
    result = []
    a = 3
    while a >= 0:
        result.append(n//(2**a))
        if result[-1] == 1:
            a -= 2**a
    return result

T = int(input())
for tc in range(1, T+1):
    print(f'#{tc}', end=' ')
    n, n16 = map(str, input().split())
    for i in range(int(n)):
        t