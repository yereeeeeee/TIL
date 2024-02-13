import sys
sys.stdin = open('input.txt')

def route(ls, s, g):
    stack = ls[s]
    while g:
        if stack:
            here = stack.pop()
            stack = ls[here]
        else:
            return 0
    return 1

T = int(input())
for tc in range(1, T+1):
    print(f'#{tc}')
    v, e = map(int, input().split())
    ls = [[] * 51 for _ in range(51)]
    for i in range(e):
        a, b = map(int, input().split())
        ls[a].append(b)
    s, g = map(int, input().split())
    print(route(ls, s, g))
