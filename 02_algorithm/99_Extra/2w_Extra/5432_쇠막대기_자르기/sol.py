import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    print(f'#{tc}', end=' ')

    arr = list(input())
    stack = 0
    before = ''
    cnt = 0
    for char in arr:
        if char == '(':
            stack += 1
        else:
            if before == ')':
                stack -= 1
                cnt += 1
            else:
                stack -= 1
                cnt += stack
        before = char
    print(cnt)
    # timeout