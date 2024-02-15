import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    length = int(input())
    string = list(input())
    stack = []
    result = []

    # 후위표기식
    for s in string:
        if s == '+':
            while stack:
                result.append(stack.pop())
            stack.append(s)
        else:
            result.append(s)
    if stack:
        for t in stack:
            result.append(stack.pop())

    # 계산
    for r in result:
        if r == '+':
            num2 = int(stack.pop())
            num1 = int(stack.pop())
            stack.append(num1+num2)
        else:
            stack.append(r)

    print(f'#{tc} {stack[0]}')