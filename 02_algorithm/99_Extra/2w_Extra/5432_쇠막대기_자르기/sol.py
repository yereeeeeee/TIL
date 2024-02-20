import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    print(f'#{tc}', end=' ')

    arr = list(input())
    stack = []
    before = ''
    cnt = 0
    while arr:
        a = arr.pop(0)
        if a == '(':
            stack.append(a)
        else:
            if before == ')':
                stack.pop()
                cnt += 1
            else:
                stack.pop()
                cnt += len(stack)
        before = a
    print(cnt)
    # timeout