import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N, pw = input().split()
    n = int(N)
    stack = [pw[0]]
    top = 0

    for i in range(1, len(pw)):
        try:
            if pw[i] == stack[top]:
                stack.pop()
                top -= 1
            else:
                stack.append(pw[i])
                top += 1
        except:     # stack에 아무것도 없을 때
            stack.append(pw[i])
            top += 1

    print(f'#{tc}', end=' ')
    print(*stack, sep='')