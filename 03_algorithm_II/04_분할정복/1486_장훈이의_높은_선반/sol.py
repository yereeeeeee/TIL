import sys
sys.stdin = open('input.txt')

def backtracking(h, i):
    if h == b:
        exit(print(0))
        return

    if h > b:
        result.append(h - b)
        return

    if i < n:
        backtracking(h+s[i], i+1)
        backtracking(h, i+1)


T = int(input())
for tc in range(1, T+1):
    print(f'#{tc}', end=' ')
    n, b = map(int, input().split())
    s = list(map(int, input().split()))
    result = []
    backtracking(0, 0)

    print(min(result))