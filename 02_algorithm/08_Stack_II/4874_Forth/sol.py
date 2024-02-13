import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    forth = input().split()
    stack = []
    print(f'#{tc}', end=' ')
    for i in forth:
        try:
            if i.isnumeric():
                stack.append(int(i))
            elif i == '.':
                if len(stack) == 1:
                    print(stack.pop())
                else:
                    print('error')
            else:
                if i == '+':
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(a+b)
                elif i == '*':
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(a*b)
                elif i == '-':
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b-a)
                elif i == '/':
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b//a)
        except:
            print('error')
            break
