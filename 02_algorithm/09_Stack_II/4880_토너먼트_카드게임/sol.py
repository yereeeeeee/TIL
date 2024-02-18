import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    print(f'#{tc}', end=' ')
    N = int(input())
    card = list(enumerate(map(int, input().split())))
    stack = [card]
    rsp = []

    while stack:
        a = stack.pop(0)
        if len(a) == 1 or 2:
            rsp.append(a)
        if len(card) % 2 == 0:
            stack.append(a[:len(a)//2])
            stack.append(a[len(a)//2:])
        else:
            stack.append(a[:len(a)//2])
            stack.append(a[len(a)//2:len(a)-1])
            stack.append([a[-1]])