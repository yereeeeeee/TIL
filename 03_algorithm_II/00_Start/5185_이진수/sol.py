import sys
sys.stdin = open('input.txt')

AtoF = ['A', 'B', 'C', 'D', 'E', 'F']

# 16진수 -> 2진수
def to2_(x):
    result = []
    for i in range(3, -1, -1):
        result.append(x // (2**i))
        x %= (2**i)
    print(*result, sep='', end='')
    return

T = int(input())
for tc in range(1, T+1):
    print(f'#{tc}', end=' ')
    n, n16 = map(str, input().split())
    n = int(n)

    # 하나하나
    for i in range(n):
        if n16[i].isdigit():
            k = int(n16[i])
            to2_(k)
        else:
            j = 10 + AtoF.index(n16[i])
            to2_(j)
    print()