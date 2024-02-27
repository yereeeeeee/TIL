import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    print(f'#{tc}', end=' ')
    n = float(input())

    result = []

    for i in range(1, 13):
        j = 2**(i*-1)
        if n == 0:
            break

        if n >= j:
            n -= j
            result.append(1)
        else:
            result.append(0)

    if n == 0:
        print(*result, sep='')
    else:
        print('overflow')