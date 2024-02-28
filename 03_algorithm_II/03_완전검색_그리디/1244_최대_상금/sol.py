import sys
sys.stdin = open('input.txt')

def get_sub(tar):
    for i in range(n):
        if tar & 0x1:
            print(info[i], end='')
        tar >> 1

T = int(input())
for tc in range(1, T+1):
    print(f'#{tc}', end=' ')

    info, num = map(int, input().split())
    info = list(str(info))
    n = len(info)

    for tar in range(0, 1 << n):
        print('{', end='')
        get_sub(tar)
        print('}')